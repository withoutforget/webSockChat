from pydantic import BaseModel

class Message(BaseModel):
    from_username:str
    text:str
    timestamp:int

class MessageList(BaseModel):
    messages: list[Message]

    
