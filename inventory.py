# ========The beginning of the Shoe class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity): # class with 5 parameters
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

# this method gets the cost of each shoe

    def get_cost(self):
        return f"This shoe costs £{self.cost}"

# this method gets the quantity of each shoe

    def get_quantity(self):
        return f"The quantity for this shoe is {self.quantity}."

# this str method returns detail info of each shoe

    def __str__(self):
        return f'COUNTRY:   {self.country}\nCODE:      {self.code}\nPRODUCT:   {self.product}\nCOST:      {self.cost}\nQUANTITY:  {self.quantity}'


shoe_list = [] # shoe list to store the shoes

# this function reads the data from a text file and appends the contents to the shoe_list.

def read_shoes_data():
    try:
        with open("inventory.txt", "r") as read:
            file = read.readlines()[1:]
            for line in file:
                data = line.strip()
                data = data.split(",")
                shoe_list.append(data)
        print("\nData read from 'inventory.txt' and added to shoe_list ")
    except IOError:
        print("File not recognised, try again")
        menu()

# with this function you can add an entry in the shoe list

def capture_shoes():

    place = input("Please enter the country: ").capitalize()
    c = input("Please enter the code: ").upper()
    p = input("Please enter the product: ").capitalize()
    price = int(input("Please enter the cost: "))
    quant = int(input("Please enter the quantity: "))

    shoe_object = Shoe(place, c, p, price, quant)
    shoe_list.append(shoe_object)

# this function displays  detail info for each  shoe

def view_all():
    print("\n_______________[ SHOE LIST ]_________________")
    with open("inventory.txt", "r") as read:
        file = read.readlines()[1:]
        for line in file:
            data = line.strip().split(",")
            shoe_list.append(data)

            object = Shoe(data[0], data[1], data[2], data[3], data[4])
            print("_____________________________________________")
            print(object)

# this function is used to restock the shoe with the lowest quantity

def re_stock():
    with open("inventory.txt", "r") as read:
        file = read.readlines()[1:]
        for line in file:
            data = line.strip()
            data = data.split(",")
            shoe_list.append(data)

    print(shoe_list)

    smallest = 10
    lowest_quantity = []

    for shoe in shoe_list:
        if int(shoe[4]) < smallest:
            smallest = int(shoe[4])
            lowest_quantity = shoe

    print("This is the shoe with the lowest stock.")
    print("______________________________")
    print(f"COUNTRY: {lowest_quantity[0]}")
    print(f"CODE: {lowest_quantity[1]}")
    print(f"PRODUCT: {lowest_quantity[2]}")
    print(f"COST: {lowest_quantity[3]}")
    print(f"QUANTITY: {lowest_quantity[4]}")
    print("______________________________")
    choice = input("Would you like to restock? Y/N: ").upper()
    if choice == "Y":
        try:
            num = int(input("Please enter number: "))
            for shoe in shoe_list:
                if shoe == lowest_quantity:
                    shoe[4] = int(shoe[4])
                    shoe[4] += num
                    shoe[4] = str(shoe[4])
            with open("inventory.txt", "w") as write:
                for shoe in shoe_list:
                    shoe_string = ",".join(shoe)
                    write.write(shoe_string + "\n")

        except ValueError:
            print("\nincorrect input, try again")
            re_stock()

    elif choice == "N":
        menu()

    else:
        print("Incorrect input, try again")
        re_stock()

# you can search for any shoe using the code with this function

def search_shoe():
    pick = input("\nplease enter the code of the shoe that you would like to view: ").upper()
    with open("inventory.txt", "r") as get:
        file = get.readlines()[1:]
        for line in file:
            line = line.strip()
            line = line.split(",")
            if pick == line[1]:
                print(f"\n_______[ {line[1]}, {line[2]} ]________ ")
                print("______________________________")
                print(f"COUNTRY: {line[0]}")
                print(f"CODE: {line[1]}")
                print(f"PRODUCT: {line[2]}")
                print(f"COST: {line[3]}")
                print(f"QUANTITY: {line[4]}")
                print("______________________________")


# this function returns the total value of each shoe in stock


def value_per_item():
    print(f"________[ TOTAL INVENTORY PER SHOE ]________")

    with open("inventory.txt", "r") as get:
        file = get.readlines()[1:]
        for line in file:
            line = line.strip()
            line = line.split(",")
            total = int(line[3]) * int(line[4])

            print("______________________________")
            print(f"COUNTRY: {line[0]}")
            print(f"PRODUCT: {line[2]}")
            obj = Shoe(line[0], line[1], line[2], line[3], line[4])
            print(obj.get_quantity())
            print(obj.get_cost())
            print(f"Total price of inventory is {total}")
            print("______________________________")

# this function finds the shoe with the most stock then apply a discount

def highest_qty():
    most = 10

    with open("inventory.txt", "r") as get:
        file = get.readlines()[1:]
        for line in file:
            line = line.strip()
            line = line.split(",")
            shoe_list.append(line)

    for shoe in shoe_list:
        if int(shoe[4]) > most:
            most = int(shoe[4])
            s = shoe
            shoe[4] = int(shoe[4])
            sale = shoe[4] / 2

    print("______________________________")
    print(f"COUNTRY: {s[0]}")
    print(f"CODE: {s[1]}")
    print(f"PRODUCT: {s[2]}")
    print(f"COST: {s[3]} now cost {sale} ")
    print(f"QUANTITY: {s[4]}")
    print("______________________________")

# menu

def menu():

    while True:
        print("\n___________[ SELECTION ]____________")
        print("1 to read shoes data")
        print("2 to add shoes")
        print("3 to view all shoes")
        print("4 to re-stock ")
        print("5 to search shoe")
        print("6 for total inventory per shoe ")
        print("7 for sale shoe with highest quantity: ")
        user = input("8 to exit: ")

        if user == "1":
            read_shoes_data()
        elif user == "2":
            capture_shoes()
        elif user == "3":
            view_all()
        elif user == "4":
            re_stock()
        elif user == "5":
            search_shoe()
        elif user == "6":
            value_per_item()
        elif user == "7":
            highest_qty()
        elif user == "8":
            exit()
        else:
            print("Incorrect input, try again")
            menu()


menu()




