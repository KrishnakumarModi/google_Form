# Auto_Fill_form
## Google Form Automation and Email Sending

This repository contains a Python script that automates the process of filling out a Google Form, capturing a screenshot of the filled form, and sending an email with the screenshot as an attachment. The script uses `Selenium` for browser automation and `smtplib` for sending the email.

## Features

- **Automates the filling of a Google Form** using Selenium.
- **Captures a screenshot** of the filled-out form.
- **Sends an email** with the screenshot as an attachment.
- **Uses environment variables** to securely store email credentials.

## Prerequisites

Before running the project, make sure you have the following installed:

- **Python 3.6 or higher**.
- **Selenium** for browser automation.
- **ChromeDriver** (or any other WebDriver) that is compatible with your browser.


### Install Dependencies

To install the necessary libraries, use the following commands:

`pip install selenium smtplib python-dotenv`

## Note
smtplib is part of Python's standard library, so it doesn't need to be installed separately. If you encounter an error related to smtplib, it typically means something else is wrong, like a misconfiguration or a missing dependency in the system, but not the library itself.

