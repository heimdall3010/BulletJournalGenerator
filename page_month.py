from imports import *
from constants import *
from structure import *
from helper import *

sys.path.append("./")


def generate_note_page(year, month):
    """
    Generate the HTML content for the monthly notes page.

    The function creates a centered notes-page header containing the title
    "Notes", a decorative horizontal line, and the current month-year label.
    The centering is calculated based on the visible text length, while the
    HTML formatting tags are added afterwards.

    Args:
        year (int): The calendar year displayed on the notes page.
        month (int): The month number, from 1 to 12.

    Returns:
        str: HTML-formatted content for the notes-page header.
    """

    # Get the localized month name from the global MONTH_NAMES list.
    month_name = MONTH_NAMES[month - 1]

    # Define the visible text elements used in the notes-page header.
    title = "Notes"
    date_text = f"{month_name} | {year}"
    line = "_" * 35

    # Calculate the number of non-breaking spaces needed to center each line.
    title_spaces = (SYMBOL_PER_LINE - len(title)) // 2
    line_spaces = (SYMBOL_PER_LINE - len(line)) // 2
    date_spaces = (SYMBOL_PER_LINE - len(date_text)) // 2

    # Build the HTML string for the notes-page header.
    # Only the visible text is used for centering; HTML tags are added afterwards.
    note_page_header = (
        "&nbsp;" * title_spaces
        + f"<strong>{title}</strong><br/>"
        + "&nbsp;" * line_spaces
        + line
        + "<br/><br/>"
        + "&nbsp;" * date_spaces
        + f"<strong>{date_text}</strong><br/><br/>"
    )

    return note_page_header


def generate_month_overview(year, month):
    """
    Generate the HTML content for a monthly calendar overview.

    The function creates a two-column-like monthly overview. The first half
    of the month is written on the left side, and the corresponding later
    days of the month are written on the right side. Important dates are added
    to the respective days when they are configured for the monthly view.

    Args:
        year (int): The calendar year.
        month (int): The month number, from 1 to 12.

    Returns:
        str: HTML-formatted content for the monthly overview page.
    """

    # Get the localized month name and calendar metadata for the selected month.
    month_name = MONTH_NAMES[month - 1]
    num_days = calendar.monthrange(year, month)[1]
    first_weekday = calendar.weekday(year, month, 1)

    # Start the monthly overview with a bold month-year header.
    month_overview = f"<strong>{month_name} | {year}</strong><br/>"
    month_overview += "_" * 30 + "<br/><br/><br/>"

    # Track the weekday while iterating through the days of the month.
    current_weekday = first_weekday

    # Iterate through the first part of the month.
    # The later part is added beside it using day + 16.
    for day in range(1, num_days - 14):

        # Add weekday abbreviation for the current left-side day.
        month_overview += WEEKDAY_NAMES[current_weekday] + " "

        # Format single-digit days with a leading zero.
        if day < 10:
            month_overview += f"0{day}.{month}"

            # Collect important dates for the current day in monthly view.
            important_dates = add_important_dates(day, month, year, "month")
            dates = ""

            # Convert all matching important dates into one display string.
            for date in important_dates:
                dates += " " + date

        else:
            month_overview += f"{day}.{month}"

            # Collect important dates for the current day in monthly view.
            important_dates = add_important_dates(day, month, year, "month")
            dates = ""

            # Convert all matching important dates into one display string.
            for date in important_dates:
                dates += " " + date

        # Add important-date text after the current date.
        month_overview += dates

        # Add spacing between the left-side and right-side date columns.
        # If images are included, the string length is adjusted because HTML tags
        # make the string longer than the visible content.
        if len(dates):
            if "<img src=" in dates:
                month_overview += "&nbsp;" * (25 - (len(dates) - 47))
            else:
                month_overview += "&nbsp;" * (25 - len(dates))
        else:
            month_overview += "&nbsp;" * 25

        # Move to the next weekday.
        current_weekday = (current_weekday + 1) % 7

        # Calculate the weekday for the right-side day.
        current_weekday_2 = (current_weekday + 15) % 7

        # Add the corresponding right-side day if it still belongs to the month.
        if day + 16 <= num_days:
            month_overview += WEEKDAY_NAMES[current_weekday_2] + " "
            month_overview += f"{day+16}.{month}"

            # Collect important dates for the right-side day in monthly view.
            important_dates_2 = add_important_dates(day + 16, month, year, "month")
            dates_2 = ""

            # Convert all matching important dates into one display string.
            for date_2 in important_dates_2:
                dates_2 += " " + date_2

            # Add important-date text after the right-side date.
            month_overview += dates_2

            # Add vertical spacing before the next row.
            month_overview += "<br/><br/><br/>"

    return month_overview


def create_monthly_inlay(year):
    """
    Create one monthly inlay PDF for each month of the selected year.

    The function iterates over all twelve months, creates the required output
    folder if necessary, generates a monthly overview page and a notes page,
    and writes both pages into a separate PDF file for each month.

    Each generated PDF is saved as "inlay_month_X.pdf" inside the
    "inlay_month" folder, where X is the month number.

    Args:
        year (int): The calendar year for which the monthly PDFs are created.

    Returns:
        None
    """

    # Generate one PDF file for each month of the year.
    for month in range(1, 13):

        # Define the output file name and target folder for the current month.
        file_name = f"inlay_month_{month}.pdf"
        folder_name = "inlay_month"
        folder_path = os.path.join(os.path.dirname(file_name), folder_name)

        # Create the output folder if it does not exist yet.
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Create the ReportLab PDF document for the current monthly inlay.
        doc = SimpleDocTemplate(os.path.join(folder_path, file_name), pagesize=A4)

        # Define the paragraph style used for all monthly inlay content.
        custom_style = ParagraphStyle(
            name="CustomStyle", fontSize=12, fontName="CustomFont"
        )

        # Generate the monthly overview page and the notes page.
        month_overview = generate_month_overview(year, month)
        note_overview = generate_note_page(year, month)

        # Add both pages to the global monthly PDF element list.
        elementsInMonthlyInlay_PDF.extend(
            [
                Paragraph(month_overview, style=custom_style),
                PageBreak(),
                Paragraph(note_overview, style=custom_style),
                PageBreak(),
            ]
        )

        # Build and save the PDF for the current month.
        doc.build(elementsInMonthlyInlay_PDF)
