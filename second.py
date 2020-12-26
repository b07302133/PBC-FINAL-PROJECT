# second page

import csv

class Restaurant:
    def __init__ (self, name, meal, locate, style, address, phone, star):
        self.name = name
        self.meal = meal
        self.locate = locate
        self.style = style
        self.address = address
        self.phone = phone
        self.star = star
       
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

    def check_style(self):  # choose_style should be a list
    	if self.style in choose_style:
    		return True
    	else:
    		return False

def choose_style_sorted(choose_style):  # 為了演算法而讓每個類型有個分數
    list_style = choose_style.split(',')
    list_sequence_point = []
    list_tmp = []
    count = 99
    for style in list_style:
        list_tmp = []
        list_tmp.append(style)
        list_tmp.append(count)
        count -= 1
        list_sequence_point.append(list_tmp)

    return list_sequence_point  # [[韓式, 99],[日式, 98],.....]

def recommendation(restaurant_dict):
    preference = input()  # 方案ㄧ排序還是方案二排序，這邊a是方案一（星數優先），b是方案二（類型優先）
    if preference == 'a':
        recommendation_list = sorted(restaurant_dict.items(), key = lambda x: (x[1][5], x[1][6]), reverse = True)
    else:
        recommendation_list = sorted(restaurant_dict.items(), key = lambda x: (x[1][6], x[1][5]), reverse = True)

    return recommendation_list


with open('canteen.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    name2locate = dict()
    name2meal = dict()
    name2style = dict()
    name2phone = dict()
    name2address = dict()
    name2star = dict()

    choose_locate = input()  # 第一頁的結果
    choose_meal = input()  # 第一頁的結果
    choose_style = input()  # 第二頁填完
    restaurant_dict = dict()

    for row in reader:
        row.pop(0)
        # print(row)
        name2locate[row[0]] = row[1]
        name2meal[row[0]] = row[2]
        name2style[row[0]] = row[3]
        name2phone[row[0]] = row[4]
        name2address[row[0]] = row[5]
        name2star[row[0]] = row[6]

        name = row[0]
        meal = row[2]
        locate = row[1]
        style = row[3]
        address = row[5]
        phone = row[4]
        star = row[6]
        res = Restaurant(name, meal, locate, style, address, phone, star)
        if res.check_locate() == True:
            if res.check_meal() == True:
                if res.check_style() == True:
                    for style in choose_style_sorted(choose_style):
                        if res.style in style:
                            restaurant_dict[res.name] = [res.locate, res.meal, res.style, res.address, res.phone, res.star, style[1]]  # 都是符合時間、地點、類型的餐廳、以及該類型的分數

for data in recommendation(restaurant_dict):
    print(data)

