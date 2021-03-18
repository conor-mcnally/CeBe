import speech_recognition as sr
from playsound import playsound
import moviepy.editor as mp
import pyttsx3
import csv

# Speech variables
r = sr.Recognizer()


def swear_words():
    with open('swearWords.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for entry in csv_reader:
            return entry


def convert_video_to_audio(clip):
    clip = mp.VideoFileClip(clip)
    clip.audio.write_audiofile(r"converted.wav")


def convert_audio_to_text():
    audio = sr.AudioFile("converted.wav")
    with audio as source:
        audio_file = r.record(source)
    result = r.recognize_google(audio_file)
    return result


def detect_profanity_from_audioText(text):
    swearWords = swear_words()
    for word in swearWords:
        if word in text:
            print("Profanity detected!: " + word)
            playsound('/Users/cmcn2802/PycharmProjects/CeBe/beep.wav')
#           Do something


detect_profanity_from_audioText(convert_audio_to_text())


def convert_text_to_speech(command):
    # Initialise the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Driver code
if __name__ == '__main__':
    while 1:
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print("Did you say " + MyText)
                convert_text_to_speech(MyText)

        except sr.RequestError as e:
            print("could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("Unknown error occurred")
