import os
import time

YELLOW, BROWN, RESET = '\033[93m', '\033[38;5;52m', '\033[0m'

def garden(stage):
    flower = f"      {YELLOW}(q*){RESET}          "
    soil = f"{BROWN}{'#' * 16}{RESET}"
    frames = ["                  "] * 4 + [f"{BROWN}{'~' * 16}{RESET}"] + [soil] * 5
    if stage < 5:
        frames[stage] = flower
    else:
        frames[5 + (stage - 5)] = f"{BROWN}######{YELLOW}(q*){BROWN}######{RESET}"
    return "\n".join(frames)

def animate():
    try:
        while True:
            for i in range(10):  # Increased to 10 stages
                os.system('cls' if os.name == 'nt' else 'clear')
                print(garden(i))
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nAnimation stopped.")

if __name__ == "__main__":
    animate()