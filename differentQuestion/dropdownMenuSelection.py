from random import choice

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from randomChoice.dropdownRandomMenuSelection import getDropdownChoiceList


def select_random_area(driver, title_id):
    choice_list_xpath = f'//*[@id="q{title_id}"]'
    choice_list = getDropdownChoiceList(driver, choice_list_xpath)
    selected_area = choice(choice_list)
    title_name = f"q{title_id}"
    # 使用选定的区域名称选择下拉菜单中的选项
    select = Select(driver.find_element(By.NAME, title_name))
    select.select_by_visible_text(selected_area)
