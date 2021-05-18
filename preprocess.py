import csv

# the following custom pre-processing module handles time and date data for
# the raw Hounslow vehicle accident dataset.

# the file path and name of the CSV file that we wish to read
READ_FILE_PATH_AND_NAME = "hounslow_accidents.csv"

# the file path and name of the CSV file we wish to write to
WRITE_FILE_PATH_AND_NAME = "hounslow_accidents_with_time_categories.csv"

# the index of the column that contains the old H:MM time format
INDEX_OLD_TIME_NOMINAL = 7

# the index of the column that contains the old DD/MM/YY date format
INDEX_OLD_DATE_NOMINAL = 5

# CSV characters
CSV_NEW_LINE_CHAR = ''
CSV_DELIMITER_CHAR = ','
CSV_QUOTE_CHAR = '|'

# the new attribute names that will be used when appending data
TIME_CATEGORY_ATTR_NAME = "Time_category"
MONTH_CATEGORY_ATTR_NAME = "Month"

# the replacement time category values
NOMINAL_REPLACEMENT_LATE_NIGHT = "LATE NIGHT"
NOMINAL_REPLACEMENT_DAWN = "DAWN"
NOMINAL_REPLACEMENT_EARLY_MORNING = "EARLY MORNING"
NOMINAL_REPLACEMENT_LATE_MORNING = "LATE MORNING"
NOMINAL_REPLACEMENT_MIDDAY = "MIDDAY"
NOMINAL_REPLACEMENT_EARLY_AFTERNOON = "EARLY AFTERNOON"
NOMINAL_REPLACEMENT_LATE_AFTERNOON = "LATE AFTERNOON"
NOMINAL_REPLACEMENT_DUSK = "DUSK"
NOMINAL_REPLACEMENT_EARLY_NIGHT = "EARLY NIGHT"
NOMINAL_REPLACEMENT_MIDNIGHT = "MIDNIGHT"
NOMINAL_REPLACEMENT_UNKNOWN = "UNKNOWN"

# the replacement month values
NOMINAL_REPLACEMENT_JANUARY = "JANUARY"
NOMINAL_REPLACEMENT_FEBRUARY = "FEBRUARY"
NOMINAL_REPLACEMENT_MARCH = "MARCH"
NOMINAL_REPLACEMENT_APRIL = "APRIL"
NOMINAL_REPLACEMENT_MAY = "MAY"
NOMINAL_REPLACEMENT_JUNE = "JUNE"
NOMINAL_REPLACEMENT_JULY = "JULY"
NOMINAL_REPLACEMENT_AUGUST = "AUGUST"
NOMINAL_REPLACEMENT_SEPTEMBER = "SEPTEMBER"
NOMINAL_REPLACEMENT_OCTOBER = "OCTOBER"
NOMINAL_REPLACEMENT_NOVEMBER = "NOVEMBER"
NOMINAL_REPLACEMENT_DECEMBER = "DECEMBER"


def main():

    # write file to open
    write_file = open(WRITE_FILE_PATH_AND_NAME, "a")

    with open(READ_FILE_PATH_AND_NAME, 'r') as csv_file:

        row_reader = csv.reader(csv_file, delimiter=CSV_DELIMITER_CHAR)

        index = 0
        for row in row_reader:

            # copy header row and continue
            if index == 0:
                row.append(TIME_CATEGORY_ATTR_NAME)
                row.append(MONTH_CATEGORY_ATTR_NAME)
                write_file.write(','.join(row) + "\n")
                index = index + 1
                continue

            # the old values for time and date
            time_old_str = row[INDEX_OLD_TIME_NOMINAL]
            date_old_str = row[INDEX_OLD_DATE_NOMINAL]

            time_category = get_time_category(time_old_str)
            month_category = get_month_from_date(date_old_str)

            # append values to the end of the row
            row.append(time_category)
            row.append(month_category)

            # write the row to the file
            write_file.write(','.join(row) + "\n")

            # notify user of a processed row
            print("PROCESSED ROW #", index)

            # increase index
            index = index + 1

    # close write file
    write_file.close()

    # notify user that processing is complete
    print("\nDONE")


def get_time_category(time):

    # find relevant time category
    if time.startswith("00:"):
        return NOMINAL_REPLACEMENT_MIDNIGHT
    elif time.startswith("01:") or time.startswith("02:") or time.startswith("03:"):
        return NOMINAL_REPLACEMENT_LATE_NIGHT
    elif time.startswith("04:") or time.startswith("05:"):
        return NOMINAL_REPLACEMENT_DAWN
    elif time.startswith("06:") or time.startswith("07:") or time.startswith("08:"):
        return NOMINAL_REPLACEMENT_EARLY_MORNING
    elif time.startswith("09:") or time.startswith("10:"):
        return NOMINAL_REPLACEMENT_LATE_MORNING
    elif time.startswith("11:") or time.startswith("12:"):
        return NOMINAL_REPLACEMENT_MIDDAY
    elif time.startswith("13:") or time.startswith("14:"):
        return NOMINAL_REPLACEMENT_EARLY_AFTERNOON
    elif time.startswith("15:") or time.startswith("16:"):
        return NOMINAL_REPLACEMENT_LATE_AFTERNOON
    elif time.startswith("17:") or time.startswith("18:"):
        return NOMINAL_REPLACEMENT_DUSK
    elif time.startswith("19:") or time.startswith("20:") or time.startswith("21:"):
        return NOMINAL_REPLACEMENT_EARLY_NIGHT
    elif time.startswith("22:"):
        return NOMINAL_REPLACEMENT_LATE_NIGHT
    elif time.startswith("23:") or time.startswith("24:"):
        return NOMINAL_REPLACEMENT_MIDNIGHT
    else:
        return NOMINAL_REPLACEMENT_UNKNOWN


def get_month_from_date(date):

    month = date.split("/")[1]

    # find relevant month category
    if month == "01":
        return NOMINAL_REPLACEMENT_JANUARY
    elif month == "02":
        return NOMINAL_REPLACEMENT_FEBRUARY
    elif month == "03":
        return NOMINAL_REPLACEMENT_MARCH
    elif month == "04":
        return NOMINAL_REPLACEMENT_APRIL
    elif month == "05":
        return NOMINAL_REPLACEMENT_MAY
    elif month == "06":
        return NOMINAL_REPLACEMENT_JUNE
    elif month == "07":
        return NOMINAL_REPLACEMENT_JULY
    elif month == "08":
        return NOMINAL_REPLACEMENT_AUGUST
    elif month == "09":
        return NOMINAL_REPLACEMENT_SEPTEMBER
    elif month == "10":
        return NOMINAL_REPLACEMENT_OCTOBER
    elif month == "11":
        return NOMINAL_REPLACEMENT_NOVEMBER
    elif month == "12":
        return NOMINAL_REPLACEMENT_DECEMBER
    else:
        return NOMINAL_REPLACEMENT_UNKNOWN

if __name__ == '__main__':
    main()
