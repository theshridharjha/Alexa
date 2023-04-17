# Importing different modules to facilitate the code

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# listener to catch the voice
listener = sr.Recognizer()

# text to speech commmand
engine = pyttsx3.init()

# conversion of male voice to female voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

# funtion to take the command


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

# funtion to run alexa


def run_alexa():
    comand = take_command()
    print(comand)

    # running alexa with playing song
    if 'play' in comand:
        song = comand.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    # running alexa with telling the time
    elif 'time' in comand:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current Time is : ' + time)

    # running alexa for describing a person or a topic
    elif 'Tell me more about ' in comand:
        person = comand.replace('Tell me more about ', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    # running alexa for asking her for a date
    elif 'date' in comand:
        talk('Sure, I would love to date you!')

    # running alexa for asking her if she is single
    elif 'are you single' in comand:
        talk('Yes I am single, but you are not single!')

    # running alexa for telling jokes
    elif 'joke' in comand:
        talk(pyjokes.get_joke())

    # if alexa didn't understood what you told
    else:
        talk('Please repeat the command!')


# main infinite loop
while True:
    run_alexa()
