# -*- coding: utf-8 -*-
"""
Module Name: decode_message.py
Author: Kendall Whitbeck
Date: March 30, 2024

Description: This module decodes an encoded message file using a pyramidal decode scheme.

Usage: The message_file input must be placed in the current directory or sub-directory.
[PowerShell]: py .\decode_message.py
"""

def decode(message_file):
    """Decode an encoded message file using a pyramidal decode scheme.

    Args:
        message_file (str): The path to the encoded message file.

    Raises:
        ValueError: If the number of lines in the encoded message does not equal the highest integer value used,
                    or if the numbers used in the encoded message are not unique, or if the encoded message has
                    an invalid number of lines.
        FileNotFoundError: If the specified file does not exist.

    Returns:
        str: The decoded message.
    """

    try:
        # Open the encoded message file for reading.
        with open(message_file, 'r') as file:
            lines = file.readlines()

        # Initialize an empty dictionary for lines in the encoded message.
        encoded_words = {}

        # Assign the number of lines in the encoded message for error checking.
        num_lines = len(lines)

        # Iterate through the lines in the encoded message.
        for line in lines:
            # Parse the number and word in each line.
            number, word = line.strip().split(' ')
            number = int(number)

            # Ensure the number of lines in the encoded message is the same as the highest number used.
            if number > num_lines:
                raise ValueError("The number of lines in the encoded message must equal the highest integer value used.")

            # Ensure the numbers used in the encoded message are unique.
            if number in encoded_words:
                raise ValueError("The numbers used in the encoded message must all be unique.")

            # Add the number-word key-value pair to the encoded words dictionary.
            encoded_words[number] = word

        # Initialize variables for looping through encoded words.
        decoded_words = []
        current_row_start = 1  # Start from the first row.
        current_row_length = 1  # First row has 1 integer.
        current_row_end = 1

        # Iterate through the encoded words to decode via the pyramidal scheme.
        while current_row_end < len(encoded_words):
            # Determine the end of the current row.
            current_row_end = current_row_start + current_row_length - 1

            if current_row_end > len(encoded_words):
                # Raise ValueError if the number of lines in the encoded message does not form a valid pyramid.
                raise ValueError("The encoded message has an invalid number of lines.")

            # Only consider words at the end of a pyramid row.
            decoded_words.append(encoded_words[current_row_end])

            # Update the next row's starting value and length.
            current_row_start = current_row_end + 1
            current_row_length += 1

        # Join decoded words into a single message separated by spaces.
        decoded_message = ' '.join(decoded_words)

        # Return the decoded message.
        return decoded_message

    except FileNotFoundError:
        # If the input file does not exist, raise FileNotFoundError.
        raise FileNotFoundError("The specified file does not exist.")

# The main code that executes the message decoding.
def main():
    # Assign input file for decoding.
    # For this implementation, coding_qual_input.txt must be located in the same directory as this file.
    input_file = "coding_qual_input.txt"

    # Execute the decode function using the input file.
    decoded_message = decode(input_file)

    # Print the decoded message.
    print(decoded_message)

# Ensure main() is executed only if this .py file is executed directly (i.e., not imported by another .py file).
if __name__ == "__main__":
    main()