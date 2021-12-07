#function here
from import_ import * 

#主程式
'''
定義對話關鍵字:
if input_ == '關鍵字':
	函數名稱()

'''
def main_function(input_):
	chat_list_count = 0
	try:
		if input_ == '天氣':
			weather()
		#if input_ == '':
	except:
		difflib_function(input_)
	
#模糊判斷
def difflib_function(input_):
	#cutoff: 誤差, n:回傳幾筆近似資料
	data = difflib.get_close_matches(input_, cutoff = 0.5, n=1)
	print('你是不是想說: ' + data)

#從這裡開始是定義對話關鍵字的函式
def weather():



	
