# Consider the date June 10, 1960. It's intriguing because when represented as 6/10/60, multiplying the month (6) by the day (10) gives the year (60). Your task is to develop a program that prompts the user to input a month (numerically), a day, and a two-digit year. The program should then ascertain if the product of the month and day matches the year. If there's a match, the program should display "The date is magic." If not, it should indicate "The date is not magic. Have two function, main function and is_magic_date that will accept the month, day, year. For example is_magic_date(month, day, year). Have the main function get the month, day and year and pass it to the is_magic_date function

def is_magic_date(month, day, year):
    if month * day == year:
        return True
    else:
        return False

def main():
    month = int(input("Enter the month (numerically): "))
    day = int(input("Enter the day: "))
    year = int(input("Enter the two-digit year: "))

    if is_magic_date(month, day, year):
        print("The date is magic.")
    else:
        print("The date is not magic.")

if __name__ == "__main__":
    main()
