import time

WORK_MINUTES = 25
BREAK_MINUTES = 5


def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r", flush=True)
        time.sleep(1)
        seconds -= 1
    print("00:00")


def pomodoro_cycle(cycle_number):
    print(f"\n--- Pomodoro {cycle_number} ---")
    print("Work! Focus for 25 minutes.")
    countdown(WORK_MINUTES * 60)
    print("Break time! Relax for 5 minutes.")
    countdown(BREAK_MINUTES * 60)
    print("Cycle complete!")


def main():
    cycle = 1
    try:
        while True:
            pomodoro_cycle(cycle)
            cycle += 1
    except KeyboardInterrupt:
        print("\nExiting Pomodoro. Good work!")


if __name__ == "__main__":
    main()
