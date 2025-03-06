import time
from random import choice

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from randomChoice.dropdownRandomMenuSelection import getDropdownChoiceList


def city_checkbox(driver, title_id):
    # province_xpath = f'//*[@id="divFrameData"]/div/div[1]/div/select'
    # province_list=getDropdownChoiceList(driver, province_xpath)
    # random_probince=choice(province_list)
    random_probince='山东'
    province_select = Select(driver.find_element(By.NAME, "province"))
    province_select.select_by_visible_text(random_probince)
    city_checkbox_xpath=f'//*[@id="divFrameData"]/div/div[2]/div/select'
    city_list=getDropdownChoiceList(driver, city_checkbox_xpath)
    random_city=choice(city_list)
    city_select = Select(driver.find_element(By.NAME, "city"))
    city_select.select_by_visible_text(random_city)
    time.sleep(1)
    button_xpath='//*[@id="divFrameData"]/div/div[3]/a'
    driver.find_element(By.XPATH, button_xpath).click()
