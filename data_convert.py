# -*- coding: utf-8 -*-

def L(en, fr, es, de, it, pt, hi):
    return {"en": en, "fr": fr, "es": es, "de": de, "it": it, "pt": pt, "hi": hi}

INTRO = L(
 "Becoming Muslim is not a ritual. It is a simple, sincere return to your Creator - with no intermediaries, no priests, no baptism, no fees. Just you and Allah. If you believe there is no god but Allah and that Muhammad is His Messenger, you are one step away.",
 "Devenir musulman n'est pas un rituel. C'est un retour simple et sincere a votre Createur - sans intermediaires, sans pretres, sans frais. Juste vous et Allah.",
 "Convertirse en musulman no es un ritual. Es un regreso simple y sincero a tu Creador - sin intermediarios, sin sacerdotes, sin tarifas. Solo tu y Allah.",
 "Muslim zu werden ist kein Ritual. Es ist eine einfache, aufrichtige Rueckkehr zu deinem Schoepfer - ohne Vermittler, ohne Priester, ohne Gebuehren. Nur du und Allah.",
 "Diventare musulmano non e un rituale. E un ritorno semplice e sincero al tuo Creatore - senza intermediari, senza sacerdoti, senza tasse. Solo tu e Allah.",
 "Tornar-se muculmano nao e um ritual. E um retorno simples e sincero ao seu Criador - sem intermediarios, sem sacerdotes, sem taxas. Apenas voce e Allah.",
 "Muslim banna koi rasam nahi hai. Yeh aapke Khaliq ki taraf ek seedha, sacha wapsi hai - koi beech mein nahi, koi pandit nahi, koi fees nahi. Sirf aap aur Allah.",
)

