from abc import ABCMeta, abstractmethod

class ICubeB(metaclass = ABCMeta):
    '''A Interface for an object'''

    @staticmethod
    @abstractmethod
    def create(top_left_front, bottom_right_back):
        '''Manufactures a cube with coordinates offset'''
        

