from GoogleNews import GoogleNews
from voice import speak

def news(lan):
    gnews = GoogleNews()
    # gnews = GoogleNews()

    gnews.setlang(lan)
    gnews.search('India')
    # gnews.getpage(1)

    # rs2 = gnews.result()
    rs = gnews.gettext()
    # print(rs)
    speak(rs)
    # say = takecommand()
    # if 'stop' in say:
    #     speak('ohk, stop news')
    #     pass

news("en")