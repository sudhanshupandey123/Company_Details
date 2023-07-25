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
Details=[]
@given(u'He Opened Google Page')
def opening_google(context):
    context.driver=webdriver.Chrome()
    context.driver.get('https://www.google.com/')
    context.driver.maximize_window()



@when(u'He Search Company Name "{company_name}"')
def step_impl(context,company_name):
    context.company_name=company_name
    context.driver.find_element(By.XPATH,"//*[@type='search']").send_keys(company_name,Keys.ENTER)


@when(u'He Look For Card Apperance')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH,"//*[@id='_oKS_ZN3BA4_cseMP7YepoAI_42']")
    except:
        context.name=context.company_name
        context.address='Null'
        context.rating='Null'
        context.reviews='Null'
        context.Log_and_Lat='Null'
        D = {}
        D['Company_Name'] = context.name
        D['Company_Address'] = context.address
        D['Google_Rating'] = context.rating
        D['Reviews'] = context.reviews
        D['Log_and_Lat'] = context.Log_and_Lat.replace('@', '')
        Details.append(D)
        field_names = ['Company_Name', 'Company_Address', 'Google_Rating', 'Reviews', 'Log_and_Lat']
        with open('Company_Details.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(Details)



@then(u'He Save Details Of Company')
def step_impl(context):
    try:
        context.name = context.driver.find_element(By.XPATH, "(//*[@class='SPZz6b']/descendant::span)[1]").text
        context.address = context.driver.find_element(By.XPATH, "(//span[@class='LrzXr'])").text
        context.rating = context.driver.find_element(By.XPATH, "(//*[@class='CJQ04']/descendant::span)[1]").text
        context.reviews = context.driver.find_element(By.XPATH, "(//*[@class='CJQ04']/descendant::a)").text
        directions = context.driver.find_element(By.XPATH, "(//div[@class='QqG1Sd'])[2]").click()
        time.sleep(5)
        url = str(context.driver.current_url)
        lan = re.search('@\S+,\S+,', url)
        context.Log_and_Lat = lan.group()
        D = {}
        D['Company_Name'] = context.name
        D['Company_Address'] = context.address
        D['Google_Rating'] = context.rating
        D['Reviews'] = context.reviews
        D['Log_and_Lat'] = context.Log_and_Lat.replace('@', '')
        Details.append(D)
        field_names = ['Company_Name', 'Company_Address', 'Google_Rating', 'Reviews', 'Log_and_Lat']
        with open('Company_Details.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(Details)
    except Exception as msg:
        print(msg)


#s='https://www.google.com/maps/dir/12.9614549,77.7108679/g7cr/@12.977352,77.5817119,12z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x3bae167e2fa71621:0x1f56c87698101c58!2m2!1d77.5989907!2d12.9760336?entry=ttu'
# import re
# res=re.search('@\S+/',s)
# print(res.group())

# driver=webdriver.Chrome()
# driver=webdriver.Chrome()
# driver.get('https://www.google.com/')
# driver.maximize_window()
# driver.find_element(By.XPATH,"//*[@type='search']").send_keys('g7cr',Keys.ENTER)
# #driver.get('https://www.google.com/maps/dir/12.9614549,77.7108679/g7cr/@12.977352,77.5817119,12z/data=!3m1!5s0x3bae167afe46e27b:0xf955ec9efa77b1be!4m9!4m8!1m1!4e1!1m5!1m1!1s0x3bae167e2fa71621:0x1f56c87698101c58!2m2!1d77.5989907!2d12.9760336?entry=ttu')
# driver.find_element(By.XPATH,"(//div[@class='QqG1Sd'])[2]").click()
# time.sleep(3)
# print(driver.current_url)


