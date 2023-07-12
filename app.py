import speech_recognition as sr
import keyboard
import pyttsx3
import time


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=2) as mic:
        recognizer.adjust_for_ambient_noise(mic)
        print("Pode falar")
        audio = recognizer.listen(mic)
        try:
            audio = recognizer.recognize_google(audio,language='pt-br')
            print(audio)
            opcao_escrever = str(input('Deseja escrever automaticamente?(Y/N)\ncaso sua resposta seja sim, responda Y e clique onde deseja escrever\n'))
            if opcao_escrever == 'Y':
                time.sleep(10)
                keyboard.write(audio,delay=0.05)
            else:
                pass
        except sr.UnknownValueError:
            print("não consegui entender")
            
print('1-Text to speech\n2-Speech to text')
opcao = str(input('Escolha uma opção: '))
if opcao == "1":
    print('Opção disponivel em breve')
if opcao == "2":
    listen()