#!/usr/bin/python3
"""
0-validate_utf8.py
"""
import codecs


def validUTF8(data):
    """
    validate utf-8
    """

    try:
        byte_string = bytes(data)
        # decoded_text = byte_string.decode('utf-8')
        return True
    except ValueError:
        return False
