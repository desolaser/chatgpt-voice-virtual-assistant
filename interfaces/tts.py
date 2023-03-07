import abc

class TTSInterface(metaclass=abc.ABCMeta):
    """Class to implement text to speech modules"""

    @classmethod
    def __subclasshook(cls, subclass):
        return (hasattr(subclass, 'play') and 
                callable(subclass.play) or 
                NotImplemented)

    @abc.abstractmethod
    def play(self, text):
        """Get response from chatbot"""
        raise NotImplementedError