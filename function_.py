#function here
#-*- coding:utf-8 -*-
from tkinter import EXCEPTION, Label
from tkinter.constants import NONE
from typing import cast
from requests.api import get
from import_ import * 

'''
定義對話關鍵字:
if input == '關鍵字':
    函數名稱()

'''

#關鍵字對話程式
#input_為使用者輸入文字, label_element為label元素
def talking_function(input_, label_element):
        #關鍵字清單
        interact_text = ['天氣','你好']
        input_ = str(input_)
        if input_ == '天氣':
                weather(input_, label_element)
         #if input == '':
        else:
                difflibfunction(input_, interact_text, label_element)

#模糊判斷
def difflibfunction(input_, interact_text, label_element):
        #cutoff: 誤差, n:回傳幾筆近似資料
        try:
                data = difflib.get_close_matches(input_, interact_text, cutoff = 0.5, n=1)
                label_element['text'] = '你是不是想說: ' + data[0]
        except:
                label_element['text'] = '不支援的關鍵字。' 

#從這裡開始是定義對話關鍵字的函式
#未來七天天氣預報
def weather(input_location, label_element):
        collect_information = ['']
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=rdec-key-123-45678-011121314'
        locations = {'基隆市':'12', '臺北市':'9', '新北市':'3', '桃園市':'13', '新竹縣':'0', '新竹市':'21', '苗栗縣':'2', '臺中市':'20', '彰化縣':'8', '雲林縣':'5', '南投縣':'10', '嘉義縣':'18', '嘉義市':'17', '臺南市':'6', '高雄市':'7', '屏東縣':'19', '臺東縣':'16', '花蓮縣':'14', '宜蘭縣':'4', '金門縣':'1', '澎湖縣':'11', '連江縣':'15'}
        
        #判斷是否有資料
        try:
                #label_element['text'] = '請輸入台灣行政區' 
                print(type(input_location))
                location_number = locations[input_location]
                get_data = requests.get(url).text
                get_data = json.loads(get_data)
                data = ''
                data = get_data['records']
                data = data['locations']
                data = data[0]
                data = data['location']
                data = data[int(location_number)]

                #凱擇,這裡讓使用者輸入「降雨機率預報」套用weather_predict_information(data)函式
                #return型態為List,其內容為未來七天的天氣資訊,還有原網址
                weather_predict_information(data, label_element)
                

        except KeyError:
                #loction_list為可以被查詢的縣市
                print("輸入未支援的地區")
                locations_list = ['支援的縣市:']
                for key in locations.keys():
                        locations_list[0] += key + ' '
                print(locations_list[0])
                label_element['text'] = '輸入未支援的地區。\n' + locations_list

        except Exception as e:
                #凱擇,這裡用Label修改文字="發生未知錯誤"
                label_element['text'] = '發生未知錯誤。錯誤代碼訊息: ' + e

#未來七天降雨機率
def weather_predict_information(data, label_element):
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
                label_element['text'] = '發生未知錯誤。錯誤代碼訊息: ' + e
