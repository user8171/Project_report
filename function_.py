#function here
#-*- coding:utf-8 -*-
from import_ import * 

def btn_col(status_code, entry_element, scrolledtext_element, button_element):
	if entry_element.get() != '':
		#status_code 設定為一般聊天
		if status_code == 1:
			talking_function(entry_element.get(), entry_element, scrolledtext_element, button_element, status_code)
			#entry_element.delete(0,"end")
		#status_code 設定為查詢天氣資訊
		elif status_code == 2:
			weather(entry_element.get(), entry_element, scrolledtext_element, button_element, status_code)
			entry_element.delete(0,"end")

#關鍵字對話程式
#input_text為使用者輸入文字, scrolledtext_element為label元素
def talking_function(input_text, entry_element, scrolledtext_element, button_element, status_code):
	#關鍵字清單
	interact_text = ['天氣','你好','時間','美食', '運動']
	if input_text == '天氣':
		weather(input_text, entry_element, scrolledtext_element, button_element, status_code)
		entry_element.delete(0,"end")
	elif input_text == '你好':
		hello(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '時間':
		get_time(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '美食':
		good_food_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '運動':
		exercise_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	else:
		difflibfunction(input_text, interact_text, scrolledtext_element, entry_element)
	
#模糊判斷
def difflibfunction(input_text, interact_text, scrolledtext_element, entry_element):
	#cutoff: 誤差, n:回傳幾筆近似資料
	try:
		data = difflib.get_close_matches(input_text, interact_text, cutoff = 0.5, n=1)
		output_str = '你是不是想說: ' + data[0] + '\n'
		scrolledtext_element.insert(tk.END, output_str)
		entry_element.delete(0,"end")
		entry_element.insert(0,data[0])
	except:
		output_str = '不支援的關鍵字。' + '\n' 
		scrolledtext_element.insert(tk.END, output_str)

#從這裡開始是定義對話關鍵字的函式
#未來七天天氣預報 
#def weather(input_text):
def weather(input_text, entry_element, scrolledtext_element, button_element, status_code):
	if status_code == 1:
		output_str = '請輸入台灣行政區,輸入「取消」以停止搜尋天氣資訊' + '\n'
		scrolledtext_element.insert(tk.END, output_str)
		button_element['command'] = command=lambda: btn_col(2, entry_element, scrolledtext_element, button_element)
		#button_element.configure(command=lambda: btn_col(2))
		return True
	elif input_text == '取消':
		#button_element['command'] = 'command=lambda: btn_col(1)' 
		button_element.configure(command=lambda: btn_col(1, entry_element, scrolledtext_element, button_element))
		output_str = '已結束搜尋天氣資訊。'  + '\n'
		scrolledtext_element.insert(tk.END, output_str)
		return 0
        
	#修改button的status_code
	button_element['command'] = 'command=lambda: btn_col(2)' 
	url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-D0047-091?Authorization=rdec-key-123-45678-011121314'
	locations = {'基隆市':'12', '臺北市':'9', '新北市':'3', '桃園市':'13', '新竹縣':'0', '新竹市':'21', '苗栗縣':'2', '臺中市':'20', '彰化縣':'8', '雲林縣':'5', '南投縣':'10', '嘉義縣':'18', '嘉義市':'17', '臺南市':'6', '高雄市':'7', '屏東縣':'19', '臺東縣':'16', '花蓮縣':'14', '宜蘭縣':'4', '金門縣':'1', '澎湖縣':'11', '連江縣':'15'}
        
	#判斷是否有資料
	try:
		location_number = locations[input_text]
		get_data = requests.get(url).text
		get_data = json.loads(get_data)
		data = ''
		data = get_data['records']
		data = data['locations']
		data = data[0]
		data = data['location']
		data = data[int(location_number)]

		#return型態為List,其內容為未來七天的天氣資訊,還有原網址
		weather_predict_information(data, scrolledtext_element)
		button_element.configure(command=lambda: btn_col(1, entry_element, scrolledtext_element, button_element))

	except KeyError:
		#loction_list為可以被查詢的縣市
		locations_list = ['支援的縣市:']
		for key in locations.keys():
			locations_list[0] += key + ' '
		output_str = '輸入未支援的地區。\n\n' + locations_list[0] +'\n請重新輸入。' + '\n'
		scrolledtext_element.insert(tk.END, output_str)
		button_element.configure(command=lambda: btn_col(2, entry_element, scrolledtext_element, button_element))
		pass

	except Exception as e:
		output_str = '發生未知錯誤。錯誤代碼訊息: ' + e + '\n'
		scrolledtext_element.insert(tk.END, output_str)

#未來七天降雨機率
def weather_predict_information(data, scrolledtext_element):
	collect_weather_information = ''
	try:
		data = data['weatherElement']
		data = data[10]
		data = data['time']
		for i in range(0, 7):
			present_data = data[i]
			collect_weather_information +='開始時間: ' + present_data.get('startTime') + '\n結束時間: ' + present_data.get('endTime') + '\n天氣資訊:\n'
			present_data = present_data['elementValue']
			present_data = present_data[0]
			collect_weather_information += present_data.get('value') + '\n\n'
		collect_weather_information += "更多資訊: https://data.gov.tw/dataset/9308" + '\n'
		output_str = collect_weather_information
		scrolledtext_element.insert(tk.END, output_str)

	except Exception as e:
		output_str = '發生未知錯誤。錯誤代碼訊息: ' + e
		scrolledtext_element.insert(tk.END, output_str)

def hello(input_, scrolledtext_element):
	output_str = '您好,歡迎與我聊天' + '\n'
	scrolledtext_element.insert(tk.END, output_str)

def get_time(input_, scrolledtext_element):
	output_str = '現在時間是: ' + str(datetime.datetime.now()) + '\n'
	scrolledtext_element.insert(tk.END, output_str)

def good_food_osusume(input_, scrolledtext_element):
	good_food_list = ['藍獸亓--香酥黃金雞飯',  '二口炒飯--綜合鐵板麵', '快炒王--火腿蛋炒飯', '福禾--無骨雞丁便當', '古早味便當--大雞腿便當', '翔鶴--雞排便當', '樂謎雞排--原味雞排', '八兩--雞排', '豪大要倒了']
	good_drink_list = ['水云茶堂--珍珠紅茶無糖去冰', '多多茶坊--核廢料', '喫茶小舖--薑汁撞奶', '春水堂--珍珠奶茶']
	output_str = '今天推薦 ' + good_food_list[random.randint(0, len(good_food_list)-1)] + ',搭配 ' + good_drink_list[random.randint(0, len(good_drink_list)-1)] + '\n'
	scrolledtext_element.insert(tk.END, output_str)

def exercise_osusume(input_, scrolledtext_element):
	exercise_list = ['籃球', '羽球', '網球', '排球']
	output_str = '運動建議: ' + exercise_list[random.randint(0, len(exercise_list))-1] + '\n'
	scrolledtext_element.insert(tk.END, output_str)