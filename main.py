#!/usr/bin/env python3

"""
File: main.py
Description: Run the application, which provides a simple two-hotkey solution for quickly entering course registration numbers (CRNs) into the University of Dayton's course registration system which uses Self-Service Banner (SSB).
Author: Joseph Lefkovitz (github.com/lefkovitzj)
Date: 2026-04-08
"""

__author__ = "Joseph Lefkovitz"

import time

import keyboard
import pyautogui

if __name__ == "__main__":
    print("BetterBannerRegistration is running. Press <fwd-hotkey> to enter the next CRN, and <backward-hotkey> to enter the previous CRN.")
    print("Press Ctrl+C to exit.")
