# autoQuestionnaire 自动问卷填写程序

`autoQuestionnaire` 是一个基于 Python 和 Selenium 的自动化工具，旨在帮助用户自动填写问卷星上的问卷。通过此工具，您可以大大减少在重复性问卷填写上的时间和精力投入。

## 功能特点

当前程序支持的题型包括：

- **单选题**：自动选择单选题中的一个选项。
- **多选题**：从多选题的复选框列表中选择多个选项。
- **填空题**：自动填写问卷中的输入框，支持预定义答案或调用 AI 生成答案。
- **文本题**：针对问卷中的简答题，自动填写长文本内容，支持预定义答案或调用 AI 生成答案。。
- **排序题**：根据预定义或随机顺序，对选项进行排序。
- **下拉框题**：从下拉菜单中自动选择一个选项。
- **量表题**：自动在量表中选择对应的评分值。
- **矩阵量表题**：在矩阵量表中自动选择对应的选项。
- **评分题**：根据题目要求自动进行评分。

## 安装指南

在运行程序之前，请按照以下步骤配置您的环境并安装所需依赖：

### 1. 安装 Python

确保您的系统中已安装 `Python 3.x`。如果尚未安装，请前往 [Python 官网](https://www.python.org/downloads/)下载并安装适合您操作系统的版本。

### 2. 安装 Selenium

`Selenium` 是用于 Web 自动化测试的 Python 库，您可以使用 pip 进行安装：

```
pip install selenium
```

### 3. 配置 OpenAI

程序利用 `OpenAI` 的 `API` 来处理填空题的自动回答。您需要在 `openAi` 文件夹下的 `get_openai_response.py` 文件中配置您的 `OpenAI API` 密钥：

```
openai.api_key = "your-api-key-here"
```

将 `"your-api-key-here"` 替换为您自己的 `API` 密钥。

## 使用方法

1. **配置环境**：按照上述步骤完成所有依赖的安装。
2. **运行程序**：在终端或命令行中导航到项目目录，并运行主程序文件。
3. **自动填写问卷**：程序将根据配置的逻辑自动进行问卷的填写。

未来版本将继续添加更多题型的支持，优化现有功能，并改善用户体验。

## 注意事项

- **API 调用**：在使用 `OpenAI` 进行填空题回答时，请确保您的 `API` 调用次数和费用在可控范围内。
- **依赖安装**：在程序使用过程中，如遇到缺少依赖的提示，请根据提示使用 `pip install` 命令进行安装。

希望这个工具能为您的问卷填写工作带来便利！