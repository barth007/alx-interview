#!/usr/bin/python3
"""
"""
import pyperclip


def minOperations(n):
    """
    """

    initial_text = "H"
    number_of_opp = 0
    while  len(initial_text) <= n:
        if len(initial_text) != n:
            #Copy All
            pyperclip.copy(initial_text)
            number_of_opp += 1
            pastes_chars = pyperclip.paste()
            initial_text += pastes_chars
            number_of_opp += 1
    return number_of_opp

        

minOperations(3)
