# page1 & a little page2
'''
博文要注意的地方：可以control F，打自己的名字來查
前端要注意的地方：可以control F，打「前端」來查
'''

import csv

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
    if preference == 'planA':
        recommendation_list = sorted(restaurant_dict.items(), key = lambda x: (x[1][3], x[1][4]), reverse = True)
    else:
        recommendation_list = sorted(restaurant_dict.items(), key = lambda x: (x[1][4], x[1][3]), reverse = True)

    return recommendation_list


class Restaurant:
    def __init__ (self, name, meal, locate, style, day, name2open, star):
        self.name = name  # 餐廳名稱
        self.meal = meal  # 早中晚宵
        self.locate = locate  # 地點
        self.style = style  # 風格(Ex.日式)
        # 博文：新加了兩個
        self.day = day  # 輸入之日期
        self.name2open = name2open  # 日期對應開放時間的dictionary
        self.star = star
    
    def put_name(self):  # call餐廳名稱
        return self.name

    def check_meal(self):  # 所選時段餐廳有沒有開的布林
        meallist = self.meal.split(', ')  # 預設為字串，前端用list設定選擇時段的話：可刪!!
        cnt = 0
        for meal in meallist:
            cnt += 1
            if meal in choose_meal:
                return True  # 選擇的任一時段餐廳有開的話即回傳True
                break
            if cnt == len(meallist):
                return False

    def check_locate(self):  # 選擇地點並讓其回傳布林
        if self.locate in choose_locate:
            return True
        else:
            return False
    
    def check_day(self):  # 回傳選擇的日期有沒有開的布林
        cnt = 0
        weeklist = ['MON','TUE','WED','THU','FRI','SAT','SUN']
        if self.name2open[self.name][weeklist.index(self.day)]== '':
            return False
        else:
            return True

    def check_style(self):  # 選擇風格並回傳布林
        if self.style in choose_style:
            return True
        else:
            return False

with open('canteen.csv', 'r', encoding='utf-8') as f:  # 讀csv檔
    # 製作各種字典（除星期），之後可能會用到
    reader = csv.reader(f)
    name2locate = dict()
    name2meal = dict()
    name2style = dict()
    name2phone = dict()
    name2address = dict()
    name2stars = dict()  # 博文注意，多加了：星星的字典 在這!!

    # 前端注意!!請將input改成你們botton函數回傳的值
    choose_locate = input()  # 目前應輸入string，要輸入list的話請回去把第16行刪掉
    choose_meal = input()
    choose_style = input()
    day = input() # 輸出的日期
    
    restaurant_dict = dict()  # 點好後輸出的清單在這!!（博文、前端）
    
    name2open = dict()  # 博文、振安：跑check_day的dictionary
    for row in reader:  # 跑csv檔的每一行
        row.pop(0)
        # print(row)
        name2locate[row[0]] = row[1]
        name2meal[row[0]] = row[2]
        name2style[row[0]] = row[3]
        name2phone[row[0]] = row[4]
        name2address[row[0]] = row[5]
        name2stars[row[0]] = row[6]
        name2open[row[0]] = [row[8],row[10],row[12],row[14],row[16],row[18],row[20]]  # 博文、振安：跑check_day的dictionary
        
        # 要class所需要的值
        name = row[0]
        locate = row[1]
        meal = row[2]
        style = row[3]
        star = row[6]
        res = Restaurant(name, meal, locate, style, day, name2open, star)  # 開始使用class Restaurant
        # print(res.check_locate())
        # print(res.check_meal())
        # print(res.check_style())
        # print(res.check_day())
        
        # 用布林篩選輸出的清單
        if res.check_locate() == True:
            if res.check_meal() == True:
                if res.check_day() == True:
                    if res.check_style() == True:
                        for style_ in choose_style_sorted(choose_style):
                            if res.style in style_:
                                restaurant_dict[res.name] = [res.locate, res.meal, res.style, res.star, style_[1]]                        

print(recommendation(restaurant_dict))

                        

