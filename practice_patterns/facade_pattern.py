from abc import ABCMeta, abstractmethod
from enum import Enum
State = Enum("State", "new running sleeping restart zombie")

class Server(metaclass = ABCMeta):

    @abstractmethod
    def __init__(self):
        pass
    
    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass
    
    @abstractmethod
    def kill(self, restart =  True):
        pass


class FileServer(Server):
    def __init__(self) -> None:
        '''Actions required for initializing the file server'''
        self.name = 'FileServer'
        self.state = State.new
    
    def boot(self):
        print(f"Booting the {self}")
        '''actions required for booting the file server'''
        self.state = State.running
    
    def kill(self, restart = True):
        print(f'Killing {self}')
        '''Actions required for killing the file server'''
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        '''Check validity of permissions , user rights etc'''
        print(f'Trying to create the file {name} for user {user} with permissions {permissions}')


class ProcessServer(Server):

    def __init__(self):
        '''actions required for initializing the process server'''
        self.name = "ProcessServer"
        self.state = State.new

    def boot(self):
        print(f"Booting the {self}")
        '''Actions required for booting the process server'''
        self.state = State.running
    
    def kill(self, restart = True):
        print(f"Killing {self}")
        '''actions required for killing the process server'''
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        '''Check user rights, generate PIds etc'''
        print(f"Trying to create the process {name} for user {user}")


class OperatingSystem:
    '''The facade'''
    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()
    
    def start(self):
        [ i.boot() for i in (self.fs, self.ps) ]
    
    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file("foo", "hello", "-rw-r-r")
    os.create_process("bar", "ls /tmp")


if __name__ == "__main__":
    main()



