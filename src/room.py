# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[], n_to=None, e_to=None, w_to=None, s_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.w_to = w_to
        self.s_to = s_to
        self.e_to = e_to
        self.items = items

    def printItems(self):
        items=[]
        for i in self.items:
            items.append(i.name)
            print (f' {i.name}')
        return items
    def removeItems(self, name):
        for i in self.items:
            if i.name == name:
                self.items.remove(i)
        return self.items

    def __str__(self):
        return f'{self.name}\n{self.description}\n{self.items}'
