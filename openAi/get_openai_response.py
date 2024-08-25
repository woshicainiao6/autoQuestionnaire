import openai

from static.configuration import api_key, base_url, default_headers

# 初始化OpenAI API配置
openai.api_key = api_key
openai.base_url = base_url
openai.default_headers = default_headers


def get_openai_response(content):
    """
    调用OpenAI API并返回不同的回答。
    参数:
    content (str): 用户输入的内容。
    返回:
    str: OpenAI模型生成的回答。
    """
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": content + ",请使用简短的中文且符合问卷调查的话语回答我，不要反问我根据你的理解直接给出答案，以第一人称回答，要求陈述句，不要使用对话的形式",
                },
            ],
        )
        # 返回模型的回答
        return completion.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"

# if __name__ == "__main__":
#     # 测试函数
#     response = get_openai_response("你好")
#     print(response)
#
#     # 你可以传入不同的内容调用该函数
#     another_response = get_openai_response("你好，你是谁")
#     print(another_response)
