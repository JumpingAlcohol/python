import tkinter as tk
import tkinter.messagebox

class Word:
    def __init__(self, english_name: str, chinese_name: str) -> None:
        self.english_name = english_name
        self.chinese_name = chinese_name

    def __str__(self) -> str:
        return f"{self.english_name},{self.chinese_name}"

# 读取文件函数
def read_file(file_name: str) -> list:
    with open(file_name, "r", encoding="utf-8") as f:
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

# 写入文件函数
def write_file(file_name: str):
    f = open(file_name, "a", encoding="utf-8")
    new_item_eng = input("Enter the new item in English: ")
    new_item_chi = input("Enter the new item in Chinese: ")
    f.write(new_item_eng + "\n")
    f.write(new_item_chi + "\n")
    f.close()

# 英文单词线性查找
def LinearSearch_eng(words: list, word: str):
    i = 0
    while i < len(words) and words[i].english_name != word:
        i += 1
    if i >= len(words):
        return -1
    else:
        return i

# 创建按钮
def create_button(window, text, command):
    button = tk.Button(window, text=text, command=command)
    button.pack()
    return button

# 创建标签
def create_label(window, text, font):
    label = tk.Label(window, text=text, font=font)
    label.pack()
    return label

# 创建文本输入框
def create_entry(window, textvariable, font):
    entry = tk.Entry(window, textvariable=textvariable, font=font)
    entry.pack()
    return entry

# 主要的界面和事件处理
def main_action():
    global string_eng_word
    global string_chi_word

    # 清空窗口内容
    for widget in window.winfo_children():
        widget.destroy()

    # 创建英文单词输入框
    string_eng_word = tk.StringVar()  # StringVar 变量绑定
    create_label(window, "Enter English Word:", ("Arial", 14))
    create_entry(window, string_eng_word, ("Arial", 14))

    # 创建中文单词输入框
    string_chi_word = tk.StringVar()  # StringVar 变量绑定
    create_label(window, "Enter Chinese Translation:", ("Arial", 14))
    create_entry(window, string_chi_word, ("Arial", 14))

    # 创建提交按钮
    create_button(window, "Submit", submit_action)

# 提交处理函数
def submit_action():
    eng_word = string_eng_word.get()  # 获取 Entry 的值
    chi_word = string_chi_word.get()  # 获取 Entry 的值

    if eng_word == "" or chi_word == "":
        tk.messagebox.showerror("Error", "Both fields must be filled!")
    else:
        print(f"English: {eng_word}, Chinese: {chi_word}")
        # 在这里执行进一步的处理，比如保存数据

# 创建主窗口
window = tk.Tk()
window.geometry("400x300")
main_action()  # 显示主界面

window.mainloop()