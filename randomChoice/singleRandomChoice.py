import random


def single_random_choice(question_num, weights=None):
    # 生成1到question_num的数字列表
    numbers = list(range(1, question_num + 1))
    # 如果weights为空或者为None，直接进行随机选择
    if not weights:
        selected = random.choice(numbers)
    else:
        # 如果weights不为空，确保其长度与question_num一致
        if len(weights) != question_num:
            raise ValueError("权重列表的长度必须等于question_num的值")

        # 使用random.choices根据权重进行选择
        selected = random.choices(numbers, weights=weights, k=1)[0]

    return selected
