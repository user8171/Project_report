#function here
#-*- coding:utf-8 -*-
from tkinter import EXCEPTION
from typing import cast
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
        
        #判斷是否有資料
        try:
                location_number = locations[input_location]
                get_data = requests.get(url).text
                get_data = json.loads(get_data)
                data = ''
                data = get_data['records']
                #type: dict
                data = data['locations']
                #type: list
                data = data[0]
                #type: dict
                data = data['location']
                #type: list
                data = data[int(location_number)]
                #type: dict

                #凱擇,這裡讓使用者輸入「降雨機率預報」套用weather_predict_information(data)函式
                #return型態為List,其內容為未來七天的天氣資訊,還有原網址

                #weather_predict_information(data)

                #type: dict
                #weather_raindown_persent(data)
                


        except KeyError:
                #凱擇,這裡用Label修改文字="輸入未支援的地區"
                #loction_list為可以被查詢的縣市
                print("輸入未支援的地區")
                locations_list = ['支援的縣市:']
                for key in locations.keys():
                        locations_list[0] += key + ' '
                print(locations_list[0])

        except Exception as e:
                #凱擇,這裡用Label修改文字="發生未知錯誤"
                print(f"發生未知錯誤,code: {e}")

#未來七天降雨機率
def weather_predict_information(data):
        collect_weather_information = ['', '', '', '', '', '', '','']
        try:
                data = data['weatherElement']
                data = data[10]
                data = data['time']
                for i in range(0, 7):
                        present_data = data[i]
                        collect_weather_information[i] +='開始時間: ' + present_data.get('startTime') + '\n結束時間: ' + present_data.get('endTime') + '\n天氣資訊'
                        present_data = present_data['elementValue']
                        present_data = present_data[0]
                        collect_weather_information[i] += present_data.get('value') + '\n'
                collect_weather_information[7] += "更多資訊: https://data.gov.tw/dataset/9308"
                return collect_weather_information
        except Exception as e:
                #凱擇,這裡用Label修改文字="發生未知錯誤"
                print(f"發生未知錯誤,code: {e}")

#weather('新竹縣')
#weather('基隆市')
weather('GG市')