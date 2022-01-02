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
	interact_text = ['查看天氣','天氣','未來三天天氣如何呢?','你好','時間','查看時間','幫我查看現在的時間','幫我想可以吃什麼?','幫我想可以吃什麼?','幫我決定可以吃什麼呢?','幫我決定可以吃什麼?','今天可以吃什麼?','那我可以吃什麼呢?','那去吃飯','去吃飯','吃飯','我想吃飯','我想運動','運動','哈囉','Hello','你吃飽了嗎?','你覺得我今天可以做什麼?','你覺得我今天可以做什麼呢?','我可以做哪些運動呢?','但是我想繼續跟你聊天','繼續跟你聊天','我想聊天','功能','查詢功能','你可以做什麼?','你有哪些功能呢?']
	if input_text == '天氣':
		weather(input_text, entry_element, scrolledtext_element, button_element, status_code)
		entry_element.delete(0,"end")
	elif input_text == '未來三天天氣如何呢?':
		weather(input_text, entry_element, scrolledtext_element, button_element, status_code)
		entry_element.delete(0,"end")
	elif input_text == '查看天氣':
		weather(input_text, entry_element, scrolledtext_element, button_element, status_code)
		entry_element.delete(0,"end")
	elif input_text == '你吃飽了嗎?':
		full(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '你好':
		hello(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == 'Hello':
		hello(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '哈囉':
		hello(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '繼續跟你聊天':
		keep1(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '我想聊天':
		keep1(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '但是我想繼續跟你聊天':
		keep(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '時間':
		get_time(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '查看時間':
		get_time(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '幫我查看現在的時間':
		get_time(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '你覺得我今天可以做什麼?':
		doing(input_text, scrolledtext_element)
	elif input_text == '你覺得我今天可以做什麼呢?':
		doing(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '今天可以吃什麼?':
		good_food_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '那我可以吃什麼呢?':
		good_food_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '吃飯':
		good_food_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '我想吃飯':
		good_food_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '那去吃飯':
		good_food_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '去吃飯':
		good_food_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '選擇吃飯':
		good_food_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '幫我想可以吃什麼?':
		good_food_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '幫我想可以吃什麼呢?':
		good_food_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '幫我決定可以吃什麼?':
		good_food_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '幫我決定可以吃什麼呢?':
		good_food_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '運動':
		exercise_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '我想運動':
		exercise_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '我可以做哪些運動呢?':
		exercise_osusume(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '功能':
		fu(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '查詢功能':
		fu(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '你可以做什麼?':
		fu(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	elif input_text == '你有哪些功能呢?':
		fu(input_text, scrolledtext_element)
		entry_element.delete(0,"end")
	else:
		difflibfunction(input_text, interact_text, scrolledtext_element, entry_element)
	
#模糊判斷
def difflibfunction(input_text, interact_text, scrolledtext_element, entry_element):
	#cutoff: 誤差, n:回傳幾筆近似資料
	try:
		data = difflib.get_close_matches(input_text, interact_text, cutoff = 0.5, n=1)
		output_str = '你是不是想說: ' + data[0] + ' ?' + '\n' + '---------------------------------------------------------'
		scrolledtext_element.insert(tk.END, output_str)
		entry_element.delete(0,"end")
		entry_element.insert(0,data[0])
	except:
		output_str = '不支援的關鍵字,如果不知道有哪些功能用可以問問機器人,ex:查詢功能' + '\n' 
		scrolledtext_element.insert(tk.END, output_str)

#從這裡開始是定義對話關鍵字的函式
#未來三天天氣預報 
#def weather(input_text):
def weather(input_text, entry_element, scrolledtext_element, button_element, status_code):
	if status_code == 1:
		output_str = '如果想知道天氣如何,那請輸入該縣市名稱 ' + 'ex:臺中市\n' + '如果不用的話,那請輸入「取消」即可停止搜尋天氣資訊' + '\n' + '---------------------------------------------------------'
		scrolledtext_element.insert(tk.END, output_str)
		button_element['command'] = command=lambda: btn_col(2, entry_element, scrolledtext_element, button_element)
		#button_element.configure(command=lambda: btn_col(2))
		return True
	elif input_text == '取消':
		#button_element['command'] = 'command=lambda: btn_col(1)' 
		button_element.configure(command=lambda: btn_col(1, entry_element, scrolledtext_element, button_element))
		output_str = '已結束搜尋天氣資訊。'  + '\n' + '---------------------------------------------------------'
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

		#return型態為List,其內容為未來三天的天氣資訊,還有原網址
		weather_predict_information(data, scrolledtext_element)
		button_element.configure(command=lambda: btn_col(1, entry_element, scrolledtext_element, button_element))

	except KeyError:
		#loction_list為可以被查詢的縣市
		locations_list = ['支援的縣市:']
		for key in locations.keys():
			locations_list[0] += key + ' '
		output_str = '輸入未支援的地區。\n\n' + locations_list[0] +'\n請重新輸入。' + '\n' + '---------------------------------------------------------'
		scrolledtext_element.insert(tk.END, output_str)
		button_element.configure(command=lambda: btn_col(2, entry_element, scrolledtext_element, button_element))
		pass

	except Exception as e:
		output_str = '發生未知錯誤。錯誤代碼訊息: ' + e + '\n' + '---------------------------------------------------------'
		scrolledtext_element.insert(tk.END, output_str)

#未來三天降雨機率
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
		collect_weather_information += "更多資訊: https://data.gov.tw/dataset/9308" + '\n' + '---------------------------------------------------------'
		output_str = collect_weather_information
		scrolledtext_element.insert(tk.END, output_str)

	except Exception as e:
		output_str = '發生未知錯誤。錯誤代碼訊息: ' + e + '\n' + '---------------------------------------------------------'
		scrolledtext_element.insert(tk.END, output_str)

def hello(input_, scrolledtext_element):
	output_str = '您好,歡迎與我聊天,請問有什麼事嗎? 或有什麼想聊的嗎?' + '\n' + '---------------------------------------------------------'
	scrolledtext_element.insert(tk.END, output_str)

def get_time(input_, scrolledtext_element):
	now = datetime.datetime.now()
	output_str = '現在時間是: ' + now.strftime("%Y年%m月%d號 %H時%M分%S秒") + '\n' + '---------------------------------------------------------'
	scrolledtext_element.insert(tk.END, output_str)

def good_food_osusume(input_, scrolledtext_element):
	good_food_list = ['藍獸亓--香酥黃金雞飯',  '二口炒飯--綜合鐵板麵', '快炒王--火腿蛋炒飯', '福禾--無骨雞丁便當', '古早味便當--大雞腿便當', '翔鶴--雞排便當', '樂謎雞排--原味雞排', '八兩--雞排']
	good_drink_list = ['水云茶堂--珍珠紅茶無糖去冰', '多多茶坊--核廢料', '喫茶小舖--薑汁撞奶', '春水堂--珍珠奶茶']
	output_str = '我覺得你今天可以吃 : \n' + good_food_list[random.randint(0, len(good_food_list)-1)] + ' 搭配 ' + good_drink_list[random.randint(0, len(good_drink_list)-1)] + '\n' + '---------------------------------------------------------'
	scrolledtext_element.insert(tk.END, output_str)

def exercise_osusume(input_, scrolledtext_element):
	exercise_list = ['打籃球', '打羽球', '打網球', '打排球','踢足球','打撞球','打桌球']
	output_str = '你今天可以去 : ' + exercise_list[random.randint(0, len(exercise_list))-1] + '\n' + '---------------------------------------------------------'
	scrolledtext_element.insert(tk.END, output_str)

def full(input_, scrolledtext_element):
	full_list = ['雖然只有電,但是我吃很飽謝謝關心!!','痾....當然有吃飽,不然還能跟你聊天?']
	output_str = full_list[random.randint(0, len(full_list))-1] + '請問還有什麼事呢? 或是想聊的?' + '\n' + '---------------------------------------------------------'
	scrolledtext_element.insert(tk.END, output_str)

def doing(input_, scrolledtext_element):
	doing_list = [' 運動 ',' 睡覺 ',' 吃一中街食物 ']
	output_str = '我覺得你可以去' + doing_list[random.randint(0, len(doing_list))-1] + '或 繼續陪我聊天 ' + '\n' + '---------------------------------------------------------'
	scrolledtext_element.insert(tk.END, output_str)

def keep(input_, scrolledtext_element):
	keep_list = ['當然沒有問題!!','謝謝~我很歡迎','那有什麼問題!']
	output_str = keep_list[random.randint(0, len(keep_list))-1] + '那你想聊什麼呢?' + '\n' + '---------------------------------------------------------'
	scrolledtext_element.insert(tk.END, output_str)

def keep1(input_, scrolledtext_element):
	output_str = '那你想聊什麼呢?' + '\n' + '---------------------------------------------------------'
	scrolledtext_element.insert(tk.END, output_str)

def fu(input_, scrolledtext_element):
	output_str = '我有以下這些功能:\n' + '查看天氣\n' + '查看時間\n' + '建議你今天可以做什麼\n' + '幫你想可以吃什麼食物,但僅限於一中街\n' + '建議你可以做什麼運動\n' + '\n' + '---------------------------------------------------------'
	scrolledtext_element.insert(tk.END, output_str)