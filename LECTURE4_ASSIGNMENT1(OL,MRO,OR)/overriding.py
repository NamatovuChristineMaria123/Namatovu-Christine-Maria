class SmartAppliance:
    def performFunction(self):
        print("Appliance is running.")

class SmartFridge(SmartAppliance):
    def performFunction(self):
        print("Fridge is cooling items.")

class SmartOven(SmartAppliance):
    def performFunction(self):
        print("Oven is baking food.")


fridge = SmartFridge()
fridge.performFunction()  

oven = SmartOven()
oven.performFunction()  
