import twitch
import speech_recognition as sr
import pyttsx3

# Twitch Variables
clientId = 'gz3pppp9elbk6smuodu5pxeswaox7p'
clientSecret = 'wc40p5dwvcoenypeymop7mla17l0pf'

# Speech variables
r = sr.Recognizer()


def connect_to_twitch():
    helix = twitch.Helix(clientId, clientSecret)
    print(helix.user('mcnaldo69').display_name)


def convert_speech_to_text(command):
    # Initialise the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


if __name__ == '__main__':
    connect_to_twitch()
    while True:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)

                audio2 = r.listen(source2)

                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("Did you say " + MyText)
                convert_speech_to_text(MyText)
        except sr.RequestError as e:
            print("could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown error occurred")

