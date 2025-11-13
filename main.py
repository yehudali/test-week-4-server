from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from Encryption_Caesar import  encrypt, decrypt
from Encrypt_Fence import encrypt, decrypt

class Text_and_Mod(BaseModel):
    text:str
    offset:int
    mode:str

app = FastAPI()

@app.get("/test")
def read_test():
    return  {"msg": "hi from test"}

@app.get("/test/{name_user}")
def endpoint_test(name_user : str):
    with open("names.txt", "a")as n:
        n.write(name_user+"\n")
        return { "msg": f"saved: {name_user}"}

@app.post("/caesar")
def Caesar_cipher_endpoint(input :Text_and_Mod):
    if input.mode is "encrypt":
        x=encrypt(input.text,input.offset)
        { "encrypted_text": x }

    if input.mode is "decrypt":
        x=decrypt(input.text,input.offset)
        return { "decrypted_text": x }




@app.get("/fence/encrypt")
def Fence_cipher_endpoints_1(text: str):
    x=encrypt(text)
    return { "encrypted_text":x}

@app.post("/fence/decrypt/{text: str}")
def Fence_cipher_endpoints_2(text: int):
    x=decrypt(text)
    return { "decrypted": x }

    








if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)



