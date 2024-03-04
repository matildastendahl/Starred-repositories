from typing import Union
from fastapi import FastAPI, Depends, HTTPException, Response
import os
import requests
from urllib.parse import parse_qs

app = FastAPI()

ID = "78b56c56898a8692e345"
SECRET = "dd53a4d74f81012fe8259b56806ad01af07bdac7"
REDIRECT = "http://127.0.0.1:8000/callback"

authentication = f"https://github.com/login/oauth/authorize?client_id={ID}&redirect_uri={REDIRECT}&scope=repo"

count = 0

@app.get("/")
async def login():
    html = os.path.join("templates", "index1.html")
    with open(html, "r") as file:
        html = file.read()
    
    html = html.replace("{authentication}", authentication)
    
    return Response(content=html, media_type="text/html")


@app.get("/callback")
async def callback(code : str):
    access_url = f"https://github.com/login/oauth/access_token?client_id={ID}&client_secret={SECRET}&code={code}"
    request = requests.post(access_url)

    data = parse_qs(request.content.decode())
    access_token_list = data.get("access_token", [])
    access_token = access_token_list[0] if access_token_list else None

    starred = fetch_starred(access_token)
    count = len(starred)

    return Response(content = render_html(access_token, starred["count"], starred["repositories"]), media_type="text/html")


def fetch_starred(access_token: str):
    headers = {
        "Authorization": f"Bearer {access_token}",  
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get("https://api.github.com/user/starred", headers = headers)
    
    starred = []
    for i in response.json():
        if not i["private"]:
            starred_data = {
                "name": i["name"], 
                "description": i["description"],
                "url": i["html_url"],
                "license": i.get("license", {}).get("name"),  
                "topics": i["topics"] 
            }
            starred.append(starred_data) 

    return {"count": len(starred), "repositories": starred}

def render_html(access_token: str, count: int, repositories: list):
    starred_html = os.path.join("templates", "starred.html")
    with open(starred_html, "r") as file:
        html = file.read()

    html = html.replace("{access_token}", access_token)
    html = html.replace("{count}", str(count))

    list = ""
    for i in repositories:
        i_item = f"""
            <div class="repository">
                <h3>{i['name']}</h3>
                <p>{i['description']}</p>
                <p><a href="{i['url']}">{i['url']}</a></p>
                <p>License: {i['license']}</p>
                <p>Topics: {', '.join(i['topics'])}</p>
            </div>
        """
        list += i_item

    html = html.replace("{repositories}", list)

    return html