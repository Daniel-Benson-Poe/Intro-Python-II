import sys
from user import User
from department import Department
from products import Product

class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments

    def __str__(self):
        return f"Wecome to the Quarantine store! Have a nice shopping experience!"

    def print_departments(self):
        for id in self.departments:
            print(self.departments[id])
        print()

departments = {
    23: Department(23, "Groceries", [Product("Bananas", 0.60), Product("Avocados", 2), Product("Watermelons", 6)]), 
    9: Department(9, "Books", [Product("Game of Thrones", 10), Product("Fahrenheit 451", 15), Product("Working in Public", 25)]), 
    13: Department(13, "Electronics", [Product("Samsung 4K TV", 300), Product("iPhone SE", 400), Product("Pixel 4A", 100)]), 
    7: Department(7, "Clothes", [Product("Graphic T-shirts", 20), Product("Kanye Sweater", 700), Product("Sketchers", 25)]), 
    15: Department(15, "Toys", [Product("Lightsaber", 200), Product("Nerf Guns", 200), Product("Settlers of Catan",40), Product("Nintendo Lego Set", 400)])
}

store = Store("Quarantine Store", departments)

# user will pass in either 0 or 1 command-line arguments to the program
num_args = len(sys.argv)
# if they pass 0, will default their money to $100
if num_args == 1:
    user = User(100)
# if they pass 1 argument (a number), set their money to that amount
elif num_args == 2:
    user = User(int(sys.argv[1]))
else:
    print("Usage: store.py [money]")
    sys.exit(1)

# print store's welcom messge
print(store)

# print user's status
print(user, '\n')

    
while True:

    # print departments
    store.print_departments()

    selection = input("Which department would you like to visit? ")

    if selection == 'quit' or selection == 'q':
        break

    # expect user to type in a number that is read in as a string
    # parse it into an integer, then check if int is a valid 
    # department number.
    dep_num = int(selection)

    if dep_num not in departments:
        print("\nThat is not a valid department.\n")
        continue
    
    selected_dep = departments[dep_num]
    print(f"\nYou picked department number {dep_num}, the {selected_dep.name} department.\n")

    selected_dep.print_products()

    # we want user to be able to add products to their cart
    product_selection = int(input("What would you like to add to your cart? \n"))

    possible_products = selected_dep.products

    # index into the current department's list of products using the 'product_selection'
    selected_product = possible_products[product_selection]

    user.add_to_cart(selected_product)