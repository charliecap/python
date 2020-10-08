from datetime import date
import datetime



def calculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)

    # raised when birth date is February 29
    # and the current year is not a leap year
    except ValueError:
        birthday = born.replace(year=today.year,
                                month=born.month + 1, day=1)

    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

# variables set for my details and age formula
name = "you"
my_name = "Charlie"
my_age = calculateAge(date(1988, 6, 8))
my_trainer_id = "CharlieCap"

# print(my_name, my_age, my_trainer_id)

# more variables added

# how to set a name to grab the input on the page
greeting = "Hello there, " + name
print(greeting)

