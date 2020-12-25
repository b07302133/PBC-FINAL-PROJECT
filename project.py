import csv

class Restaurant:
    def __init__ (self, name, meal, locate):
        self.name = name
        self.meal = meal
        self.locate = locate

        
    def called(self):
        meallist = self.meal.split(', ')
        for meal in meallist:
            if meal in choose_meal:
                return True
                break

    def check_locate(self):
        if self.locate in choose_locate:
            return True
        else:
            return False

    

with open('canteen.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    name2locate = dict()
    name2meal = dict()
    name2style = dict()
    name2phone = dict()
    name2address = dict()

    choose_locate = input()
    choose_meal = input()

    for row in reader:
        row.pop(0)
        # print(row)
        name2locate[row[0]] = row[1]
        name2meal[row[0]] = row[2]
        name2style[row[0]] = row[3]
        name2phone[row[0]] = row[4]
        name2address[row[0]] = row[5]

        name = row[0]
        meal = row[2]
        locate = row[1]
        res = Restaurant(name, meal, locate)
        print(res.check_locate())
    f.close