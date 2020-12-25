import csv

with open('canteen.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        row.pop(0)
        print(row)
        '''
        string = ""
        for subject in row:
            subject = subject.replace('\t', ',')
            string += subject
        strlist = string.split(',')
        strlist.pop(0)

        for i in range(len(strlist)):
            if (strlist[i] == '是') or (strlist[i] == '否'):
                strlist[i] += (', ' + strlist[i+1])
        
        droplist = [8,9,10,11,12,13,14]
        for i in droplist:
            strlist.pop(i)

        # print(strlist)  # 每筆strlist是每筆餐廳的資料
        '''
        # strlist[0] == '餐廳名稱'
        # strlist[1] == '地區'
        # strlist[2] == '早中晚宵'
        # strlist[3] == '類型'
        # strlist[4] == '電話'
        # strlist[5] == '地址'
        # strlist[6] == '星級'
        # strlist[7] == '星期一'
        # strlist[8] == '星期二'
        # strlist[9] == '星期三'
        # strlist[10] == '星期四'
        # strlist[11] == '星期五'
        # strlist[12] == '星期六'
        # strlist[13] == '星期日'
        # strlist[14] == '低消'
        # strlist[15] == '訂位'

        
        f.close
