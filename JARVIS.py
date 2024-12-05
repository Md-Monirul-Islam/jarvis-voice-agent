# import pyttsx3
# import speech_recognition as sr


# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voices',voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# speak('Hello Munna')


# def commands():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print('Listing....')
#         r.pause_threshold=1
#         r.adjust_for_ambient_noise(source,duration=1)
#         audio = r.listen(source)

#     try:
#         print("wait for few moments....")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"You just said: {query}\n")
    
#     except Exception as e:
#         print(e)
#         speak('Please tell me again....')
#         query='none'
    
#     return query


# query = commands().lower()

import os
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak('Hello Munna')

def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=2)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print('Processing audio...')
            query = r.recognize_google(audio, language='en-in')
            print(f"You just said: {query}\n")
            return query.lower()
        except sr.UnknownValueError:
            print("Speech Recognition could not understand the audio.")
            speak('Please tell me again....')
            return 'none'
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak('There was an issue with the recognition service.')
            return 'none'
        except Exception as e:
            print(f"An error occurred: {e}")
            speak('Please tell me again....')
            return 'none'

# query = commands()

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('Good Morning Sir....')
        speak('Good Morning Sir')

    elif hour>=12 and hour<17:
        print('Good afternoon Sir....')
        speak('Good afternoon sir')

    elif hour>=17 and hour<21:
        print('Good evening sir.....')
        speak('Good evening sir')

    else:
        print('Good night sir.....')
        speak('good night sir')


if __name__ == '__main__':
    wishings()
    query = commands().lower()
    if 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f'Sir, the time is {strTime}')

    elif 'open firefox' in query:
        speak('opening firefox application sir.....')
        os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

    elif 'wikipedia' in query:
        speak('Searching in wikipedia....')
        try:
            query=query.replace('wikipedia','')
            results = wikipedia.summary(query,sentences=2)
            speak('According to wikipedia,')
            print(results)
            speak(results)

        except:
            speak('no results found...')
            print('No results found....')
        
