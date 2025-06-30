import re
from openai import OpenAI
import json
from datetime import date
class event_eval:
    API_KEY = "sk-651f226536574f9794f0a41fea2b529f"
    MODEL = "deepseek-chat"  # "deepseek-chat" == deepseek-v3, "deepseek-reasoner" == deepseek-r1
    def __init__(self, api_key = API_KEY, model_name = MODEL, temperature = 0.5):
        self.prompt = """
你是一个日程事件信息提取助手，请从用户输入的一句话中，提取出事件的核心信息。

要求你返回一个 JSON 对象，包含以下字段：

- "title"：事件简短标题（不超过10字）
- "info"：事件的详细说明，尽量保留用户提供的信息
- "category"：事件类型（如学习、会议、运动、娱乐等）
- "StartTime"：开始时间，格式为 "yyyy-MM-dd HH:mm"
- "EndTime"：结束时间，格式为 "yyyy-MM-dd HH:mm"

当前日期是：{{TODAY}}

请严格按照格式返回 JSON 结构，内容如下：
{
  "title": "...",
  "info": "...",
  "category": "...",
  "StartTime": "...",
  "EndTime": "..."
}

用户输入：{{用户输入的事件句子}}

        """
        self.api_key = api_key
        self.model_name = model_name
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.temperature = temperature

    def eval(self, text):
        today_str = date.today().strftime("%Y-%m-%d")
        prompt_filled = self.prompt.replace("{{TODAY}}", today_str).replace("{{用户输入的事件句子}}", text)

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": prompt_filled
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            stream=False,
            temperature=self.temperature
        )
        raw = response.choices[0].message.content
        match = re.search(r'\{.*\}', raw, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except Exception as e:
                print("解析 JSON 失败：", e)
                return None
        else:
            print("未匹配到 JSON 内容")
            return None
