class ToDoList:
    """Class that contains attributes of a to do list"""
    def __init__ (self):
        # Instance variables for ToDoList class
        self.toDoList = []  # Creates a new empty list for each new instance of ToDoList class

    """Returns the to do list"""
    def showList(self):
        return self.toDoList

    """Adds an item to the to do list"""
    def addListItem(self, item):
        self.toDoList.append(item)

    """Moves an item to a new location in the to do list"""
    def moveListItem(self, item, location):
        self.toDoList.insert(location, self.toDoList.pop(item))

    """Completes an item in the to do list and removes it"""
    def completeListItem(self, item):
        del self.toDoList[item]

    """Ends the to do list editing"""
    def endList(self):
        return "\n* * * To Do List Ended * * *"
