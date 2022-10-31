from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep

browser = Chrome('chromedriver')
url = 'https://uakino.club'

browser.get(url)

# Let's make a button
button_1 = browser.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div/header/div/div[1]/div/i')
print(button_1)

button_1.click()  # press the button
find_fill = browser.find_element_by_xpath(
    '/html/body/div[1]/div[1]/div/header/div/div[2]/form/div/input')

find_fill.send_keys('Фейкові копи', Keys.ENTER)

title = browser.find_element_by_xpath(
    '/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/a')
title.send_keys(Keys.ENTER)
sleep(5)

# BeautifulSoup now
soup = BeautifulSoup(browser.page_source, 'lxml')
name_ukr = soup.find(
    'div', class_="alltitle").find(
        'span', class_="solototle").text
name_angl = soup.find(
    'div', class_="alltitle").find(
        'span', class_="origintitle").text
print(
    soup.find('div', class_="alltitle").find(
        'span', class_="origintitle").get('href'))

print("Name is Ukrainian", name_ukr)
print("Name is English", name_angl)

another = soup.find_all('div', class_="fi-desc")

print("Another informathion")
for i in another:
    print(i.text)
