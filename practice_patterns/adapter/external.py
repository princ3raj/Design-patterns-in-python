
class Musician:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'The Musician {self.name}'
    
    def play(self):
        return 'Plays music'


class Dancer:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'The dancer {self.name}'

    def dance(self):
        return 'does a dance performance'
