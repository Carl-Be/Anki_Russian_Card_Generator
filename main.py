# This is a sample Python script.
import image
import csv
import os
import forvo
import asyncio
import anki


def cleanUp(imageName, audioFile=''):

    command = str("rm " + " " + imageName + " " + audioFile)
    os.system(command)


def errorCheck(status, function):
    if type(status) == int and status < 0:
        print(f"Error with {function} status code {status}")
        exit(status)


async def controller():
    BAD_FILE_NAME = -2

    RUSSIAN_WORD_INDEX = 0
    ENGLISH_MEANING_INDEX = 1
    WORD_TYPE = 2

    print("Starting...")
    fileName = 'word_list.csv' #input("Enter the files name: ")

    if str(fileName).strip() == "":
         exit(BAD_FILE_NAME)

    print("Opening wordlist " + fileName + "\n")

    with open(fileName, newline='') as csvfile:
        wordlist = csv.reader(csvfile, delimiter=',')
        for row in wordlist:
            russianWord = row[RUSSIAN_WORD_INDEX]
            translation = row[ENGLISH_MEANING_INDEX]
            wordType = row[WORD_TYPE]

            print("Getting image for: " + translation)
            link = await image.getImageLink(translation)
            errorCheck(link, f"image.getImageLink({translation})")
            imageName = await image.downLoadImage(link)
            value = await image.prepPicture(imageName, wordType, russianWord)
            print("Image downloaded to: " + imageName)

            value = await forvo.getAudioLink(russianWord)

            print("Creating anki card for: " + russianWord)
            await anki.addCard(translation, russianWord)
            print("Finished creating anki card " + russianWord)

            print("Cleaning up for files: " + russianWord)
            cleanUp("*.png", "*.mp3")
            print("Clean up done.\n")

            break # remove when testing is done for 1 image

    print("Closing file: " + fileName)
    csvfile.close()
    print("File closed")
    print("Program Finished Running")


if __name__ == '__main__':
    asyncio.run(controller())
