from fastapi import FastAPI
import uvicorn
import json
from item import Item
from fence_item import Item1
app = FastAPI()

@app.get("/test")
def test():
    return {"msg":"hi from test"}

@app.get("/test/{name}")
def server_name(name):
    return {"msg":name}

@app.post("/caesar")
def create(item:Item):
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

