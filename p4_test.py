class PageFour(Frame):    
    
    def __init__(self, master):
        Frame.__init__(self, master)
        # 上一步按鍵
        self.back_btn = Button(self, text="回到上一頁", width=8, height=2, bg = "white",\
        command=lambda: master.switch_frame(PageThree)).grid(row = 6, column = 2)
        # 重來按鍵
        self.restart_btn = Button(text = "重來", bg = "white", width=8, height=2,\
        command=lambda: master.switch_frame(StartPage)).grid(row = 7, column = 2)
        #餐廳名稱
        self.res_name_label = Label(text= res.name + "的資訊", bg = "skyblue")
        self.res_name_label.config(height=3,font ="微軟正黑體 20")
        self.res_name_label.pack(side="top")
        # 餐廳地址
        self.res_address_label = Label(text="地址："+ name2address[res.name], bg = "skyblue")
        self.res_address_label.config(height=3,font ="微軟正黑體 20")
        self.res_address_label.pack(side="top")
        # 餐廳電話
        self.res_phone_label = Label(text= "電話："+name2phone[res.name], bg = "skyblue")
        self.res_phone_label.config(height=3, font ="微軟正黑體 20")
        self.res_phone_label.pack(side="top")
        # 餐廳營業時間
        self.res_time_label = Label(text="營業時間："+name2open[res.name], bg = "skyblue")
        self.res_time_label.config(height=3, font ="微軟正黑體 20")
        self.res_time_label.pack(side="top")
        # 餐廳星級
        self.res_star_label = Label(text="星級："+ name2stars[res.name], bg = "skyblue")
        self.res_star_label.config(height=3, font ="微軟正黑體 20")
        self.res_star_label.pack(side="top")
        # 時間提醒
        self.info_label = Label(text="", bg = "white", width=8, height=2)