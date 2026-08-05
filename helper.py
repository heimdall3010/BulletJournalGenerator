from imports import *
from constants import *
from structure import *

sys.path.append("./")


def add_important_dates(day, month, year, view):
    """
    Return all important dates that match a specific calendar day.

    The function checks the global IMPORTANT_DATES list and selects all entries
    that match the given day and month. It also checks whether the requested
    view type, for example "week" or "month", is enabled for the date entry.

    If an icon is assigned to the date entry, the function creates an HTML
    image tag with an appropriate icon size. If the date entry contains a
    reference year, the current anniversary or age is added to the output.

    Args:
        day (int): The day of the month.
        month (int): The month number.
        year (int): The current calendar year.
        view (str): The view in which the date should appear, e.g. "week" or "month".

    Returns:
        list: A list of HTML-formatted date entries for the given day.
    """

    # Store all matching date entries for the requested day.
    date_list = []

    # Temporary string for one formatted important-date entry.
    date_entry = ""

    # Iterate over all globally defined important dates.
    for important_date in IMPORTANT_DATES:

        # Check whether day, month, and view match the current important-date entry.
        if (
            important_date[0] == day
            and important_date[1] == month
            and (view in important_date[5])
        ):

            # If the entry has an icon file, create an HTML image element.
            if important_date[3] != "":
                date_entry = f"<img src='{ICONS_FOLDER_PATH}/{important_date[3]}'"

                # Use custom icon dimensions for specific icon types.
                if important_date[3] == "cake.png":
                    date_entry += f"width='15' height='15'/> "
                elif important_date[3] == "heart.png":
                    date_entry += f"width='22' height='22'/> "
                elif important_date[3] == "ramadan.png":
                    date_entry += f"width='37' height='33'/> "
                elif important_date[3] == "easter.png":
                    date_entry += f"width='30' height='30'/> "
                else:
                    date_entry += f"width='20' height='20'/> "

                # Add the visible name of the important date after the icon.
                date_entry += f"{important_date[2]}"

            # If no icon is defined, use only the plain date name.
            if important_date[3] == "":
                date_entry = important_date[2]

            # If a reference year is given, add the calculated year difference.
            if important_date[4] != "":
                date_entry += f" {year - important_date[4]}"

            # Add the final formatted entry to the result list.
            date_list.append(date_entry)

    return date_list


def num_weeks_in_year(year):
    """
    Calculate the number of calendar weeks generated for the given year.

    The function iterates over all twelve months and estimates how many weekly
    blocks are needed based on the number of days in each month and the weekday
    of the first day of the month.

    Args:
        year (int): The calendar year.

    Returns:
        int: The calculated number of weeks for the given year.
    """

    # Store the accumulated number of weeks.
    num_weeks = 0

    # Iterate through all months of the year.
    for month in range(1, 13):

        # Get the number of days in the current month.
        num_days = calendar.monthrange(year, month)[1]

        # Add the number of required week rows for the current month.
        num_weeks += (num_days + calendar.weekday(year, month, 1)) // 7

    return num_weeks


def get_kw_1_monday(year):
    """
    Return the date of the Monday belonging to the first calendar week.

    The first calendar week is determined according to the week that contains
    the first Thursday of January. Based on this Thursday, the corresponding
    Monday is calculated. If this Monday lies in the previous year, the function
    returns the corrected December date.

    Args:
        year (int): The calendar year.

    Returns:
        int: The day number of the Monday that starts the first calendar week.
    """

    # Only January is needed to determine the first calendar week.
    month = 1

    # Get the weekday of January 1st.
    first_day_of_month_weekday = calendar.weekday(year, month, 1)

    # Calculate the offset from January 1st to the first Thursday.
    offset_to_thursday = (3 - first_day_of_month_weekday + 7) % 7

    # Determine the date of the first Thursday in January.
    first_thursday_date = offset_to_thursday + 1

    # The Monday of the same calendar week is three days before Thursday.
    first_monday_date = first_thursday_date - 3

    # Correct negative values when the first Monday lies in December of the previous year.
    date_correction = {-1: 31, -2: 30, -3: 29, -4: 28, -5: 27}

    # Apply correction for dates that belong to the previous year.
    if first_thursday_date in date_correction:
        first_thursday_date = date_correction[first_thursday_date]

    return first_monday_date
