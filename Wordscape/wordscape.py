import sys
import os




def anagrams(letters, pre = "", found = []) :
    index = 0
    #base case
    if not ' ' in pre and pre in wordList and not pre in found:
        print(pre)
        found.append(pre)

    #standard case
    elif ' ' in pre :
        for i in range(len(pre)) :
            if pre[i] == ' ' :
                index = i
                break
        for i in range(len(letters)) :

            anagrams(letters[ : i] + letters[i + 1 : ], pre[ : index] + letters[i] + pre[index + 1 : ], found)


def binary_search(ary, item, offset = 0) :
    """Iterative binary search method. 
    ary is an array which shrinks with each call. 
    offset tracks where the current array would fall in the original
    item is the item to find.
    Returns the index if found, None if not."""
    
    start = 0
    end = len(ary) - 1
    found = False
    middle = 0

    while True :
        middle = (end - start) // 2

        if start > end :
            found = False
            break
        elif ary[middle] == item :
            found = True
            break
        elif ary[middle] < item :
            start = middle + 1
        else :
            end = middle - 1

    if found :
        return middle
    else :
        return None






    




#get dictionary for optimization
class dictionary :
    def __init__(self, file) :
        self.wordList = list(file)

        for i in range(len(self.wordList) - 1) :
            self.wordList[i] = self.wordList[i][ : len(self.wordList[i]) - 1]

    

        
    def __contains__(self, item) :
        return item in self.wordList
        return binary_search(self.wordList, item) != None




file = open("words_alpha.txt", 'r')
wordList = dictionary(file)
file.close()

pre=''
found = []
newWord = False
while(True) :
    if pre == "<exit>" :
        break
    letters = input("What letters? ")
    if letters == "666" or letters == "<exit>":
        break
    while(True) :

        pre = input("Format: ")

        options = letters
        for letter in pre :
            if letter != ' ' :
                i = 0
                while i < len(options) :
                    if options[i] == letter :
                        options = options[ : i] + options[i + 1 : ]
                        break
                    i += 1


        if pre == "666" or pre == "<exit>":
            break
        elif pre == "<all>" :
            pre = []
            for i in range(3, len(options) + 1, 1) :
                toAppend = ' ' * i
                pre.append(toAppend)
            for i in pre :
                anagrams(options, i, found)
        else :
            anagrams(options, pre, found)
            found = []



        


