# importing needed syntax
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#  choosing webdriver
driver = webdriver.Chrome()
driver.get("https://duckduckgo.com/")
time.sleep(3)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# searc bar
elem = driver.find_element(By.XPATH, '//*[@id="searchbox_input"]')
elem.send_keys('Flipkart')
elem.send_keys(Keys.ENTER)
time.sleep(3)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# website
elem = driver.find_element(By.XPATH, '//*[@id="r1-0"]/div[2]/div/div/a/div/p/span').click()
time.sleep(3)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# search bar
elem = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
elem.send_keys('Mobiles')
elem.send_keys(Keys.ENTER)
time.sleep(6)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# scrapping part
products = driver.find_elements(By.CLASS_NAME, 'KzDlHZ')  # Replace with actual selector
prices = driver.find_elements(By.TAG_NAME, '.yRaY8j ZYYwLA')  # Replace with actual selector

# Extract the text from the elements
product_names = [product.text for product in products]
product_prices = [price.text for price in prices]

# Debugging output: Check the length and contents
print(f"Length of product_names: {len(product_names)}")
print(f"Length of product_prices: {len(product_prices)}")

# Check the data
print("Product Names:", product_names)
print("Product Prices:", product_prices)

# Ensure both lists have the same length by adding None for missing items
max_length = max(len(product_names), len(product_prices))
product_names.extend([None] * (max_length - len(product_names)))
product_prices.extend([None] * (max_length - len(product_prices)))

# Combine the data into a dictionary
data = {
    'Product Name': product_names,
    'Price': product_prices
}

# Create the DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("scraped_data.xlsx", index=False)
print("Data has been saved to 'scraped_data.xlsx'")