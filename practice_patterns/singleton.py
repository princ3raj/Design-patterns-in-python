import urllib.parse
import urllib.request

class SingletonType(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class URLFetcher(metaclass = SingletonType):


    def __init__(self) -> None:
        self.urls = []

    def fetch(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                the_page = response.read()
                print(the_page)
                self.urls.append(url)
    
    def dump_url_registry(self):
        return ', '.join(self.urls)


def main():

    MY_URLS = [
        "https://www.python.org/error",
        "https://www.voidspace.org.uk/",
        "https://www.google.com/",
        "https://fast.com/"
    ]

    print(URLFetcher() is URLFetcher())
    fetcher = URLFetcher()
    for url in MY_URLS:
        try:
            fetcher.fetch(url)
        except Exception as e:
            print(e)
    print('------------')
    done_urls = fetcher.dump_url_registry()
    print(f'Done urls: {done_urls}')

    
if __name__ == "__main__":
    main()

