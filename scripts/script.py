from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Navigate to Google's homepage
    driver.get("https://www.google.com")

    # Find the search box element
    search_box = driver.find_element(By.NAME, "q")

    # Type the search query
    search_query = "OpenAI"
    search_box.send_keys(search_query)

    # Press ENTER to perform the search
    search_box.send_keys(Keys.RETURN)

    # Wait for the results to load and display the titles
    driver.implicitly_wait(5)  # wait for 5 seconds

    # Find and print the titles of the search results
    search_results = driver.find_elements(By.CSS_SELECTOR, 'h3')
    for index, result in enumerate(search_results, start=1):
        print(f"{index}. {result.text}")

finally:
    # Close the browser
    driver.quit()
