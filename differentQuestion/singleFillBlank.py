import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from openAi.get_openai_response import get_openai_response
from randomChoice.timeRandomClick import time_random_click


def single_fill_blank(driver, title_id):
    # 定位输入框的XPath
    fill_blank_xpath = f'//*[@id="q{title_id}"]'
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, fill_blank_xpath))
    )
    if input_element.get_attribute('class') == 'datebox':
        input_element.click()
        time.sleep(1)
        time_random_click(driver)
        time.sleep(1)
        # confirm_button_xpath = f'//*[@id="layui-laydate1"]/div[2]/div/span[3]'
        # driver.find_element(By.XPATH, '//*[@id="layui-laydate1"]/div[2]/div/span[3]').click()
    else:
        # 定位问题的XPath
        title_xpath = f'//*[@id="div{title_id}"]/div[1]/div[2]'
        title_text = driver.find_element(By.XPATH, title_xpath).text

        # 获取OpenAI生成的答案
        answer_text = get_openai_response(title_text)

        # 等待answer_text生成
        while not answer_text:
            time.sleep(0.1)
        # 填写答案到输入框中
        input_element.send_keys(answer_text)
