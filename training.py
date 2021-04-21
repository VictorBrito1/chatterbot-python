import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

robot = None
trainer = None
similar_words = ["coronavírus", "vírus", "corona", "covid", "covid-19"]

CONFIGS = [
    "D:\Projetos\IFBA\IA\chatterbot-python\configs\greetings.json",
    "D:\Projetos\IFBA\IA\chatterbot-python\configs\\infos.json"
]

def init():
    global robot
    global trainer
    
    robot = ChatBot('Robô de atendimento Coronavírus')
    trainer = ListTrainer(robot)

def load_chats():
    chats = []
    
    for config_file in CONFIGS:
        with open(config_file, 'r', encoding='utf-8') as file:
            config = json.load(file)
            chats.append(config['chats'])
            
            file.close()
            
    return chats

def train_robot(chats):
    global trainer
    global similar_words
    
    for chat in chats:
        for messages_answer in chat:
            messages = messages_answer['messages']
            answer = messages_answer['answer']
            
            for message in messages:
                if '%vírus%' in message:
                    for similar in similar_words:
                        msg = message.replace('%vírus%', similar)
                        trainer.train([msg, answer])
                        
                        print('Treinando o robô: ', 'mensagem - ', msg, '| resposta - ', answer)
                else:
                    trainer.train([message, answer])
                    print('Treinando o robô: ', 'mensagem - ', message, '| resposta - ', answer)

if __name__ == '__main__':
    init()
    chats = load_chats()
    
    if chats:
        train_robot(chats)
    