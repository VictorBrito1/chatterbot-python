from chatterbot import ChatBot
from difflib import SequenceMatcher

ACCEPTANCE = 0.70

def compare_messages(message, candidate_message):
    confidence = 0.0
    message_text = message.text
    candidate_message_text = candidate_message.text
    
    if message_text and candidate_message_text:
        confidence = SequenceMatcher(
            None,
            message_text,
            candidate_message_text
        )
        
        confidence = round(confidence.ratio(), 2)
        
        if confidence < ACCEPTANCE:
            confidence = 0.0
        else:
            print('Mensagem do usuario:', message_text, '| Mensagem candidata:', candidate_message, '| Nível de confiança:', confidence)
        
    return confidence

def select_answer(message, answer_list, storage=None):
    return answer_list[0]

def execute():
    robot = ChatBot('Robô de atendimento Coronavírus',
        read_only=True,
        statement_comparison_function=compare_messages,
        response_selection_method=select_answer,
        logic_adapters=[
            {
                "import_path": "chatterbot.logic.BestMatch",
            }
        ])
    
    while True:
        text = input("Digite alguma coisa...\n")
        answer = robot.get_response(text)
        
        if (answer.confidence > 0.0):
            print(answer)
        else:
            print('Ainda não sei como responder essa pergunta. Por favor, pergunte novamente.')
    

if __name__ == '__main__':
    execute()
    