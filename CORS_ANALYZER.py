import requests,os,json
from urllib.parse import urlparse

def analyzeOrigin(requrl, caption, payload, allowedOrigins):
    # Установка заголовка для OPTIONS-запроса
    headers = json.loads('{{"Origin":"{0}","Access-Control-Request-Method":"GET"}}'.format(payload))
    response = requests.options(requrl, headers=headers) 
    # Обработка результатов запроса
    try:    ACAC = response.headers["Access-Control-Allow-Credentials"]
    except: ACAC = "None"
    try:        ACAO = response.headers["Access-Control-Allow-Origin"]
    except:     ACAO = "None"  
    # Сравнение полученного ACAO и ACAC с переданным, а также с разрешенными доменами
    if ((ACAO=="None")|(ACAO.replace("https://","") in allowedOrigins)|(ACAO.replace("http://","") in allowedOrigins)|(ACAO=="*")):
        print(green + "[!] Origin: " + payload + " тест пройден!")
    elif ((ACAO==payload)):
        if ACAC.lower() == "true":
            print(red + caption + payload )
        else:
            print(yellow + caption + payload )
    else:
        print(yellow + "[!] Origin: " + payload + " необходима ручная проверка!")

if __name__=="__main__":
    red = "\033[0;31m" 
    green = "\033[0;32m" 
    yellow = "\033[0;33m" 
    white = "\033[0;37m"
    banner= '''
   __________  ____  _____ __              __
  / ____/ __ \/ __ \/ ___// /_____  ____  / /
 / /   / / / / /_/ /\__ \/ __/ __ \/ __ \/ / 
/ /___/ /_/ / _, _/___/ / /_/ /_/ / /_/ / /  
\____/\____/_/ |_|/____/\__/\____/\____/_/   

'''
    print(banner)
    print(red + "[RED] Кража данных злоумышленником возможна.")
    print(yellow + "[YELLOW] Кража данных невозможна, но CORS настроен неверно, \n\t либо необходима ручная проверка.")
    try:
        urlsJson = json.load(open('sample.json','r'))
    except:
        print(red + "[ERROR] Файл с ресурсами не найден")
        os._exit(1)
    for data in urlsJson:
        allowedOrigins =[]
        try:
            url = data['url']
            print(white + "\n[INFO] Анализирую URL: " + url)
            try: 
                allowedOrigins.extend(data['domains'])
                allowedOrigins.append(urlparse(url).netloc)
                print(white + "[INFO] Доверенные домены: " + ", ".join(allowedOrigins) + "\n")
            except:
                allowedOrigins.append(urlparse(url).netloc)
                print(white + "[INFO] Доверенный домен: " + allowedOrigins[0] + "\n")
            # Открытие файла с полезной нагрузкой
            PayloadsJson = json.load(open('pattern_base.json','r'))
            # Главный цикл
            for origin in allowedOrigins:
                for payloads in PayloadsJson:
                    payload = (payloads['payload']).replace("DOMAIN", origin)
                    analyzeOrigin(url, payloads['caption'], payload, allowedOrigins)
        except KeyboardInterrupt:
            os._exit(1)
        except:
            print(white + "[ERROR] Обязательный параметр не задан!")
            os._exit(1)
    print(white + "\n[INFO] Тесты окончены")







    