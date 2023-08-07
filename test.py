from llm import LLM
from agent import Agent

question = "博德之门3的评价如何？"
robot = LLM()
agent = Agent()
tool = agent.which_tools(question)
ans = robot.run(
    "下面我会给你一个问题，同时附上文档。请你根据文档回答我的问题\n"
    "文档\n"
    f"{tool(question,max_length=1500)}\n"
    "---\n"
    "问题\n"
    f"{question}"
          )
print(ans['response'])

