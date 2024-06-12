import tkinter as tk
from gtts import gTTS
from gtts import lang
from googletrans import Translator

def convert_text():
    text = text_entry.get()
    target_language = language_dropdown.get()

    try:
        translator = Translator()
        translated_text = translator.translate(text, dest=target_language).text

        languages = lang.tts_langs()
        language_codes = [code for code, _ in languages.items()]

        if target_language not in language_codes:
            status_label.config(text="Selected language is not supported for TTS.")
            return

        speech = gTTS(text=translated_text, lang=target_language, slow=False)
        speech.save("C:/text mp3/ui_new.mp3")  # Replace with your preferred path
#         os.system("start new4.mp3")
        status_label.config(text="Text converted to speech successfully!")

    except Exception as e:
        status_label.config(text=f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("Text-to-Speech Converter")

# Text input field
text_label = tk.Label(root, text="Enter text:")
text_label.pack(pady=10)
text_entry = tk.Entry(root, width=50)
text_entry.pack(pady=5)

# Language selection dropdown
language_label = tk.Label(root, text="Choose language:")
language_label.pack(pady=10)
language_options = lang.tts_langs()
language_dropdown = tk.StringVar(root)
language_dropdown.set(list(language_options.keys())[0])  # Set default language
language_menu = tk.OptionMenu(root, language_dropdown, *language_options.keys())
language_menu.pack(pady=5)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_text)
convert_button.pack(pady=10)

# Status label
status_label = tk.Label(root, text="")
status_label.pack(pady=5)

# Run the main event loop
root.mainloop()
