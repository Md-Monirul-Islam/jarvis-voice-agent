# # import pyttsx3
# # import speech_recognition as sr


# # engine = pyttsx3.init('sapi5')
# # voices = engine.getProperty('voices')
# # engine.setProperty('voices',voices[0].id)

# # def speak(audio):
# #     engine.say(audio)
# #     engine.runAndWait()

# # speak('Hello Munna')


# # def commands():
# #     r = sr.Recognizer()
# #     with sr.Microphone() as source:
# #         print('Listing....')
# #         r.pause_threshold=1
# #         r.adjust_for_ambient_noise(source,duration=1)
# #         audio = r.listen(source)

# #     try:
# #         print("wait for few moments....")
# #         query = r.recognize_google(audio, language='en-in')
# #         print(f"You just said: {query}\n")
    
# #     except Exception as e:
# #         print(e)
# #         speak('Please tell me again....')
# #         query='none'
    
# #     return query


# # query = commands().lower()

# import os
# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import pywhatkit
# import pyautogui

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# # speak('Hello Munna')

# def commands():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print('Listening...')
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source, duration=2)
#         try:
#             audio = r.listen(source, timeout=15, phrase_time_limit=10)
#             print('Processing audio...')
#             query = r.recognize_google(audio, language='en-in')
#             print(f"You just said: {query}\n")
#             return query.lower()
#         except sr.UnknownValueError:
#             print("Speech Recognition could not understand the audio.")
#             speak('Please tell me again....')
#             return 'none'
#         except sr.RequestError as e:
#             print(f"Could not request results; {e}")
#             speak('There was an issue with the recognition service.')
#             return 'none'
#         except Exception as e:
#             print(f"An error occurred: {e}")
#             speak('Please tell me again....')
#             return 'none'

# # query = commands()

# def wishings():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         print('Good Morning Sir....')
#         speak('Good Morning Sir')

#     elif hour>=12 and hour<17:
#         print('Good afternoon Sir....')
#         speak('Good afternoon sir')

#     elif hour>=17 and hour<21:
#         print('Good evening sir.....')
#         speak('Good evening sir')

#     else:
#         print('Good night sir.....')
#         speak('good night sir')


# # if __name__ == '__main__':
# #     wishings()
# #     query = commands().lower()
# #     if 'time' in query:
# #         strTime = datetime.datetime.now().strftime("%H:%M:%S")
# #         speak(f'Sir, the time is {strTime}')

# #     elif 'open firefox' in query:
# #         speak('opening firefox application sir.....')
# #         # os.startfile('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
# #         # os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
# #         os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

# #     elif 'wikipedia' in query:
# #         speak('Searching in wikipedia....')
# #         try:
# #             query=query.replace('wikipedia','')
# #             results = wikipedia.summary(query,sentences=2)
# #             speak('According to wikipedia,')
# #             print(results)
# #             speak(results)

# #         except:
# #             speak('no results found...')
# #             print('No results found....')

# #     elif 'play' in query:
# #         query=query.replace('play','')
# #         speak('Playing '+query)
# #         pywhatkit.playonyt(query)

    
# #     elif 'type' in query:
# #         query=query.replace('type','')
# #         speak('Please tell me what should I write')
# #         pyautogui.write(query)
        
# # if __name__ == '__main__':
# #     wishings()
# #     while True:
# #         query = commands().lower()
# #         if 'time' in query:
# #             strTime = datetime.datetime.now().strftime("%H:%M:%S")
# #             speak(f'Sir, the time is {strTime}')

# #         elif 'open firefox' in query:
# #             speak('opening firefox application sir.....')
# #             os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

# #         elif 'what is' in query or 'who is' in query:
# #             # Automatically use Wikipedia if a general question is asked
# #             speak('Searching in Wikipedia...')
# #             try:
# #                 results = wikipedia.summary(query, sentences=2)
# #                 speak('According to Wikipedia,')
# #                 print(results)
# #                 speak(results)
# #             except wikipedia.exceptions.DisambiguationError as e:
# #                 speak('The query is ambiguous. Please provide more specific details.')
# #                 print(f"Disambiguation Error: {e}")
# #             except wikipedia.exceptions.PageError:
# #                 speak('No results found on Wikipedia.')
# #                 print('No results found.')
# #             except Exception as e:
# #                 speak('An error occurred while fetching results.')
# #                 print(f"Error: {e}")

