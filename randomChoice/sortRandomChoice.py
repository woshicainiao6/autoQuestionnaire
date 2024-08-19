import random

from selenium.webdriver.common.by import By


def sort_random_choice(driver, question_num, title_id):
    # 生成1到question_num的数字列表，并随机选择question_num个不重复的数字
    choices = random.sample(range(1, question_num + 1), question_num)
    choice_text = []
    for choice in choices:
        choice_text_xpath = f'//*[@id="div{title_id}"]/ul/li[{choice}]/div[2]'
        choice_text.append(driver.find_element(By.XPATH, choice_text_xpath).text)
    return choice_text
