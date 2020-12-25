import csv

with open('canteen.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    name2locate = dict()
    name2meal = dict()
    name2style = dict()
    name2phone = dict()
    name2address = dict()
    for row in reader:
        row.pop(0)
        # print(row)
        name2locate[row[0]] = row[1]
        name2meal[row[0]] = row[2]
        name2style[row[0]] = row[3]
        name2phone[row[0]] = row[4]
        name2address[row[0]] = row[5]

    class Dictrionary:
        def __init__ (self, name):
            self.name = name
    f.close