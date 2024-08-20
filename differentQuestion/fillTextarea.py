from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from mainCode.get_title_text import get_title_text
from openAi.get_openai_response import get_openai_response

def fill_textarea(driver, title_id):
    title_text = get_title_text(driver, title_id)

    # 获取OpenAI生成的答案
    answer_text = get_openai_response(title_text)

    # 定位输入框的XPath
    fill_blank_xpath = f'//*[@id="q{title_id}"]'
    input_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, fill_blank_xpath))
    )

    # 确保输入框可见后填写答案
    WebDriverWait(driver, 10).until(EC.visibility_of(input_element))

    # 填写答案到输入框中
    input_element.send_keys(answer_text)
