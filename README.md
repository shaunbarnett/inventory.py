# inventory.py
A Python program that will read from the text file inventory.txt and perform various tasks using OOP programming.

Inside the inventory.py file, I created a class named Shoes with the following attributes:

● country,
● code,
● product,
● cost, and
● quantity. 

Inside this class define the following methods:

▪ get_cost - Returns the cost of the shoes.
▪ get_quantity -Returns the quantity of the shoes.
▪ __str__ - This method returns a string representation of a class.

Outside this class  I created a variable with an empty list. This variable
will be used to store a list of shoes objects

Then I defined the following functions outside the class:

▪ read_shoes_data - This function will open the file
inventory.txt and read the data from this file, then create a
shoes object with this data and append this object into the
shoes list. One line in this file represents data to create one
object of shoes. I used the try-except in this function
for error handling. 

▪ capture_shoes - This function will allow a user to capture
data about a shoe and use this data to create a shoe object
and append this object inside the shoe list.

▪ view_all - This function will iterate over the shoes list and
print the details of the shoes returned from the __str__
function. 

▪ re_stock - This function will find the shoe object with the
lowest quantity, which is the shoes that need to be
re-stocked. The user is asked if they want to add this quantity of
shoes and then update it. This quantity will be updated
on the file for this shoe.

▪ seach_shoe - This function will search for a shoe from the list
using the shoe code and return this object so that it will be
printed.

▪ value_per_item - This function will calculate the total value
for each item and prints this information on the console
for all the shoes.

▪ highest_qty - Code to determine the product with the
highest quantity and print this shoe as being for sale.

In my main, I create a menu that executes each function
above. This menu is inside the while loop.

