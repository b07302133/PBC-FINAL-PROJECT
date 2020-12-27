name2stars = {"上海小館":4.6,}
name2address = {"上海小館":"新北市永和區"}
name2phone = {"上海小館":"02-2345-6789"}
name2open = {"上海小館":"11:30~17:00"}


class PageThree(Frame):    
    def __init__(self, master):
        Frame.__init__(self, master)
        res_name = ""
        self.res_var = StringVar()
        def get_res():
            res_name = var.get()
            
        self.no1_option = Radiobutton(self, width = 20, height = 4, text="第一推薦："+ \
                          res_sort_list[0][0], variable = res_var, value = res_sort_list[0][0], command=lambda:[get_res(),master.switch_frame(PageFour)])
        self.no2_option = Radiobutton(self, width = 20, height = 4, text="第二推薦："+ \
                          res_sort_list[1][0], variable = res_var, value = res_sort_list[1][0], command=lambda:[get_res(),master.switch_frame(PageFour)])
        self.no3_option = Radiobutton(self, width = 20, height = 4, text="第三推薦："+ \
                          res_sort_list[2][0], variable = res_var, value = res_sort_list[2][0], command=lambda:[get_res(),master.switch_frame(PageFour)])
        self.no4_option = Radiobutton(self, width = 20, height = 4, text="第四推薦："+ \
                          res_sort_list[3][0], variable = res_var, value = res_sort_list[3][0], command=lambda:[get_res(),master.switch_frame(PageFour)])
        self.no5_option = Radiobutton(self, width = 20, height = 4, text="第五推薦："+ \
                          res_sort_list[4][0], variable = res_var, value = res_sort_list[4][0], command=lambda:[get_res(),master.switch_frame(PageFour)])

        self.no1_option.pack(side="top")
        self.no2_option.pack(side="top")
        self.no3_option.pack(side="top")
        self.no4_option.pack(side="top")
        self.no5_option.pack(side="top")

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
        self.res_name_label = Label(text= res_name + "的資訊", bg = "skyblue")
        self.res_name_label.config(height=3,font ="微軟正黑體 20")
        self.res_name_label.pack(side="top")
        # 餐廳地址
        self.res_address_label = Label(text="地址："+ name2address[res_name], bg = "skyblue")
        self.res_address_label.config(height=3,font ="微軟正黑體 20")
        self.res_address_label.pack(side="top")
        # 餐廳電話
        self.res_phone_label = Label(text= "電話："+name2phone[res_name], bg = "skyblue")
        self.res_phone_label.config(height=3, font ="微軟正黑體 20")
        self.res_phone_label.pack(side="top")
        # 餐廳營業時間
        self.res_time_label = Label(text="營業時間："+name2open[res_name], bg = "skyblue")
        self.res_time_label.config(height=3, font ="微軟正黑體 20")
        self.res_time_label.pack(side="top")
        # 餐廳星級
        self.res_star_label = Label(text="星級："+ name2stars[res_name], bg = "skyblue")
        self.res_star_label.config(height=3, font ="微軟正黑體 20")
        self.res_star_label.pack(side="top")
        # 時間提醒
        #self.info_label = Label(text="", bg = "white", width=8, height=2)
        
