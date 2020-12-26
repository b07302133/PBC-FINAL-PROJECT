from tkinter import*

page_4 = Tk()
page_4.title("選擇風格與排序方法")
page_4.geometry("800x600")
page_4.config(background="skyblue")  # 背景顏色
page_4.resizable(False, False)  # 固定視窗大小

res_name_label = Label(text= res.name + "的資訊", bg = "skyblue")
res_name_label.config(width=13, height=3, font ="微軟正黑體 20")
res_name_label.pack(side="top")

res_address_label = Label(text=res.address, bg = "skyblue")
res_address_label.config(width=13, height=3, font ="微軟正黑體 20")
res_address_label.pack(side="top")

res_phone_label = Label(text= res.phone, bg = "skyblue")
res_phone_label.config(width=13, height=3, font ="微軟正黑體 20")
res_phone_label.pack(side="top")

res_name_label = Label(text=res.time, bg = "skyblue")
res_name_label.config(width=13, height=3, font ="微軟正黑體 20")
res_name_label.pack(side="top")

res_star_label = Label(text=res.star, bg = "skyblue")
res_star_label.config(width=13, height=3, font ="微軟正黑體 20")
res_star_label.pack(side="top")

# 上下一步按鈕
back_btn = Button(text = "上一步", bg = "white")
back_btn.config(width=10, height=2)
back_btn.grid(row = 6, column = 2)

next_btn = Button(text = "重來", bg = "white")
next_btn.config(width=10, height=2)
next_btn.grid(row = 7, column = 2)
