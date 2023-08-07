from chatglm import ChatGLM
from agent import Agent

question = "最近steam有什么游戏打折了？"
robot = ChatGLM()
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

