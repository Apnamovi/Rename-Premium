import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5552531861:AAFIAB4cR8-OZMuQxR3Wi4IgBi5mTX_gfIs")

API_ID = int(os.environ.get("API_ID", "23560088"))

API_HASH = os.environ.get("API_HASH", "999c01704d5c417749a98f4b8785fe88")

STRING = os.environ.get("STRING", "BQFnf5gAcrlqjnIKKGMx5Z6TUujM6axfRyIvEZwB4nJtA9NJ8cKONavzMj6GsNwVwZk8qyIaSz1-ghrfaVzBNwFnpsre-aJBmrC2rgvCXvgk6cSZ-LCu0wE_V1DtmDq7CC4_d3dZM56gjsI5RhKREjya73fBHpbY5mlNOq3xYZ9K2r5b9WaA34QL4XZa2s-z3YAHjM6qhfQCByNQHtx7KCkO-JYjjmva3r9k13fRdVq2rm0ITbMjIdAcFBtTTyOk4iEJPK7suTeB5bmWejs7rdbqTD5y9bgrH8vFh6ETP7lH_HPmiPPO69t53vlHs5LLL-ri94MMQA8EhwynZ7wT6flnQxiQRAAAAABvJ4dUAA")


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
