import os
def app():
    def listen():
        
        with sr.Microphone(device_index=2) as mic:
            recognizer.adjust_for_ambient_noise(mic)
            print("Pode falar")
            audio = recognizer.listen(mic)
            try:
                audio = recognizer.recognize_google(audio,language='pt-br')
                print(audio)    
                save_text = str(input("Salvar em arquivo? (Y/N) "))
                print(save_text)
                if save_text == "Y" or save_text == "y":
                        name_text_file = str(input("Insira o nome do arquivo: "))
                        with open(name_text_file+'.txt',"w") as file:
                            file.write(audio)
                if save_text == "N" or save_text == "n":
                    pass
                
            except sr.UnknownValueError:
                print("não consegui entender")

    def change_voice(words):
            os.system('cls')
            global voice_index
            change_voice_options = int(input("1-Escutar voz selecionada\n2-Trocar voz\n3-voltar\n(As vozes disponiveis dependem das que você tem instaladas no seu computador)\n"))
            
            if change_voice_options == 1:
                engine.setProperty('voice', voices[voice_index].id)
                engine.say(words)
                engine.runAndWait()
                change_voice(words)
            elif change_voice_options == 2:
                if voice_index == 0:
                    voice_index = 1
                elif voice_index == 1:
                    voice_index = 0
                change_voice(words)
            elif change_voice_options == 3:
                pass
            engine.setProperty('voice', voices[voice_index].id)
            engine.runAndWait()

    def talk(word):
            
        engine.setProperty('voice', voices[voice_index].id)
        engine.say(word)
        engine.runAndWait()
        change_voice_option = str(input("Mudar Voz? (Y/N) "))
        if change_voice_option == 'Y' or change_voice_option == 'y':
            change_voice(word)
        elif change_voice_option == 'N' or change_voice_option == 'n':
            pass
        save = str(input("Salvar audio? (Y/N) "))
        if save == "Y" or save == "y":
            filename = str(input("Insira o nome do arquivo: "))
            engine.save_to_file(word,filename+".mp3")
            engine.runAndWait()



    print('1-Text to speech\n2-Speech to text')
    opcao = str(input('Escolha uma opção: '))
    if opcao == "1":
        word = input(str('Insira o texto: '))
        talk(word)

    if opcao == "2":
        listen()
try:
    import speech_recognition as sr
    import pyttsx3
    engine = pyttsx3.init()
    recognizer = sr.Recognizer()
    voice_index = 0
    voices = engine.getProperty('voices')
    app()
except ModuleNotFoundError:
    install_library = str(input('Parece que você não tem as bibliotecas nescessarias para o app funcionar corretamente (SpeechRecognition e pyttsx3) \ndeseja instala-las? (S/N)\n'))
    if install_library == 's' or install_library == 'S':
        os.system('python -m pip install --upgrade pip')
        os.system('pip install SpeechRecognition')
        os.system('pip install pyttsx3')
        print('\nReinicie o app para funcionar\n')
    else:
        pass
