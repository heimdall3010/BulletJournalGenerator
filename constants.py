LANG = "en"

elementsInMonthlyInlay_PDF = []
elementsInWeeklyInlay_PDF = []

SYMBOL_PER_LINE = 67
HALF_LINE = SYMBOL_PER_LINE // 2 + 1


WEEKDAY_NAMES_de = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
MONTH_NAMES_de = [
    "Januar",
    "Februar",
    "März",
    "April",
    "Mai",
    "Juni",
    "Juli",
    "August",
    "September",
    "Oktober",
    "November",
    "Dezember",
]


WEEKDAY_NAMES_en = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MONTH_NAMES_en = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

if LANG == "de":
    WEEKDAY_NAMES = WEEKDAY_NAMES_de
    MONTH_NAMES = MONTH_NAMES_de

if LANG == "en":
    WEEKDAY_NAMES = WEEKDAY_NAMES_en
    MONTH_NAMES = MONTH_NAMES_en


IMPORTANT_DATES = [
    # List structure
    # [
    # 	0	day,
    # 	1	month,
    # 	2	name,
    # 	3	file.png,
    # 	4	year,
    # 	5	view: ["week", "month"] beides, ["week"] nur Wochenansicht, ["month"] nur Monatsansicht
    # ]
    # Personal

    # B-days Musicians
    [6, 1, "Scriabin", "cake.png", 1872, ["week", "month"]],
    [27, 1, "Mozart", "cake.png", 1756, ["week", "month"]],
    [31, 1, "Schubert", "cake.png", 1797, ["week", "month"]],
    [3, 2, "Felix Mendelssohn", "cake.png", 1756, ["week", "month"]],
    #[23, 2, "Händel", "cake.png", 1685, ["week", "month"]],
    #[4, 3, "Vivaldi", "cake.png", 1678, ["week", "month"]],
    [31, 3, "Bach", "cake.png", 1685, ["week", "month"]],
    [31, 3, "Haydn", "cake.png", 1732, ["week", "month"]],
    [1, 3, "Chopin", "cake.png", 1810, ["week", "month"]],
    [7, 3, "Ravel", "cake.png", 1875, ["week", "month"]],
    [18, 3, "Rimsky-Korsakov", "cake.png", 1844, ["week", "month"]],
    [1, 4, "Rachmaninoff", "cake.png", 1873, ["week", "month"]],
    [23, 4, "Leoncavallo", "cake.png", 1857, ["week", "month"]],
    [14, 5, "E. Mayer", "cake.png", 1812, ["week", "month"]],
    [17, 5, "Satie", "cake.png", 1866, ["week", "month"]],
    [7, 5, "Brahms", "cake.png", 1833, ["week", "month"]],
    [12, 5, "Fauré", "cake.png", 1845, ["week", "month"]],
    [22, 5, "Wagner", "cake.png", 1813, ["week", "month"]],
    [2, 6, "Gluck", "cake.png", 1714, ["week", "month"]],
    [8, 6, "R. Schumann", "cake.png", 1810, ["week", "month"]],
    [15, 6, "Grieg", "cake.png", 1843, ["week", "month"]],
    #[17, 6, "Stravinsky", "cake.png", 1882, ["week", "month"]],
    #[7, 7, "Mahler", "cake.png", 1860, ["week", "month"]],
    [22, 8, "Debussy", "cake.png", 1862, ["week", "month"]],
    [13, 9, "C. Schumann", "cake.png", 1819, ["week", "month"]],
    [25, 9, "Schostakowitsch", "cake.png", 1975, ["week", "month"]],
    [9, 10, "Saint-Saëns", "cake.png", 1835, ["week", "month"]],
    [10, 10, "Verdi", "cake.png", 1813, ["week", "month"]],
    [22, 10, "Liszt", "cake.png", 1811, ["week", "month"]],
    #[27, 10, "Paganini", "cake.png", 1782, ["week", "month"]],
    [6, 11, "Tschaikowski", "cake.png", 1893, ["week", "month"]],
    [14, 11, "Fanny Mendelssohn", "cake.png", 1805, ["week", "month"]],
    [17, 12, "Beethoven", "cake.png", 1858, ["week", "month"]],
    [22, 12, "Puccini", "cake.png", 1858, ["week", "month"]],
    # B-days Scientists
    # [23, 7, "Turing","cake.png",1912,["week"]],
    # [14, 3, "Einstein","cake.png",1879,["week"]],
    # [7, 12, "Chomsky","cake.png",1928,["week"]],
    # [13, 3, "Grice","cake.png",1913,["week"]],
    # Holidays
    [1, 1, "New Year", "party.png","",["week", "month"]],
    [24, 12, "X-Mas", "xmas.png","",["week", "month"]],
    [25, 12, "1. X-Mas", "xmas.png","",["week", "month"]],
    [26, 12, "2. X-Mas", "xmas.png","",["week", "month"]],
    [31, 12, "New Year's Eve", "party.png","",["week", "month"]],
    [1, 5, "Tag d. Arbeit", "", 1919,["week", "month"]],
    [3, 10, "D-Einheit", "", 1990,["week", "month"]],
    # Dynamic Holidays

]
