import os

chat_language = os.getenv("INIT_LANGUAGE", default = "zh")

MSG_LIST_LIMIT = int(os.getenv("MSG_LIST_LIMIT", default = 7))
LANGUAGE_TABLE = {
  "zh": "食品材料分析",
  "en": "Food Material Analysis"
}

AI_GUIDELINES = '你是食品材料、營養專家，能分析食品材料成份，回應是否為全素、奶素、蛋奶素、五辛素、葷食、腎臟病、糖尿病等慢性疾病患者不適合食用等等建議，請簡化回應，只要其中有一項材料是葷食，即該項食品為葷食；若不是葷食只要其中有一項是蛋，即為蛋奶素；若不是葷食、蛋奶素只要其中有一項是奶，即為奶素；若不是葷食只要其中有一項為五辛，即為五辛素；不是葷食、蛋奶素、奶素、五辛素，即為全素。腎臟病及糖尿病等建議仍可以詳列，無論提問使用何種語言，一律使用繁體中文回答。'

class Prompt:
    def __init__(self):
        self.msg_list = []
        self.msg_list.append(
            {
                "role": "system", 
                "content": f"{LANGUAGE_TABLE[chat_language]}, {AI_GUIDELINES})"
             })    
    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.msg_list.pop(0)
        self.msg_list.append({"role": "user", "content": new_msg})

    def generate_prompt(self):
        return self.msg_list
