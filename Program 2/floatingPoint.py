""" Floating Point Program to alter a list of floating point numbers """

if __name__ == "__main__":

    end = False
    floatingList = []

    print('* * * Floating-point program started * * *')

    while not (end):
        n = input('\nEnter a command: ')

        if 'Insert' in n:
            inputList = n.split(' ')
            command = inputList[0]
            number = float(inputList[1])

            index = 0
            floatingList.append(number)
            print('\nThe array currently contains: ')
            for values in floatingList:
                print('Values[' + str(index) + '] = ' + '%.5f' % values)
                index = index + 1

        elif 'Delete' in n:
            inputList = n.split(' ')
            command = inputList[0]
            number = float(inputList[1])

            index = 0
            if number in floatingList:
                floatingList.remove(number)
                print('\nThe array currently contains: ')
                for values in floatingList:
                    print('Values[' + str(index) + '] = ' + '%.5f' % values)
                    index = index + 1
            else:
                print('\nThat number was not in the list.')

        elif n == 'Sum':
            total = sum(floatingList)
            print('\nThe total is ' + str(total))

        elif n == 'End':
            end = True
            print('\n* * * Floating-point program ended * * *\n')

        else:
            print('\nInvalid option: please choose [Insert, Delete, Sum, End]')
