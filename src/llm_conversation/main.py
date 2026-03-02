'''
TODO: 
- Have a conversation size window that drops earlier entries if the conversation
    moves beyond a set limit. Might need to add a length field to Response.
'''
from dataclasses import dataclass
from typing import Literal


@dataclass
class Response:
    role: Literal['user', 'assistant']
    text: str


class Conversation:

    def __init__(self):

        self.overall_prompt: str = None
        self.context: list[str] = []
        self.history: list[Response] = []

        self.reasoning_level: str = None


    def set_reasoning_level(self, level: str):

        VALID_LEVELS = ('low', 'medium', 'high')

        if level not in VALID_LEVELS:
            raise ValueError(f'Invalid level. Valid options are {VALID_LEVELS}!')

        self.reasoning_level = level

        return


    def set_overall_prompt(self, text: str):

        self.overall_prompt = text

        return


    def add_context(self, text: str):
        '''
        Add background context the system can reference.
        '''

        self.context.append(text)

        return


    def add_response(self, role: str, text: str):
        '''
        Add either a user or assistant (currently only these
        two supported) response to an ongoing conversation.
        '''

        VALID_ROLES = ('user', 'assistant')

        if role not in VALID_ROLES:
            raise ValueError(f'Invalid role. Valid options are {VALID_ROLES}!')

        self.history.append(Response(role=role, text=text))

        return


    def to_dict(self):
        '''
        Generate a dictionary equivalent to the harmony conversation.
        This let's you create an API friendly data object that can be
        easily reconstituted into a conversation.
        '''

        result = {}

        result['reasoning_level'] = self.reasoning_level
        result['overall_prompt'] = self.overall_prompt  # str.
        result['context'] = self.context  # List of str.
        result['history'] = [{'role': h.role, 'text': h.text} for h in self.history]

        return result


    def from_dict(self, data: dict):
        '''
        Build an instance of Conversation() from a dictionary.
        '''

        NEEDED_FIELDS = (
            'reasoning_level',
            'overall_prompt',
            'context',
            'history')

        if not set(NEEDED_FIELDS) == set(data.keys()):
            raise ValueError('Input "data" is unaligned to needed keys!')

        self.reasoning_level = data['reasoning_level']
        self.overall_prompt = data['overall_prompt']
        self.context = data['context']
        self.history = [Response(role=h['role'], text=h['text']) for h in data['history']]

        return


if __name__ == '__main__':

    c = Conversation()
    c.set_overall_prompt(text='Your name is Harry Potter.')
    c.add_context(text='You are a third year student at a special school for magic.')
    c.add_context(text='Your best friends are named Ron and Hermione.')

    c.add_response(role='user', text='Hi, how are you?')
    c.add_response(role='assistant', text='Awesome, because Im a wizard.')

    d = Conversation()
    d.from_dict(data=c.to_dict())

    print(d.to_dict())

    pass
