import os, time


def add():
    file = open("/home/holmes/Documents/medition", "a+")
    added = input("write what to add > ").capitalize()
    if added=='':
        print()
        print('nothing was added \n')
        time.sleep(1)
        os.system("clear")
    else:
        file.write(f"{added}\n")
        file.close()
        os.system("clear")
        print("ADDED")
        time.sleep(1)
        os.system("clear")


def view():
    file = open("/home/holmes/Documents/medition", "r")
    reading = file.read()
    print(reading)
    file.close()
    time.sleep(5)
    os.system("clear")


def adding_number():
    # read the file and numbered it.
    file = open("/home/holmes/Documents/medition", "r")
    reading = file.read()
    lines = reading.split("\n")
    numbering = []
    number = 1

    for i in lines:
        if i == "":  # to avoid adding number to the last empty item.
            continue
        numbered = str(number) + "." + i
        number += 1
        if (
            numbered[:1] == i[:1]
        ):  # if the first 2 characters are thesame dont overide it just return it.
            numbering.append(i)
        else:
            numbering.append(numbered)
    first = 0
    # override the file.
    for change in numbering:
        if first == 0:
            file = open("/home/holmes/Documents/medition", "w")
            first += 1
        # append change to the newly overrided file.
        file = open("/home/holmes/Documents/medition", "a+")
        file.write(f"{change}\n")
        file.close()


while True:
    green = "\33[32m"
    white = "\33[0m"
    print(f"{green}WHAT DO YOU WISH TO ADD {white}", end="\n\n")
    activity = input("(1)add\n(2)view\n(3)exit >> ")
    time.sleep(0.15)
    os.system("clear")

    if not activity in ["1", "2", "3"]:
        print("invalid option")
        print("try again")
        print()
        continue
    else:
        if activity == "1":
            add()

        elif activity == "2":
            adding_number()
            view()

        elif activity == "3":
            adding_number()
            print()
            print("bye bye".upper())
            break
