server_name = "Ubuntu-Server"

while True:
    try:
        failed_logins = int(input("Enter number of failed logins: "))

        if failed_logins < 0:
            print("ERROR: Failed logins cannot be negative.")
            continue

        if failed_logins >= 10:
            print("HIGH ALERT: Possible brute-force attack!")

        elif failed_logins >= 5:
            print("MEDIUM ALERT: Multiple failed login attempts!")

        elif failed_logins >= 1:
            print("LOW ALERT: Failed login detected.")

        else:
            print("No failed login attempts detected.")

        break

    except ValueError:
        print("ERROR: Please enter a valid whole number.")
