from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import csv
import re

Details = []


@given(u'He Opened Google Page')
def opening_google(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.google.com/')
    context.driver.maximize_window()


@when(u'He Search Company Name "{company_name}"')
def searching_company(context, company_name):
    context.company_name = company_name
    context.driver.find_element(By.XPATH, "//*[@type='search']").send_keys(company_name, Keys.ENTER)


@when(u'He Save Details Of Company')
def extracting_information(context):
    D = {}
    try:
        D['name'] = context.driver.find_element(By.XPATH, "(//*[@class='SPZz6b']/descendant::span)[1]").text
    except:
        D['name'] = 'Null'
    try:
        D['address'] = context.driver.find_element(By.XPATH, "(//span[@class='LrzXr'])").text
    except:
        D['address'] = 'Null'
    try:
        D['rating'] = context.driver.find_element(By.XPATH, "(//*[@class='CJQ04']/descendant::span)[1]").text
    except:
        D['rating'] = 'Null'
    try:
        D['reviews'] = context.driver.find_element(By.XPATH, "(//*[@class='CJQ04']/descendant::a)").text
    except:
        D['reviews'] = 'Null'
    try:
        directions = context.driver.find_element(By.XPATH, "(//div[@class='QqG1Sd'])[2]").click()
        time.sleep(5)
        url = str(context.driver.current_url)
        lan = re.search('@\S+,\S+,', url)
        Log_and_Lat = lan.group()
        D['Log_and_Lat'] = Log_and_Lat.replace('@', '')
    except:
        D['Log_and_Lat'] = 'Null'
    Details.append(D)


@then(u'He Make Csv File Of That')
def makeing_csv_file(context):
    field_names = ['name', 'address', 'rating', 'reviews', 'Log_and_Lat']
    with open('company_report.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(Details)
