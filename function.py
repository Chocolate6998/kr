import json

with open('operations.json', 'r', encoding='utf-8') as operations_json:
    operations = json.load(operations_json)


def executed(operation):
    """Отсеивает отмененные операции"""
    executed_list = [i for i in operation if i.get('state') == "EXECUTED"]
    return executed_list


def from_number(number):
    """Определяет есть номер счета или карты отправителя и маскирут их"""
    if number:
        if len(number) == 25:
            return f'Счет **{number[-4:]} ->'
        else:
            return f'{number[:-12]} {number[-12:-10]}** **** {number[-4:]} ->'
    else:
        return ''


def to_number(number):
    """маскирут номер счета"""
    return f'**{number[-4:]}'


def last_operations():
    """Сортирует по дате и выводит информацию о 5 последних операциях"""
    last = sorted(executed(operations), key=lambda x: x.get("date"), reverse=True)[:5]
    for i in last:
        print(f"""{i['date'][:10]} {i['description']}
{from_number(i.get('from'))} Счет {to_number(i["to"])}
{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n""")
