# cors-auditor
Python script for auditing CORS headers mechanism

![image](https://github.com/olegbrain-offsec/cors-auditor/assets/160741328/cf078264-c2c0-4641-90f6-65ec8e35e630)


## In English
### The idea
The idea of writing my own tool came to me during BugBounty, when I found a misconfig on an endpoint working with confidential information. To automate the search for such errors, I decided to develop a tool that is able to audit multiple points and determine the possibility of exploiting a vulnerability. The developed tool will not only detect the CORS misconfig, but also indicate whether it can be used to access the user's info. For example, trusting an arbitrary Origin with Access-Control-Allow-Credentials: true is dangerous.
### How to use
1. Collect endpoint addresses using katana or another tool;
2. Filter out simple ades that do not lead to endpoints that work with the information we are interested in;
3. If you know that the web resource allows data to be received by partners, subdomains, add them to the sample JSON file.json;
#### sample.json
```
[
{
"url":"http://olegbrain.ru/user/private-info ",
"domains":["allowed.com ", "allowed2.com "]
}
]
```

4. Run the script and observe the analysis of all web resource addresses:)
### Payload
To customize payloads, an approach based on payload templates and its description is presented. In the pattern_base file.I have collected all possible CORS analysis options available for attack, but if your task is fuzzing testing, then you can generate your own dictionary and use it in addition to the one presented.

## На русском
### Идея
Идея о написании своего инструмента пришла ко мне во время BugBounty, когда я нашел мисконфиг на конечной точке, работающей с конфиденциальной информацией. Для автоматизации поиска таких ошибок я решил разработать инструмент, который способен произвести аудит множества точек и определить возможность эксплуатации уязвимости. Разработанный инструмент не только обнаружит мисконфиг CORS, но и при этом укажет может ли он быть использован для доступа к инфо пользователя. Например, доверие произвольному Origin при Access-Control-Allow-Credentials: true является опасным. 
### Как использовать
1. Соберите адреса конечных точек при помощи katana или другого инструмента;
2. Отфильтруйте простые адеса, которые не ведут к конечным точкам, работающим с интересующей нас информацией;
3. Если вы знаете, что веб-ресурс допускает получение данных партнерами, поддоменами, добавьте их в JSON-файл sample.json;
#### sample.json
```
[
{
    "url":"http://olegbrain.ru/user/private-info",
    "domains":["allowed.com", "allowed2.com"]
}
]
```
4. Запустите скрипт и наблюдайте за анализом всех адресов веб-ресурса:)

 ### Полезная нагрузка
 Для кастомизации полезных нагрузок представлен подход, основанный на шаблонах полезной нагрузки и ее описании. В файле pattern_base.json я собрал всевозможные доступные для атаки варианты анализа CORS, но если Ваша задача фаззинг-тестирование, то вы можете сгенерировать собственный словарь и использовать его в дополнение к представленному.

```
[
    {"payload":"null","caption":"[!] Доверие null: "},
    {"payload":"https://evil.com","caption":"[!] Доверие любому домену: "},
    {"payload":"https://DOMAINevil.com","caption":"[!] Слияние доменов: "},
    {"payload":"https://evil.comDOMAIN","caption":"[!] Слияние доменов: "},
    {"payload":"https://ß.evil.com","caption":"[!] Ошибка парсинга Unicode-символов: "},
    {"payload":"https://DOMAIN.evil.com","caption":"[!] Доверие произвольному TLD: "},
    {"payload":"http://subdomain.DOMAIN","caption":"[!] SSL Downgrade "},
    {"payload":"https://evil.DOMAIN","caption":"[!] Доверие поддомену: "},
    {"payload":"https://DOMAIN!.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN=.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN&.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN'.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN(.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN).evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN*.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN,.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN;.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN=.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN^.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN`.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN{.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN|.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN}.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN~.evil.com","caption":"[!] Атака на Safari: "},
    {"payload":"https://DOMAIN$.evil.com","caption":"[!] Атака на Safari, Firefox: "},
    {"payload":"https://DOMAIN+.evil.com","caption":"[!] Атака на Safari, Firefox: "},
    {"payload":"https://DOMAIN_.evil.com","caption":"[!] Атака на Safari, Chrome, Edge, Firefox, IE: "}
]
```
