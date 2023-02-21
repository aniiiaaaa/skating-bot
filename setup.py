from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import telegram
import requests

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "https://app.cituro.com/booking/scc#step=1"
wait = WebDriverWait(driver, 20)

def telegram_bot_sendtext(bot_message):
   bot_token = os.getenv("BOT_TOKEN")
   bot_chatID = os.getenv("BOT_CHAT_ID")

   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
   response = requests.get(send_text)
   return response.json()

# compare the request's html
while True:
    try:
        driver.get(link)
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[4]/div[2]/div/div[6]'))).click()
        page_html = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/section/div[2]/div[2]/div[2]/div/div[2]/div'))).get_attribute('innerText')
        time.sleep(900) #900 seconds = 15min
        driver.refresh()  # refresh page
        wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[4]/div[2]/div/div[6]'))).click()
        page_html2 = wait.until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div/section/div[2]/div[2]/div[2]/div/div[2]/div'))).get_attribute('innerText')
        # driver.close()
        chrome_options = Options()
        if page_html == page_html2:
            #test = telegram_bot_sendtext('nothing changed ' + page_html)
            driver.refresh()
            continue

        # if something changed in the hashes
        else:
            print(page_html2)
            wait = WebDriverWait(driver, 20)

            print(page_html2)
            telegram_bot_sendtext('SCC Free Training: ' + page_html2)

            # wait for 30 seconds
            time.sleep(60)
            continue

    # To handle exceptions
    except Exception as e:
        print("error",e)
