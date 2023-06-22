
from voice import *
import datetime

def task(user):
    if 'news' in user:
        from News_update import news
        speak('coming up today headlines')
        news('en')

    elif 'weather today' in user or 'temperature' in user or 'weather' in user:
        from Weather import weather
        weather()

    elif 'time' in user:
        tim = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + tim)

  # Pc files open commend ################################################################################################

    elif "open notepad" in user or 'notepad open ' in user:
        npath = "C:\\Windows\\notepad.exe"
        speak('sure, just wait,  opening notepad')
        os.startfile(npath)

    elif "open pycharm" in user:
        apath = "D:\\PyCharm Community Edition 2021.1.2\\bin\\PyCharm.exe"
        speak('sure, just wait, opening PyCharm')
        os.startfile(apath)

    elif "open chrome" in user or "chrome open" in user:
        cpath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        speak('sure, just wait,  opening chrome')
        os.startfile(cpath)

    elif "open file" in user or "file open" in user:
        fpath = "C:\\Users\\subha\\OneDrive\\Desktop"
        speak('sure, just wait, opening files.')
        os.startfile(fpath)

# task("open notepad")