from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile

import pylator


class TextTranslate:


    def __init__(self, root):
        myframe = Frame(root)
        frame = Frame(root, relief=GROOVE)
        
        myframe.pack()

        frame.pack(side=LEFT)

        #list of all supported languages
        self.languages = ['af', 'en', 'am', 'ar', 'hy',
                 'az', 'eu', 'be', 'bn', 'bs',
                'bg', 'ca', 'ceb', 'ny', 'zh-cn',
                 'zh-tw', 'co', 'hr', 'cs', 'da', 
                'nl', 'sq', 'eo', 'et', 'tl', 'fi',
                 'fr', 'fy', 'gl', 'ka', 'de', 'el',
                 'gu', 'ht', 'ha', 'haw', 'iw', 'he',
                'hi', 'hmn', 'hu', 'is', 'ig', 'id',
                'ga', 'it', 'ja', 'jw', 'kn', 'kk',
                 'km', 'ko', 'ku', 'ky', 'lo', 'la',
                 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 
                'ml', 'mt', 'mi', 'mr', 'mn', 'my',
                 'ne', 'no', 'or', 'ps', 'fa', 'pl',
                'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 
                 'sr', 'st', 'sn', 'sd', 'si', 'sk',
                 'sl', 'so', 'es', 'su', 'sw', 'sv',
                 'tg', 'ta', 'te', 'th', 'tr', 'uk',
                  'ur', 'ug', 'uz', 
                 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']

        self.lb1 = Label(myframe, text = "Text Translate", )
        self.lb1.pack(side =  TOP)

        self.text_box = Text(myframe, font=('calibre', 10, 'bold'))
        self.text_box.insert(INSERT, "Enter text to translate...")
        self.text_box.pack()

        self.lb2 = Label(myframe, text = "Select laanguages: ",  
        font = ("Times New Roman", 10))
        self.lb2.pack()
        self.n = StringVar()
        self.language_choosen = ttk.Combobox(myframe, width = 27, textvariable = self.n)
        self.language_choosen['values'] = tuple(self.languages)
        self.language_choosen.pack()
        # Shows english as a default value 
        # might add full language mode at upcoming update
        self.language_choosen.current(1)
        self.translate_result = Label(frame, text="Translated text",font=('calibre', 10, 'bold'))
        self.translate_result.pack(side=LEFT)
        self.button = Button(myframe, text= "translate",bg = "green", 
         command = lambda:[self.get(), self.lang(), self.translate(language, text_value)], width= 20)
        self.button.pack(side=LEFT)
        self.save = Button(myframe,text="Save",bg = "green", command= self.save_file, width = 20)
        self.save.pack(side=LEFT)
        

    def get(self):
        global text_value
        text_value = self.text_box.get(1.0,END)

    def  lang(self):
        global language
        language = self.language_choosen.get()


    def save_file(self):
        file_save = asksaveasfile(mode='w', defaultextension="*.txt")

        if file_save:
            file_save.write(translated)
            file_save.close()


    def translate(self, lang, _text):
        global translated
        translated = pylator.translate(lang, _text)
        self.translate_result["text"] = f"{translated}"

def main():
    root = Tk()
    root.title('Text Translate')
    root.resizable(False,False)
    app = TextTranslate(root)
    root.mainloop()

if __name__ == "__main__":
    main()