from googletrans import Translator
import requests

def chat(value):
	if("sahibin kim" in value):
		print("kenan")
		return "Sahibim namıdeğer r4isy."
	else:
		translator = Translator()
		t = translator.translate(value, dest="en")
		response = requests.get("http://api.brainshop.ai/get?bid=153868&key=rcKonOgrUFmn5usX&uid=1&msg=" + t.text)
		veri = response.text.split(':"')[-1].split('"}')[0]
		translated = translator.translate(veri, dest="tr")
		if("zackybot" in translated.text):
			new_string = "Adım, kenu-ai. r4isy tarafından yazıldım."
			return new_string
		elif("Accobot" in translated.text):
			return "Sahibim namıdeğer r4isy."
		else:
			return translated.text