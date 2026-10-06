import os, json, sqlite3, hashlib
from functools import lru_cache
from datetime import datetime, timedelta
from flask import Flask, render_template, session, redirect, request, g, url_for, abort, Response
from data_arguments import ARGUMENTS
from data_muhammad import LIFE, CHARACTER, TESTIMONIES as MUH_TESTIMONIES, NON_MUSLIMS, VERSES_ABOUT_HIM
from data_jesus import (JESUS_INTRO, MARY_INTRO, MESSAGE_CHRISTIANS, VERSE_REFS,
                        COMPARISON, MARYAM_VERSES_PREVIEW, MIRACLES, QUESTIONS, PROPHECIES)
from data_women import (INTRO as WOMEN_INTRO, MISCONCEPTIONS, STORIES as WOMEN_STORIES,
                        TESTIMONIES as WOMEN_TESTIMONIES, RIGHTS, VERSES as WOMEN_VERSES)
from data_hindu import INTRO_HI, QUESTIONS_HINDU, COMPARISON_HI
from data_convert import INTRO as CONV_INTRO, STEPS as CONV_STEPS, AFTER as CONV_AFTER, STORIES as CONV_STORIES

BASE = os.path.dirname(os.path.abspath(__file__))
TRANS_DIR = os.path.join(BASE, "translations")
DB_PATH = os.path.join(BASE, "beauty.db")
LANGS = ["en", "fr", "es", "de", "it", "pt", "hi", "ar"]

ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "washmi2026")
SECRET_SALT = os.environ.get("SECRET_SALT", "boi-salt-change-me")

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "boi-2026-secret")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


