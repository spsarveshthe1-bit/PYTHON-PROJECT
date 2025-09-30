import random
class Dominos:
    menu={
        "veg":{"margerita":129,"cheese_and_corn":169,"peppi_paneer":260,
               "veg_loaded":210,"tomato_tangi":170},
        "non_veg":{"pepper_barbeque":199,"non_veg_loaded":169,
                "chicken_sausage":200},
        "snacks":{"garlic_bread":120,"zingy":59,
                  "chicken_cheese_balls":170},
        "desserts":{"choco_lava":100,"mousse cake":169},
        "drinks":{"coke":90,"pepsi":78,"sprite":50}
    }
    def __init__(self,name,email,phno):
        self.name=name
        self.email=email
        self.phno=phno
        self.login_status=True #to validate login state
        self.cart={}#to store orders
        #main program
        while True:
            if not self.login_status:
                print("------------WELCOME TO DOMINOS🍕APP--------------")
                print("Login")
                ch=input("Do you want to login?(y/n):").lower()
                if ch=="y":
                    self.login()
            if self.login_status==True:
                print("------------------------------------------------")
                print("User👤:",self.name)
                print("Enter 1: Order")
                print("Enter 2: Show cart")
                print("Enter 3: Logout")
                choice=int(input("Enter choice:"))
                if choice==1:
                    self.order()
                elif choice==2:
                    pass
                elif choice==3:
                    self.logout()
                else:
                    print("Invalid choice")
    @staticmethod
    def validate_otp(value):
        while True:
            print("-------------------------------------------------")
            og_otp=random.randint(1000,9999)
            print(f"An otp has been sent to (value)")
            print(f"Your dominos otp is:{og_otp}")
            otp=int(input("Enter otp:"))
            if otp==og_otp:
                print("Login successful✅")
                return True
            print("Incorrect otp enter correct otp....")

    def login(self):
        print("Enter 1: Login with phone")
        print("Enter 2: Login with Email")
        ch=int(input("Enter choice:"))
        if ch==1:
            #phone no validation
            print("Phone no validation")
            phno=int(input("Enter your phone number:"))
            if phno==self.phno:
                state=self.validate_otp(phno)#True
                self.login_status=state
            else:
                print("Incorrect phno")
        elif ch==2:
            #email validatiion
            email=input("Enter email:")
            if email==self.email:
                state=self.validate_otp(email)
                self.login_status=state
            else:
                print("Incorrect email")

        else:
            print("Invalid choice")

    def order(self):
        print("-------------Dominos Menu------------")
        for category in Dominos.menu:#display categories
            print(category)
        cat=input("Enter category:")
        if cat in Dominos.menu:
            d= Dominos.menu[cat]
            for item in d: #display items respective category 
                print(item,"           Rs.",d[item])
            item=input("Enter item: ")
            if item in d:
                q=int(input("Enter quantity:"))
                if item in self.cart:
                    self.cart[item]+=d[item]*q
                else:
                    self.cart[item]=d[item]*q#var[key]=new val
                print(f"{item} added to the cart🛒")
                print(self.cart)
            else:
                print(f"{item} is not available ❌")
        else:
            print(f"{cat} is not available ❌")
    def show_cart(self):
        pass
    def logout(self):
        ch=input("do you want to logout? (y/n):")
        if ch=='y':
            self.login_status=False
            print("Logged out ✅")

ob=Dominos("sarvesh","sarvesh💘💖beat@gmail.com",5843489458)