import time

def countdown_timer(seconds, hours, minutes):
    while seconds >= 0:
        print(f"{hours} hours, {minutes} minutes, {seconds} seconds remaining")
        #delaying the time py
        time.sleep(1)
        seconds -= 1
        if seconds < 0:
            break
        if seconds == 0:
            if minutes == 0:
                if hours == 0:
                    print("Countdown complete!")
                    break
                else:
                    hours -= 1
                    minutes = 59
            else:
                minutes -= 1
                seconds = 59
    print("Time's up!")

def main():
    try:
        total_seconds = int(input("Enter the countdown time in seconds: "))
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        countdown_timer(seconds, hours, minutes)
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds.")

if __name__ == "__main__":
    main()
