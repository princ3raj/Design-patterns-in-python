from abc import ABCMeta, abstractmethod
import urllib.request

class ResourceContent:
    """
    Define the abstraction's interface
    Maintain a reference to an object which implements the Implementor.
    """

    def __init__(self, imp):
        self._imp = imp
    
    def show_content(self, path):
        self._imp.fetch(path)

class ResourceContentFetcher(metaclass = ABCMeta):
    '''
    Define the interface for implementation classes that fetch content.
    '''
    @abstractmethod
    def fetch(path):
        pass


class URLFetcher(ResourceContentFetcher):
    '''Implement the Implementor interface and define its concrete implementations'''

    def fetch(self, path):
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)

class LocalFileFetcher(ResourceContentFetcher):
    '''Implement the implementor interface and define its concrete implementations'''

    def fetch(self, path):
        # path is the filepath to a textfile
        with open(path) as f:
            print(f.read())

def main():
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content("https://python.org")

    print("-----------------")

    localfs_fetcher = LocalFileFetcher()
    iface = ResourceContent(localfs_fetcher)
    iface.show_content("file.txt")


if __name__ == "__main__":
    main()