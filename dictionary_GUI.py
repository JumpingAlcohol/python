import tkinter as tk
import tkinter.messagebox

class Word:
    def __init__(self,english_name:str,chinese_name:str)->None:
        self.english_name=english_name
        self.chinese_name=chinese_name

    def __str__(self)->str:
        return f"{self.english_name},{self.chinese_name}"

def read_file(file_name: str) -> list:
    with open(file_name, "r",encoding="utf-8") as f:
        words = []
        while True:
            line1 = f.readline().strip()  # 读取英文名称
            if not line1:
                break  # 文件读取结束
            line2 = f.readline().strip()  # 读取中文名称
            if not line2:
                break  # 文件不完整
            word_record = Word(line1, line2)
            words.append(word_record)
    return words

def write_file(file_name:str):
    global eng_value,chi_value
    f=open(file_name,"a",encoding="utf-8")
    f.write(eng_value+"\n")
    f.write(chi_value+"\n")
    f.close()

def LinearSearch_eng(words:list,word:str):
    i=0
    while i<len(words) and words[i].english_name!=word:
        i+=1
    if i>=len(words):
        return -1
    else:
        return i
    
def LinearSearch_chi(words:list,word:str):
    i=0
    while i<len(words) and words[i].chinese_name!=word:
        i+=1
    if i>=len(words):
        return -1
    else:
        return i
    
def insertionSort(words:list):
    global words_record
    for i in range(1,len(words)):
        j=i-1
        InsertV=words[i]
        InsertV_eng=words[i].english_name
        while j>=0 and InsertV_eng<words[j].english_name:
            words[j+1]=words[j]
            j-=1
        words[j+1]=InsertV
    clear_text()
    text_print(words_record,words)
    return words

def create_button(window, text, command):
        button = tk.Button(window, text=text, command=command)
        button.pack()
        return button

def create_label(window, text,font):
    label = tk.Label(window, text=text,font=font)
    label.pack()
    return label

def create_entry(window, textvariable, font):
    entry = tk.Entry(window,textvariable=textvariable,font=font)
    entry.pack()
    return entry

def create_text(window,width,height):
    text = tk.Text(window,width=width,height=height)
    text.pack()
    return text
    
def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()

def init_window():
    global window
    window = tk.Tk()
    window.title("Dictionary")
    window.geometry("500x300")
    return window

def welcome():
    global window
    clear_window(window)
    create_label(window, "Welcome to Dictionary",('Arial', 20)).place(x=30, y=50, anchor='nw')
    create_button(window, "Translation", translation_action).place(x=30, y=100, anchor='nw')
    create_button(window, "Adding", adding_action).place(x=30, y=150, anchor='nw')
    create_button(window, "Exit", lambda:window.destroy()).place(x=30, y=200, anchor='nw')

def clear_label():
    global eng_word,chi_word
    eng_word.delete(0,tk.END) 
    chi_word.delete(0,tk.END) 

def clear_text():
    global words_record
    words_record.delete(1.0,tk.END)

def text_print(words_record,words):
    for w in words:
        words_record.insert("insert",w)
        words_record.insert("insert","\n")

def translate():
    global window,words,string_eng_word,string_chi_word
    words=read_file("TOFEL.txt")
    eng_value=string_eng_word.get()
    chi_value=string_chi_word.get()
    if eng_value != "":
        index=LinearSearch_eng(words,eng_value)
        if index!=-1:
            chi_value=words[index].chinese_name
            chi_word.insert(0,chi_value)
        else:
            tkinter.messagebox.showerror(title='Hi', message='Not in the dictionary！') 
    elif chi_value != "":
        index=LinearSearch_chi(words,chi_value)
        if index!=-1:
            eng_value=words[index].english_name
            eng_word.insert(0,eng_value)
        else:
            tkinter.messagebox.showerror(title='Hi', message='Not in the dictionary！') 
    return eng_value,chi_value

def add():
    global window,string_eng_word,string_chi_word,eng_value,chi_value
    eng_value=string_eng_word.get()
    chi_value=string_chi_word.get()
    if eng_value != "" and chi_value != "":
        write_file("TOFEL.txt")
        tkinter.messagebox.showinfo(title='Hi', message='Added successfully！') 
        adding_action()
    else: 
        tkinter.messagebox.showerror(title='Hi', message='Please enter the words！')


def translation_action():
    global window,eng_word,chi_word,string_eng_word,string_chi_word
    clear_window(window)
    create_label(window, "English",('Arial', 10)).place(x=30, y=50, anchor='nw')
    string_eng_word = tk.StringVar()
    string_chi_word = tk.StringVar()
    eng_word = create_entry(window,string_eng_word,('Arial', 14))
    eng_word.place(x=30, y=80, anchor='nw')
    create_label(window, "中文",('Arial', 10)).place(x=30, y=110, anchor='nw')
    chi_word = create_entry(window,string_chi_word,('Arial', 14))
    chi_word.place(x=30, y=140, anchor='nw')
    create_button(window, "Translate", translate).place(x=30, y=170, anchor='nw')
    create_button(window, "Clear", clear_label).place(x=100, y=170, anchor='nw')
    create_button(window, "Return to the main menu", lambda:welcome()).place(x=30, y=220, anchor='nw')


def adding_action():
    global window,words,words_record,string_eng_word,string_chi_word,eng_word,chi_word
    words=read_file("TOFEL.txt")
    clear_window(window)
    create_label(window, "English",('Arial', 10)).place(x=30, y=50, anchor='nw')
    string_eng_word = tk.StringVar()
    string_chi_word = tk.StringVar()
    eng_word = create_entry(window,string_eng_word,('Arial', 14))
    eng_word.place(x=30, y=80, anchor='nw')
    create_label(window, "中文",('Arial', 10)).place(x=30, y=110, anchor='nw')
    chi_word = create_entry(window,string_chi_word,('Arial', 14))
    chi_word.place(x=30, y=140, anchor='nw')
    create_button(window, "Add", add).place(x=30, y=170, anchor='nw')
    create_button(window, "Clear", clear_label).place(x=100, y=170, anchor='nw')
    create_button(window, "Sort", lambda:insertionSort(words)).place(x=30, y=210, anchor='nw')
    create_button(window, "Return to the main menu", lambda:welcome()).place(x=30, y=250, anchor='nw')
    words_record=create_text(window,150,70)
    words_record.place(x=450, y=10, anchor='nw')
    text_print(words_record,words)
 


if __name__=="__main__":   
    
    init_window()
    welcome()

    window.mainloop()