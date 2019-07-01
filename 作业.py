
#反转字符串中的单词，"   I  love china!"--》 china! love i
#缺点是： 多个空格就不能保留下来
def reverseStrByWord(s):
    listWord = s.split(" ")
    listWord.reverse()
    return " ".join(listWord)
# print(reverseStrByWord("I love china!"))
#反转单词改进版
    #首先定义一个一个反转任意一个单词的方法
def myReverse(list,start,end):
    while start < end:
        # print("start:"+str(start)+" end:"+str(end))
        list[start],list[end] = list[end],list[start]
        start += 1
        end -= 1
    #然后开始写单词反转的方法
def reverseSentence():
    sentense = "i love  china!   "
    listSentence = list(sentense) #['i', ' ', 'l', 'o', 'v', 'e', ' ', ' ', 'c', 'h', 'i', 'n', 'a', '!', ' ', ' ', ' ']
    index=0
    while index < len(listSentence):
        if listSentence[index] != " ":
            end = index
            while (end+1 < len(listSentence)) and (listSentence[end+1]!=" ") :
                end +=1

            print("index:" + str(index) + " end:" + str(end))
            myReverse(listSentence,index,end)
            index = end+1
        else:
            index +=1

    listSentence.reverse()
    # print(listSentence)
    print("".join(listSentence))

reverseSentence()

#给定一个范围容器，和一个值A，从容器中找到相邻2位加起来等于