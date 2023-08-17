import time
from playsound import playsound

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            playsound("alarm_sound.mp3")  # Replace with your alarm sound file
            break
        time.sleep(1)  # Wait for 1 second before checking again

def main():
    alarm_time = input("Enter the alarm time in HH:MM:SS format: ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
