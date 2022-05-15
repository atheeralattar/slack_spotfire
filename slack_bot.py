mport slack
import pyautogui
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('C:/Users/aalattar/Desktop/playground/slack_spotfire') / '.env'
load_dotenv(dotenv_path=env_path)
print(env_path)
client = slack.WebClient(token = os.environ['SLACK_TOKEN'])
file_path = 'C:\Temp\spotfire_screenshot.png' 
client.files_upload(channels = "#observations", file =file_path, initial_comment = comment)


