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
import threading

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
driver2 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
driver3 = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)


def telegram_bot_sendtext(bot_message):
   bot_token = os.getenv("BOT_TOKEN")
   bot_chatID = os.getenv("BOT_CHAT_ID")

   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
   response = requests.get(send_text)
   return response.json()

#SCC Free training
def check_scc():
    while True:
        try:
            driver.get("https://app.cituro.com/booking/scc#step=1")
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[4]/div[2]/div/div[6]'))).click()
            page_html = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/div[2]/div[2]/div[2]/div/div[2]/div'))).get_attribute('innerText')
            time.sleep(900) #900 seconds = 15min
            driver.refresh()  # refresh page
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[4]/div[2]/div/div[6]'))).click()
            page_html2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/div[2]/div[2]/div[2]/div/div[2]/div'))).get_attribute('innerText')
            chrome_options = Options()
            if page_html == page_html2:
                #telegram_bot_sendtext('nothing changed SCC')
                driver.refresh()
                continue
            else:
                telegram_bot_sendtext('SCC Free Training: ' + page_html2)
                driver.refresh()
                time.sleep(60)
                continue
        except Exception as e:
            print("error",e)



#check BEV
def check_bev():
    while True:
        try:
            driver3.get("https://app.cituro.com/booking/bev#step=1")
            #click PHS
            time.sleep(3)
            title1 = WebDriverWait(driver3, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[5]/div/div/div[1]'))).get_attribute('innerText')
            WebDriverWait(driver2, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[5]/div/div'))).click()
            page_html3 = WebDriverWait(driver2, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/div[2]/div[2]/div[2]/div/div[2]/div'))).get_attribute('innerText')
            #click EHE
            driver3.refresh()  # refresh page
            time.sleep(3)
            title2 = WebDriverWait(driver3, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[2]/div/div/div[1]'))).get_attribute('innerText')
            WebDriverWait(driver3, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[2]/div/div'))).click()
            page_html5 = WebDriverWait(driver3, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/div[2]/div[2]/div[2]/div/div[2]/div'))).get_attribute('innerText')
            #click p9 Open
            driver3.refresh()  # refresh page
            time.sleep(3)
            title3 = WebDriverWait(driver3, 20).until(EC.visibility_of_element_located(
               (By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[10]/div/div/div[1]'))).get_attribute('innerText')
            WebDriverWait(driver3, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[10]/div/div'))).click()
            page_html7 = WebDriverWait(driver3, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/section/div[2]/div[2]/div[2]/div/div[2]/div'))).get_attribute('innerText')
            driver3.refresh()  # refresh page
            time.sleep(3)
            #click competition times
            title4 = WebDriverWait(driver3, 20).until(EC.visibility_of_element_located(
               (By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[13]/div/div/div[1]'))).get_attribute('innerText')
            WebDriverWait(driver3, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[13]/div/div'))).click()
            page_html9 = WebDriverWait(driver3, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/section/div[2]/div[2]/div[2]/div/div[2]/div'))).get_attribute('innerText')
            
            #wait N minutes
            time.sleep(450)  # 900 seconds = 15min
            
            #click PHS again
            driver3.refresh()
            time.sleep(3)
            WebDriverWait(driver2, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[5]/div/div'))).click()
            page_html4 = WebDriverWait(driver2, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/section/div[2]/div[2]/div[2]/div/div[2]/div'))).get_attribute('innerText')
            chrome_options = Options()
            #click EHE again
            driver3.refresh()
            time.sleep(3)
            WebDriverWait(driver3, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[2]/div/div'))).click()
            page_html6 = WebDriverWait(driver3, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/section/div[2]/div[2]/div[2]/div/div[2]/div'))).get_attribute('innerText')
            #click P9 Open again
            driver3.refresh()
            time.sleep(3)
            WebDriverWait(driver3, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[10]/div/div'))).click()
            page_html8 = WebDriverWait(driver3, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/section/div[2]/div[2]/div[2]/div/div[2]/div'))).get_attribute('innerText')
            #click competition times again
            driver3.refresh()
            time.sleep(3)
            WebDriverWait(driver3, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/section/div[2]/div[2]/div/div/div[13]/div/div'))).click()
            page_html10 = WebDriverWait(driver3, 20).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div/section/div[2]/div[2]/div[2]/div/div[2]/div'))).get_attribute('innerText')
            
            #send texts
            if page_html3 == page_html4 and 'Unfortunately' not in page_html4:
               telegram_bot_sendtext(title1 + ': \n' + page_html4)
               driver3.refresh()
               continue
            elif page_html5 != page_html6 and 'Unfortunately' not in page_html6:
                telegram_bot_sendtext(title2 + ': \n' + page_html6)
                driver3.refresh()
                continue
            elif page_html7 != page_html8 and 'Unfortunately' not in page_html8:
                telegram_bot_ sendtext(title3 + ': \n'  + page_html8)
                driver3.refresh()
                continue
            elif page_html9 != page_html10 and 'Unfortunately' not in page_html10:
                telegram_bot_sendtext(title4 + ': \n'  + page_html10)
                driver3.refresh()
                continue
            else:
                driver3.refresh()
                time.sleep(60)
                continue
        except Exception as e:
            print("error", e)           
            
#run
thread1 = threading.Thread(target=check_scc).start()
thread2 = threading.Thread(target=check_bev).start()
