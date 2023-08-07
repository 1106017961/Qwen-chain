import config
from duckduckgo_search import DDGS
from llm import LLM
from loguru import logger

class Agent():
    def __init__(self) -> None:
        self.robot = LLM()

    def which_tools(self, prompt: str):
        """
        输入：用户的输入
        输出：工具函数
        本方法用于将用户的输入格式化后，发送给LLM思考。LLM得出应该使用哪一个工具后返回工具函数
        """
        format_prompt = (
            "你是一个善于使用工具的模型。下面是提供给你可以使用的工具列表。[网络搜索，计算器]\n"
            f"下面我会给你一段文字，请你根据文字判断应该使用哪个工具。\n---\n{prompt}\n---\n"
            "请**直接输出你选择的工具名称**，不要有多余输出，不要有其他文字。"
        )
        ans = self.robot.run(format_prompt)['response']
        if "网络搜索" in ans:
            return self.web_search
        elif "本地知识库查询" in ans:
            return "本地知识库查询"
        elif "图片生成" in ans:
            return "图片生成"

        return "notools"
    
    def web_search(self,prompt , max_length: int = 300):
        format_prompt = (
            "你是一个善于使用搜索引擎的人工智能助理\n"
            f"下面我会给你一段用户的输入，请你根据用户的输入，将其改写为更适合搜索的关键词。\n---\n{prompt}\n---\n"
        )
        ans = self.robot.run(format_prompt)['response'][1:-1]
        logger.debug(ans)
        length = 0
        content = []
        with DDGS(proxies=config.PROXY_ADDRESS, timeout=20) as ddgs:
            for r in ddgs.text(ans, region=config.REGION):
                body = r.get('body', '')
                remaining_length = max_length - length
                if len(body) <= remaining_length:
                    content.append(body)
                    length += len(body)
                else:
                    content.append(body[:remaining_length])
                    break

        return content

if __name__ == "__main__":
    question = "古龙有哪些作品？"
    test = Agent()
    tools = test.which_tools(question)
    ans = tools(question)
    



