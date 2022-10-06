from abc import ABCMeta, abstractmethod

class ICubeA(metaclass = ABCMeta):
    '''An interface for an object'''

    @staticmethod
    @abstractmethod
    def manufacture(width, height, depth):
        '''Manufactures a cube'''




