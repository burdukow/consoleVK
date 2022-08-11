import requests
import os

ver = str(5.131) # Версия VKAPI.

def auth(token):
    
    authentication = "https://api.vk.com/method/users.get?access_token=",token,"&v=",ver # Ссылка на метод users.get, позволяющий определить валидность токена.
    try: 
        response  = requests.get(''.join(authentication)).json() # Запрос к VKAPI и сохранение ответа от сервера.
        response = response['response'][0]
    except Exception:
        print("Что-то пошло не так, возможно, токен неверный или произошёл сбой.") # В случае ошибки просто закрывается.
        if os.path.isfile("token.txt"):
            print("Удалить файл с токеном? Возможно, это исправит ситуацию. y/N")
            if input() == "y":
                os.remove("token.txt")
                print("Файл удалён")
        exit()
    global personalid
    personalid = response['id']
    print('Добро пожаловать,',response["first_name"],response["last_name"]+'!') # Приветствие, в случае успешного входа


def checkupd(curver):
    versionlink = "https://raw.githubusercontent.com/burdukow/consoleVK/master/version.txt"
    getlink = requests.get(versionlink).text
    if getlink != curver:
        print("Версии не совпадают, установите новую с github.\n Актуальная версия: ", getlink,"Ваша версия: ", curver)
    else: print("Версии совпадают.")


def messages(token, filter):
    msgget = "https://api.vk.com/method/messages.getConversations?access_token=",token,"&count=10&filter=",filter,"&v=",ver
    response  = requests.get(''.join(msgget)).json()['response']["items"] # Запрос к VKAPI и сохранение ответа от сервера.
    count = requests.get(''.join(msgget)).json()['response']['count']
    if count == 0:
        print("\nСообщений нет")
    for i in range(len(response)):
        msgtext = response[i]["last_message"]["text"]
        if msgtext == "":
            msgtext = "Вложение"
        convtype = response[i]["conversation"]["peer"]["type"]
        lastmsgid = response[i]["last_message"]["from_id"]
        if convtype == "chat":
            name = '"'+response[i]["conversation"]["chat_settings"]["title"]+'"\n └───'
            if lastmsgid == personalid:
                msg = "Вы: "+msgtext
            else:
                userget = "https://api.vk.com/method/users.get?access_token=",token,'&user_ids=',lastmsgid,"&v=",ver
                req = requests.get(''.join(map(str,userget))).json()
                msg = msgtext
                if len(req['response'])>0:
                    req = req['response'][0]
                    msg = req["first_name"]+" "+req["last_name"]+": "+msgtext
        elif convtype == "user":
            userid = response[i]["conversation"]["peer"]["id"]
            userget = "https://api.vk.com/method/users.get?access_token=",token,'&user_ids=',userid,"&v=",ver
            req = requests.get(''.join(map(str,userget))).json()
            req = req['response'][0]
            name = req["first_name"]+" "+req["last_name"]+'\n └─── '
            if lastmsgid == personalid:
                msg = "Вы: "+msgtext
            else:
                msg = msgtext
        elif convtype == "group":
            groupid = response[i]["conversation"]["peer"]["local_id"]
            groupget = "https://api.vk.com/method/groups.getById?access_token=",token,"&group_id=",groupid,"&v=",ver
            name = requests.get(''.join(map(str,groupget))).json()
            name = name['response'][0]["name"]+'\n └───'
            if lastmsgid == personalid:
                msg = "Вы: "+msgtext
            else:
                msg = " "+msgtext
        print("\n"+str(name)+" "+str(msg.split('\n',1)[0]))
    

