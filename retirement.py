# Tiffany Harrell
# CSC 256.0001
# 8/16/2021


class RetireAge:
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.rate_year = 0
        self.rate_month = 0
        self.month_count = 0
        self.year_count = 0


def set_rate(retire_object):
    # Set Rate Values
    if retire_object.year >= 1960:
        retire_object.rate_year = 67
        retire_object.rate_month = 0
    elif retire_object.year == 1959:
        retire_object.rate_year = 66
        retire_object.rate_month = 10
    elif retire_object.year == 1958:
        retire_object.rate_year = 66
        retire_object.rate_month = 8
    elif retire_object.year == 1957:
        retire_object.rate_year = 66
        retire_object.rate_month = 6
    elif retire_object.year == 1956:
        retire_object.rate_year = 66
        retire_object.rate_month = 4
    elif retire_object.year == 1955:
        retire_object.rate_year = 66
        retire_object.rate_month = 2
    elif (retire_object.year <= 1954) and (retire_object.year >= 1943):
        retire_object.rate_year = 66
        retire_object.rate_month = 0
    elif retire_object.year == 1942:
        retire_object.rate_year = 65
        retire_object.rate_month = 10
    elif retire_object.year == 1941:
        retire_object.rate_year = 65
        retire_object.rate_month = 8
    elif retire_object.year == 1940:
        retire_object.rate_year = 65
        retire_object.rate_month = 6
    elif retire_object.year == 1939:
        retire_object.rate_year = 65
        retire_object.rate_month = 4
    elif retire_object.year == 1938:
        retire_object.rate_year = 65
        retire_object.rate_month = 2
    elif retire_object.year <= 1937:
        retire_object.rate_year = 65
        retire_object.rate_month = 0


def calculate(retire_object):
    retire_object.month_count = retire_object.month + retire_object.rate_month
    retire_object.year_count = retire_object.year + retire_object.rate_year
    if retire_object.month_count > 12:
        clean_months(retire_object)


def pretty_print(retire_object):
    # displays the age (with additional months) for obtaining full SSA benefits
    print(
        "The full retirement age is "
        + str(retire_object.rate_year)
        + " years and "
        + str(retire_object.rate_month)
        + " months."
    )
    # displays the year and month for obtaining full SSA benefits
    print(
        "This will be in "
        + month_conversion(retire_object)
        + " of "
        + str(retire_object.year_count)
        + "."
    )


def clean_months(retire_object):
    # cleaning up if months > 12
    retire_object.month_count = retire_object.month_count - 12
    retire_object.year_count = retire_object.year_count + 1


def month_conversion(retire_object):
    if retire_object.month_count == 1:
        return "January"
    elif retire_object.month_count == 2:
        return "February"
    elif retire_object.month_count == 3:
        return "March"
    elif retire_object.month_count == 4:
        return "April"
    elif retire_object.month_count == 5:
        return "May"
    elif retire_object.month_count == 6:
        return "June"
    elif retire_object.month_count == 7:
        return "July"
    elif retire_object.month_count == 8:
        return "August"
    elif retire_object.month_count == 9:
        return "September"
    elif retire_object.month_count == 10:
        return "October"
    elif retire_object.month_count == 11:
        return "November"
    elif retire_object.month_count == 12:
        return "December"
    else:
        print("Not a valid month value. Exiting Program.")
        quit()


if __name__ == "__main__":
    print("Social Security Full Age Calculator")
    year = 0
    while year != "":
        year = input("Enter year of birth or press enter to exit: ")
        if year != "":
            if (int(year) <= 2021) and (int(year) >= 1900):
                month = input("Enter month of birth: ")
                # should add error handling for integers - for now type casting
                retirement = RetireAge(int(year), int(month))
                set_rate(retirement)
                calculate(retirement)
                pretty_print(retirement)
            else:
                print("Invalid year entered, exiting program.")
                print("Exiting program")
                quit()
    print("Exiting program")
    quit()
