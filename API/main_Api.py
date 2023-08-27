from fastapi import FastAPI, Request, Response
import uvicorn
import os
from dotenv import load_dotenv
from chat_bot import chat
import ast


# setup FastAPI app
app = FastAPI()
load_dotenv()

# get environment variables
VERIFY_TOKEN = os.getenv('FB_VERIFY_TOKEN')
@app.get('/')
def get_func():
    return 'all infos geted'

@app.post('/webhook')
def init_messenger(request: Request):
    fb_token =request.headers.get('token')
    
    message=request.query_params["message"]
    
    
    if fb_token == VERIFY_TOKEN:
        result=chat(message)
        return result
    return "failed to verify token"

if __name__ == "__main__":
     uvicorn.run("main_Api:app",  reload=True)