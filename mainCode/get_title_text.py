from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def get_title_text(driver, title_id):
    title_xpath_list = [
        f'//*[@id="div{title_id}"]/div[1]/div[2]',
        f'//*[@id="div{title_id}"]/div[1]/div'
    ]

    for xpath in title_xpath_list:
        try:
            element = driver.find_element(By.XPATH, xpath)
            if element:
                return element.text
        except NoSuchElementException:
            continue
    return ""
