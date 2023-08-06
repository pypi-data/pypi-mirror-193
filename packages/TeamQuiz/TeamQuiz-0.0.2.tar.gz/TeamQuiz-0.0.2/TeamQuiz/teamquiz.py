import requests
class Quiz:
    def __init__(self):
        url = "http://vccfinal.online:8000/questions"
        
        response = requests.get(url)
        if response.status_code == 200:
            self.questions=response.json()['message']

    def generate_map(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        map = ""
        for i in range(self.rows):
            for j in range(self.columns):
                map += "#"
            map += "\n"
        return map

    def get_all(self):
        return self.questions

    def get_question(self,num: int):
        self.num=num-1
        return self.questions[self.num]

    def submit(self,question_num: int, answer: str):
        question_num-=1
        url = "http://vccfinal.online:8000/submit/"+str(question_num)+"/"+answer
        response = requests.post(url)
        if response.status_code == 200:
           return response.json()['message']
        

