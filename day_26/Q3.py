         
# Atm machine code
class Atm():
    def __init__(self):
        self.pin=''
        self.balence= 0
        self.menu()       
    def menu(self):
        user_input=input("""     
        how can i help you?
        press 1 = create pin
        presh 2 = change pin
        presh 3 = cheak your balence
        presh 4 = withdraw 
        presh 5 = any thing exist
        """)
        if user_input== '1':
            self.create_pin()
        elif user_input== '2':
            self.change_pin()
        elif user_input == '3':
            self.balnece()
        elif user_input == '4':
            self.withdraw()
        else:
            exit()
    def create_pin(self):
            user_pin = input("Enter your pin")
            self.pin = user_pin
            user_balence = input("Enter your balence")
            self.balence = user_balence
            
            print("pin created succesfully")
            self.menu()

    def change_pin(self):
            old_pin = input("Enter your old balnce")
            if old_pin == self.pin:
                new_pin = input("enter your new pin")
                self.pin = new_pin
                
                print("pin change succesfully")
                
                print("Data not found")
                self.menu()
    
    def balence(self):
            
            user_balence = input("Enter your pin")
            if user_balence == self.pin:
                
                print("balence of your account= " ,self.balence)
                self.menu()
            else:
                print("wrong input")
                self.menu()

    def withdraw(self):
            user_pin=input("enter the pin")
            if user_pin==self.pin:
                Ammount=int(input("enter your ammount"))
                if Ammount <= self.balence:
                    self.balnece = self.balence-Ammount
                    print("withdrawll succesfull",self.balence)
                else:
                    print("insuffient balence")
            else:
                print("wrong pin")
            self.menu()
                              
                              
obj = Atm()
obj.menu() 

            
            
        