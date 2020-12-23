import requests
import json

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


# 輸入欲查找的商家名稱或地址
resteraunt = str(input('輸入欲查找的商家名稱或地址：'))

# 開啟 web driver
chromedriver = '/usr/local/bin/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.maximize_window()  # 最大化視窗，方便觀看

# 前往該網址
print('打開 Google map中...')
url = 'https://www.google.com.tw/maps/@23.546162,120.6402133,8z?hl=zh-TW'
browser.get(url) 

# 搜尋自動化
def search_automation():
    # 搜尋鈕元素定位 
    print('搜尋中...')
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.ID, 'searchbox')))
    resterauntname_input = browser.find_elements_by_xpath('//*[@id="searchboxinput"]')[0]
    
    # 向搜尋欄傳入
    resterauntname_input.send_keys(resteraunt)
    time.sleep(1)
    
    # 按下搜尋鈕
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchbox"]/div[1]')))
    search_bottom = browser.find_elements_by_xpath('//*[@id="searchbox"]/div[1]')[0]
    search_bottom.click()

# 選取第一個搜尋結果
def select_first_search_result():
    print('展開第一個搜尋結果')
    
    try:  
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME,
        'section-result')))
        
        top_result = browser.find_elements_by_class_name('section-result')[0]
        top_result.click()
    
    # 當僅有一個搜尋結果時，便不需要點擊低一個搜尋結果。
    except TimeoutException:
        print('只有一項顯示結果')
        print()
        
# 展開評論功能
def show_more_comment_result():
    print('正在展開更多評論...')
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,
    '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span/span[1]/span[2]/span[1]/button')))
    
    more_comment = browser.find_elements_by_xpath(
        '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span/span[1]/span[2]/span[1]/button')[0]
    
    # 取出評論數，並進行處理 
    raw_comment_number = more_comment.text    
    raw_comment_number = raw_comment_number.split(' ')
    
    # 僅留下數字的評論數
    comment_number = raw_comment_number[0]
    print(comment_number + '則評論')
    
    # 點擊更多評論
    more_comment.click()
    time.sleep(5)
    
    return(int(comment_number))


# WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME,
# 'section-layout section-scrollbox scrollable-y scrollable-show')))

# 自動捲動搜尋結果
def auto_scorolling(comment_number):
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,
    '//*[@id="pane"]/div/div[1]/div/div/div[2]')))
    
    round_count = 0 
    
    if (comment_number - 8) % 10 != 0:
        needed_looping_times = (comment_number - 8)//10 + 1
        print('未整除')
        
        
    elif (comment_number - 8) % 10 == 0:
        needed_looping_times = (comment_number - 8)//10
        print('整除')
    
    print(needed_looping_times)
    
    for i in range(needed_looping_times):
        js='document.getElementsByClassName("section-layout section-scrollbox scrollable-y scrollable-show")[0].scrollTop=100000' 
        browser.execute_script(js)
        time.sleep(1.5)
    
        round_count += 1        
        print('Scrolling...' + str(int(round_count)))

        # 這邊在嘗試抓加載頁面 element 時，停止刷新。
        # WebDriverWait(browser, 10).until_not(EC.invisibility_of_element_located((By.XPATH,
        # '//*[@id="pane"]/div/div[1]/div/div/div[2]/div[10]/div[3]')))
    

# 抓取所有評論
def catch_all_comment():
    print('==結果輸出==')
    print()
    
    comment_list = browser.find_elements_by_class_name('section-review-review-content')
    file_name = 'comment list improve'
    file = open(file_name, 'w', encoding = 'utf-8')
    file.write('總共有：' + str(len(comment_list)) + ' 筆評論'+ '\n')
    file.write('=====' + '\n')
    print('總共有：' + str(len(comment_list)) + ' 筆評論')
    print('=====' + '\n')
    
    return(file, comment_list)


# 將評論存入檔案
def writing_and_print_all_comment(file, comment_list):
    for j in range(len(comment_list)):  
            # 如果爬完了所有可讀文字，便終止迴圈
            if len(comment_list[j].text) == 0:
                print('Empty comment found!End loop.')
                break
        
            # 去除換行
            # 去除空白字元
            comment_input = comment_list[j].text
            comment_input = comment_input.replace('\n', '')
            comment_input = comment_input.replace(' ', '，')
            
            print(comment_input)
            print('=====')
            
            file.write(comment_input + '\n')
    
    file.close()

search_automation()
select_first_search_result()
comment_number = show_more_comment_result()
auto_scorolling(comment_number)
file, comment_list = catch_all_comment()
writing_and_print_all_comment(file, comment_list)

