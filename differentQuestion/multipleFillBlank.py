import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from mainCode.getChoiceNum import getChoicesNum
from openAi.get_openai_response import get_openai_response


def multipleFillBlank(driver, title_id):
    question_num_xpath = f'//*[@id="divRefTab{title_id}"]/tbody'
    question_num = int(getChoicesNum(driver, question_num_xpath) / 2)
    title_text_xpath = f'//*[@id="div{title_id}"]/div[1]/div[2]'
    title_text = driver.find_element(By.XPATH, title_text_xpath).text
    for index, question in enumerate(range(question_num)):
        question_title_xpath = f'//*[@id="drv{title_id}_{index + 1}"]/td[1]/div/span'
        question_title = driver.find_element(By.XPATH, question_title_xpath).text
        total_title = title_text + question_title
        answer_text = get_openai_response(total_title)
        # 等待answer_text生成
        while not answer_text:
            time.sleep(0.1)
        input_xpath = f'//*[@id="q{title_id}_{index}"]'
        input_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, input_xpath))
        )
        input_element.send_keys(answer_text)