# 4 steps
STEPS = [
    {
        "num": 1,
        "icon": "1",
        "title": L("Heartfelt Conviction","Conviction du Coeur","Conviccion del Corazon","Herzliche Ueberzeugung","Convinzione del Cuore","Conviccao do Coracao","Dil Ki Yaqeen"),
        "text": L("Believe in your heart that there is no god but Allah - the One who has no partner, no son, no image - and that Muhammad is His final Messenger.",
                 "Croyez de tout votre coeur qu'il n'y a de dieu qu'Allah - l'Unique sans associe, sans fils, sans image - et que Muhammad est Son dernier Messager.",
                 "Cree en tu corazon que no hay mas dios que Allah - el Unico sin socio, sin hijo, sin imagen - y que Muhammad es Su ultimo Mensajero.",
                 "Glaube von Herzen, dass es keinen Gott ausser Allah gibt - den Einen ohne Partner, ohne Sohn, ohne Bild - und dass Muhammad Sein letzter Gesandter ist.",
                 "Credi nel tuo cuore che non c'e dio all'infuori di Allah - l'Unico senza soci, senza figli, senza immagine - e che Muhammad e il Suo ultimo Messaggero.",
                 "Creia de coracao que nao ha deus alem de Allah - o Unico sem parceiro, sem filho, sem imagem - e que Muhammad e Seu ultimo Mensageiro.",
                 "Dil se maano ke Allah ke siwa koi khuda nahi - woh Ek, jiska koi shareek nahi, na beta, na murti - aur Muhammad uske aakhri Rasool hain."),
    },
    {
        "num": 2,
        "icon": "2",
        "title": L("Pronounce the Shahada","Prononcer la Shahada","Pronunciar la Shahada","Die Schahada sprechen","Pronunciare la Shahada","Pronunciar a Shahada","Shahada Padho"),
        "text": L("Say the testimony of faith aloud, with full sincerity, in Arabic (or in your own language if you cannot). This is the moment you become Muslim. Angels witness it.",
                 "Prononcez le temoignage de foi a voix haute, avec une pleine sincerite, en arabe (ou dans votre langue). C'est le moment ou vous devenez musulman.",
                 "Di el testimonio de fe en voz alta, con total sinceridad, en arabe (o en tu idioma si no puedes). Este es el momento en que te vuelves musulman.",
                 "Sprich das Glaubensbekenntnis laut und aufrichtig auf Arabisch (oder in deiner Sprache). Dies ist der Moment, in dem du Muslim wirst.",
                 "Pronuncia la testimonianza di fede ad alta voce, con piena sincerita, in arabo (o nella tua lingua). Questo e il momento in cui diventi musulmano.",
                 "Diga o testemunho de fe em voz alta, com total sinceridade, em arabe (ou em seu idioma). Este e o momento em que voce se torna muculmano.",
                 "Shahada ko zor se, poori sacchai ke saath, Arabic mein padho (ya apni zubaan mein). Yeh woh lamha hai jab aap Muslim ban jate hain."),
    },
    {
        "num": 3,
        "icon": "3",
        "title": L("Purification (Ghusl)","Purification (Ghusl)","Purificacion (Ghusl)","Reinigung (Ghusl)","Purificazione (Ghusl)","Purificacao (Ghusl)","Ghusl - Nahana"),
        "text": L("Take a full bath - washing the entire body - as a symbol of spiritual rebirth. Like a newborn, your past sins are washed away. You begin with a clean slate.",
                 "Prenez un bain complet - lavant tout le corps - comme symbole de renaissance spirituelle. Comme un nouveau-ne, vos peches passes sont effaces.",
                 "Toma un bano completo - lavando todo el cuerpo - como simbolo de renacimiento espiritual. Como un recien nacido, tus pecados pasados son borrados.",
                 "Nimm ein vollstaendiges Bad - wasche den ganzen Koerper - als Zeichen geistiger Wiedergeburt. Wie ein Neugeborenes sind deine Suenden abgewaschen.",
                 "Fai un bagno completo - lavando tutto il corpo - come simbolo di rinascita spirituale. Come un neonato, i tuoi peccati passati sono cancellati.",
                 "Tome um banho completo - lavando todo o corpo - como simbolo de renascimento espiritual. Como um recem-nascido, seus pecados passados sao apagados.",
                 "Poora ghusl karo - pura jism dhoyo - roohani nayi zindagi ki nishani ke taur par. Naye bachche ki tarah aapke pichhle gunah dhul jate hain."),
    },
    {
        "num": 4,
        "icon": "4",
        "title": L("Begin to Learn","Commencer a Apprendre","Comenzar a Aprender","Anfangen zu Lernen","Iniziare a Imparare","Comecar a Aprender","Seekhna Shuru Karo"),
        "text": L("Learn the five daily prayers, read the Quran daily (even a few verses), fast in Ramadan, give charity, and connect with your local mosque. Take it one step at a time - Allah loves steady deeds.",
                 "Apprenez les cinq prieres quotidiennes, lisez le Coran chaque jour, jeûnez pendant le Ramadan, donnez la charite, et connectez-vous a votre mosquee locale.",
                 "Aprende las cinco oraciones diarias, lee el Coran cada dia, ayuna en Ramadan, da caridad, y conectate con tu mezquita local.",
                 "Lerne die fuenf taeglichen Gebete, lies den Koran taeglich, faste im Ramadan, spende und verbinde dich mit deiner Moschee.",
                 "Impara le cinque preghiere quotidiane, leggi il Corano ogni giorno, digiuna in Ramadan, dai l'elemosina, e connettiti alla tua moschea.",
                 "Aprenda as cinco oracoes diarias, leia o Alcorao diariamente, jejue no Ramada, de caridade, e conecte-se a sua mesquita local.",
                 "Paanch namazein seekho, roz Quran padho, Ramadan mein roza rakho, zakat do, aur apni local masjid se jude raho. Ek-ek qadam lo - Allah ko hamesha wale kaam pasand hain."),
    },
]

# After becoming Muslim - what to do
AFTER = [
    L("Learn the 5 daily prayers","Apprendre les 5 prieres quotidiennes","Aprender las 5 oraciones diarias","Die 5 Gebete lernen","Imparare le 5 preghiere","Aprender as 5 oracoes","Paanch namaz seekho"),
    L("Read a few verses of the Quran daily","Lire quelques versets du Coran chaque jour","Leer algunos versiculos del Coran cada dia","Taeglich einige Koranverse lesen","Leggere alcuni versetti ogni giorno","Ler alguns versiculos diariamente","Roz thodi ayat padho"),
    L("Fast during Ramadan","Jeûner pendant le Ramadan","Ayunar en Ramadan","Im Ramadan fasten","Digiunare in Ramadan","Jejuar no Ramada","Ramadan mein roza rakho"),
    L("Give charity (Zakat) to the poor","Donner la zakat aux pauvres","Dar zakat a los pobres","Zakat den Armen geben","Dare la zakat ai poveri","Dar zakat aos pobres","Zakat ghareebon ko do"),
    L("Visit a local mosque","Visiter une mosquee locale","Visitar una mezquita local","Eine Moschee besuchen","Visitare una moschea","Visitar uma mesquita","Local masjid jao"),
    L("Learn from trustworthy teachers","Apprendre de professeurs fiables","Aprender de maestros confiables","Von zuverlaessigen Lehrern lernen","Imparare da insegnanti affidabili","Aprender com professores confiaveis","Bharosemand ustaadon se seekho"),
    L("Avoid what Allah forbade - one step at a time","Eviter ce qu'Allah a interdit - pas a pas","Evitar lo que Allah prohibio - paso a paso","Meiden, was Allah verboten hat - Schritt fuer Schritt","Evitare cio che Allah ha proibito - passo dopo passo","Evitar o que Allah proibiu - passo a passo","Jo Allah ne mana kiya usse bacho - ek-ek qadam"),
    L("Ask Allah for guidance every day","Demander la guidée a Allah chaque jour","Pedir guia a Allah cada dia","Allah taeglich um Fuehrung bitten","Chiedere guida ad Allah ogni giorno","Pedir guia a Allah todo dia","Allah se roz hidayat mango"),
]

