from fastapi import FastAPI

app = FastAPI()#อินสแตนซ์

@app.get('/') #กำหนดรับเส้นทาง

def index():# ฟังชันกำหนด
    #return 'hello Luck'
    return {'data':{'name': 'Sutanat'}}#กำหนดรูปแบบ JSON

@app.get('/about')

def about():
    return {'page' : {'this is about'}}

    