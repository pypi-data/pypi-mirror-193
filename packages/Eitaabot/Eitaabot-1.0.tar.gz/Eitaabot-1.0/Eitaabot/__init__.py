CYAN = '\033[96m'
YELLOW = '\033[93m'
WHITE = '\033[97m'
GREEN = '\033[92m'
BLUE = '\033[94m'


version = "1.0"
print(WHITE+" [+] "+CYAN+"TyroBot "+BLUE+"library"+CYAN+" version "+GREEN+version+WHITE+"\n\n [+] "+CYAN+"TytoBOt "+BLUE+"Copyright"+CYAN+" (C) 2023 "+GREEN+"mrsalar\n")
print(WHITE+" [+] "+CYAN+"chanel"+BLUE+" Eitaa "+CYAN+":  "+GREEN+"@Tyro_code"+YELLOW+"\n   [--------------- "+BLUE+"TYRO BOT"+YELLOW+" ---------------]")

import requests
from bs4 import BeautifulSoup
from os.path import isfile

class Bot(object):
    def __init__(self, token):
        self.token = token
        
    
    def get_my_info(self):
        r = requests.get(f"https://eitaayar.ir/api/{self.token}/getMe")
        return r.json()["result"]
    
    @staticmethod
    def get_info(channel_id):
        r = requests.get(f"https://eitaa.com/{channel_id}")
        soup = BeautifulSoup(r.text, 'html.parser')
                
        channel_name = soup.find('div', attrs = {'class':'tgme_page_title'}).text
            
        channel_image_url = "https://eitaa.com" + soup.find('img', attrs = {'class':'tgme_page_photo_image'})['src'] 

        users_count = (str(soup.find('div', attrs = {'style':'display: block;text-align: center;font-weight: bold'}).text).split(' '))[0]
        desc = soup.find('div', attrs = {'class':'text-center'}).text 

        result = {
            'name' : " ".join(channel_name.split()),
            'image_url' : channel_image_url,
            'users' : users_count,
            'desc' : desc,
        }
        return result
        
    def send_message(self, chat_id, text, pin=False, view_to_delete=-1,
                    disable_notification=False, reply_to_message_id=None):
        r = requests.post(
            f"https://eitaayar.ir/api/{self.token}/sendMessage",
            data={
                'chat_id': chat_id,
                'text': text,
                'pin': int(pin),
                'viewCountForDelete': view_to_delete,
                'disable_notification': int(disable_notification),
                'reply_to_message_id' : reply_to_message_id if reply_to_message_id != None else '',
            }
        )
        print(type(r.json()))
        return r.json()

    def send_file(self, chat_id, caption, file, pin=False, view_to_delete=-1,
                disable_notification=False, reply_to_message_id=None):
        if not isfile(file):
            raise Exception(f"File `{file}` not found")

        r = requests.post(
            f"https://eitaayar.ir/api/{self.token}/sendFile",
            data={
                'chat_id': chat_id,
                'caption': caption,
                'pin': int(pin),
                'viewCountForDelete': view_to_delete,
                'disable_notification': int(disable_notification),
                'reply_to_message_id' : reply_to_message_id if reply_to_message_id != None else '',
            },
            files={
                'file': open(file, 'rb'),
            }
        )
        return r.json()
    
    @staticmethod
    def get_trends():
        result = {
            "last_12_hours": [],
            "last_24_hours": [],
            "last_7_days": [],
            "last_30_days": [],
        }

        r = requests.get(
            f"https://trends.eitaa.com"
        )

        soup = BeautifulSoup(r.text, 'html.parser')

        last_12_hours = soup.find("div",{"class":"col-xl-3 col-lg-6 col-md-6 col-sm-12 animateIn animated zoomInLeft"})
        last_24_hours = soup.find("div",{"class":"col-xl-3 col-lg-6 col-md-6 col-sm-12 animateIn animated zoomInDown"})
        last_7_days = soup.find("div",{"class":"col-xl-3 col-lg-6 col-md-6 col-sm-12 animateIn animated zoomInRight"})
        last_30_days = soup.find("div",{"col-xl-3 col-lg-6 col-md-6 col-sm-12 animateIn animated zoomInUp"})


        for trend in last_12_hours.find_all("div",{"class":"row item"}):
            trend_name = trend.find("div",{"class":"col-9 text-right hashtag"})
            trend_count = trend.find("div",{"class":"col-3 text-left number"})

            result["last_12_hours"].append({
                "name": trend_name.text,
                "count": trend_count.text,
            })

        for trend in last_24_hours.find_all("div",{"class":"row item"}):
            trend_name = trend.find("div",{"class":"col-9 text-right hashtag"})
            trend_count = trend.find("div",{"class":"col-3 text-left number"})

            result["last_24_hours"].append({
                "name": trend_name.text,
                "count": trend_count.text,
            })
        
        for trend in last_7_days.find_all("div",{"class":"row item"}):
            trend_name = trend.find("div",{"class":"col-9 text-right hashtag"})
            trend_count = trend.find("div",{"class":"col-3 text-left number"})

            result["last_7_days"].append({
                "name": trend_name.text,
                "count": trend_count.text,
            })
        
        for trend in last_30_days.find_all("div",{"class":"row item"}):
            trend_name = trend.find("div",{"class":"col-9 text-right hashtag"})
            trend_count = trend.find("div",{"class":"col-3 text-left number"})

            result["last_30_days"].append({
                "name": trend_name.text,
                "count": trend_count.text,
            })
        return result
