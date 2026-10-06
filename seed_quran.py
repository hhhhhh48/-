# -*- coding: utf-8 -*-
"""Fetch full Quran from alquran.cloud (Arabic + EN + FR + ES) into SQLite."""
import sqlite3, os, time, sys
try:
    import requests
except ImportError:
    print("Install requests: pip install requests")
    sys.exit(1)

DB = os.path.join(os.path.dirname(__file__), "beauty.db")

EDITIONS = {
    "ar": "quran-uthmani",
    "en": "en.sahih",
    "fr": "fr.hamidullah",
    "es": "es.cortes",
}


def init_tables():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.executescript("""
    CREATE TABLE IF NOT EXISTS surahs (
        number INTEGER PRIMARY KEY,
        name_en TEXT, name_ar TEXT, name_translation TEXT,
        verses_count INTEGER, place TEXT
    );
    CREATE TABLE IF NOT EXISTS verses (
        surah_number INTEGER,
        number INTEGER,
        ar TEXT, en TEXT, fr TEXT, es TEXT,
        PRIMARY KEY (surah_number, number)
    );
    """)
    conn.commit()
    return conn


def fetch_meta():
    for _ in range(3):
        try:
            r = requests.get("https://api.alquran.cloud/v1/surah", timeout=25)
            if r.status_code == 200:
                return r.json()["data"]
        except Exception as e:
            print(f"  retry: {e}")
            time.sleep(2)
    return None


def fetch_surah(num, edition):
    url = f"https://api.alquran.cloud/v1/surah/{num}/{edition}"
    for attempt in range(3):
        try:
            r = requests.get(url, timeout=25)
            if r.status_code == 200:
                return r.json()["data"]["ayahs"]
        except Exception:
            time.sleep(2)
    return None


def seed():
    conn = init_tables()
    c = conn.cursor()

    done = c.execute("SELECT COUNT(*) FROM verses").fetchone()[0]
    if done > 6200:
        print(f"✅ Already seeded ({done} verses).")
        conn.close()
        return

    # 1. metadata
    if c.execute("SELECT COUNT(*) FROM surahs").fetchone()[0] != 114:
        print("⏳ Fetching surah metadata...")
        meta = fetch_meta()
        if not meta:
            print("❌ Could not fetch metadata.")
            conn.close()
            return
        for s in meta:
            c.execute("""INSERT OR REPLACE INTO surahs
                (number, name_en, name_ar, name_translation, verses_count, place)
                VALUES (?,?,?,?,?,?)""",
                (s["number"], s["englishName"], s["name"],
                 s["englishNameTranslation"], s["numberOfAyahs"],
                 s["revelationType"]))
        conn.commit()
        print(f"✅ {len(meta)} surahs metadata inserted.")

    # 2. verses
    for n in range(1, 115):
        existing = c.execute("SELECT COUNT(*) FROM verses WHERE surah_number=?", (n,)).fetchone()[0]
        if existing > 0:
            print(f"⏭  Surah {n} already done.")
            continue

        sys.stdout.write(f"⏳ Surah {n}... ")
        sys.stdout.flush()

        data = {}
        for lang, ed in EDITIONS.items():
            ayahs = fetch_surah(n, ed)
            if ayahs is None:
                print(f"❌ failed on {lang}")
                data = None
                break
            data[lang] = ayahs
            time.sleep(0.25)

        if data is None:
            continue

        for i in range(len(data["ar"])):
            c.execute("""INSERT OR REPLACE INTO verses
                (surah_number, number, ar, en, fr, es)
                VALUES (?,?,?,?,?,?)""",
                (n, data["ar"][i]["numberInSurah"],
                 data["ar"][i]["text"],
                 data["en"][i]["text"],
                 data["fr"][i]["text"],
                 data["es"][i]["text"]))
        conn.commit()
        print(f"✅ {len(data['ar'])} verses")

    conn.close()
    print("\n🎉 Quran complete!")


if __name__ == "__main__":
    seed()