# New Muslim stories
STORIES = [
    {
        "name": "Yusuf Estes",
        "country": L("United States","Etats-Unis","Estados Unidos","Vereinigte Staaten","Stati Uniti","Estados Unidos","America"),
        "story": L("An American Christian preacher who studied Islam to refute it - and ended up embracing it. He became one of the most famous Muslim speakers in the English-speaking world.",
                   "Un predicateur chretien americain qui a etudie l'Islam pour le refuter - et a fini par l'embrasser. Il est devenu l'un des conferenciers musulmans les plus connus.",
                   "Un predicador cristiano estadounidense que estudio el Islam para refutarlo - y termino abrazandolo. Se convirtio en uno de los oradores musulmanes mas famosos.",
                   "Ein amerikanischer christlicher Prediger, der den Islam studierte, um ihn zu widerlegen - und ihn schliesslich annahm.",
                   "Un predicatore cristiano americano che studio l'Islam per confutarlo - e fini per abbracciarlo.",
                   "Um pregador cristao americano que estudou o Isla para refuta-lo - e acabou abracando-o.",
                   "Ek Ameriki Isai padri jis ne Islam ko jhutlane ke liye padha - aur khud Islam qubool kar liya."),
    },
    {
        "name": "Aminah Assilmi",
        "country": L("United States","Etats-Unis","Estados Unidos","Vereinigte Staaten","Stati Uniti","Estados Unidos","America"),
        "story": L("An American feminist and Christian who set out to prove Islam wrong. After months of study, she found the truth she had been seeking all her life. She said: 'Islam gave me peace I never knew.'",
                   "Une feministe americaine chretienne qui voulait prouver que l'Islam etait faux. Apres des mois d'etude, elle trouva la verite qu'elle cherchait toute sa vie.",
                   "Una feminista cristiana estadounidense que queria probar que el Islam era falso. Tras meses de estudio, encontro la verdad.",
                   "Eine amerikanische Feministin und Christin, die den Islam widerlegen wollte. Nach Monaten des Studiums fand sie die Wahrheit.",
                   "Una femminista cristiana americana che voleva provare che l'Islam era falso. Dopo mesi di studio, trovo la verita.",
                   "Uma feminista crista americana que queria provar que o Isla era falso. Depois de meses de estudo, encontrou a verdade.",
                   "Ek Ameriki feminist Isai khatoon jis ne Islam ko galat sabit karna chaha. Mahino ki padhai ke baad, usse sach mila."),
    },
    {
        "name": "Hamza Yusuf",
        "country": L("United States","Etats-Unis","Estados Unidos","Vereinigte Staaten","Stati Uniti","Estados Unidos","America"),
        "story": L("Born Mark Hanson, an Irish-American from a Christian family. He converted at 19 after reading the Quran. Today he is one of the most respected Islamic scholars in the West.",
                   "Ne Mark Hanson, un americain d'origine irlandaise. Converti a 19 ans apres avoir lu le Coran. Aujourd'hui l'un des savants islamiques les plus respectes.",
                   "Nacido Mark Hanson, un irlandes-estadounidense. Se convirtio a los 19 anos tras leer el Coran. Hoy es uno de los sabios mas respetados.",
                   "Geboren als Mark Hanson, irisch-amerikanischer Herkunft. Konvertierte mit 19 nach dem Lesen des Korans. Heute einer der angesehensten Gelehrten.",
                   "Nato Mark Hanson, irlandese-americano. Si converti a 19 anni dopo aver letto il Corano. Oggi uno degli studiosi piu rispettati.",
                   "Nascido Mark Hanson, irlandes-americano. Converteu-se aos 19 anos apos ler o Alcorao. Hoje um dos sabios mais respeitados.",
                   "Mark Hanson ke naam se paida hue, Irish-American. 19 saal ki umar mein Quran padh kar Muslim bane. Aaj maghrib ke sab se izzat wale ulema mein se hain."),
    },
]
