import twitch
import speech_recognition as sr
import pyttsx3
import csv

# Twitch Variables
clientId = ''
clientSecret = ''

# Speech variables
r = sr.Recognizer()


def connect_to_twitch():
    helix = twitch.Helix(clientId, clientSecret)
    print(helix.user('mcnaldo69').display_name)


def convert_text_to_speech(command):
    # Initialise the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def swear_words():
    with open('swearWords.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for entry in csv_reader:
            return entry


if __name__ == '__main__':
    connect_to_twitch()
    swearWords = swear_words()
    while 1:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("Did you say " + MyText)
                convert_text_to_speech(MyText)
                for word in swearWords:
                    if word == MyText:
                        print("Bad word detected!")


        except sr.RequestError as e:
            print("could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown error occurred")
