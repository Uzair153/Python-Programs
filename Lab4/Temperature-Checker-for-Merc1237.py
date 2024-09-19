'''A project in Pggc. requires Merc1237 to be continually heated in a vat. You have been asked to check the temperature every 20 minutes. If the temperature does not exceed 107.5 degrees Celsius, then you do nothing. However, if the temperature is greater than 107.5 degrees Celsius, then you
must turn down the vat’s thermostat, wait 10 minutes, and check the temperature again. You repeat these steps until the temperature does not exceed 107.5 degrees Celsius. You have been asked to write a program to guides you through this process.
Here is the algorithm:
1. Get the Merc1237 temperature.
2. Repeat the following steps as long as the temperature is greater than 107.5 degrees
Celsius:
a. Tell the technician to turn down the thermostat, wait 10 minutes, and check the
temperature again.
b. Get the temperature.
3. After the loop finishes, let the program state the temperature is acceptable and to
check it again in 20 minutes.'''


import time

def get_temperature():
    while True:
        try:
            temperature = float(input("Enter the temperature (in degrees Celsius): "))
            return temperature
        except ValueError:
            print("Please enter a valid numerical temperature.")

def check_temperature():
    while True:
        temperature = get_temperature()
        if temperature <= 107.5:
            print("Temperature is acceptable.")
            break
        else:
            print("Temperature is too high. Turn down the thermostat and wait 10 minutes.")
            time.sleep(600)  # Wait for 10 minutes (10 minutes = 600 seconds)

print("Welcome to the Merc1237 temperature monitoring system.")
while True:
    check_temperature()
    print("Check temperature again in 20 minutes.")
    time.sleep(1200)  # Wait for 20 minutes (20 minutes = 1200 seconds)

