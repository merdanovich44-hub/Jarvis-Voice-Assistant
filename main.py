import os
import subprocess
import time
import webbrowser
import speech_recognition as sr
import pyttsx3


class JarvisAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)
        self.engine.setProperty('volume', 1.0)

    def speak(self, text: str):
        print(f"Джарвис: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.microphone as source:
            print("Говорите...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="ru-RU")
            print(f"Вы сказали: {text}")
            return text.lower()
        except sr.UnknownValueError:
            self.speak("Не удалось распознать речь.")
            return ""
        except sr.RequestError:
            self.speak("Проблема с интернет-сервисом распознавания.")
            return ""

    def execute(self, command: str):
        if not command:
            return

        if "привет" in command or "здравствуй" in command:
            self.speak("Здравствуйте, хозяин. Чем могу помочь?")
        elif "открой браузер" in command or "открой google" in command:
            webbrowser.open("https://www.google.com")
            self.speak("Открываю браузер.")
        elif "открой youtube" in command:
            webbrowser.open("https://www.youtube.com")
            self.speak("Открываю YouTube.")
        elif "открой яндекс" in command:
            webbrowser.open("https://ya.ru")
            self.speak("Открываю Яндекс.")
        elif "открой папку документы" in command:
            os.startfile(os.path.join(os.path.expanduser("~"), "Documents"))
            self.speak("Открываю папку документов.")
        elif "открой папку загрузки" in command:
            os.startfile(os.path.join(os.path.expanduser("~"), "Downloads"))
            self.speak("Открываю папку загрузок.")
        elif "открой калькулятор" in command:
            subprocess.Popen("calc")
            self.speak("Открываю калькулятор.")
        elif "открой блокнот" in command:
            subprocess.Popen("notepad")
            self.speak("Открываю блокнот.")
        elif "выход" in command or "завершение" in command:
            self.speak("До свидания, хозяин.")
            raise SystemExit
        elif "время" in command:
            current_time = time.strftime("%H:%M")
            self.speak(f"Сейчас {current_time}.")
        elif "дата" in command:
            current_date = time.strftime("%d.%m.%Y")
            self.speak(f"Сегодня {current_date}.")
        else:
            self.speak("Команда не распознана. Попробуйте сказать: открыть браузер, открыть YouTube, открыть калькулятор или выход.")

    def run(self):
        self.speak("Голосовой помощник Джарвис запущен.")
        while True:
            command = self.listen()
            self.execute(command)


if __name__ == "__main__":
    assistant = JarvisAssistant()
    assistant.run()
