import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os
load_dotenv()

def send_email():
    # Email Configuration
    from_email =(os.getenv("email_Id"))
    to_email = "tech@themedius.ai"
    cc_email = "hr@themedius.ai"
    subject = f"Python (Selenium) Assignment - {str(os.getenv('fullname'))}"
    
    # Create the email container
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Cc'] = cc_email
    msg['Subject'] = subject

    # Email body content
    body = f"""
    Dear Sir/Ma'am,

    Please find the required documents below for the Python (Selenium) assignment:

    1. Screenshot of the form filled via code .
    2. Source code (GitHub repository):  https://github.com/KrishnakumarModi/Auto_fill_Form
    3. Your resume.
    4. Links to past projects/work samples:  https://github.com/KrishnakumarModi
    5. Brief documentation of your approach:
        Setup:
        Use Selenium to automate the browser and interact with the Google Form.
        Install necessary libraries, such as Selenium and WebDriver for browser automation.

        Automating Google Form:
        Open the Google Form using Selenium.
        Fill in the form fields automatically (e.g., name, email, resume).
        Submit the form after all required fields are filled.

        Screenshot Capture:
        After filling the form, take a screenshot of the form using Selenium’s built-in screenshot functionality.

        Email Preparation:
        Use Python's smtplib to configure email settings.
        Compose an email with a clear subject and body, explaining the documents.
        Attach files: form screenshot, source code, documentation, resume, and project links.
        Email Sending:
        Send the email with all attachments using the configured SMTP server.

   
    6. Confirm your availability to work full time (10 am to 7 pm) for the next 3-6 months:
        Yes, I am available to work full-time from 10 AM to 7 PM for the next 3-6 months in a work-from-home setup.

    Best regards,
    {str(os.getenv('fullname'))}
    """
    msg.attach(MIMEText(body, 'plain'))

    # Attach files
    files = [
        str(os.getenv("form_screenshot")),  # Screenshot of the form
        str(os.getenv("resume")),           # Resume       
    ]

    for file in files:
        if os.path.exists(file):  # Check if the file exists
            with open(file, "rb") as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f"attachment; filename= {file}")
                msg.attach(part)
        else:
            print(f"File not found: {file}")

    # SMTP configuration (For Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    password = (os.getenv("email_password")) 

    try:
        # Establish a connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        server.login(from_email, password)  # Login to your email account
        server.sendmail(from_email, [to_email, cc_email], msg.as_string())  # Send the email
        server.quit()  # Terminate the SMTP session
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")

# Send the email
send_email()


