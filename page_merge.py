from imports import *
from constants import *
from structure import *
from helper import *

sys.path.append("./")


def add_pdf(writer, pdf_path):
    """
    Add all pages of a single PDF file to an existing PdfWriter object.

    The function opens the PDF file from the given path, reads all pages in
    their original order, and appends them to the provided PdfWriter instance.
    This is used as a helper function for assembling the final bullet journal
    PDF from multiple smaller PDF files.

    Args:
        writer (PdfWriter): The PdfWriter object that collects the pages.
        pdf_path (Path): The path to the PDF file that should be added.

    Returns:
        None
    """

    # Open the PDF file as a PdfReader object.
    reader = PdfReader(str(pdf_path))

    # Add every page of the input PDF to the output writer.
    for page in reader.pages:
        writer.add_page(page)


def merge_pdf(interval_list=None):
    """
    Merge the generated bullet journal PDFs into one final PDF file.

    The function creates a new PdfWriter object and appends the individual
    bullet journal parts in the desired order. First, it adds the front page.
    Then, for each month, it adds the corresponding monthly PDF followed by
    a configurable number of weekly PDFs.

    The number of weekly PDFs after each month is defined by interval_list.

    Example:
        interval_list = [4, 4, 5, 4, 4, 5, 4, 4, 5, 4, 4, 5]

    This means:
        Month 1 -> 4 weeks
        Month 2 -> 4 weeks
        Month 3 -> 5 weeks
        ...

    Args:
        interval_list (list, optional): A list with 12 integer values.
            Each value defines how many weekly PDFs should be added after
            the corresponding month. Defaults to 4 weeks per month.

    Returns:
        None
    """

    # Use a default interval list if no custom list is provided.
    if interval_list is None:
        interval_list = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]

    # Check that the interval list contains exactly one value per month.
    if len(interval_list) != 12:
        raise ValueError("interval_list must contain exactly 12 values.")

    # Create a PdfWriter object for the final merged PDF.
    writer = PdfWriter()

    # Add the front page as the first page of the bullet journal.
    add_pdf(writer, FRONT_PDF)

    # Start counting weekly PDFs from week 1.
    week_number = 1

    # Add each monthly PDF followed by the configured number of weekly PDFs.
    for month_number in range(1, 13):

        # Build the path to the current monthly PDF.
        month_pdf = MONTH_DIR / f"inlay_month_{month_number}.pdf"

        # Add the current monthly PDF to the final document.
        add_pdf(writer, month_pdf)

        # Get the number of weekly PDFs that should follow this month.
        week_interval = interval_list[month_number - 1]

        # Add the configured number of weekly PDFs after the current month.
        for i in range(week_interval):

            # Stop if all 52 weekly PDFs have already been added.
            if week_number > 52:
                break

            # Build the path to the current weekly PDF.
            week_pdf = WEEK_DIR / f"inlay_week_{week_number}.pdf"

            # Add the current weekly PDF to the final document.
            add_pdf(writer, week_pdf)

            # Move to the next weekly PDF.
            week_number += 1

    # Write the complete merged PDF to the root output file.
    with open(OUTPUT_PDF, "wb") as file:
        writer.write(file)

    # Print the location of the generated bullet journal PDF.
    print(f"Bullet Journal wurde erstellt: {OUTPUT_PDF}")
