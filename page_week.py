from imports import *
from constants import *
from structure import *
from helper import *

sys.path.append("./")


def generate_weekly_overview(year):
    """
    Generate the HTML content for all weekly bullet journal pages.

    The function creates a list of weekly layouts for the given year. Each week
    consists of two HTML strings: one for the first half of the week
    (Monday to Wednesday) and one for the second half of the week
    (Thursday to Sunday).

    The first calendar week is calculated from the Monday belonging to KW 1.
    The function then iterates through all weekdays, adds date labels, empty
    writing lines, important dates, and week headers. Each generated week is
    appended to a list and later used to create individual weekly PDF files.

    Args:
        year (int): The calendar year for which the weekly overview is generated.

    Returns:
        list: A list of weekly layouts. Each item contains two HTML strings:
              one for the first weekly page and one for the second weekly page.
    """

    # Determine the first Monday belonging to calendar week 1.
    day = get_kw_1_monday(year)

    # Calculate how many weekly layouts need to be generated for the year.
    num_weeks_of_year = num_weeks_in_year(year)

    # Initialize counters for days and calendar weeks.
    day_counter = 1
    kw_counter = 1

    # Start the calendar generation in January.
    month = 1

    # Get the number of days in the current month.
    num_days_of_month = calendar.monthrange(year, month)[1]

    # Get the localized month name for the current month.
    month_name = MONTH_NAMES[month - 1]

    # Store all generated weekly layouts.
    weekly_layout_list = []

    # Store the HTML content for the first and second page of each week.
    weekly_overview_1 = ""
    weekly_overview_2 = ""

    # Generate weekly layouts until all calendar weeks have been processed.
    while kw_counter <= num_weeks_of_year:

        # Iterate through all weekday names defined in the selected language.
        for weekday_name in WEEKDAY_NAMES:

            # Add the centered week header to the first weekly page.
            if weekday_name == WEEKDAY_NAMES[0]:
                header_text = f"KW {kw_counter} | {month_name} | {year}"
                header_spaces = (SYMBOL_PER_LINE - len(header_text)) // 2

                weekly_overview_1 += "&nbsp;" * header_spaces
                weekly_overview_1 += f"<strong>{header_text}</strong>"
                weekly_overview_1 += "<br/><br/><br/>"

            # Add Monday, Tuesday, and Wednesday to the first weekly page.
            if weekday_name in (WEEKDAY_NAMES[0], WEEKDAY_NAMES[1], WEEKDAY_NAMES[2]):
                weekly_overview_1 += weekday_name + "  "

                # Define possible negative or zero dates that may occur when
                # the first calendar week starts in the previous year.
                date_correction_days = [0, -1, -2, -3, -4, -5, -6, -7]

                # Correct dates that belong to December of the previous year.
                if day in date_correction_days and month == 1:
                    day = 31 - (-1 * day)
                    month = 12
                    year = year - 1

                # Add the date and a writing line for the current weekday.
                weekly_overview_1 += f"{day}.{month}<br/>"
                weekly_overview_1 += "_" * 18
                weekly_overview_1 += "<br/><br/>"

                # Add important dates configured for the weekly view.
                if add_important_dates(day, month, year, "week"):
                    date_list = add_important_dates(day, month, year, "week")
                    for date in date_list:
                        weekly_overview_1 += date + "<br/>"

                # Add vertical spacing after Monday and Tuesday.
                if weekday_name != WEEKDAY_NAMES[2]:
                    weekly_overview_1 += "<br/>" * 16

            # Add the centered week header to the second weekly page.
            if weekday_name == WEEKDAY_NAMES[3]:
                header_text = f"KW {kw_counter} | {month_name} | {year}"
                header_spaces = (SYMBOL_PER_LINE - len(header_text)) // 2

                weekly_overview_2 += "&nbsp;" * header_spaces
                weekly_overview_2 += f"<strong>{header_text}</strong>"
                weekly_overview_2 += "<br/><br/><br/>"

            # Add Thursday and Friday to the second weekly page.
            if weekday_name in (WEEKDAY_NAMES[3], WEEKDAY_NAMES[4]):
                weekly_overview_2 += weekday_name + "  "
                weekly_overview_2 += f"{day}.{month}<br/>"
                weekly_overview_2 += "_" * 18
                weekly_overview_2 += "<br/><br/>"

                # Add important dates configured for the weekly view.
                if add_important_dates(day, month, year, "week"):
                    date_list = add_important_dates(day, month, year, "week")
                    for date in date_list:
                        weekly_overview_2 += date + "<br/>"

                # Add vertical spacing after Thursday and Friday.
                weekly_overview_2 += "<br/>" * 16

            # Add Saturday and Sunday in one shared weekend section.
            if weekday_name == WEEKDAY_NAMES[5]:
                weekly_overview_2 += weekday_name + " "
                weekly_overview_2 += f"{day}.{month}" + "&nbsp;" * 25
                weekly_overview_2 += WEEKDAY_NAMES[6] + " "

                # Prepare the Sunday date.
                so_day = 1
                so_month = month

                # If Sunday is still in the current month, use the next day.
                # Otherwise, move Sunday to the first day of the next month.
                if (day + 1) <= num_days_of_month:
                    so_day = day + 1
                else:
                    so_month = month + 1

                # Add the Sunday date and one long weekend writing line.
                weekly_overview_2 += f"{so_day}.{so_month}" + "<br/>"
                weekly_overview_2 += "_" * 55
                weekly_overview_2 += "<br/><br/>"

                # Add important dates for Saturday and Sunday if available.
                if add_important_dates(day, month, year, "week") or add_important_dates(
                    day + 1, month, year, "week"
                ):
                    date_list_sa = add_important_dates(day, month, year, "week")
                    date_list_so = add_important_dates(day + 1, month, year, "week")

                    # Determine how many date entries can be printed side by side.
                    date_amount_min = min(len(date_list_sa), len(date_list_so))
                    date_amount_max = max(len(date_list_sa), len(date_list_so))

                    # Add paired Saturday and Sunday entries on the same line.
                    for i in range(date_amount_min):
                        weekly_overview_2 += (
                            date_list_sa[i]
                            + "&nbsp;" * (32 - len(date_list_sa[i]))
                            + date_list_so[i]
                            + "<br/><br/>"
                        )

                    # Add remaining Saturday entries if Saturday has more entries.
                    if len(date_list_so) < len(date_list_sa):
                        for i in range(date_amount_min, date_amount_max):
                            weekly_overview_2 += date_list_sa[i] + "<br/><br/>"

                    # Add remaining Sunday entries if Sunday has more entries.
                    if len(date_list_so) > len(date_list_sa):
                        for i in range(date_amount_min, date_amount_max):
                            weekly_overview_2 += (
                                "&nbsp;" * 32 + date_list_so[i] + "<br/><br/>"
                            )

            # Once seven days have been processed, save the current weekly layout.
            if day_counter % 7 == 0:
                kw_counter += 1
                weekly_layout_list.append([weekly_overview_1, weekly_overview_2])
                weekly_overview_1 = ""
                weekly_overview_2 = ""

            # Move to the next day.
            if day <= num_days_of_month:
                day += 1

            # If the current month is finished, move to the next month.
            if day > num_days_of_month:
                if month < 12:
                    month += 1
                else:
                    month = 1
                    year += 1

                # Refresh month-specific metadata after changing the month.
                num_days_of_month = calendar.monthrange(year, month)[1]
                month_name = MONTH_NAMES[month - 1]
                day = 1

            # Count the processed calendar day.
            day_counter += 1

    return weekly_layout_list


