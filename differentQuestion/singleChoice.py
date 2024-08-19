import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from mainCode.getChoiceNum import getChoicesNum
from mainCode.wait_and_click import wait_and_click
from openAi.get_openai_response import get_openai_response
from randomChoice.singleRandomChoice import single_random_choice


def simple_choice(driver, title_id):
    title_num_xpath = f'//*[@id="div{title_id}"]/div[2]'
    title_num = getChoicesNum(driver, title_num_xpath)
    select_choice = single_random_choice(title_num)
    choice_xpath = f"//div[@for='q{title_id}_{select_choice}']"
    wait_and_click(driver, choice_xpath)
    input_xpath = f'//*[@id="tqq{title_id}_{select_choice}"]'
    title_xpath = f'//*[@id="div{title_id}"]/div[1]/div[2]'
    title_text = driver.find_element(By.XPATH, title_xpath).text
    try:
        # 检查输入框是否存在
        input_elements = WebDriverWait(driver, 0.1).until(
            EC.presence_of_all_elements_located((By.XPATH, input_xpath))
        )

        if input_elements:
            # 填写输入框
            # 获取OpenAI生成的答案
            answer_text = get_openai_response(title_text)
            # 等待answer_text生成
            while not answer_text:
                time.sleep(0.1)
            input_element = input_elements[0]  # 获取第一个找到的输入框
            input_element.send_keys(answer_text)
        else:
            print(f"输入框未找到: {input_xpath}")

    except TimeoutException:
        pass
    except NoSuchElementException:
        pass
