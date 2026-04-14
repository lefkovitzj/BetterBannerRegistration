#!/usr/bin/env python3

"""
File: main.py
Description: Run the application, which provides a simple two-hotkey solution for quickly entering course registration numbers (CRNs) into the University of Dayton's course registration system which uses Self-Service Banner (SSB).
Author: Joseph Lefkovitz (github.com/lefkovitzj)
Date: 2026-04-08
"""

__author__ = "Joseph Lefkovitz"

import os
import time

import keyboard
import pyautogui
import pyperclip
from dotenv import load_dotenv

start_key = "f8"

def load_parse_crns():
    """ Load CRNs from the .env file and parse them into a list."""
    load_dotenv()
    crns = [crn.strip() for crn in os.getenv("CRNS", "").split(",")]
    for crn in crns:
        if not crn.isdigit():
            print(f"Warning: '{crn}' is not a valid CRN.")
    return crns

def full_auto():
    """ Fully automatic mode that enters all CRNs in sequence with a delay. """
    crns = load_parse_crns()
    print(f"Loaded CRNs: {crns}")
    for crn in crns:
        print(f"Entering CRN: {crn}")
        pyperclip.copy(crn)
        pyautogui.hotkey('ctrl', 'v')
        if crn != crns[-1]:
            print("Pressing Tab to move to the next field...")
            pyautogui.press('tab')
        #pyautogui.press('enter')
        time.sleep(0.2)  # Adjust delay as needed

def main(crns = load_parse_crns()):
    """ Main function to set up hotkeys and run the application."""
    keyboard.add_hotkey(start_key, full_auto)
    # Keep the program running
    while True:
        keyboard.wait()

if __name__ == "__main__":
    print(f"BetterBannerRegistration is running. Press {start_key} to begin the sequence.")
    print("Press Ctrl+C to exit.")
    main()
