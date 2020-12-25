# page4 後端
'''
前端要注意的地方：可以control F，打「前端」來查
博文要注意的地方：可以control F，打自己的名字來查(其實沒什麼要你注意的地方XD)
'''

import csv

select = input()  # 前端：你們用博文寫好的演算法篩選之後，最後篩出的餐廳請放在這(換掉input)

'''
前端：製作好的dictionary再p1back.py，把兩個黨並在一起後後端就可以做餐廳資料的label
地址 = name2address[select]
電話 = name2phone[select]
星星 = name2stars[select]
'''

import datetime
current_time = datetime.datetime.now()  # 前端：這是當下的時間，你們「距離休息時間」的botton按下去函示就可以把這個時間接住，拿來跟營業時間比
# print(current_time)
current_hour = int(str(current_time)[str(current_time).find(' ')+1:str(current_time).find(':')]) # 我把current_time換成整數(小時)才好比較
# print(current_hour)

# datetime的星期是用數字計，所以我用dictionary讓他記得我們星期botton的命名方式
num2day = dict()
num2day[1] = 'MON'
num2day[2] = 'TUE'
num2day[3] = 'WED'
num2day[4] = 'THU'
num2day[5] = 'FRI'
num2day[6] = 'SAT'
num2day[7] = 'SUN'

with open('canteen.csv', 'r', encoding='utf-8') as f:  # 讀csv檔
    reader = csv.reader(f)
    for row in reader:  # 跑csv檔的每一行
        row.pop(0)
        if row[0] == select:
            select_row = row
            break
    
    # 用dictionary記住我們選的餐廳每天的營業時間
    select2open = dict()
    select2open['MON'] = select_row[8]
    select2open['TUE'] = select_row[10]
    select2open['WED'] = select_row[12]
    select2open['THU'] = select_row[14]
    select2open['FRI'] = select_row[16]
    select2open['SAT'] = select_row[18]
    select2open['SUN'] = select_row[20]

    select_day = num2day[datetime.datetime.now().weekday()]  # 看使用者當時使用時是星期幾
    time_data_list = select2open[select_day].split(', ')  # 所選餐廳當天的營業時間叫time_data_list(因為很多餐廳中午晚上之間有休息，所以用list存)
    # print(time_data_list)
    
    # 因為很多餐廳一天開兩次店(中餐，晚餐)，所以要先篩選使用者當下的時間和哪個開店的時間比較近，先刪掉比較遠的
    open_max = -25
    for time in time_data_list:
        if '~' in time:
            open_hour = int(time[:time.find('~')-3])
            # print(open_hour)
            close_hour = int(time[time.find('~')+1:len(time)-3])
            if (current_hour - open_hour) > open_max:
                open_max = (current_hour - open_hour)
                open_time_str = (time[:time.find('~')]+':00.000000')
                close_time_str = (time[time.find('~')+1:]+':00.000000')
            '''
            我解釋一下這裡的思路，可以不用看！:
            營業時間通常長這樣:['11:30~14:30', '17:15~20:45']
            所以我用'~'往前三個字符('分鐘'都一樣佔2個字符，所以不會有問題)來取open_hour(開店時間)
            關店時間也是一樣的概念，大家不放心的話可以自行檢查
            '''
        if '–' in time:  # 有的人時間輸'-'，所以再做一次
            open_hour = int(time[:time.find('-')-3])
            close_hour = int(time[time.find('-')+1:len(time)-3])
            if (current_hour - open_hour) > open_max:
                open_max = (current_hour - open_hour)
                open_time_str = (time[:time.find('-')]+':00.000000')
                close_time_str = (time[time.find('-')+1:]+':00.000000')
    '''
    做完之後我存了兩個字串(open_time_str跟close_time_str)，分別代表刪選過後的開店、關店時間
    用字串的原因是因為datetime不太好比大小
    print(open_time_str)
    print(close_time_str)
    '''
    
    # 將open_time_str轉化成可比較的數值(轉化順序: 有符號的str - datetime - 只有數字的str - int)
    open_time = datetime.datetime.strptime(open_time_str, '%H:%M:%S.%f')
    time_passStr = str(current_time - open_time)
    min_passStr = time_passStr[time_passStr.find('s')+3:]
    # min_pass是已經開店多少分鐘的意思
    min_pass = int(min_passStr[:min_passStr.find(':')])*60 + int(min_passStr[min_passStr.find(':')+1:min_passStr.find(':')+3])

    # 將close_time_str轉化成可比較的數值(轉化順序: 有符號的str - datetime - 只有數字的str - int)
    close_time = datetime.datetime.strptime(close_time_str, '%H:%M:%S.%f')
    time_leftStr = str(close_time - current_time)
    min_leftStr = time_leftStr[time_leftStr.find('s')+3:]
    # min_left是還剩幾分鐘關店的意思
    min_left = int(min_leftStr[:min_leftStr.find(':')])*60 + int(min_leftStr[min_leftStr.find(':')+1:min_leftStr.find(':')+3])
    
    # print(min_pass)
    # print(min_left)
    
    run_timeStr = str(close_time - open_time)  # 篩選出來我們要比較的營業時間
    # print(run_timeStr)
    
    # 用分鐘計營業總時長
    if run_timeStr == '0:00:00':  # 不打烊的話
        run_time = 1440
    elif 'day' in run_timeStr:  # 營業久到關店比開店早的話(Ex. ['07:00~00:00']會變成: -1 day, 17:00:00)
        run_time = int(run_timeStr[run_timeStr.find(',')+2:run_timeStr.find(':')])*60 + int(run_timeStr[run_timeStr.find(':')+1:run_timeStr.find(':')+3])
    else: # 正常的情況
        run_time = int(run_timeStr[:run_timeStr.find(':')])*60 + int(run_timeStr[run_timeStr.find(':')+1:run_timeStr.find(':')+3])
    # print(run_time)

    # 最後印出來的結果，設計對白供前端參考
    if min_pass > run_time:  # 已經開店的時間大於營業總時常的話，就代表已經關店了
        print('今天目前還沒開窩！再等等')
    else:
        if min_left <= 90:  # 小於90分鐘，提醒注意
            print('一個半小時內關門窩！要吃要快')
        else:  # 正常情況
            print('正在賣窩！可以去吃')

    f.close
