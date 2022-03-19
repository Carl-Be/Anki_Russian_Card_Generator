import requests


async def addCard(translation, russianWord):

    ankiJson = {
        "action": "guiAddCards",
        "version": 6,
        "params": {
            "note": {
                "deckName": "testDeck",
                "modelName": "Basic",
                "fields": {
                    "Back": translation
                },
                "options": {
                    "closeAfterAdding": True
                },
                "tags": [
                    "russian"
                ],
                "picture": [{
                    "path": "/Users/carlbechie/PycharmProjects/ankiCardGenerator/cardImage.png",
                    "filename": russianWord + ".png",
                    "fields": [
                        "Front"
                    ]
                }],
                "audio": {
                    "path": "/Users/carlbechie/PycharmProjects/ankiCardGenerator/tempAudio.mp3",
                    "filename": russianWord + ".mp3",
                    "fields": [
                        "Front"
                    ]
                }
            }
        }
    }

    response = requests.post('http://127.0.0.1:8765', json=ankiJson)
    print("Added Card Response")
    print(response.content)

