
import toDoList

"""Runs the main program and interfaces with the ToDoList class"""
if __name__ == "__main__":

    checkList = toDoList.ToDoList()
    end = False
    print('* * * To Do List * * *')

    while not(end):

        n = input('\nEnter a command (Show, Add, Move, Complete) or End\n')

        if n == 'Show':
            listItems = checkList.showList()
            index = 1
            for listItem in listItems:
                print(str(index) + '.', listItem)
                index = index + 1

        elif 'Add' in n:
            inputList = n.split(' ', 1)
            item = inputList[1]
            checkList.addListItem(item)

        elif 'Complete' in n:
            inputList = n.split(' ', 1)
            item = int(inputList[1])
            if item > 0 and item <= len(checkList.showList()):
                checkList.completeListItem(item - 1)
            else:
                print('The list does not contain this entry')

        elif 'Move' in n:
            inputList = n.split()
            location = int(inputList[1]) - 1
            destination = int(inputList[2]) - 1
            checkList.moveListItem(location, destination)

        elif n == 'End':
            print(checkList.endList())
            end = True

        else:
            print(n, 'is an unrecognized command')
