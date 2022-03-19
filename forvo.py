import urllib.parse
import requests
import os


async def getAudioLink(word):
    FORVO_API_KEY = <Your Key Goes Here>
    word = urllib.parse.quote(word)
    url = f'https://apifree.forvo.com/action/word-pronunciations/format/json/word/{word}/id_lang_speak/138/order/rate-desc/limit/1/key/{FORVO_API_KEY}/'
    r = requests.get(str(url))
    thisJson = r.json()

    link = thisJson['items'][0]['pathmp3']
    print("Downloading MP3")
    await downloadAudio(link)

    return 0


async def downloadAudio(link):
    os.system("wget --content-disposition  " + link + " && mv ./*.mp3 ./tempAudio.mp3")
    return 0
