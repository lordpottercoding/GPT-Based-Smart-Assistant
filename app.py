from openai import OpenAI
from apikey import api_data
import os
import speech_recognition as sr # converts voice commands to text
import pyttsx3 # Read out text output to voice
import webbrowser

Model="gpt-4"
client=OpenAI(api_key=api_data)

def reply(question):
    completion = client.chat.completions.create(  # Use 'completions' instead of 'completion'
        model=Model,
        messages=[
            {'role': "system", "content": "You are a helpful Assistant"},
            {'role': 'user', 'content': question}
        ],
        max_tokens=200
    )
    answer = completion.choices[0].message.content  # Correct way to extract the response
    return answer

#Text to Speech
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello! How are yyou?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1 # wait 1sec before considering the end of phrase
        audio=r.listen(source)
    try:
        print("Recognising....")
        query= r.recognize_google(audio,language='en-in')
        print("user Said: {} \n".format(query))
    except Exception as e:
        print("Say that again...")
        return 'None'
    return query

if __name__=='__main__':
    while True:
        query = takeCommand().lower()
        if query == 'none':
            continue

        ans=reply(query)
        print(ans)
        speak(ans)

        #specific browser related tasks
        if "open youtube" in query:
            webbrowser.open('www.youtube.com')
        if "open Google" in query:
            webbrowser.open('www.google.com')
        if "bye" in query:
            break