from selenium import webdriver
import pyautogui
import urllib

driver = webdriver.Chrome('E:\ChromeDriver/chromedriver')
driver.get("https://www.jain.software/")
pyautogui.rightClick()
pyautogui.moveRel(200,250)
pyautogui.click()
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
pyautogui.hotkey('ctrl','shift','w')
