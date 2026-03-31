import speech_recognition as sr

def get_voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # Calibrate for 1 second to ignore background static
        r.adjust_for_ambient_noise(source, duration=1) 
        print("Speak now...")
        # Added a phrase time limit so it doesn't listen forever
        audio = r.listen(source, phrase_time_limit=5)

    try:
        text = r.recognize_google(audio)
        print("You said (Raw):", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""