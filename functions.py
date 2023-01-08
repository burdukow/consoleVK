import requests
import os

ver = str(5.131) # Версия VKAPI.

def auth(token):
    if token == "removed":
        exit()
    else:
        authentication = "https://api.vk.com/method/messages.getConversations?access_token=",token,"&v=",ver # Ссылка на метод users.get, позволяющий определить валидность токена.
        try: 
            response  = requests.get(''.join(authentication)).json() # Запрос к VKAPI и сохранение ответа от сервера.
            if response['response']:
                pass
            elif response['error']['error_code'] == 15:
                        print("\033[37m\033[41mОшибка 15. Доступ к методу запрещён.\033[0m")
                        print("\033[0mПровертье разрешения токена, возможно, токену запрещён доступ к сообщениям.")
                        exit()
            elif response['error']['error_code'] == 5:
                        print("\033[37m\033[41mОшибка 5. Неудачная авторизация, токен невалидный.\033[0m")
                        print("\033[0mПроверьте правильность токена.")
                        exit()
            elif response['error']:
                        print("\033[37m\033[41mНеизвестная ошибка.\033[0m")
                        print("\033[0mВозможные варианты ошибки:\n    Проблема в токене;\n    Проблема в коде;\n    Проблема на стороне ВК.")
                        exit()
        except Exception:
            print("Что-то пошло не так, возможно, токен неверный или произошёл сбой.") # В случае ошибки просто закрывается.
            if os.path.isfile("token.txt"):
                print("Удалить файл с токеном? Возможно, это исправит ситуацию. y/N")
                if input() == "y":
                    os.remove("token.txt")
                    print("Файл удалён")
            exit()
        else: 
            userinfo = requests.get(''.join("https://api.vk.com/method/users.get?access_token="+token+"&v="+ver)).json()['response'][0]
            first_name, last_name = userinfo["first_name"],userinfo["last_name"]
            global personalid
            personalid = userinfo['id']
            print('Добро пожаловать,',first_name,last_name+'!') # Приветствие, в случае успешного входа


def checkupd():
    curver = open("version.txt", "r")
    curver = curver.read()
    versionlink = "https://raw.githubusercontent.com/burdukow/consoleVK/master/version.txt"
    getlink = requests.get(versionlink).text

    try:
        open("dev.txt", "r")
    except FileNotFoundError:
        if getlink != curver:
            print("Версии не совпадают, установите новую с github.\n Актуальная версия: ", getlink,"Ваша версия: ", curver)
            return "upd"
        else: 
            return 0

def rmtoken(token):
    try:
        os.remove("token.txt")
    except Exception:
        pass
    print("Токен удалён")
    token = "removed"
    auth(token)

def messages(offset, token, filter):
    while not offset.isdigit():
        offset = input("\nСмещение (0 по стандарту): ")
    msgget = "https://api.vk.com/method/messages.getConversations?access_token=",token,"&offset=",offset,"&count=10&filter=",filter,"&v=",ver
    response  = requests.get(''.join(msgget)).json()['response']["items"] # Запрос к VKAPI и сохранение ответа от сервера.
    count = requests.get(''.join(msgget)).json()['response']['count']
    if count == 0:
        print("\nСообщений нет")
    for i in range(len(response)):
        if "unread_count" in response[i]["conversation"]:
            unread = ' ('+str(response[i]["conversation"]["unread_count"])+')'
        else: unread = ""
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
        print("\n"+str(i+1)+") "+str(name)+" "+str(msg.split('\n',1)[0])+unread)
    