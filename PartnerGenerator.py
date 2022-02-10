# This is a sample Python script.
import random
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Person:
    name = ""
    family = ""
    HasPartner = 0

    def __init__(self,name,family):
        self.name = name
        self.family = family

def GetPartners(People,Partners):
    # for i in List:
    #     print(f"{i.name} is in family {i.family}")
    # for i in Partner:
    #     print(f"{i.name} is in family {i.family}")
    pass



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numberOfPeople = input("Enter the number of people: ")
    while(numberOfPeople.isdigit() == False):
        numberOfPeople = input("Enter the number of people: ")
    ListofNames = []
    ListofNames2 = []
    size = int(numberOfPeople)

    for i in range(0,size):
        name = input("Enter a name: ")
        last = input("Enter a family name/key: ")
        person = Person(name,last)
        ListofNames.append(person)
    ListofNames2 = ListofNames.copy()
    print()

    flag = 1
    while flag != 0:
        flag = 0
        for i in range(0, size):
            if ListofNames2[i].name == ListofNames[i].name or ListofNames2[i].family == ListofNames[i].family:
                random.shuffle(ListofNames2)
                flag = 1
    print("With Keys:")
    for i in range(0, size):
        print(f"Number: {i} \033[1m{ListofNames[i].name} {ListofNames[i].family}\033[0m has \033[1m{ListofNames2[i].name} {ListofNames2[i].family}\033[0m for christmas")

    print()
    print()
    print("Without Keys:")
    for i in range(0, size):
        print(f"Number: {i} \033[1m{ListofNames[i].name}\033[0m has \033[1m{ListofNames2[i].name}\033[0m for christmas")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
