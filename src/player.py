# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__ (self , name , current_room,inventory=[] ):
        self.name=name
        self.current_room=current_room
        self.inventory = inventory
    def addItem(self, value):
        self.inventory.append(value)
        Item(value.name , value.description).on_take()


    def __str__ (self):
        return f'{self.name} ,{self.current_room}, {self.inventory}'

    