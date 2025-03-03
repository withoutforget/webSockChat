from src.models.message import Message, MessageList
from src.repository.messages import Messages


class MessageService:
    messages: Messages

    def __init__(self, messages: Messages):
        self.messages = messages

    def get_update(self, after_time: int = 0) -> MessageList:
        return self.messages.get_after(after_time)

    def send_message(self, username: str, text: str, timestamp: int) -> None:
        msg = Message(from_username=username, text=text, timestamp=timestamp)
        self.messages.add(msg)
