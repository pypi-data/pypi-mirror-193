import datetime
import json
import os
import time
from typing import Union

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
def read_root():
    html = """
    <html>
        <head>
            <title> Thirteen GPU dashboard </title>
        </head>
        <body>
            {}
        </body>
    </html>
    """
    
    scheduler_off = False
    
    available_job_slots = open("available_job_slots.txt").read().strip()
    
    # get last update time of `status.json`
    last_update = os.path.getmtime("status.json")
    last_update = datetime.datetime.fromtimestamp(last_update) + datetime.timedelta(hours=9)
    
    # if `last_update` not updated for 1 hour, set it to `None`
    if datetime.datetime.now() + datetime.timedelta(hours=9) - last_update > datetime.timedelta(minutes=5):
        scheduler_off = True
    
    last_update = last_update.strftime("%Y-%m-%d %H:%M:%S")
    
    status = json.load(open("status.json"))
    text = "<a href='http://54.180.160.135:2016/'>GPU Status</a> <br>"
    
    if scheduler_off:
        text += f"<h3> Scheduler is off, Last Update: {last_update} </h3>"
    else:
        text += f"<h3> Last Update: {last_update} </h3>"
    
    text += f"<h3> Job Slots: {available_job_slots} </h3>"
    
    projects = []
    for project_name, project_status in status.items():
        user = project_status["user"]
        submit_at = project_status["submit_at"]
        
        status_info = [(status_name, status_count) for status_name, status_count in project_status["status"].items()]
        
        projects.append((project_name, user, submit_at, status_info))
        
    projects = sorted(projects, key=lambda x: x[2], reverse=True)
    
    for project_name, user, submit_at, status_info in projects:
        text += f"""
            <h2> Project: {project_name} </h2>
        """
        text += f"user: {user} / submitted at: {submit_at} <br>"
        
        for status_name, status_count in status_info:
            text += f" {status_name}: {status_count} "
    
    if len(projects) == 0:
        text += "No projects"
        
            
    contents = html.format(text)
    
    # return HTML Rendered Page
    return HTMLResponse(content=contents, status_code=200)