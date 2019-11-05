import requests

def ya_translate_en_ru(source_text: str):
    API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': API_KEY,
        'text': source_text,
        'lang': 'en-ru'
    }
    response = requests.get(URL, params=params)
    json_ = response.json()
    return json_

if __name__=='__main__':
    print(ya_translate_en_ru('Hello, darkness, my old friend'))