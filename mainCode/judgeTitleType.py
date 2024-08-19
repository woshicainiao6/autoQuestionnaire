from differentQuestion.dropdownMenuSelection import select_random_area
from differentQuestion.fillTextarea import fill_textarea
from differentQuestion.matrixScaleChoice import matrix_scale_choice
from differentQuestion.multipleChoice import multiple_choice
from differentQuestion.multipleFillBlank import multipleFillBlank
from differentQuestion.scaleChoice import scale_choice
from differentQuestion.singleChoice import simple_choice
from differentQuestion.singleFillBlank import single_fill_blank
from differentQuestion.sortChoice import sort_choice


# 判读选项的类型
def judgeTitleType(driver, title_id, title_type):
    if title_type != None:
        match title_type:
            case "1":
                single_fill_blank(driver, title_id)
            case "2":
                fill_textarea(driver, title_id)
            case "3":
                simple_choice(driver, title_id)
            case "4":
                multiple_choice(driver, title_id)
            case "5":
                scale_choice(driver, title_id)
            case "6":
                matrix_scale_choice(driver, title_id)
            case "7":
                select_random_area(driver, title_id)
            case "8":
                print(title_id)
                print('title8')
            case "9":
                multipleFillBlank(driver, title_id)
            case "10":
                print(title_id)

                print('title10')
            case "11":
                sort_choice(driver, title_id)
            case _:
                print("Unknown title")
