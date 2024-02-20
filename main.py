from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
start_time = time.time()

five_min = time.time() + 60*5  # 5 minutes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
b = {}
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
for item in items:
    item_id = item.get_attribute("id")
    item_price_text = item.find_element(By.CSS_SELECTOR, "b").text
    # Filter out non-digit characters
    item_price_digits = ''.join(filter(str.isdigit, item_price_text))
    # Check if there are any digits in the text
    if item_price_digits:
        item_price = int(item_price_digits)
        b[item_price] = item_id

while True:
    cookie.click()

    if time.time() - start_time >= 5:
        # Get the current amount of money
        money = int(driver.find_element(By.ID, "money").text)


        # Find the maximum price you can afford
        max_affordable_price = max(price for price in b if price <= money)
        item_to_buy = b[max_affordable_price]

        # Click on the item
        driver.find_element(By.ID, item_to_buy).click()
        start_time = time.time()
    if time.time() > five_min:
        count = driver.find_element(by=By.ID, value="cps").text
        print(count)
        break

# Close the driver
driver.close()
