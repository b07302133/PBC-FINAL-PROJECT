class PageThree(Frame):    
    
    def __init__(self, master):
        Frame.__init__(self, master)
        self.no1_label = Label(self, width = 20, height = 4, 
                                             text="第一推薦")
        self.no1_label.grid(row = 1, column = 0, sticky = 'w')
        
        self.no2_label = Label(self, width = 20, height = 4, 
                                             text="第二推薦")
        self.no2_label.grid(row = 2, column = 0, sticky = 'w')
        
        self.no3_label = Label(self, width = 20, height = 4, 
                                             text="第三推薦")
        self.no3_label.grid(row = 3, column = 0, sticky = 'w')
        
        self.no4_label = Label(self, width = 20, height = 4, 
                                             text="第四推薦")
        self.no4_label.grid(row = 4, column = 0, sticky = 'w')
        
        self.no5_label = Label(self, width = 20, height = 4, 
                                             text="第五推薦")
        self.no5_label.grid(row = 5, column = 0, sticky = 'w')
        
        self.no1_res_btn = Button(self, width = 20, height = 4, text= res_sort_list[0][0])
        self.no1_res_btn.config(width = 20, height = 1, font=('Helvetica', 12))
        self.no1_res_btn.grid(row = 1, column = 1, sticky = 'n'+'s')
        
        self.no2_res_btn = Button(self, width = 20, height = 4, text= res_sort_list[1][0])
        self.no2_res_btn.config(width = 20, height = 1, font=('Helvetica', 12))
        self.no2_res_btn.grid(row = 1, column = 1, sticky = 'n'+'s')
        
        self.no3_res_btn = Button(self, width = 20, height = 4, text= res_sort_list[2][0])
        self.no3_res_btn.config(width = 20, height = 1, font=('Helvetica', 12))
        self.no3_res_btn.grid(row = 1, column = 1, sticky = 'n'+'s')
        
        self.no4_res_btn = Button(self, width = 20, height = 4, text= res_sort_list[3][0])
        self.no4_res_btn.config(width = 20, height = 1, font=('Helvetica', 12))
        self.no4_res_btn.grid(row = 1, column = 1, sticky = 'n'+'s')
        
        self.no5_res_btn = Button(self, width = 20, height = 4, text= res_sort_list[4][0])
        self.no5_res_btn.config(width = 20, height = 1, font=('Helvetica', 12))
        self.no5_res_btn.grid(row = 1, column = 1, sticky = 'n'+'s')

def show_res_info():
    return 