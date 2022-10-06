import copy

class Website:
    def __init__(self,name, domain, description, author, **kwargs):
        self.name = name
        self.domain = domain
        self.description = description
        self.author = author
        for key in kwargs:
            setattr(self, key, kwargs[key])
        
    def __str__(self):
        summary = [ f'website {self.name}\n' ]
        infos = vars(self).items()
        ordered_infos = sorted(infos)
        for attr, val in ordered_infos:
            if attr == 'name':
                continue
            summary.append(f'{attr}: {val}\n')
        return ''.join(summary)

class Prototype:

    def __init__(self):
        self.objects = dict()
    
    def register(self, identifier, obj):
        self.objects[identifier] = obj
    
    def unregister(self, identifier):
        del self.objects[identifier]

    def clone(self, identifier, **attrs):
        found = self.objects.get(identifier)
        if not found:
            raise ValueError(f'Incorrect Object Identifier! : {identifier}')
        obj = copy.deepcopy(found)
        for key in attrs:
            setattr(obj, key, attrs[key])
        return obj


def main():
    keywords = ('python', 'data', 'apis', 'automation')
    site1 = Website('Content-Gardening', domain="contentgardening.com", description='content channel', author='prince', category = 'foods', keywords = keywords)
    prototype = Prototype()
    identifier = 'ka-cg-1'
    prototype.register(identifier=identifier, obj= site1)
    site2 = prototype.clone(identifier=identifier, name = "ClonedContentGardener", domain = "play.garen.com", category = "Sports",creation_date = "2022-09-09")

    for site in (site1, site2):
        print(site)
    
    print(f" ID site1 : {id(site1)} != Id site2: {id(site2)}")


if __name__ == "__main__":
    main()