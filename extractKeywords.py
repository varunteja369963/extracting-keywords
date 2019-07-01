import re

def keywordsExtract():
    sentence = input("Enter your string: ")
    words_list = []
    keywords_list = []
    userless_list = ["in", "on", "the", "hii", "and", "for", "if", "the", "else", "then", "but", "of", "then",  "or", "get", "put", "why", "how", "are", "you", "is", "contain", "this", "a", "an", "iff", "hello", "what"]
    word = ""
    for letter in sentence:
        if letter == " ":
            words_list.append(word)
            word = ""
        else:
            word += letter
    words_list.append(word)
    for keyword in words_list:
        print(keyword)
        if keyword not in useless_list:
            regEx1 = re.findall(r"ed\B", keyword)
            regEx2 = re.search(r"ing\B", keyword)
            if (regEx1):
                continue
            else:
                keywords_list.append(keyword)
    print("\n")
    print("_________________________")
    for final_keywords in keywords_list:
        print(final_keywords)
    print("___________________________")
keywordExtract()            
    
    
