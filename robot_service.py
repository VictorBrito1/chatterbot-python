from robot import *
from flask import Flask

VERSION = '1.0'

robot = ChatBot('Robô de atendimento Coronavírus',
    read_only=True,
    statement_comparison_function=compare_messages,
    response_selection_method=select_answer,
    logic_adapters=[
        {
            "import_path": "chatterbot.logic.BestMatch",
        }
    ])

robot_service = Flask(__name__)

@robot_service.route('/answer/<message>', methods=['GET'])
def get_answer(message):
    return robot.get_response(message).text

@robot_service.route('/version', methods=['GET'])
def get_version():
    return VERSION

if __name__ == '__main__':
    robot_service.run()
    