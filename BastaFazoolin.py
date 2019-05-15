class Business:
    def __init__(self, name, franchises):
        pass

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
        
    def __repr__(self):
        return self.address

    def available_menus(self, time):
        menu_aval = []
        self.time = time
        if time >= 1100 and time <1600:
            menu_aval.append("Brunch")
        if time >= 1500 and time <1800:
            menu_aval.append("Early Bird")
        if time >= 1700 and time <2300:
            menu_aval.append("Dinner")
        if time >= 1100 and time <2100:
            menu_aval.append("Kids")
            
        return "Available menus: ", menu_aval

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
      return "{me} menu available from {st} to {et}".format(me=self.name, st=self.start_time, et=self.end_time)
  
  def calculate_bill(self, purchased_items):
      bill = 0
      for purchased_item in purchased_items:
          if purchased_item in self.items:
              bill += self.items[purchased_item]
      return bill

brunch_menu = {
    'pancakes': 7.50, 'waffles': 9.00, 
    'burger': 11.00, 'home fries': 4.50, 
    'coffee': 1.50, 'espresso': 3.00, 
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
    }
brunch = Menu("Brunch", brunch_menu, 1100, 1600)

early_bird_menu = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 
    'coffee': 1.50, 'espresso': 3.00
    }
early_bird = Menu("Early Bird", early_bird_menu, 1500, 1800)

dinner_menu = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 
    'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
    }
dinner = Menu("Dinner", dinner_menu, 1700, 2300)

kids_menu = {
    'chicken nuggets': 6.50, 
    'fusilli with wild mushrooms': 12.00, 
    'apple juice': 3.00
    }
kids = Menu("Kids", kids_menu, 1100, 2100)

arepas_menu = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 
    'guayanes arepa': 8.00, 'jamon arepa': 7.50
    }

flagship_store = Franchise('1232 West End Road', [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
new_installment = Franchise('12 East Mulberry Street', [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])

business = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])
business2 = Business('Take a\' Arepa', [arepas_place])