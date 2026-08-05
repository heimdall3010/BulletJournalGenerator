import argparse

from page_front import *
from page_month import *
from page_week import *
from page_merge import *


def create_bullet_journal(year=2026):
    """
    Create the complete bullet journal PDF for a given year.

    This function runs the full PDF generation pipeline. First, it creates the
    front page. Then, it creates all monthly inlay PDFs and all weekly inlay
    PDFs. Finally, it merges the generated PDFs into one complete bullet
    journal file.

    Args:
        year (int, optional): The calendar year for which the bullet journal
            should be created. Defaults to 2026.

    Returns:
        None
    """

    # Create the front page PDF for the selected year.
    create_front_page(year)

    # Create all monthly inlay PDFs for the selected year.
    create_monthly_inlay(year)

    # Create all weekly inlay PDFs for the selected year.
    create_weekly_inlay(year)

    # Merge the generated front, monthly, and weekly PDFs into one final PDF.
    merge_pdf([5,4,4,5,4,4,5,4,4,5,4,4])


if __name__ == "__main__":

    # Create a command-line argument parser for the script.
    parser = argparse.ArgumentParser(
        description="Create a bullet journal PDF for a given year."
    )

    # Add an optional positional argument for the year.
    # If no year is provided in the terminal, the default year 2026 is used.
    parser.add_argument(
        "year",
        nargs="?",
        type=int,
        default=2026,
        help="Year for the bullet journal, e.g. 2027. Default: 2026.",
    )

    # Parse the command-line arguments.
    args = parser.parse_args()

    # Start the bullet journal generation with the selected year.
    # e.g. python3 main.py 2027
    create_bullet_journal(args.year)
