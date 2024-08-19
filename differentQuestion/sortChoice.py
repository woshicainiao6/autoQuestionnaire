import time

from selenium.webdriver.common.by import By

from mainCode.getChoiceNum import getChoicesNum
from mainCode.wait_and_click import wait_and_click
from randomChoice.sortRandomChoice import sort_random_choice


def sort_choice(driver, title_id):
    # 获取元素总数
    title_num_xpath = f'//*[@id="div{title_id}"]/ul'
    titleNum = getChoicesNum(driver, title_num_xpath)

    # 获取需要点击的排序顺序，例如 [1, 3, 2]
    sort_choice = sort_random_choice(driver, titleNum, title_id)
    # print('sort_choice:', sort_choice)
    clicked_texts = []
    for click_order_text in sort_choice:
        # 每次点击前重新获取当前所有li元素
        li_elements = driver.find_elements(By.XPATH, f'//*[@id="div{title_id}"]/ul/li')
        # 找到并点击符合条件的元素
        for index,li in enumerate(li_elements) :
            # 获取元素的文本内容
            text = li.find_element(By.XPATH, './div[2]').text
            # print('text:', text)

            # 如果文本内容符合当前点击顺序且未被点击过，则点击它
            if text == click_order_text and text not in clicked_texts:
                # 点击该元素
                li_xpath = f'//*[@id="div{title_id}"]/ul/li[{index + 1}]/div[2]'
                # print('li_xpath:', li_xpath)

                # 点击该元素
                wait_and_click(driver, li_xpath)

                # 添加到已点击列表
                clicked_texts.append(text)

                # 点击后等待页面更新
                time.sleep(1)
                break
