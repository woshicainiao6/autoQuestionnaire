from selenium.webdriver.common.by import By


# 获取选项的数量
def getChoicesNum(driver, xpath):
    parentElement = driver.find_element(By.XPATH, xpath)
    children_num = len(parentElement.find_elements(By.XPATH, "./*"))
    return children_num
