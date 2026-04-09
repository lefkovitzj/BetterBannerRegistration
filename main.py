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
from dotenv import load_dotenv

fwd_hotkey = "["
backward_hotkey = "]"

def load_parse_crns():
    """ Load CRNs from the .env file and parse them into a list."""
    load_dotenv()
    crns = [crn.strip() for crn in os.getenv("CRNS", "").split(",")]
    for crn in crns:
        if not crn.isdigit():
            print(f"Warning: '{crn}' is not a valid CRN.")
    return crns

crns = load_parse_crns()

def main(crns = load_parse_crns()):
    """ Main function to set up hotkeys and run the application."""
    # Start before the first CRN so that the first hotkey press enters the first CRN.
    current_index = -1
    print(f"Loaded CRNs: {crns}")

    def enter_crn(index):
        """ Enter the CRN at the specified index. """
        if 0 <= index < len(crns):
            crn = crns[index]
            print(f"Entering CRN: {crn}")
            pyautogui.press('backspace')
            pyautogui.typewrite(crn, interval=0.05)
            # Short delay to ensure the CRN is entered before the next action.
            time.sleep(0.1)
            return True
        else:
            print("No more CRNs in that direction.")
            return False

    def next_crn():
        """ Enter the next CRN. """
        nonlocal current_index
        if current_index < len(crns) - 1:
            current_index += 1
        enter_crn(current_index)

    def previous_crn():
        """ Enter the previous CRN. """
        nonlocal current_index
        if current_index > 0:
            current_index -= 1
        enter_crn(current_index)

    keyboard.add_hotkey(fwd_hotkey, lambda: next_crn())
    keyboard.add_hotkey(backward_hotkey, lambda: previous_crn())

    # Keep the program running
    while True:
        keyboard.wait()

if __name__ == "__main__":
    print("BetterBannerRegistration is running. ",
        f"Press {fwd_hotkey} to enter the next CRN, and {backward_hotkey}",
        " to enter the previous CRN.")
    print("Press Ctrl+C to exit.")
    main()
