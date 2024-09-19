'''Write a program that asks the user to enter a number of seconds, and works as follows:
There are 60 seconds in a minute. If the number of seconds entered by the user is greater than or equal to 60, the program should display the number of minutes in that many seconds.
There are 3,600 seconds in an hour. If the number of seconds entered by the user is greater than or equal to 3,600, the program should display the number of hours in that many seconds.
There are 86,400 seconds in a day. If the number of seconds entered by the user is greater than or equal to 86,400, the program should display the number of days in that many seconds'''


def convert_seconds(seconds):
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return days, hours, minutes, seconds

def main():
    seconds = int(input("Enter the number of seconds: "))
    days, hours, minutes, remaining_seconds = convert_seconds(seconds)
    
    if days > 0:
        print("Days:", days)
    if hours > 0:
        print("Hours:", hours)
    if minutes > 0:
        print("Minutes:", minutes)
    if remaining_seconds > 0:
        print("Seconds:", remaining_seconds)

if __name__ == "__main__":
    main()
