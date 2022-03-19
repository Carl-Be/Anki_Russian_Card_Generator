from googleapiclient.discovery import build
import wget
from PIL import Image, ImageFont, ImageDraw


async def getImageLink(word):
    NO_IMAGE_FOUND = -1
    # get the API KEY here: https://developers.google.com/custom-search/v1/overview
    API_KEY = "AIzaSyAR5tsS9qnQcqTQApuY5qxRx31F7xXrWKE"
    # get your Search Engine ID on your CSE control panel
    SEARCH_ENGINE_ID = "e6c328ea274f14b4f"

    service = build("customsearch", "v1",
                    developerKey=API_KEY)

    res = service.cse().list(
        q=word,
        cx=SEARCH_ENGINE_ID,
        searchType='image',
        num=1,
        imgType='clipart',
        fileType='*',
        safe='off'
    ).execute()

    if not 'items' in res:
        return NO_IMAGE_FOUND
    else:
        return res['items'][0]['image']['thumbnailLink']


async def downLoadImage(imageLink):
    print("Downloading: " + imageLink)
    results = wget.download(imageLink, 'tmpImage.png')
    return results


async def prepPicture(imageName, wordType, russianWord):
    FONT_SIZE = 35
    RESIZED_NAME = "resizedImage.png"
    FINAL_NAME = "cardImage.png"
    my_font = ImageFont.truetype('arial/arial.ttf', FONT_SIZE)
    rgbOptions = {'m': (0, 64, 255),
                  'f': (255, 51, 204),
                  'n': (140, 140, 140),
                  '-': (0, 255, 0)
                  }

    # Resize image
    my_image = Image.open(imageName)
    my_image = my_image.resize((200, 200))
    my_image.save(RESIZED_NAME)

    # Write on image
    my_image = Image.open(RESIZED_NAME)
    image_editable = ImageDraw.Draw(my_image)
    w, h = my_font.getsize(russianWord)
    x, y = (100, 100)
    image_editable.rectangle((x - (w/2), y - (h/2), x + (w/2), y + (h/2)), fill='black')
    image_editable.text((x, y), russianWord, rgbOptions[wordType], my_font, anchor="mm")
    my_image.save(FINAL_NAME)

    return 0
