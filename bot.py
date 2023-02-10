import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5552531861:AAFIAB4cR8-OZMuQxR3Wi4IgBi5mTX_gfIs")

API_ID = int(os.environ.get("API_ID", "23560088"))

API_HASH = os.environ.get("API_HASH", "999c01704d5c417749a98f4b8785fe88")

STRING = os.environ.get("STRING", "BQCjrxOQ0DdKwD6qnk6M6kTOmBxo8rZJC5uHQ0p9maTOXhclOV45ZgfjPicK-iIRN6_iRC5MqAcm_reHVXRqITQdDFJ_bjK_diho9DlYq3MyGjJw4W3lqUW40pY0FruPxb2OWKGP_OclkAesTmhBn6l9zvTQBWzXJpHVQnpKsaEJma1jvFxjO4TaCfurRX7xD9t1GH7bDtSkUp-B_grARBhdpbsJIyLW25HnueErS55wyECRryxP7PLIS-wz1574Op7hWO2S72YPKGkMwhO7GaaY3UklO-6vL2lkMy-xwjxYy6mNZguhXbCdiQtArWvfAj85rxlqDIiWMfN07EMCTDnHbyeHVAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
