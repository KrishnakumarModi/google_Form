from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import time
import os
load_dotenv()

# Environment variable
fullname=str(os.getenv("fullname"))  
contact_NO=str(os.getenv("contact_NO"))  
address=str(os.getenv("address"))  
pin_Code=str(os.getenv("pin_Code"))  
email_Id=str(os.getenv("email_Id"))
DOB=str(os.getenv("DOB"))
gender=str(os.getenv("gender"))
screenshort_Path=str(os.getenv("screenshort_Path"))

# Setup the browser
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


# URL of the Google Form
form_url = "https://forms.gle/WT68aV5UnPajeoSc8"  


# Open the Google Form
driver.get(form_url)
driver.maximize_window()
# Wait until the form is fully loaded
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))  

# Fill the Name field
try:
    name_field = driver.find_element(By.XPATH, '//div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')  
    name_field.send_keys(fullname)
except:
    pass
# Fill the Contact number 
try:
    contact_field = driver.find_element(By.XPATH, '//div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')  
    contact_field.send_keys(contact_NO)
except:
    pass

# Fill the Email ID field
try:
    email_field = driver.find_element(By.XPATH, '//div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')  
    email_field.send_keys(email_Id)
except:
    pass
# Fill the Address field
try:
    address_field = driver.find_element(By.XPATH, '//div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')  
    address_field.send_keys(address)
except:
    pass
# Fill the Pin Code field
try:
    pin_field = driver.find_element(By.XPATH, '//div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input') 
    pin_field.send_keys(pin_Code)
except:
    pass
# Fill the Date of Birth field
try:
    dob_field = driver.find_element(By.XPATH, '//div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')  
    dob_field.send_keys(DOB)  
except:
    pass
# Fill the Gender field
try:
    gender_field = driver.find_element(By.XPATH, '//div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')  
    gender_field.send_keys(gender)
except:
    pass
# Fill the code field
try:
    code_field_text = driver.find_element(By.XPATH, '//span[1]/b').text.strip()
    code_field = driver.find_element(By.XPATH, '//div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    code_field.send_keys(code_field_text)
except:
    pass
# Submit the form
try:
    submit_button = driver.find_element(By.XPATH, '//div[2]/div/div[3]/div[1]/div[1]/div/span')  
    submit_button.click()
except:
    pass
# Wait for the form to be submitted
time.sleep(2)
# Take a screenshot and save it to the specified file path
driver.save_screenshot(screenshort_Path)
# Close the browser
driver.quit()

