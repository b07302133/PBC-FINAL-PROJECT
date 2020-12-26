import tkinter as tk

# 將視窗作為一個物件
class window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.title('吃什麼？')
        self.geometry('800x600')  # 這裡的乘是小x

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()

# 開始頁面
# 將開始頁面作為一個物件，設立一個框架 frame
class StartPage(tk.Frame):    
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        # 顯示選擇早中晚宵夜的標籤框
        self.meal_selection_display = tk.Label(self, bg = 'white smoke', width = 30, height = 4, text='')
        self.meal_selection_display.grid(row = 0, column = 0)
        
        # 顯示選擇地點的標籤框
        self.location_selection_display = tk.Label(self, bg = 'white smoke', width = 30, height = 4, text='')
        self.location_selection_display.grid(row = 0, column = 2)
        
        # 顯示選擇星期幾的標籤框
        self.weekday_display = tk.Label(self, bg = 'white smoke', width = 30, height = 4, text='')
        self.weekday_display.grid(row = 0, column = 3)
        
        # testing 這邊頁面最下方，顯示輸出的視窗，只有在不跳轉頁面時才看得到
        self.meal_location_weekday_display = tk.Label(self, bg = 'white smoke', width = 30, height = 4, text='')
        self.meal_location_weekday_display.grid(row = 6, column = 0, columnspan = 6, sticky = 'e' + 'w')
        
        # 定義 all Checkbutton 也就是頁面上看到的送出鈕
        # 若不想要跳轉頁面，把'master.switch_frame(PageTwo)' 這邊拿掉即可
        acb = tk.Button(self, text = '送出', command = lambda:[self.all_check(), master.switch_frame(PageTwo)], height = 2)    
        acb.grid(row = 5, column = 0, columnspan = 6, sticky = 'e' + 'w')
        
        # 設置 all check button 中 meal_location_weekday_check_bool 的初始值
        self.meal_location_weekday_check_bool = False
        
        # 定義  meal 的 Checkbutton 選項
        # 設立  meal 的 Checkbutton 的變數
        # meal 的 Checkbutton 變數
        # mcb = meal check button
        self.mcbvar1 = tk.IntVar()
        self.mcbvar2 = tk.IntVar()
        self.mcbvar3 = tk.IntVar()
        self.mcbvar4 = tk.IntVar()
            
        # 定義 location 的 Checkbutton 選項並放置
        # 設立 location 的 Checkbutton 的變數
        # location 的 Checkbutton 變數
        # lcb = location check button
        self.lcbvar1 = tk.IntVar()
        self.lcbvar2 = tk.IntVar()
        self.lcbvar3 = tk.IntVar()
        self.lcbvar4 = tk.IntVar()
        
        # 設立 meal 的每一個按鈕
        # mcb = meal check button
        mcb1 = tk.Checkbutton(self, text='早餐',variable = self.mcbvar1, onvalue=1, 
                              offvalue=0, command = self.meal_selection, height = 2)    
        
        
        mcb2 = tk.Checkbutton(self, text='午餐',variable = self.mcbvar2, onvalue=1,
                              offvalue=0, command = self.meal_selection, height = 2)
        
        
        mcb3 = tk.Checkbutton(self, text='晚餐',variable = self.mcbvar3, onvalue=1, 
                              offvalue=0, command = self.meal_selection, height = 2)
        
        
        mcb4 = tk.Checkbutton(self, text='宵夜',variable = self.mcbvar4, onvalue=1,
                              offvalue=0, command = self.meal_selection, height = 2)
        
        # 放置 meal check button
        mcb1.grid(row = 1, column = 0, columnspan = 2, sticky = 'w')
        mcb2.grid(row = 2, column = 0, columnspan = 2, sticky = 'w')
        mcb3.grid(row = 3, column = 0, columnspan = 2, sticky = 'w')
        mcb4.grid(row = 4, column = 0, columnspan = 2, sticky = 'w')
        
        # 設立 location 的每一個按鈕
        #  lcb = location check button
        lcb1 = tk.Checkbutton(self, text = '公館地區',variable = self.lcbvar1, onvalue=1, 
                              offvalue=0, command = self.location_selection, height = 2)    
        
        
        lcb2 = tk.Checkbutton(self, text = '118巷',variable = self.lcbvar2, onvalue=1,
                              offvalue=0, command = self.location_selection, height = 2)
        
        
        lcb3 = tk.Checkbutton(self, text = '溫州街',variable = self.lcbvar3, onvalue=1, 
                              offvalue=0, command = self.location_selection, height = 2)
        
        
        lcb4 = tk.Checkbutton(self, text = '偏鄉',variable = self.lcbvar4, onvalue=1,
                              offvalue=0, command = self.location_selection, height = 2)
        
        # 放置 location check button
        lcb1.grid(row = 1, column = 2, columnspan = 2, sticky = 'w')
        lcb2.grid(row = 2, column = 2, columnspan = 2, sticky = 'w')
        lcb3.grid(row = 3, column = 2, columnspan = 2, sticky = 'w')
        lcb4.grid(row = 4, column = 2, columnspan = 2, sticky = 'w')


        # 定義星期幾的下拉清單
        OptionList1 = ["MON", "TUE", "WED", "THU", 'FRI', 'SAT', 'SUN'] 
        self.weekday_variable = tk.StringVar()
        self.weekday_variable.set(OptionList1[0])
        
        weekday_pull = tk.OptionMenu(self, self.weekday_variable, *OptionList1)
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
    
# 第二頁
class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        # tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).grid()
        tk.Button(self, text="回到上一頁",
                  command=lambda: master.switch_frame(StartPage)).grid(
                      row = 5, column = 0, columnspan = 6, sticky = 'e' + 'w')


if __name__ == "__main__":
    app = window()
    app.mainloop()