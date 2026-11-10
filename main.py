#!/usr/bin/env python3

"""
File: main.py
Description: Run the application, which provides a simple two-hotkey solution for quickly entering course registration numbers (CRNs) into the University of Dayton's course registration system which uses Self-Service Banner (SSB).
Author: Joseph Lefkovitz (github.com/lefkovitzj)
Date: 2026-11-09
"""

__author__ = "Joseph Lefkovitz"

import os
import time

import keyboard
import pyautogui
from dotenv import load_dotenv

# Shorten the delay between PyAutoGUI actions.
pyautogui.PAUSE = 0.01

FIRST_BUFFER = 0.25
BETWEEN_BUFFER = 0.25
START_KEY = "f8"

def load_parse_crns():
    """ Load CRNs from the .env file and parse them into a list."""
    load_dotenv()
    crns = [crn.strip() for crn in os.getenv("CRNS", "").split(",")]
    for crn in crns:
        if not crn.isdigit():
            print(f"Warning: '{crn}' is not a valid CRN.")
    return crns

def full_auto(crns):
    """ Fully automatic mode that enters all CRNs in sequence with a delay. """
    print(f"Loaded CRNs: {crns}")
    start = time.perf_counter()

    for crn in crns:
        if crn == crns[0]: # Additional buffer for the first CRN.
            time.sleep(FIRST_BUFFER)
        print(f"Entering CRN: {crn}")
        pyautogui.write(crn, interval=0.02)
        if crn != crns[-1]:
            print("Pressing Tab to move to the next field...")
            pyautogui.press('tab')
        time.sleep(BETWEEN_BUFFER)  # Adjust delay as needed
    end = time.perf_counter()
    print(f"Total time taken: {end - start:.4f} seconds")

def main(crns = load_parse_crns()):
    """ Main function to set up hotkeys and run the application."""
    keyboard.add_hotkey(START_KEY, full_auto, args=(crns,))
    # Keep the program running
    while True:
        keyboard.wait()

if __name__ == "__main__":
    print(f"BetterBannerRegistration is running. Press {START_KEY} to begin the sequence.")
    print("Press Ctrl+C to exit.")
    main()
