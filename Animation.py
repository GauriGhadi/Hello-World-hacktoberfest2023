import time
import os

def animate_text(text, speed=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def main():
    while True:
        clear_screen()
        animate_text("Hello, World!")
        time.sleep(2)  # Wait for 2 seconds before repeating the animation

if __name__ == "__main__":
    main()
