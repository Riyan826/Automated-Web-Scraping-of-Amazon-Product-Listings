from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os

# Ensure "data" directory exists
if not os.path.exists("data"):
    os.makedirs("data")  # Create the folder if it doesn't exist

driver = webdriver.Chrome()

query = "laptop"

file = 0

for i in range(1, 5):  # Loop through pages
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}")

    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")

    
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html","w",encoding="utf-8") as f:
            f.write(d)
            file+=1

    print(f"{len(elems)} items found on page {i}")
    time.sleep(5)  

driver.quit()  # Close the WebDriver after all pages are processed
