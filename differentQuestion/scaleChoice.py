from mainCode.wait_and_click import wait_and_click
from randomChoice.singleScaleChoice import getSingleScaleChoice


def scale_choice(driver, title_id):
    select_choice = getSingleScaleChoice(driver, title_id)
    xpath = f'//*[@id="div{title_id}"]/div[2]/div/ul/li[{select_choice}]/a'
    wait_and_click(driver, xpath)
