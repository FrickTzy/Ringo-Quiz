import speech_recognition as sr


def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)  # adjust for ambient noise

    print("Listening...")

    try:
        while True:
            with microphone as source:
                audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)  # recognize speech using Google Speech Recognition
                print("You said:", text)
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        print("Program stopped")


if __name__ == "__main__":
    main()