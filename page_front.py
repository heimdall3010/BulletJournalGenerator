from imports import *
from constants import *
from structure import *
from helper import *

sys.path.append("./")


def generate_front_page(year):
    """
    Generate the HTML content for the bullet journal front page.

    The function creates a simple centered front page layout containing the
    title "Bullet Journal", a decorative horizontal line, and the selected
    calendar year. The visible text length is used to calculate the number
    of non-breaking spaces required for approximate horizontal centering.

    Args:
        year (int): The calendar year displayed on the front page.

    Returns:
        str: HTML-formatted content for the front page.
    """

    # Define the visible text elements used on the front page.
    title = "Bullet Journal"
    year_text = str(year)
    line = "_" * 30

    # Calculate the number of non-breaking spaces needed to center each line.
    title_spaces = (SYMBOL_PER_LINE - len(title)) // 2
    line_spaces = (SYMBOL_PER_LINE - len(line)) // 2
    year_spaces = (SYMBOL_PER_LINE - len(year_text)) // 2

    # Build the HTML string for the front page.
    # Only the visible text is used for the centering calculation,
    # while the <strong> tags are added afterwards for formatting.
    note_front_page = (
        "&nbsp;" * title_spaces
        + f"<strong>{title}</strong>"
        + "<br/><br/>"
        + "&nbsp;" * line_spaces
        + line
        + "<br/><br/>"
        + "&nbsp;" * year_spaces
        + f"<strong>{year_text}</strong>"
        + "<br/>"
    )

    return note_front_page


def create_front_page(year):
    """
    Create the front page PDF for the bullet journal.

    The function creates the output folder for the front-page PDF if it does
    not already exist. It then generates the front-page HTML content, wraps it
    in a ReportLab Paragraph, and writes it to a PDF file.

    The resulting PDF is saved as "inlay_front_page.pdf" inside the
    "inlay_front" folder.

    Args:
        year (int): The calendar year used for the front page.

    Returns:
        None
    """

    # Define the PDF file name and the folder in which it should be stored.
    file_name = f"inlay_front_page.pdf"
    folder_name = "inlay_front"

    # Build the folder path for the generated front-page PDF.
    folder_path = os.path.join(os.path.dirname(file_name), folder_name)

    # Create the output folder if it does not exist yet.
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Create the ReportLab PDF document.
    doc = SimpleDocTemplate(os.path.join(folder_path, file_name), pagesize=A4)

    # Define the paragraph style used for the front-page content.
    custom_style = ParagraphStyle(
        name="CustomStyle", fontSize=12, fontName="CustomFont"
    )

    # Generate the HTML-formatted front-page content.
    front_page_overview = generate_front_page(year)

    # Add the front-page paragraph to the global PDF element list.
    elementsInMonthlyInlay_PDF.extend(
        [
            Paragraph(front_page_overview, style=custom_style),
        ]
    )

    # Build and save the final front-page PDF.
    doc.build(elementsInMonthlyInlay_PDF)
