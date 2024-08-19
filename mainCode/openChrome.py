import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from mainCode.chromeDriver import chrome_driver
from mainCode.judgeTitleType import judgeTitleType


def open_chrome(url):
    driver = chrome_driver(url)

    # 等待fieldset元素出现
    try:
        xpath = '//*[@id="fieldset1"]'
        fieldset = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )

        # 获取fieldset的子元素
        children = fieldset.find_elements(By.XPATH, "./*")

        # 输出子元素信息
        for index, child in enumerate(children):
            if child.get_attribute('style') != "display: none;":
                judgeTitleType(driver, child.get_attribute("topic"), child.get_attribute("type"))
        # time.sleep(20)

        # 提交问卷
        xpath_submit = "//div[@id='ctlNext' and contains(@class, 'submitbtn') and text()='提交']"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_submit))
        ).click()

        time.sleep(0.5)

    finally:
        # 关闭浏览器
        driver.quit()
        time.sleep(2)
