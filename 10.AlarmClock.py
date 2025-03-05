import datetime
import time
import winsound  # For Windows sound notification

# Function to set the alarm
def set_alarm():
    alarm_time = input("Enter alarm time (HH:MM:SS): ")
    alarm_date = input("Enter alarm date (YYYY-MM-DD): ")
    
    alarm_datetime = f"{alarm_date} {alarm_time}"
    alarm_datetime = datetime.datetime.strptime(alarm_datetime, "%Y-%m-%d %H:%M:%S")
    
    print(f"Alarm set for {alarm_datetime}")
    return alarm_datetime

# Function to check time and trigger alarm
def check_alarm(alarm_time):
    sounds = ["SystemAsterisk", "SystemExclamation", "SystemHand", "SystemQuestion"]
    while True:
        current_time = datetime.datetime.now()
        if current_time >= alarm_time:
            print("Time to wake up!")
            for sound in sounds:
                winsound.PlaySound(sound, winsound.SND_ALIAS)
                time.sleep(1)
            print("Time to wake up!")

            break
        time.sleep(1)  # Check every second


if __name__ == "__main__":
    alarm_time = set_alarm()
    check_alarm(alarm_time)