def create_weekly_inlay(year):
    """
    Create one weekly inlay PDF for each generated calendar week.

    The function first generates all weekly layouts for the selected year.
    Then it creates one PDF file per week. Each weekly PDF contains two pages:
    the first page for Monday to Wednesday and the second page for Thursday
    to Sunday.

    Each generated PDF is saved as "inlay_week_X.pdf" inside the
    "inlay_week" folder, where X is the week number.

    Args:
        year (int): The calendar year for which the weekly PDFs are created.

    Returns:
        None
    """

    # Generate all weekly HTML layouts for the selected year.
    weekly_layout = generate_weekly_overview(year)

    # Create one PDF file for each generated week.
    for index, week in enumerate(weekly_layout):

        # Define the output file name and target folder for the current week.
        file_name = f"inlay_week_{index + 1}.pdf"
        folder_name = "inlay_week"
        folder_path = os.path.join(os.path.dirname(file_name), folder_name)

        # Create the output folder if it does not exist yet.
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Create the ReportLab PDF document for the current weekly inlay.
        doc = SimpleDocTemplate(os.path.join(folder_path, file_name), pagesize=A4)

        # Define the paragraph style used for the weekly inlay content.
        custom_style = ParagraphStyle(
            name="CustomStyle", fontSize=12, fontName="CustomFont"
        )

        # Create the two-page content structure for the current week.
        elements = [
            Paragraph(week[0], style=custom_style),
            PageBreak(),
            Paragraph(week[1], style=custom_style),
        ]

        # Build and save the PDF for the current week.
        doc.build(elements)
