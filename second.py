# second page

import csv

class Restaurant:
    def __init__ (self, name, meal, locate, style):
        self.name = name
        self.meal = meal
        self.locate = locate
        self.style = style

        
    def check_meal(self):
        meallist = self.meal.split(', ')
        cnt = 0
        for meal in meallist:
            cnt += 1
            if meal in choose_meal:
                return True
                break

            if cnt == len(meallist):
                return False

    def check_locate(self):
        if self.locate in choose_locate:
            return True
        else:
            return False

    def check_style(self):
    	if self.style in choose_style:
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
    choose_style = input()

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
        style = row[3]
        res = Restaurant(name, meal, locate, style)
        # print(res.check_locate())
        # print(res.check_meal())
        print(res.check_style())
    f.close


