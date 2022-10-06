class Club:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f'the club {self.name}'
    
    def organize_event(self):
        return f'Hires an artist to perform for the people'


