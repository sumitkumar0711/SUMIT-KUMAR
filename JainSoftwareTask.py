from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui

browser = webdriver.Chrome('E:\ChromeDriver/chromedriver')
browser.get("https://www.jain.software/")
if(pyautogui.locateOnScreen("jain.software")==True):
    img1 = pyautogui.screenshot('File1.jpeg')