# #         elif 'play' in query:
# #             query = query.replace('play', '')
# #             speak('Playing ' + query)
# #             pywhatkit.playonyt(query)

# #         elif 'type' in query:
# #             speak('Please tell me what should I write')
# #             pyautogui.write(query.replace('type', ''))

# #         elif 'exit' in query or 'quit' in query:
# #             speak("Goodbye, sir!")
# #             break

# if __name__ == '__main__':
#     wishings()
#     while True:
#         query = commands().lower()

#         if 'time' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f'Sir, the time is {strTime}')

#         elif 'open firefox' in query:
#             speak('Opening Firefox application sir.....')
#             os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

#         elif 'play' in query:
#             query = query.replace('play', '')
#             speak('Playing ' + query)
#             pywhatkit.playonyt(query)

#         elif 'type' in query:
#             speak('Please tell me what should I write')
#             pyautogui.write(query.replace('type', ''))

#         elif 'exit' in query or 'quit' in query:
#             speak("Goodbye, sir!")
#             break

#         else:
#             # Treat any other query as a Wikipedia search
#             speak('Let me search that for you...')
#             try:
#                 results = wikipedia.summary(query, sentences=2)
#                 speak('According to Wikipedia,')
#                 print(results)
#                 speak(results)
#             except wikipedia.exceptions.DisambiguationError as e:
#                 speak('The query is ambiguous. Please provide more specific details.')
#                 print(f"Disambiguation Error: {e}")
#             except wikipedia.exceptions.PageError:
#                 speak('No results found on Wikipedia.')
#                 print('No results found.')
#             except Exception as e:
#                 speak('An error occurred while fetching results.')
#                 print(f"Error: {e}")


import os
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import pyautogui
import requests
from bs4 import BeautifulSoup

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def commands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=2)
        try:
            audio = r.listen(source, timeout=15, phrase_time_limit=10)
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

def wishings():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print('Good Morning Sir....')
        speak('Good Morning Sir')
    elif hour >= 12 and hour < 17:
        print('Good afternoon Sir....')
        speak('Good afternoon sir')
    elif hour >= 17 and hour < 21:
        print('Good evening sir.....')
        speak('Good evening sir')
    else:
        print('Good night sir.....')
        speak('Good night sir')

def search_online(query):
    """
    Fallback to search online using requests and BeautifulSoup.
    """
    try:
        speak('Searching online for more information...')
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
        search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        response = requests.get(search_url, headers=headers)
        # soup = BeautifulSoup(response.text, 'html.parser')
        soup = BeautifulSoup(response.text, 'lxml')
        result_snippets = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")

        # Get the top result snippet
        if result_snippets:
            top_result = result_snippets[0].text
            print(f"Online Search Result: {top_result}")
            speak(f"Here's what I found online: {top_result}")
        else:
            speak("Sorry, I couldn't find anything online.")
    except Exception as e:
        print(f"An error occurred during online search: {e}")
        speak("I couldn't search online due to an error.")

if __name__ == '__main__':
    wishings()
    while True:
        query = commands().lower()

        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        elif 'open firefox' in query:
            speak('Opening Firefox application sir.....')
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'play' in query:
            query = query.replace('play', '')
            speak('Playing ' + query)
            pywhatkit.playonyt(query)

        elif 'type' in query:
            speak('Please tell me what should I write')
            pyautogui.write(query.replace('type', ''))

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye, sir!")
            break

        else:
            # Treat any other query as a Wikipedia search
            speak('Let me search that for you...')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak('According to Wikipedia,')
                print(results)
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak('The query is ambiguous. Please provide more specific details.')
                print(f"Disambiguation Error: {e}")
            except wikipedia.exceptions.PageError:
                speak('No results found on Wikipedia. Let me search online.')
                search_online(query)  # Fallback to online search
            except Exception as e:
                speak('An error occurred while fetching results.')
                print(f"Error: {e}")
