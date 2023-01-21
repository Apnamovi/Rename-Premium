import os
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.progress import humanbytes

from helper.database import  insert ,find_one,used_limit,usertype,uploadlimit,addpredata
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import add_date ,check_expi
CHANNEL = os.environ.get('CHANNEL',"anumitultrabots")
import datetime
from datetime import date as date_
STRING = os.environ.get("STRING","BQFnf5gAcrlqjnIKKGMx5Z6TUujM6axfRyIvEZwB4nJtA9NJ8cKONavzMj6GsNwVwZk8qyIaSz1-ghrfaVzBNwFnpsre-aJBmrC2rgvCXvgk6cSZ-LCu0wE_V1DtmDq7CC4_d3dZM56gjsI5RhKREjya73fBHpbY5mlNOq3xYZ9K2r5b9WaA34QL4XZa2s-z3YAHjM6qhfQCByNQHtx7KCkO-JYjjmva3r9k13fRdVq2rm0ITbMjIdAcFBtTTyOk4iEJPK7suTeB5bmWejs7rdbqTD5y9bgrH8vFh6ETP7lH_HPmiPPO69t53vlHs5LLL-ri94MMQA8EhwynZ7wT6flnQxiQRAAAAABvJ4dUAA")
log_channel = int(os.environ.get("LOG_CHANNEL","-1001847011203"))

#Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
	wish = "Good morning."
elif 12 <= currentTime.hour < 12:
	wish = 'Good afternoon.'
else:
	wish = 'Good evening.'

#-------------------------------

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	old = insert(int(message.chat.id))
	try:
	    id = message.text.split(' ')[1]
	except:
	    await message.reply_text(text =f"""
	Hello {wish} {message.from_user.first_name }
	__I am file renamer bot, Please sent any telegram 
	**Document Or Video** and enter new filename to rename it__
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👼 𝙳𝙴𝚅𝚂 👼", url='https://t.me/ajak4405')
           ],[
           InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/anumitultrabots'),
           InlineKeyboardButton('🍂 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url='https://t.me/anumitultrabots')
           ],[
           InlineKeyboardButton('🍃 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
           InlineKeyboardButton('ℹ️ Subscribe 🧐', url='https://youtube.com/@anumitultrabots')
           ]]
          )
       )
	    return
	if id:
	    if old == True:
	        try:
	            await client.send_message(id,"Your Frind Alredy Using Our Bot")
	            await message.reply_text(text =f"""
	Hello {wish} {message.from_user.first_name }
	__I am file renamer bot, Please sent any telegram 
	**Document Or Video** and enter new filename to rename it__
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👼 𝙳𝙴𝚅𝚂 👼", url='https://t.me/ajak4405')
           ],[
           InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/anumitultrabots'),
           InlineKeyboardButton('🍂 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url='https://t.me/anumitultrabots')
           ],[
           InlineKeyboardButton('🍃 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
           InlineKeyboardButton('ℹ️ Subscribe 🧐', url='https://youtube.com/@anumitultrabots')
           ]]
          )
       )
	        except:
	             return
	    else:
	         await client.send_message(id,"Congrats! You Won 1GB Upload limit")
	         _user_= find_one(int(id))
	         limit = _user_["uploadlimit"]
	         new_limit = limit + 107741824
	         uploadlimit(int(id),new_limit)
	         await message.reply_text(text =f"""
	Hello {wish} {message.from_user.first_name }
	__I am file renamer bot, Please sent any telegram 
	**Document Or Video** and enter new filename to rename it__
	""",reply_to_message_id = message.id ,  
	reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👼 𝙳𝙴𝚅𝚂 👼", url='https://t.me/ajak4405')
           ],[
           InlineKeyboardButton('📢 𝚄𝙿𝙳𝙰𝚃𝙴𝚂', url='https://t.me/anumitultrabots'),
           InlineKeyboardButton('🍂 𝚂𝚄𝙿𝙿𝙾𝚁𝚃', url='https://t.me/anumitultrabots')
           ],[
           InlineKeyboardButton('🍃 𝙰𝙱𝙾𝚄𝚃', callback_data='about'),
           InlineKeyboardButton('ℹ️ Subscribe 🧐', url='https://youtube.com/@anumitultrabots')
           ]]
          )
       )
	         



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
       	try:
       		await client.get_chat_member(update_channel, user_id)
       	except UserNotParticipant:
       		await message.reply_text("**__You are not subscribed my channel__** ",
       		reply_to_message_id = message.id,
       		reply_markup = InlineKeyboardMarkup(
       		[ [ InlineKeyboardButton("Support 🇮🇳" ,url=f"https://t.me/{update_channel}") ]   ]))
       		return
       
       
       user_deta = find_one(user_id)
       try:
       	used_date = user_deta["date"]
       	buy_date= user_deta["prexdate"]
       	daily = user_deta["daily"]
       except:
           await message.reply_text("database has been Cleared click on /start")
           return
           
           
       c_time = time.time()
       
       if buy_date==None:
           LIMIT = 350
       else:
           LIMIT = 50
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:       	    
       	await message.reply_text(f"```Sorry Dude I am not only for YOU \n Flood control is active so please wait for {ltime}```",reply_to_message_id = message.id)
       else:
       		# Forward a single message
       		await client.forward_messages(log_channel, message.from_user.id, message.id)
       		await client.send_message(log_channel,f"User Id :- {user_id}")       		
       		media = await client.get_messages(message.chat.id,message.id)
       		file = media.document or media.video or media.audio 
       		dcid = FileId.decode(file.file_id).dc_id
       		filename = file.file_name
       		value = 2147483648
       		used_ = find_one(message.from_user.id)
       		used = used_["used_limit"]
       		limit = used_["uploadlimit"]
       		expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
       		if expi != 0:
       			today = date_.today()
       			pattern = '%Y-%m-%d'
       			epcho = int(time.mktime(time.strptime(str(today), pattern)))
       			daily_(message.from_user.id,epcho)
       			used_limit(message.from_user.id,0)			     		
       		remain = limit- used
       		if remain < int(file.file_size):
       		    await message.reply_text(f"Sorry! I can't upload files that are larger than {humanbytes(limit)}. File size detected {humanbytes(file.file_size)}\nUsed Daly Limit {humanbytes(used)} If U Want to Rename Large File Upgrade Your Plan ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upgrade 💰💳",callback_data = "upgrade") ]]))
       		    return
       		if value < file.file_size:
       		    if STRING:
       		        if buy_date==None:
       		            await message.reply_text(f" You Can't Upload More Then {humanbytes(limit)} Used Daly Limit {humanbytes(used)} ",reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Upgrade 💰💳",callback_data = "upgrade") ]]))
       		            return
       		        pre_check = check_expi(buy_date)
       		        if pre_check == True:
       		            await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {humanize.naturalsize(file.file_size)}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))
       		        else:
       		            await message.reply_text(f'Your Plane Expired On {buy_date}',quote=True)
       		    else:
       		          	await message.reply_text("Can't upload files bigger than 2GB ")
       		          	return
       		else:
       		    filesize = humanize.naturalsize(file.file_size)
       		    fileid = file.file_id
       		    await message.reply_text(f"""__What do you want me to do with this file?__\n**File Name** :- {filename}\n**File Size** :- {filesize}\n**Dc ID** :- {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
       		[[ InlineKeyboardButton("📝 Rename",callback_data = "rename"),
       		InlineKeyboardButton("✖️ Cancel",callback_data = "cancel")  ]]))