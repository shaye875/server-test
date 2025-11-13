from fastapi import FastAPI
import uvicorn
import json
from item import Item
from fence_item import Item1
app = FastAPI()
total_requesta_recevied_post = 0
total_requesta_recevied_get = 0
avg_handing_time= 0
@app.get("/test")
def test():
    global total_requesta_recevied_get
    dict = {"url":"/test","method":"POST"}
    total_requesta_recevied_get += 1
    dict["stats"] = {"total_requesta_recevied":total_requesta_recevied_get}
    dict = json.dumps(dict)
    with open('endpoints_data.json','a') as f:
        f.write(dict)
    return {"msg":"hi from test"}

@app.get("/test/{name}")
def server_name(name):
    global total_requesta_recevied_get
    dict = {"url": "/test/{name}", "method": "GET"}
    total_requesta_recevied_get += 1
    dict["stats"] = {"total_requesta_recevied": total_requesta_recevied_get}
    dict = json.dumps(dict)
    with open('endpoints_data.json', 'a') as f:
        f.write(dict)
    return {"msg":name}

@app.post("/caesar")
def create(item:Item):
    global total_requesta_recevied_post
    dict = {"url": "/caesar", "method": "GET"}
    total_requesta_recevied_post += 1
    dict["stats"] = {"total_requesta_recevied": total_requesta_recevied_post}
    dict = json.dumps(dict)
    with open('endpoints_data.json', 'a') as f:
        f.write(dict)
    str = ""
    laters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    if item.mode == "encrypt":
        for s in item.text:
            if laters.index(s)+item.offset < len(laters):
                str+=laters[(laters.index(s)+item.offset)]
            else:
                str+=laters[item.offset-((len(laters))-(laters.index(s)+1))-1]
    elif item.mode == "decrypt":
        for s in item.text:
                str+=laters[(laters.index(s))-item.offset]
    return {"encrypted_text":str}

@app.get("/fence/encrypt")
def get_fence(text:str):
    global total_requesta_recevied_get
    dict = {"url": "/caesar", "method": "GET"}
    total_requesta_recevied_get += 1
    dict["stats"] = {"total_requesta_recevied": total_requesta_recevied_get}
    dict = json.dumps(dict)
    with open('endpoints_data.json', 'a') as f:
        f.write(dict)
    str = ""
    str1 = ""
    for i in range(len(text)):
      if text[i] != " ":
        if i % 2 == 0:
            str+=text[i]
        else:
            str1+=text[i]
    return {"encrypted_text":str+str1}

@app.post("/fence/decrypt")
def post_fence(item:Item1):
    global total_requesta_recevied_post
    dict = {"url": "/caesar", "method": "GET"}
    total_requesta_recevied_post += 1
    dict["stats"] = {"total_requesta_recevied": total_requesta_recevied_post}
    dict = json.dumps(dict)
    with open('endpoints_data.json', 'a') as f:
        f.write(dict)
    str = ""
    if len(item.text) % 2 == 0:
        str1 = item.text[:len(item.text)//2]
        str2 = item.text[len(item.text)//2:]
        for i in range(len(str1)):
            str += str1[i]
            str += str2[i]
    else:
        str1 = item.text[:len(item.text)//2+1]
        str2 = item.text[len(item.text)//2+1:]
        for i in range(len(str1)):
            str += str1[i]
            try:
                str += str2[i]
            except:
                pass
    return {"decrypted":str}

