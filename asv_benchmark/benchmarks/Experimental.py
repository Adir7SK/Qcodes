import time
def alphabetic_order(one):
    word = list(one.lower())
    abword = ""
    i = 0
    while len(word) > i:
        if word[i] != chr(ord('z')+1) and word[i] != " ":
            w = word[i]
            d = i
            for j in range (i, len(word)):
                if w > word[j] and word[j] != " ":
                    w = word[j]
                    d = j
            abword += w
            if i != d:
                i = i-1
            word[d] = chr(ord('z')+1)
        i += 1
    #print (abword)
    return abword


def unique_chars(word):

    unique = ""
    for i in range (len(word)):
        unique += chr(ord(word[i])*2 + 2)
    print (unique)
    return unique



def longest_word(sentence):
    WordsLengths = []
    i = 0
    while len(sentence)> i:
        j = i
        while len(sentence) > j and sentence[j] != " ":
            j += 1
        if j > i:
            WordsLengths.append(j-i)
        i = j+1
    print (WordsLengths)

    longest = 0
    r, m = 0, 0
    for i in range(len(WordsLengths)):
        if WordsLengths[i] > longest:
            longest = WordsLengths[i]
            r = m
        m += WordsLengths[i] + 1
    ToPrint = ""
    while len(sentence) > r and sentence[r] != " ":
        ToPrint += sentence[r]
        r+=1
    #print (ToPrint)
    return ToPrint

def wait():
    time.sleep(0.5)
