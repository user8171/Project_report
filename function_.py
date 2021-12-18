#function here
#-*- coding:utf-8 -*-
from tkinter import EXCEPTION
from requests.api import get
from import_ import * 

'''
定義對話關鍵字:
if input == '關鍵字':
    函數名稱()

'''
#主程式
def mainfunction(input):
        #line api information: 
        chat_listcount = 0
        try:
                if input == '天氣':
                        locate_area = ''
                        '''(這裡輸入子判斷式判斷要搜尋哪個區域),
                                類似->input('請搜尋要查詢的行政區')
                        '''
                        weather()#函式內放要查詢的行政區
                #if input == '':
        except:
                difflibfunction(input)

#模糊判斷
def difflibfunction(input):
        #cutoff: 誤差, n:回傳幾筆近似資料
        data = difflib.get_closematches(input, cutoff = 0.5, n=1)
        print('你是不是想說: ' + data)

#從這裡開始是定義對話關鍵字的函式
def weather(input_location):
        collect_information = ['']
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=rdec-key-123-45678-011121314'
        locations = {'基隆市':'12', '臺北市':'9', '新北市':'3', '桃園市':'13', '新竹縣':'0', '新竹市':'21', '苗栗縣':'2', '臺中市':'20', '彰化縣':'8', '雲林縣':'5', '南投縣':'10', '嘉義縣':'18', '嘉義市':'17', '臺南市':'6', '高雄市':'7', '屏東縣':'19', '臺東縣':'16', '花蓮縣':'14', '宜蘭縣':'4', '金門縣':'1', '澎湖縣':'11', '連江縣':'15'}
            
        if input_location not in locations:
                print("error")
        else:
                get_data = requests.get(url).text
                get_data = json.loads(get_data)
                data = ''
                data = get_data['records']
                data = data['locations']
                data = data[0]
                data = data['location']
        
        #data = data[0]
        #data = data['weatherElement']
        #for i in locations:
        #        print(locations[i])
        
#weather('基隆市')
#weather('GG市')
