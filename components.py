# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        self.name= name
        self.products=[]

    def add_product(self, product):
        self.products.append(product)

    def print_products(self):
        print ("-----------------------------\n %s- " % self.name)
        
        for product in self.products:
            print (product, "")


class Product():
    def __init__(self, name, description, price):
        self.name= name
        self.description= description
        self.price= price      

    def __str__(self):
        return "- Product Name: %s \n- Description of Product: %s \n- Price of Product: %s KD \n" % (self.name,self.description,self.price)

class Cart():
    def __init__(self):
        self.products=[]   

    def add_to_cart(self, product):
        self.products.append(product)
        
    def get_total_price(self):
        p= 0
        for product in self.products:
            p += product.price

        return p
        
    def print_receipt(self):
        print ("Receipt- ")
    
        for product in self.products:
            print (product)

        print ("The total price is: %s KD" % self.get_total_price())

    def checkout(self):
        #print the receipt
        print("------------------------------------------------------------------------")
        self.print_receipt()
        #ask user to confirm
        confirm= input("Do you want to confirm your order? (yes or no)\n")
        if confirm.lower() == "yes":
            print ("Your order has been confirmed.")
        elif confirm.lower() == "no":
            print ("Your order has been cancelled.")
        else:
            print ("Please ONLY type 'yes' to confirm and 'no' to cancel")
            
