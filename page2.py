# page2
from tkinter import*
page_2 = Tk()
page_2.title("選擇風格與排序方法")
page_2.geometry("600x500+300+100")
page_2.config(background="skyblue")  # 背景顏色
page_2.resizable(False, False)  # 固定視窗大小

style_label = Label(text="風格", bg = "skyblue")
style_label.config(width=13, height=3, font ="微軟正黑體 20")
style_label.grid(row = 0, column = 1, sticky = 'w' + 'n')

order_label = Label(text="排序方法", bg = "skyblue")
order_label.config(width=13, height=3, font ="微軟正黑體 20")
order_label.grid(row = 0, column = 2, sticky = 'e' + 'n')

label_1 = Label(text="1. ", bg = "skyblue")
label_1.config(width=3, height=1, font ="微軟正黑體 12")
label_1.grid(row = 1, column = 0, sticky = 'w')

label_2 = Label(text="2. ", bg = "skyblue")
label_2.config(width=3, height=1, font ="微軟正黑體 12")
label_2.grid(row = 2, column = 0, sticky = 'w')

label_3 = Label(text="3. ", bg = "skyblue")
label_3.config(width=3, height=1, font ="微軟正黑體 12")
label_3.grid(row = 3, column = 0, sticky = 'w')

label_4 = Label(text="4. ", bg = "skyblue")
label_4.config(width=3, height=1, font ="微軟正黑體 12")
label_4.grid(row = 4, column = 0, sticky = 'w')

label_5 = Label(text="5. ", bg = "skyblue")
label_5.config(width=3, height=1, font ="微軟正黑體 12")
label_5.grid(row = 5, column = 0, sticky = 'w')

# 上下一步按鈕
back_btn = Button(text = "上一步", bg = "white")
back_btn.config(width=10, height=2)
back_btn.grid(row = 6, column = 2)

next_btn = Button(text = "下一步", bg = "white")
next_btn.config(width=10, height=2)
next_btn.grid(row = 7, column = 2)

# 風格下拉式選單
style_List = [
"日式","美式","義式",
"法式","韓式","中式",
"小吃","咖啡廳","手搖杯",
"東南亞料理","速食","素食",
"酒吧","健康餐","火鍋",
"西式","燒烤/鐵板燒/牛排館",
"肥宅/魯蛇吃宵","咖哩","水餃",
] 

style_variable = StringVar(page_2)
style_variable.set(["請選擇風格"])

style_opt1 = OptionMenu(page_2, style_variable, *style_List)
style_opt1.config(width=20, font=('Helvetica', 12))
style_opt1.grid(row = 1, column = 1, sticky = 'w')

style_opt2 = OptionMenu(page_2, style_variable, *style_List)
style_opt2.config(width=20, font=('Helvetica', 12))
style_opt2.grid(row = 2, column = 1, sticky = 'w')

style_opt3 = OptionMenu(page_2, style_variable, *style_List)
style_opt3.config(width=20, font=('Helvetica', 12))
style_opt3.grid(row = 3, column = 1, sticky = 'w')

style_opt4 = OptionMenu(page_2, style_variable, *style_List)
style_opt4.config(width=20, font=('Helvetica', 12))
style_opt4.grid(row = 4, column = 1, sticky = 'w')

style_opt5 = OptionMenu(page_2, style_variable, *style_List)
style_opt5.config(width=20, font=('Helvetica', 12))
style_opt5.grid(row = 5, column = 1, sticky = 'w')

# 排序下拉式選單
order_List = ["planA", "planB"]
order_variable = StringVar(page_2)
order_variable.set(["請選擇排序方式"])
order_opt = OptionMenu(page_2, order_variable, *order_List)
order_opt.config(width=20, font=('Helvetica', 12))
order_opt.grid(row = 1, column = 2, sticky = 'e')


page_2.mainloop()  # 常駐主視窗