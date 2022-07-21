from functions import *
print(chr(27) + "[2J")
print("Для того, чтобы использовать ConsoleVK необходим токен от страницы. \nПолучить его можно по ссылке:\nhttps://oauth.vk.com/authorize?client_id=6121396&scope=1916423&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1\nВведите данные с адресной строки:")
# Токен необходим для взаимодействия с VKAPI, он не передаётся вне рамок API VK, нигде не хранится, если пользователь сам того не хочет.
# Весь код открыт, никакие данные не передаются третьим лицам вне рамок VK.

token = input()[45:].split('&',1)[0] # Срез символов, чтобы оставить только токен.
print(chr(27) + "[2J")

auth(token) # Попытка авторизации по токену.
command = input("┌ МЕНЮ\n├─── Сообщения\n├─── Проверить обновления\n└─── Выход\nВаша команда: ").lower()

if command == "сообщения" or command == '1':
    subcommand = input("Какие сообщения показать:\n1)Все (выведутся последние 10 сообщений)\n2)Новые\nВаша команда: ").lower()
    if subcommand == '1' or subcommand == "все":
        filter='all'
        messages(token, filter)
else:
    print("не работает ничево")
    exit()
