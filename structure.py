from imports import *
from constants import *

sys.path.append("./")

script_dir = os.path.dirname("calender.ipynb")
FONT_FILE_NAME = "saxmono.ttf"
FONT_FILE_PATH = os.path.join(script_dir, "misc", "fonts", FONT_FILE_NAME)
ICONS_FOLDER_PATH = os.path.join(script_dir, "icons")
pdfmetrics.registerFont(TTFont("CustomFont", FONT_FILE_PATH))

ROOT_DIR = Path(sys.path[-1]).resolve()

FRONT_PDF = ROOT_DIR / "inlay_front" / "inlay_front_page.pdf"
MONTH_DIR = ROOT_DIR / "inlay_month"
WEEK_DIR = ROOT_DIR / "inlay_week"

OUTPUT_PDF = ROOT_DIR / "bullet_journal.pdf"
