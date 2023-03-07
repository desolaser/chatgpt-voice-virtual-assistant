import abc

class ChatbotInterface(metaclass=abc.ABCMeta):
    """Interfaces for chatbots"""
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'get_response') and 
                callable(subclass.get_response) or 
                NotImplemented)

    @abc.abstractmethod
    def get_response(self, text):
        """Get response from chatbot"""
        raise NotImplementedError