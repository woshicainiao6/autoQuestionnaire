import random

from selenium.webdriver.common.by import By


def getMultipleScaleChoice(driver, question_id, index):
    scale_choice_xpath = f'//*[@id="drv{question_id}_{index}t"]/td'
    scaleChoiceNum = int(driver.find_element(By.XPATH, scale_choice_xpath).get_attribute('colspan'))
    # print("scaleChoiceNum",scaleChoiceNum)
    scale_choice = random.randint(1, scaleChoiceNum - 1)
    return scale_choice
