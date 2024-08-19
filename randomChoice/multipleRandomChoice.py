import random


def multiple_random_choice(question_num, weights=None):
    # 随机生成一个要多选的个数 num
    num = random.randint(1, question_num)
    # 从 1 到 question_num 随机选择 num 个不重复的数
    selected_numbers = random.sample(range(1, question_num + 1), num)
    return selected_numbers
