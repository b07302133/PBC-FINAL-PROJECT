# combine1-2
from tkinter import*

# 將視窗作為一個物件
class window(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.title('吃什麼？')
        self.geometry('600x500')  # 這裡的乘是小x

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()  # 關閉視窗
        self._frame = new_frame
        self._frame.grid()

# 開始頁面
# 將開始頁面作為一個物件，設立一個框架 frame
class StartPage(Frame):    
    
    def __init__(self, master):
        Frame.__init__(self, master)
        
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
        self.meal_location_weekday_display = Label(self, bg = 'white smoke', width = 30, height = 4, text='')
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
        self.weekday_variable.set(OptionList1[0])
        
        weekday_pull = OptionMenu(self, self.weekday_variable, *OptionList1)
        weekday_pull.config(width=18, height = 2)
        weekday_pull.grid(row = 1, rowspan = 2, column = 3, sticky = 'n'+'w')
        
        # 當星期幾的下拉列表被點選，就會呼叫 weekday_selection 這個 method
        self.weekday_variable.trace("w", self.weekday_selection)
        
    
    # 定義按下「送出」按鈕的 method
    def all_check(self):
        self.meal_location_weekday = [[], [], []]
        global meal_location_weekday_check_bool
        if self.meal_location_weekday_check_bool == False:
            meal_location_weekday_check_bool = True
            list_input, list_type = self.meal_selection()
            self.meal_location_weekday[list_type].append(list_input)
            
            list_input, list_type = self.location_selection()
            self.meal_location_weekday[list_type].append(list_input)
            
            list_input, list_type = self.weekday_selection()
            self.meal_location_weekday[2].append(list_input)
            self.meal_location_weekday_display.config(text = self.meal_location_weekday)
            
        else:
            meal_location_weekday_check_bool = False
        
        return self.meal_location_weekday

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
        return meal_list, 0
    
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
        return location_list, 1
    
    # 定義星期幾下拉清單的 method
    def weekday_selection(self, *args):
        # 刷新偏好星期幾顯示
        self.weekday_display.config(text = self.weekday_variable.get())
        return str(self.weekday_variable.get()), 2
    
# 第二頁(bug)
class PageTwo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.back_btn = Button(self, text="回到上一頁", width=8, height=2, bg = "white",\
        command=lambda: master.switch_frame(StartPage)).grid(row = 6, column = 2)
        
        self.next_btn = Button(text = "下一步", bg = "white", width=8, height=2)
        self.next_btn.grid(row = 7, column = 2)
        
        self.style_label = Label(text="風格")
        self.style_label.config(width=13, height=3, font ="微軟正黑體 20")
        self.style_label.grid(row = 0, column = 1, sticky = 'w')

        self.order_label = Label(text="排序方法")
        self.order_label.config(width=13, height=3, font ="微軟正黑體 20")
        self.order_label.grid(row = 0, column = 2)

        self.label_1 = Label(text="1. ")
        self.label_1.config(width=3, height=1, font ="微軟正黑體 12")
        self.label_1.grid(row = 1, column = 0, sticky = 'w')

        self.label_2 = Label(text="2. ")
        self.label_2.config(width=3, height=1, font ="微軟正黑體 12")
        self.label_2.grid(row = 2, column = 0, sticky = 'w')

        self.label_3 = Label(text="3. ")
        self.label_3.config(width=3, height=1, font ="微軟正黑體 12")
        self.label_3.grid(row = 3, column = 0, sticky = 'w')

        self.label_4 = Label(text="4. ")
        self.label_4.config(width=3, height=1, font ="微軟正黑體 12")
        self.label_4.grid(row = 4, column = 0, sticky = 'w')

        self.label_5 = Label(text="5. ")
        self.label_5.config(width=3, height=1, font ="微軟正黑體 12")
        self.label_5.grid(row = 5, column = 0, sticky = 'w')
        
        style_List = [
        "日式","美式","義式",
        "法式","韓式","中式",
        "小吃","咖啡廳","手搖杯",
        "東南亞料理","速食","素食",
        "酒吧","健康餐","火鍋",
        "西式","燒烤/鐵板燒/牛排館",
        "肥宅/魯蛇吃宵","咖哩","水餃",
        ] 
        self.style_variable1 = StringVar(self)
        self.style_variable1.set(["請選擇風格"])
        style_opt1 = OptionMenu(self, self.style_variable1, *style_List)
        style_opt1.config(width=20, font=('Helvetica', 12))
        style_opt1.grid(row = 1, column = 1, sticky = 'w')

        self.style_variable2 = StringVar(self)
        self.style_variable2.set(["請選擇風格"])
        style_opt2 = OptionMenu(self, self.style_variable2, *style_List)
        style_opt2.config(width=20, font=('Helvetica', 12))
        style_opt2.grid(row = 2, column = 1, sticky = 'w')

        self.style_variable3 = StringVar(self)
        self.style_variable3.set(["請選擇風格"])
        style_opt3 = OptionMenu(self, self.style_variable3, *style_List)
        style_opt3.config(width=20, font=('Helvetica', 12))
        style_opt3.grid(row = 3, column = 1, sticky = 'w')

        self.style_variable4 = StringVar(self)
        self.style_variable4.set(["請選擇風格"])
        style_opt4 = OptionMenu(self, self.style_variable4, *style_List)
        style_opt4.config(width=20, font=('Helvetica', 12))
        style_opt4.grid(row = 4, column = 1, sticky = 'w')

        self.style_variable5 = StringVar(self)
        self.style_variable5.set(["請選擇風格"])
        style_opt5 = OptionMenu(self, self.style_variable5, *style_List)
        style_opt5.config(width=20, font=('Helvetica', 12))
        style_opt5.grid(row = 5, column = 1, sticky = 'w')

        # 排序下拉式選單
        order_List = ["planA", "planB"]
        self.order_variable = StringVar(self)
        self.order_variable.set(["請選擇排序方式"])
        order_opt = OptionMenu(self, self.order_variable, *order_List)
        order_opt.config(width=20, font=('Helvetica', 12))
        order_opt.grid(row = 1, column = 2, sticky = 'e')


if __name__ == "__main__":
    app = window()
    app.mainloop()
