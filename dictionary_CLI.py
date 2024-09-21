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
    f=open(file_name,"a",encoding="utf-8")
    new_item_eng=input("Enter the new item in english: ")
    new_item_chi=input("Enter the new item in chinese: ")
    f.write(new_item_eng+"\n")
    f.write(new_item_chi+"\n")
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
    for i in range(1,len(words)):
        j=i-1
        InsertV=words[i]
        InsertV_eng=words[i].english_name
        while j>=0 and InsertV_eng<words[j].english_name:
            words[j+1]=words[j]
            j-=1
        words[j+1]=InsertV
    return words


if __name__=="__main__":   
    print("      "+"Dictionary")
    print("*"*25)
    print("1.english-chinese search")
    print("2.chinese-english search")
    print("3.sort file")
    print("4.append a new item")
    print("5.quit")
    print("*"*25)
    while 1:
        choice=int(input("Please input your function choice:"))
        words=read_file("TOFEL.txt")
        if choice == 5:
            print("BYE")
            break
        while 1:
            match choice:
                case 1:
                    word=input("Enter the word. Enter 'q' to quit: ")
                    if word != "q":
                        index=LinearSearch_eng(words,word)
                        if index!=-1:
                            print(words[index].chinese_name)
                        else:
                            print("Not in the dictionary")
                    else:
                        break
                case 2:
                    word=input("Enter the word. Enter 'q' to quit: ")
                    if word != "q":
                        index=LinearSearch_chi(words,word)
                        if index!=-1:    
                            print(words[index].english_name)
                        else:
                            print("Not in the dictionary")
                    else:
                        break
                case 3:
                    words=insertionSort(words)
                    for w in words:
                        print(w)
                    break
                case 4:
                    write_file("TOFEL.txt")
                    break