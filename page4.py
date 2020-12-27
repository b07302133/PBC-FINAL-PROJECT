from tkinter import*
page_4 = Tk()
page_4.title("懂吃懂吃")
page_4.geometry("800x600")
page_4.config(background="skyblue")  # 背景顏色
page_4.resizable(False, False)  # 固定視窗大小

res_name_label = Label(text= res.name + "的資訊", bg = "skyblue")
res_name_label.config(height=3,font ="微軟正黑體 20")
res_name_label.pack(side="top")

res_address_label = Label(text="地址："+ name2address[res.name], bg = "skyblue")
res_address_label.config(height=3,font ="微軟正黑體 20")
res_address_label.pack(side="top")

res_phone_label = Label(text= "電話："+name2phone[res.name], bg = "skyblue")
res_phone_label.config(height=3, font ="微軟正黑體 20")
res_phone_label.pack(side="top")

res_time_label = Label(text="營業時間："+name2open[res.name], bg = "skyblue")
res_time_label.config(height=3, font ="微軟正黑體 20")
res_time_label.pack(side="top")

res_star_label = Label(text="星級："+ name2stars[res.name], bg = "skyblue")
res_star_label.config(height=3, font ="微軟正黑體 20")
res_star_label.pack(side="top")

# 上下一步按鈕
back_btn = Button(text = "上一步", bg = "white")
back_btn.config(width=10, height=2)
back_btn.pack(side="left")

restart_btn = Button(text = "重來", bg = "white")
restart_btn.config(width=10, height=2)
restart_btn.pack(side = "right")

page_4.mainloop()  # 常駐主視窗