@lru_cache(maxsize=16)
def load(lang):
    try:
        with open(os.path.join(TRANS_DIR, f"{lang}.json"), encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(os.path.join(TRANS_DIR, "en.json"), encoding="utf-8") as f:
            return json.load(f)


def t(key, lang=None):
    lang = lang or getattr(g, "lang", "en")
    if lang not in LANGS: lang = "en"
    data = load(lang)
    cur = data
    for p in key.split("."):
        if isinstance(cur, dict) and p in cur: cur = cur[p]
        else:
            cur = load("en")
            for p2 in key.split("."):
                cur = cur.get(p2, key) if isinstance(cur, dict) else key
            return cur
    return cur


def hash_ip(ip):
    return hashlib.sha256((ip + SECRET_SALT).encode()).hexdigest()[:16]


def get_country():
    """Guess country from Accept-Language header."""
    al = request.headers.get("Accept-Language", "")
    if not al: return "Unknown"
    # Take first language tag
    first = al.split(",")[0].split(";")[0].strip()
    if "-" in first:
        return first.split("-")[1].upper()
    return first.upper() if first else "Unknown"


@app.before_request
def set_lang_and_track():
    # Language
    lang = request.args.get("lang") or session.get("lang") or request.accept_languages.best_match(LANGS) or "en"
    if lang not in LANGS: lang = "en"
    session["lang"] = lang
    g.lang = lang

    # Track visitors (skip static, admin, favicon)
    try:
        if (request.endpoint and
            not request.path.startswith("/static") and
            not request.path.startswith("/admin") and
            not request.path.startswith("/favicon") and
            request.path not in ("/robots.txt",)):
            conn = get_db()
            ip = request.headers.get("X-Forwarded-For", request.remote_addr or "0.0.0.0").split(",")[0].strip()
            ua = request.headers.get("User-Agent", "")[:200]
            ref = request.headers.get("Referer", "")[:200]
            conn.execute("""INSERT INTO visitors
                (ip_hash, path, lang, user_agent, referer, country)
                VALUES (?,?,?,?,?,?)""",
                (hash_ip(ip), request.path[:200], lang, ua, ref, get_country()))
            conn.commit()
            conn.close()
    except Exception:
        pass


@app.context_processor
def inject():
    return {"t": lambda k: t(k, g.lang), "lang": g.lang, "langs": LANGS, "site_name": t("site_name", g.lang)}


# ==================== ROUTES ====================

@app.route("/")
def index(): return render_template("index.html")

@app.route("/god-exists")
def god_exists(): return render_template("god_exists.html", arguments=ARGUMENTS)

@app.route("/muhammad")
def muhammad():
    return render_template("muhammad.html", life=LIFE, character=CHARACTER,
                           testimonies=MUH_TESTIMONIES, non_muslims=NON_MUSLIMS, verses=VERSES_ABOUT_HIM)

@app.route("/jesus-mary")
def jesus_mary():
    return render_template("jesus_mary.html",
                           jesus_intro=JESUS_INTRO, mary_intro=MARY_INTRO,
                           message=MESSAGE_CHRISTIANS, verse_refs=VERSE_REFS,
                           comparison=COMPARISON, maryam=MARYAM_VERSES_PREVIEW,
                           miracles=MIRACLES, questions=QUESTIONS, prophecies=PROPHECIES)

@app.route("/women")
def women():
    return render_template("women.html", intro=WOMEN_INTRO,
                           misconceptions=MISCONCEPTIONS, stories=WOMEN_STORIES,
                           testimonies=WOMEN_TESTIMONIES, rights=RIGHTS, verses=WOMEN_VERSES)

@app.route("/for-hindus")
def for_hindus():
    return render_template("for_hindus.html", intro=INTRO_HI,
                           questions=QUESTIONS_HINDU, comparison=COMPARISON_HI)

@app.route("/convert")
def convert():
    return render_template("convert.html", intro=CONV_INTRO, steps=CONV_STEPS,
                           after=CONV_AFTER, stories=CONV_STORIES)

@app.route("/quran")
def quran():
    q = request.args.get("q", "").strip()
    conn = get_db()
    surahs = conn.execute("SELECT * FROM surahs ORDER BY number").fetchall()
    results = None
    if q:
        like = f"%{q}%"
        results = conn.execute("""
            SELECT * FROM verses
            WHERE en LIKE ? OR ar LIKE ? OR fr LIKE ? OR es LIKE ?
            ORDER BY surah_number, number LIMIT 80
        """, (like, like, like, like)).fetchall()
    conn.close()
    return render_template("quran.html", surahs=surahs, results=results, q=q)

@app.route("/quran/<int:number>")
def surah_view(number):
    conn = get_db()
    s = conn.execute("SELECT * FROM surahs WHERE number=?", (number,)).fetchone()
    if not s:
        conn.close()
        return redirect(url_for("quran"))
    verses = conn.execute("SELECT * FROM verses WHERE surah_number=? ORDER BY number",
                          (number,)).fetchall()
    conn.close()
    return render_template("surah.html", surah=s, verses=verses)

@app.route("/hadiths")
def hadiths():
    cat = request.args.get("cat", "").strip()
    q = request.args.get("q", "").strip()
    conn = get_db()
    sql = "SELECT * FROM hadiths"
    params, where = [], []
    if cat:
        where.append("category = ?"); params.append(cat)
    if q:
        like = f"%{q}%"
        where.append("(text_en LIKE ? OR text_ar LIKE ? OR text_fr LIKE ? OR text_es LIKE ?)")
        params.extend([like, like, like, like])
    if where: sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY id"
    rows = conn.execute(sql, params).fetchall()
    conn.close()
    return render_template("hadiths.html", hadiths=rows, cat=cat, q=q)

@app.route("/set-lang/<lang>")
def set_lang_route(lang):
    if lang in LANGS: session["lang"] = lang
    ref = request.referrer
    return redirect(ref if ref and ref.startswith(request.host_url) else url_for("index"))


# ==================== ADMIN ====================

@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        pwd = request.form.get("password", "")
        if pwd == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect(url_for("admin"))
        else:
            return render_template("admin.html", error="Wrong password", stats=None, logged=False)

    if not session.get("admin"):
        return render_template("admin.html", stats=None, logged=False)

    conn = get_db()
    c = conn.cursor()

    total = c.execute("SELECT COUNT(*) FROM visitors").fetchone()[0]
    unique = c.execute("SELECT COUNT(DISTINCT ip_hash) FROM visitors").fetchone()[0]
    today = c.execute("SELECT COUNT(*) FROM visitors WHERE date(visited_at) = date('now')").fetchone()[0]
    unique_today = c.execute("SELECT COUNT(DISTINCT ip_hash) FROM visitors WHERE date(visited_at) = date('now')").fetchone()[0]
    week = c.execute("SELECT COUNT(*) FROM visitors WHERE visited_at >= datetime('now', '-7 days')").fetchone()[0]

    top_pages = c.execute("""
        SELECT path, COUNT(*) as cnt FROM visitors
        GROUP BY path ORDER BY cnt DESC LIMIT 15
    """).fetchall()

    top_langs = c.execute("""
        SELECT lang, COUNT(*) as cnt FROM visitors
        GROUP BY lang ORDER BY cnt DESC
    """).fetchall()

    top_countries = c.execute("""
        SELECT country, COUNT(*) as cnt FROM visitors
        WHERE country != 'Unknown' AND country != ''
        GROUP BY country ORDER BY cnt DESC LIMIT 15
    """).fetchall()

    daily = c.execute("""
        SELECT date(visited_at) as d, COUNT(*) as cnt, COUNT(DISTINCT ip_hash) as u
        FROM visitors
        WHERE visited_at >= datetime('now', '-30 days')
        GROUP BY date(visited_at) ORDER BY d DESC
    """).fetchall()

    recent = c.execute("""
        SELECT path, lang, country, user_agent, referer, visited_at
        FROM visitors ORDER BY id DESC LIMIT 50
    """).fetchall()

    conn.close()

    stats = {
        "total": total, "unique": unique,
        "today": today, "unique_today": unique_today,
        "week": week,
        "top_pages": top_pages,
        "top_langs": top_langs,
        "top_countries": top_countries,
        "daily": daily,
        "recent": recent,
    }
    return render_template("admin.html", stats=stats, logged=True)


@app.route("/admin/logout")
def admin_logout():
    session.pop("admin", None)
    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
