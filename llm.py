import config
import os
import json
import requests
from typing import List
from datetime import datetime

class LLM():
    
    def __init__(self, 
                 base_address = config.BASE_ADDRESS,
                 ) -> None:
        self.url = base_address

    def run(self, prompt):
        try:
            payload = {
                "prompt": prompt,
                "max_length": 8192,  # This is truely max length of chatglm
                "top_p": 0.9,
                "temperature": 0.7
            }
            response = requests.post(url=self.url, json=payload)

            if response.status_code == 200:
                return json.loads(response.content)
            else:
                return {
                    "response": "抱歉，服务器出现了点问题。",
                    "history": [],
                    "status": 500,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
        except Exception as e:
            return {
                "response": f"发生了一个错误：{str(e)}",
                "history": [],
                "status": 500,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        
    def run_with_history(self, prompt: str, history: List):
        try:
            payload = {
                "prompt": prompt,
                "history": history,
                "max_length": 8192,  # This is truely max length of chatglm
                "top_p": 0.9,
                "temperature": 0.7
            }
            response = requests.post(url=self.url, json=payload)

            if response.status_code == 200:
                return json.loads(response.content)
            else:
                return {
                    "response": "抱歉，服务器出现了点问题。",
                    "history": [],
                    "status": 500,
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
        except Exception as e:
            return {
                "response": f"发生了一个错误：{str(e)}",
                "history": [],
                "status": 500,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
