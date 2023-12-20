# Random Password Generator

Generate secure and random passwords with this Python script.

## About

This Python script allows users to create a safe ans secure  random passwords with customizable lengths and character sets. It provides options for including uppercase letters, lowercase letters, numbers, and special characters in the generated passwords.

## Code Details

- **Author:** Sreelakshmi Odatt Venu
- **Date Created:** 19/12/2023

## Usage And How to Use

The script prompts the user to input the desired password length and preferences for including different character types. After user input their desired choices , the program generates a random password based on the specified criteria.



1. Run the script: `python password_generator.py`
2. Follow the on-screen prompts to customize your password.

## Configuration

- Open `password_generator.py` in a text editor to modify character sets and other parameters.

```python
#  Customize the character sets based on your preferences
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
special_characters = "!@#$%^&*()_+-=[]{}|;:'\"<>,.?/~`"

# Adjust the password parameters
password_length = 12