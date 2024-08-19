import openai

# 初始化OpenAI API配置
openai.api_key = "sk-jrn0VdyFcoBrbUZG92Bd2e35E0A541EeBcDe82F98aCaFc5b"
openai.base_url = "https://free.gpt.ge/v1/"
openai.default_headers = {"x-foo": "true"}


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
                    "content": content,
                },
            ],
        )
        # 返回模型的回答
        return completion.choices[0].message.content

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # 测试函数
    response = get_openai_response("你好")
    print(response)

    # 你可以传入不同的内容调用该函数
    another_response = get_openai_response("你好，你是谁")
    print(another_response)
