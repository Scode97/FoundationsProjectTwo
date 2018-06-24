# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.pop&shop.com"  # Give your site a name

def welcome():
    print("Welcome to %s \nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    
    for x in stores:
        print ("- %s" % x.name)

def get_store(store_name):
    
    for store in stores:
        if store.name.lower() == store_name.lower():
            return store
    return False
    

def pick_store():
  
    while True:
    #not store_found:
        print_stores()
        store_name = input("Pick a store by typing its name. Or type 'checkout' to pay your bills and say your goodbyes.\n")
        if store_name.lower() == "checkout":
            return "checkout"
        
        store = get_store(store_name)
        if store:
            break

        print ("No store with that name. Please try again.")

    #while True:
        #print_stores()
        #userinput = input("Pick a store by typing its name. Or type 'checkout' to pay your bills and say your goodbyes.\n")
        #if userinput.lower() == "checkout":
       
        #print ("The store you types does not exist. Try again Please.")
    return store

    

def pick_products(cart, picked_store):

    print("Add the products (from the above list) you want to your cart.\n Type 'back' to go back to the main menu where you can checkout.")
    user_input = " "

    while user_input.lower() != "back" and user_input.lower() != "checkout":
        user_input = input()
        for product in picked_store.products:
            not_found = True
            if user_input.lower() == product.name.lower():
                print ("This product is available. Choose another product:")
                cart.add_to_cart(product)
                not_found = False
                break

        if not_found and user_input != "back":
            print("NO MATCH")

    if user_input == "back":
        print ("\n Choose a different shop from the list below:")
    return user_input
    

def shop():

    cart = Cart()
    # your code goes here!
    user_input = ""
    while user_input.lower() != "checkout":
        user_input = ""
        picked_store = pick_store()
        if picked_store == "checkout":
            break
        
        picked_store.print_products()
        user_input = pick_products(cart, picked_store)

    cart.checkout()


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
