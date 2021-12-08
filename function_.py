#function here
from import_ import * 

#主程式
'''
定義對話關鍵字:
if input == '關鍵字':
    函數名稱()

'''
def mainfunction(input):
    #line api information: 
    chat_listcount = 0
    try:
        if input == '天氣':
            locate_area = ''
            collect_information = ['']
            '''(這裡輸入子判斷式判斷要搜尋哪個區域),
                類似->input('請搜尋要查詢的行政區')
            '''
            collect_information = 'test'
            weather()
        #if input == '':
    except:
        difflibfunction(input)

#模糊判斷
def difflibfunction(input):
    #cutoff: 誤差, n:回傳幾筆近似資料
    data = difflib.get_closematches(input, cutoff = 0.5, n=1)
    print('你是不是想說: ' + data)

#從這裡開始是定義對話關鍵字的函式
def weather():
    data = request.get('https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=rdec-key-123-45678-011121314%27')