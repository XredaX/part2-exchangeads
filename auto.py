from telethon import TelegramClient, events
from database import user
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import ChannelParticipantsAdmins
import base64
import random
import  time
 
api_id = '14164136'
api_hash = '95a43ca71d9576d27ed474fffa164517'
client = TelegramClient('all', api_id, api_hash)
@client.on(events.NewMessage)
async def handlmsg(event):
    try:
        chat_id = event.chat_id
        if chat_id == -1001654861712:
            msg = event.raw_text
            if msg == "Start":
                try:
                    admins = []
                    post, num = user.findpost1(collection="Post")
                    for i in range(int(num)):
                        xid = post[i]["ID"]
                        ow = post[i]["Owenr"]
                        try:
                            async for user2 in client.iter_participants(int(xid), filter=ChannelParticipantsAdmins):
                                admins.append(user2.username)
                            if "growchannels" in admins:
                                admins = []
                                user.edit1(collection = "Post", IDO = xid, Status = "True")
                        except :
                            user.edit1(collection = "Post", IDO = xid, Status = "False")
                    a = 0
                    post, num = user.findallpost(collection="Post") 
                    if int(num)%2 != 0:
                        user.edit2(collection = "Post", Owenr = "CryptoLogia", Status = "False")
                    else:
                        user.edit2(collection = "Post", Owenr = "CryptoLogia", Status = "True")
                    post, num = user.findallpost(collection="Post")
                    num1 = int((int(num))/2)
                    group = []
                    group1 = []
                    group2 = []
                    for i in range(int(num)):
                        group.append(post[i]["Owenr"])
                
                    while len(group)>0:
                        t1 = random.choice(group)
                        group1.append(t1)
                        group.remove(t1)
                        t2 = random.choice(group)
                        group2.append(t2)
                        group.remove(t2)
                
                    while a < num1:
                        ow1 = random.choice(group1)
                        ow2 = random.choice(group2)
                        post = user.findpostbyow(collection="Post", new=ow1) 
                        for p in post:
                            ads = p["Ads"]
                            xid = p["ID"]
                            Image = p["Image"] 
                        decodeit = open('new.jpg', 'wb')
                        decodeit.write(base64.b64decode((Image)))
                        decodeit.close()
                        post = user.findpostbyow(collection="Post", new=ow2) 
                        for p in post:
                            ads1 = p["Ads"]
                            xid1 = p["ID"]
                            Image1 = p["Image"] 
                        decodeit1 = open('new1.jpg', 'wb')
                        decodeit1.write(base64.b64decode((Image1)))
                        decodeit1.close()
                        await client.send_file(int(xid), "new1.jpg", caption=ads1)
                        await client.send_message(int(xid), "تبادل إعلاني ☝️☝️\n\n القناة غير مسؤولة عن محتوى القنوات التي يتم التبادل معها, نأسف لهذا الإزعاج.", link_preview=False)                
                        my_channel = int(xid)
                        offset_id = 0
                        limit = 2
                        all_messages = []
                        total_messages = 0
                        total_count_limit = 0
                        history = await client(GetHistoryRequest(
                                    peer=my_channel,
                                    offset_id=offset_id,
                                    offset_date=None,
                                    add_offset=0,
                                    limit=limit,
                                    max_id=0,
                                    min_id=0,
                                    hash=0
                                ))
                        if not history.messages:
                            for a in range(1):
                                break
                        messages = history.messages
                        for message in messages:
                            all_messages.append(message.to_dict())
                        offset_id = messages[len(messages) - 1].id
                        total_messages = len(all_messages)
                        if total_count_limit != 0 and total_messages >= total_count_limit:
                            for a in range(1):
                                break
                        for msg in all_messages:
                            user.insertpost(collection = "PostDel", IDO = int(xid), IDP = int(msg["id"]))                   
                        await client.send_file(int(xid1), "new.jpg", caption=ads)
                        await client.send_message(int(xid1), "تبادل إعلاني ☝️☝️\n\n القناة غير مسؤولة عن محتوى القنوات التي يتم التبادل معها, نأسف لهذا الإزعاج.", link_preview=False)
                        my_channel = int(xid1)
                        offset_id = 0
                        limit = 2
                        all_messages = []
                        total_messages = 0
                        total_count_limit = 0
                        history = await client(GetHistoryRequest(
                                    peer=my_channel,
                                    offset_id=offset_id,
                                    offset_date=None,
                                    add_offset=0,
                                    limit=limit,
                                    max_id=0,
                                    min_id=0,
                                    hash=0
                                ))
                        if not history.messages:
                            for a in range(1):
                                break
                        messages = history.messages
                        for message in messages:
                            all_messages.append(message.to_dict())
                        offset_id = messages[len(messages) - 1].id
                        total_messages = len(all_messages)
                        if total_count_limit != 0 and total_messages >= total_count_limit:
                            for a in range(1):
                                break
                        for msg in all_messages:
                            user.insertpost(collection = "PostDel", IDO = int(xid1), IDP = int(msg["id"]))        
                        group1.remove(ow1)
                        group2.remove(ow2)
                        a +=1
                    time.sleep(550)
                    data, number = user.countdelpost(collection="PostDel")
                    for i in range(int(number)):
                        id_group = data[i]["ID"]
                        id_message = data[i]["IDP"]
                        try:
                            await client.delete_messages(entity=int(id_group), message_ids=int(id_message))
                        except:
                            pass
                    user.deletepost(collection="PostDel", IDO = id_group, IDP = id_message)
                except:
                    pass
    except:
        pass

client.start()
client.run_until_disconnected()



