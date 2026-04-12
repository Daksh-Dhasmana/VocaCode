import speech_recognition as sr

def get_voice():
    r = sr.Recognizer()
    
    # Ensures the recognizer dynamically adjusts to background noise levels
    r.dynamic_energy_threshold = True 

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1) 
        print("Speak now... (You can dictate multiple commands)")
        
        try:
            # Addresses Task 3: Expanded phrase_time_limit from 5 to 20 seconds
            # This allows the user to dictate "multiple commands" sequentially without being cut off.
            # Added a timeout to prevent the application from hanging if no speech is detected.
            audio = r.listen(source, timeout=5, phrase_time_limit=20)
        except sr.WaitTimeoutError:
            print("Listening timed out. No speech detected.")
            return ""

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