import sys
import time
from ahk import AHK
text = 'This site is awesome'
from googletrans import Translator
translator = Translator()
ahk = AHK()

english_to_arabic = {
    'q': 'ض',
    'w': 'ص',
    'e': 'ث',
    'r': 'ق',
    't': 'ف',
    'y': 'غ',
    'u': 'ع',
    'i': 'ه',
    'o': 'خ',
    'p': 'ح',
    'a': 'ش',
    's': 'س',
    'd': 'ي',
    'f': 'ب',
    'g': 'ل',
    'h': 'ا',
    'j': 'ت',
    'k': 'ن',
    'l': 'م',
    'z': 'ئ',
    'x': 'ط',
    'c': 'ؤ',
    'v': 'ر',
    'b': 'ذ',
    'n': 'ى',
    ']':'د',
    '.': 'ز',
    'm':'ة',
    '/':'ظ',
    ';':'ك'
    # Add other mappings here
}
arabic_to_english = {v: k for k, v in english_to_arabic.items()}
def convert_to_arabic():
    clipboardOld=ahk.get_clipboard_all()
    ahk.send("^c")
    clipboardNew = ahk.get_clipboard_all()            
    if (clipboardNew != clipboardOld):
        text = ahk.get_clipboard()       
        print(text)        
        converted_text = convert(text)
        ahk.set_clipboard(converted_text)
        ahk.send("^v")
        ahk.set_clipboard("")
    else:
        print("there is no selected")
        ahk.send("{Home}")
        ahk.send("+{End}")
        ahk.send("^c")
        text=ahk.get_clipboard()
        print(text)
        converted_text = convert(text)
        ahk.set_clipboard(converted_text)
        ahk.send("^v")
        ahk.set_clipboard("")
    if (clipboardOld):  # Check if clipboardOld is not empty
            # Use set_clipboard for text, ensure clipboardOld is a string
            ahk.set_clipboard_all(str(clipboardOld))    
def convert(text):
    text=text.lower()
    if(text!="" and text[0] in english_to_arabic.keys()):
            st=translator.translate(text, dest ='ar').text
            print("english to  arabic")
    else:
            st=translator.translate(text, dest ='en').text
            print("arabic to english")
    return st        
ahk.add_hotkey('!y', callback=convert_to_arabic)
ahk.start_hotkeys()  # start the hotkey process thread
ahk.block_forever()  # not strictly needed in all scripts -- stops the script from exiting; sleep forever


