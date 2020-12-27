# combine1-2
from tkinter import*
import csv
"""
前端的部分由此開始
"""
all_condition_list = []

# 將視窗作為一個物件
class window(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.title('吃什麼？')
        self.geometry('800x600')  # 這裡的乘是小x

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  # 關閉視窗
        self._frame = new_frame
        self._frame.grid()


# 將開始頁面作為一個物件，設立一個框架 frame
# 第一頁（開始頁面）
class StartPage(Frame):    
    
    def __init__(self, master):
        Frame.__init__(self, master)
        global all_condition_list
        
        # 顯示選擇早中晚宵夜的標籤框
        self.meal_selection_display = Label(self, bg = 'white smoke', width = 30, height = 4, text='')
        self.meal_selection_display.grid(row = 0, column = 0)
        
        # 顯示選擇地點的標籤框
        self.location_selection_display = Label(self, bg = 'white smoke', width = 30, height = 4, text='')
        self.location_selection_display.grid(row = 0, column = 2)
        
        # 顯示選擇星期幾的標籤框
        self.weekday_display = Label(self, bg = 'white smoke', width = 30, height = 4, text='')
        self.weekday_display.grid(row = 0, column = 3)
        
        # testing 這邊頁面最下方，顯示輸出的視窗，只有在不跳轉頁面時才看得到
        self.meal_location_weekday_display = Label(self, width = 30, height = 4, text='')
        self.meal_location_weekday_display.grid(row = 6, column = 0, columnspan = 6, sticky = 'e' + 'w')
        
        # 定義 all Checkbutton 也就是頁面上看到的送出鈕
        # 若不想要跳轉頁面，把'master.switch_frame(PageTwo)' 這邊拿掉即可
        acb = Button(self, text = '送出', command = lambda:[self.all_check(), master.switch_frame(PageTwo)], height = 2)    
        acb.grid(row = 5, column = 0, columnspan = 6, sticky = 'e' + 'w')
        
        # 設置 all check button 中 meal_location_weekday_check_bool 的初始值
        self.meal_location_weekday_check_bool = False
        
        # 定義  meal 的 Checkbutton 選項
        # 設立  meal 的 Checkbutton 的變數
        # meal 的 Checkbutton 變數
        # mcb = meal check button
        self.mcbvar1 = IntVar()
        self.mcbvar2 = IntVar()
        self.mcbvar3 = IntVar()
        self.mcbvar4 = IntVar()
            
        # 定義 location 的 Checkbutton 選項並放置
        # 設立 location 的 Checkbutton 的變數
        # location 的 Checkbutton 變數
        # lcb = location check button
        self.lcbvar1 = IntVar()
        self.lcbvar2 = IntVar()
        self.lcbvar3 = IntVar()
        self.lcbvar4 = IntVar()
        
        # 設立 meal 的每一個按鈕
        # mcb = meal check button
        mcb1 = Checkbutton(self, text='早餐',variable = self.mcbvar1, onvalue=1, 
                              offvalue=0, command = self.meal_selection, height = 2)    
        
        
        mcb2 = Checkbutton(self, text='午餐',variable = self.mcbvar2, onvalue=1,
                              offvalue=0, command = self.meal_selection, height = 2)
        
        
        mcb3 = Checkbutton(self, text='晚餐',variable = self.mcbvar3, onvalue=1, 
                              offvalue=0, command = self.meal_selection, height = 2)
        
        
        mcb4 = Checkbutton(self, text='宵夜',variable = self.mcbvar4, onvalue=1,
                              offvalue=0, command = self.meal_selection, height = 2)
        
        # 放置 meal check button
        mcb1.grid(row = 1, column = 0, columnspan = 2, sticky = 'w')
        mcb2.grid(row = 2, column = 0, columnspan = 2, sticky = 'w')
        mcb3.grid(row = 3, column = 0, columnspan = 2, sticky = 'w')
        mcb4.grid(row = 4, column = 0, columnspan = 2, sticky = 'w')
        
        # 設立 location 的每一個按鈕
        #  lcb = location check button
        lcb1 = Checkbutton(self, text = '公館地區',variable = self.lcbvar1, onvalue=1, 
                              offvalue=0, command = self.location_selection, height = 2)    
        
        
        lcb2 = Checkbutton(self, text = '118巷',variable = self.lcbvar2, onvalue=1,
                              offvalue=0, command = self.location_selection, height = 2)
        
        
        lcb3 = Checkbutton(self, text = '溫州街',variable = self.lcbvar3, onvalue=1, 
                              offvalue=0, command = self.location_selection, height = 2)
        
        
        lcb4 = Checkbutton(self, text = '偏鄉',variable = self.lcbvar4, onvalue=1,
                              offvalue=0, command = self.location_selection, height = 2)
        
        # 放置 location check button
        lcb1.grid(row = 1, column = 2, columnspan = 2, sticky = 'w')
        lcb2.grid(row = 2, column = 2, columnspan = 2, sticky = 'w')
        lcb3.grid(row = 3, column = 2, columnspan = 2, sticky = 'w')
        lcb4.grid(row = 4, column = 2, columnspan = 2, sticky = 'w')


        # 定義星期幾的下拉清單
        OptionList1 = ["MON", "TUE", "WED", "THU", 'FRI', 'SAT', 'SUN'] 
        self.weekday_variable = StringVar()
        self.weekday_variable.set('請選擇星期幾')
        
        weekday_pull = OptionMenu(self, self.weekday_variable, *OptionList1)
        weekday_pull.config(width=18, height = 2)
        weekday_pull.grid(row = 1, rowspan = 2, column = 3, sticky = 'n'+'w')
        
        # 當星期幾的下拉列表被點選，就會呼叫 weekday_selection 這個 method
        self.weekday_variable.trace("w", self.weekday_selection)
        
    
    # 定義按下「送出」按鈕的 method
    def all_check(self):
        global all_condition_list
        
        if self.meal_location_weekday_check_bool == False:
            self.meal_location_weekday_check_bool = True
            list_input = self.meal_selection()
            all_condition_list.append(list_input)
            
            list_input = self.location_selection()
            all_condition_list.append(list_input)
            
            list_input = self.weekday_selection()
            all_condition_list.append(list_input)
            self.meal_location_weekday_display.config(text = all_condition_list)
            
        else:
            self.meal_location_weekday_check_bool = False


    # 定義按下「早餐」「午餐」「晚餐」等按鈕的 method
    def meal_selection(self):
        meal_list = []
        
        # mcb = meal check button
        # mcbvar 為 Checkbutton 的變數 1 為選取，0為未選取
        if (self.mcbvar1.get() == 1):
            meal_list.append('早餐')
            
        if (self.mcbvar2.get() == 1):     
            meal_list.append('午餐')
            
        if (self.mcbvar3.get() == 1):    
            meal_list.append('晚餐')
    
        if (self.mcbvar4.get() == 1):     
            meal_list.append('宵夜')
        
        # 刷新欲吃餐點顯示
        self.meal_selection_display.config(text = (meal_list))
        return meal_list
    
    # 定義按下「公館地區」「118巷」等按鈕的 method
    def location_selection(self):
        location_list = []
        
        if (self.lcbvar1.get() == 1):
            location_list.append('公館地區')
            
        if (self.lcbvar2.get() == 1):     
            location_list.append('118巷')
            
        if (self.lcbvar3.get() == 1):    
            location_list.append('溫州街')
    
        if (self.lcbvar4.get() == 1):     
            location_list.append('偏鄉')
            
        # 刷新偏好地點顯示
        self.location_selection_display.config(text = (location_list))
        return location_list
    
    # 定義星期幾下拉清單的 method
    def weekday_selection(self, *args):
        # 刷新偏好星期幾顯示
        self.weekday_display.config(text = self.weekday_variable.get())
        return [str(self.weekday_variable.get())]
    
# 第二頁
class PageTwo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        
        # 設置 all check button 中 style_plan_check_bool 的初始值
        self.style_plan_check_bool = False
        
        
        self.back_btn = Button(
            self, text="回到上一頁", width=20, height=2, 
            bg = "white", command=lambda: master.switch_frame(StartPage)).grid(
                row = 1, column = 4, sticky = 'w'+'e')
        
        # self.style_label = Label(text="風格", height = 2,
        #                          width = 10, font ="微軟正黑體 14")
        # self.style_label.grid(row = 0, column = 0, columnspan = 2)

        # self.order_label = Label(text="排序方法",  height = 2, 
        #                          width = 10, font ="微軟正黑體 14")
        # self.order_label.grid(row = 0, column = 3, columnspan = 2)
        
        self.back_btn = Button(
            self, text="送出", width=20, height=2, 
            bg = "white", command = lambda:[self.all_check() ,master.switch_frame(StartPage)]).grid(
            row = 2, column = 4, sticky = 'w'+'e')

        self.white_block1= Label(self, width = 15, height = 4, 
                                             text="")
        self.white_block1.grid(row = 1, column = 2, sticky = 'w')
                
        # 第一偏好顯示
        self.style_variable1_display = Label(self, width = 20, height = 4, 
                                             text="第一想吃")
        self.style_variable1_display.grid(row = 1, column = 0, sticky = 'w')
        
        # 第二偏好顯示
        self.style_variable2_display = Label(self, width = 20, height = 4, 
                                             text="第二想吃")
        self.style_variable2_display.grid(row = 2, column = 0, sticky = 'w')
        
        # 第三偏好顯示
        self.style_variable3_display = Label(self, width = 20, height = 4, 
                                             text="第三想吃")
        self.style_variable3_display.grid(row = 3, column = 0, sticky = 'w')
        
        # 第四偏好顯示
        self.style_variable4_display = Label(self, width = 20, height = 4, 
                                             text="第四想吃")
        self.style_variable4_display.grid(row = 4, column = 0, sticky = 'w')
        
        # 第五偏好顯示
        self.style_variable5_display = Label(self, width = 20, height = 4, 
                                     text="第五想吃")
        self.style_variable5_display.grid(row = 5, column = 0, sticky = 'w')
        
        # 排序偏好顯示
        self.order_variable_display = Label(self, width = 20, height = 4, 
                                     text="排序方式")
        
        self.order_variable_display.grid(row = 6, column = 0, sticky = 'w')
        
        
        style_List = ["日式","美式","義式","法式","韓式","中式",
        "小吃","咖啡廳","手搖杯","東南亞料理","速食","素食","酒吧","健康餐","火鍋",
        "西式","燒烤/鐵板燒/牛排館","肥宅/魯蛇吃宵","咖哩","水餃",] 

        # 第一偏好下拉清單設置
        self.style_variable1 = StringVar()
        self.style_variable1.set(["請選擇風格"])
        style_pull1 = OptionMenu(self, self.style_variable1, *style_List)
        style_pull1.config(width = 20, height = 2, font=('Helvetica', 12))
        style_pull1.grid(row = 1, column = 1, sticky = 'n'+'s')
        
        self.style_variable1.trace("w", self.style_variable1_selection)
            
        # # 第二偏好下拉清單設置
        self.style_variable2 = StringVar()
        self.style_variable2.set(["請選擇風格"])
        style_pull2 = OptionMenu(self, self.style_variable2, *style_List)
        style_pull2.config(width = 20, height = 2, font=('Helvetica', 12))
        style_pull2.grid(row = 2, column = 1, sticky = 'n'+'s')
        
        self.style_variable2.trace("w", self.style_variable2_selection)
        
        # 第三偏好下拉清單設置
        self.style_variable3 = StringVar()
        self.style_variable3.set(["請選擇風格"])
        style_pull3 = OptionMenu(self, self.style_variable3, *style_List)
        style_pull3.config(width = 20, height = 2, font=('Helvetica', 12))
        style_pull3.grid(row = 3, column = 1, sticky = 'n'+'s')
        
        self.style_variable3.trace("w", self.style_variable3_selection)
        
        # 第四偏好下拉清單設置
        self.style_variable4 = StringVar()
        self.style_variable4.set(["請選擇風格"])
        style_pull4 = OptionMenu(self, self.style_variable4, *style_List)
        style_pull4.config(width = 20, height = 2, font=('Helvetica', 12))
        style_pull4.grid(row = 4, column = 1, sticky = 'n'+'s')
        
        self.style_variable4.trace("w", self.style_variable4_selection)
        
        # 第五偏好下拉清單設置
        self.style_variable5 = StringVar()
        self.style_variable5.set(["請選擇風格"])
        style_pull5 = OptionMenu(self, self.style_variable5, *style_List)
        style_pull5.config(width = 20, height = 2, font=('Helvetica', 12))
        style_pull5.grid(row = 5, column = 1, sticky = 'n'+'s')
        
        self.style_variable5.trace("w", self.style_variable5_selection)
        

        # 排序下拉式選單
        order_List = ["planA", "planB"]
        self.order_variable = StringVar(self)
        self.order_variable.set(["請選擇排序方式"])
        order_pull = OptionMenu(self, self.order_variable, *order_List)
        order_pull.config(width = 20, height = 2, font=('Helvetica', 12))
        order_pull.grid(row = 6, column = 1)
        
        self.order_variable.trace("w", self.order_selection)

    def style_variable1_selection(self, *args):
        self.style_variable1_display.config(text = self.style_variable1.get())
        return str(self.style_variable1.get())

    def style_variable2_selection(self, *args):
        self.style_variable2_display.config(text = self.style_variable2.get())
        return str(self.style_variable2.get())

    def style_variable3_selection(self, *args):
        self.style_variable3_display.config(text = self.style_variable3.get())
        return str(self.style_variable3.get())
        
    def style_variable4_selection(self, *args):
        self.style_variable4_display.config(text = self.style_variable4.get())
        return str(self.style_variable4.get())
        
    def style_variable5_selection(self, *args):
        self.style_variable5_display.config(text = self.style_variable5.get())
        return str(self.style_variable5.get())

    def order_selection(self, *args):
        if str(self.order_variable.get()) == 'planA':
            self.order_variable_display.config(text = '星數優先')
            
        elif str(self.order_variable.get()) == 'planB':
            self.order_variable_display.config(text = '類型優先')
            
        return str(self.order_variable.get())
    
    def all_check(self):
        global all_condition_list
            
        list_input = [self.style_variable1_selection(),
                      self.style_variable2_selection(),
                      self.style_variable3_selection(),
                      self.style_variable4_selection(),
                      self.style_variable5_selection()]
        
        all_condition_list.append(list_input)
        
        list_input = self.order_selection()
        all_condition_list.append([list_input])
            
        
        # 檢查用
        # print(all_condition_list)         # 印出整個 list
        # print(all_condition_list[0])      # 印出 meal list
        # print(all_condition_list[1])      # 印出 location list
        # print(all_condition_list[2][0])   # 印出 day
        # print(all_condition_list[3])      # 印出 style list
        # print(all_condition_list[4][0])   # 印出 plan
        
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
            global choose_meal, choose_locate, day, choose_style
            choose_meal = all_condition_list[0]
            choose_locate = all_condition_list[1]  # 目前應輸入string，要輸入list的話請回去把第16行刪掉
            day = all_condition_list[2][0] # 輸出的日期
            choose_style = all_condition_list[3]
            
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
        
        print(all_condition_list)
        print(recommendation(restaurant_dict))
        
        # 重置、淨空 all_condition_list，否則重新搜尋時會和舊有的 list 衝突
        all_condition_list = [] 
        

def choose_style_sorted(choose_style):  # 為了演算法而讓每個類型有個分數
    list_style = choose_style
    # .split(',')
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
    
    preference = all_condition_list[4][0] # 方案ㄧ排序還是方案二排序，這邊a是方案一（星數優先），b是方案二（類型優先）
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

if __name__ == "__main__":
    app = window()
    app.mainloop()



