from mainCode.getChoiceNum import getChoicesNum
from mainCode.wait_and_click import wait_and_click
from randomChoice.matrixScaleRandomChoice import getMultipleScaleChoice


def matrix_scale_choice(driver, title_id):
    matrix_scale_choice_num_xpath = f'//*[@id="div{title_id}"]'
    matrix_scale_choice_num = getChoicesNum(driver, matrix_scale_choice_num_xpath) - 3
    # print("matrix_scale_choice_num", matrix_scale_choice_num)
    for index in range(1, matrix_scale_choice_num + 1):
        option_choice = getMultipleScaleChoice(driver, title_id, index)
        xpath = f"//tr[@id='drv{title_id}_{index}']//a[@dval='{option_choice}']"
        wait_and_click(driver, xpath)
