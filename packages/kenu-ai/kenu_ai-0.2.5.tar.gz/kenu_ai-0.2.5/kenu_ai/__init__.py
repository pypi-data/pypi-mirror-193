from googletrans import Translator
import requests
from kufpy import Kufpy

def chat(value):
    kuf = Kufpy()
    if("sahibin kim" in value.lower()):
        print("kenan")
        return "Sahibim namıdeğer r4isy."
    else:
        translator = Translator()
        t = translator.translate(value, dest="en")
        response = requests.get("http://api.brainshop.ai/get?bid=153868&key=rcKonOgrUFmn5usX&uid=1&msg=" + t.text)
        veri = response.text.split(':"')[-1].split('"}')[0]
        translated = translator.translate(veri, dest="tr")
        if("zackybot" in translated.text.lower()):
            new_string = "Adım, kenu-ai. r4isy tarafından yazıldım."
            return new_string
        elif("acobot.ai" in translated.text.lower() or "acobot" in translated.text.lower()):
            new_string = "Adım kenu-ai. r4isy tarafından yazıldım."
            return new_string
        elif(kuf.contains_profanity(translated.text)):
            return "Konuyu değiştirsek iyi olur\nhttps://tenor.com/view/heumrage-rage-kanser-vechiron-vechiron-rage-gif-21449669"
        else:
            return translated.text