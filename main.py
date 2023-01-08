from functions import *
import os

if checkupd() == "upd":
    exit(0)
if not os.path.isfile("token.txt"):
    print("Для того, чтобы использовать ConsoleVK необходим токен от страницы. \nПолучить его можно по ссылке:\nhttps://oauth.vk.com/authorize?client_id=6121396&scope=1916423&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1\nВведите данные с адресной строки:")
    # Токен необходим для взаимодействия с VKAPI, он не передаётся вне рамок API VK, нигде не хранится, если пользователь сам того не хочет.
    # Весь код открыт, никакие данные не передаются третьим лицам вне рамок VK.
    token = input()
    if token[:5] == "vk1.a":
        token = token
    else:
        token = token[45:].split('&',1)[0] # Срез символов, чтобы оставить только токен.
else:
    filetoken=open("token.txt", "r")
    token = filetoken.read()
    filetoken.close()
print(chr(27) + "[2J")

auth(token) # Попытка авторизации по токену.

if not os.path.isfile("token.txt"):
    print("Сохранить токен? y/N")
    if input() == "y":
        filetoken=open("token.txt", "w")
        filetoken.write(token)
        filetoken.close()
        print("Токен сохранён в файл token.txt")
while True:
    command = input("\n┌ МЕНЮ\n├─── 1) Сообщения (только вывод)\n├─── 2) Выход (выход из аккаунта, закрытие приложения, удаление токена)\n└─── 3) Выйти из приложения\nВаша команда: ").lower()
    if command == "сообщения" or command == '1':
        subcommand = input("\nКакие сообщения показать:\n├─── 1) Все (выведутся последние 10 сообщений)\n└─── 2) Новые\nВаша команда: ").lower()
        if subcommand == '1' or subcommand == "все":
            offset = input("\nСмещение (0 по стандарту): ")
            filter='all'
            messages(offset, token, filter)
        elif subcommand == '2' or subcommand == "новые":
            offset = input("\nСмещение (0 по стандарту): ")
            filter='unread'
            messages(offset, token, filter)
    elif command == "выход из аккаунта" or command == "2":
        subcommand=input("Вы действительно хотите выйти из аккаунта? При этом действии удалится файл токена, а приложение закроется. y/N\n").lower()
        if subcommand == "y":
            rmtoken(token)
    else:
        exit()
