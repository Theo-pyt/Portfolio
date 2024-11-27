import json
from pprint import pprint
from urllib import request

def main():
    data = request.urlopen('http://py4e-data.dr-chuck.net/comments_2128051.json')

    info = json.loads(data.read().decode('utf8'))
    print('User count:', len(info))

    pprint(info)

    print(info.keys())

    count = 0

    for item in info['comments']:
        print(item)
        print('Name', item['name'])
        count += item['count']
        print('Count', item['count'])
        print(count)


if __name__ == '__main__':
    main()