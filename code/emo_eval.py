import re
from openai import OpenAI

class emo_eval:
    API_KEY = "sk-69473092baff4de680f74095fc0dba66"
    MODEL = "deepseek-chat"  # "deepseek-chat" == deepseek-v3, "deepseek-reasoner" == deepseek-r1
    def __init__(self, api_key = API_KEY, model_name = MODEL, temperature = 0.5):
        self.prompt = """
        现在你需要分析用户输入中的情感色彩，并给出一个评分和一句对我说的话。
        要求如下
        关于评分：
        （1）评分尽量照顾到整个句子的感情色彩 （2）客观公正
        （3）分数在0-100之间，是精度为0.1的浮点数，其中，以50.0为中性标准，50.0以上为乐观积极，50.0以下为悲观消极。越偏离50.0代表对应的情感越强烈。
        关于“对我说的话”
        （0）你的设定是我的好朋友，说话要符合口语。
        （1）照顾到用户当天的感情，以鼓励、同乐或者安慰为主。
        （2）字数可以长一些，不少于200字为好.给出鼓励、支持、开导的语气
        （3）语句通顺自然，不要使用拗口的表达方式
        （4）不要太冷漠，减少语气词
        （5）禁止说教，当悲观（评分小于40.0）的时候就不要给建议了，而是表达同情和支持，要有同理心。
        输出格式为：
        “0（一个数，不能出现其他的文字）@XXXX。（对我说的话）“
        """
        self.api_key = api_key
        self.model_name = model_name
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.temperature = temperature

    def eval(self, text):
        while True:
            try:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[
                        {
                            "role": "system",
                            "content": self.prompt
                        },
                        {
                            "role": "user",
                            "content": text
                        }
                    ],
                    stream=False,
                    temperature=self.temperature
                )
                info = response.choices[0].message.content
                print(info.split('@'))
                rate, text = info.split("@")
                rate = float(rate)
                return rate, text
            except:
                pass
