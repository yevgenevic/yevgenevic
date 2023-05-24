import json

arr = []
with open('end.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower() and i.split('\n')[0]
        if n != '':
            arr.append(n)
with open('text.json','w', encoding='utf-8') as e:
    json.dump(arr, e)
