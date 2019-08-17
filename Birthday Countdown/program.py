import datetime


def print_header():
    print("----------------------------")
    print("       Birthday App")
    print("----------------------------\n")
    

def get_birthday_date():
    date = []
    date.append(int(input("What year were you born? [YYYY] : ")))
    date.append(int(input("What month were you born? [MM]  : ")))
    date.append(int(input("What day were you born? [DD]    : ")))
    bday = datetime.date(date[0], date[1], date[2])
    return bday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    d = this_year - target_date
    if d.days < 0:
        this_year = datetime.date(target_date.year + 1, original_date.month, original_date.day)
        d = this_year - target_date
        return d.days
    else:
        return d.days


def print_birthday_info(days):
    if days != 0:
        print("Your birthday is only {} days away!".format(days))
    else:
        print("Happy Birthday!!!!")


def main():
    print_header()
    bday = get_birthday_date()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_info(number_of_days)


if __name__ == "__main__":
    main()