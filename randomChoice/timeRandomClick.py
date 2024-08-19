import random
import time

from selenium.webdriver.common.by import By


def time_random_click(driver):
    left_click_num = random.randint(1, 20)
    for i in range(left_click_num):
        left_click_xpath = f'//*[@id="layui-laydate1"]/div[1]/div[1]/i[2]'
        driver.find_element(By.XPATH, left_click_xpath).click()
        time.sleep(0.1)
    tr_random = random.randint(1, 6)
    td_random = random.randint(1, 7)
    data_xpath = f'//*[@id="layui-laydate1"]/div[1]/div[2]/table/tbody/tr[{tr_random}]/td[{td_random}]'
    time.sleep(1)
    driver.find_element(By.XPATH, data_xpath).click()
