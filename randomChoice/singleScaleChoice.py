import random

from mainCode.getChoiceNum import getChoicesNum


def getSingleScaleChoice(driver, question_id):
    scale_choice_xpath = f'//*[@id="div{question_id}"]/div[2]/div/ul'
    scaleChoiceNum = getChoicesNum(driver, scale_choice_xpath)
    scale_choice = random.randint(1, scaleChoiceNum)
    return scale_choice
