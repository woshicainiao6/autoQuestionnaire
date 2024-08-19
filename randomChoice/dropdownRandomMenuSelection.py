from selenium.webdriver.common.by import By


def getDropdownChoiceList(driver, xpath):
    parentElement = driver.find_element(By.XPATH, xpath)
    children = parentElement.find_elements(By.XPATH, "./*")
    list = []
    for index, child in enumerate(children):
        if index == 0:
            continue
        list.append(child.text)
    return list
