# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 23:27:01 2020

@author: Vikram
"""
def BreakDown(text):
    import nltk
    nltk.download('punkt')
    from nameparser.parser import HumanName
    import re
    
    def listToString(s):  
    
    # initialize an empty string 
        str1 = ""  
    
    # traverse in the string   
        for ele in s:  
            str1 += ele   
    
    # return string   
        return str1
    
    def get_address(txt):
    
       # txt = "hi a tree has fallen in 1245 22nd street Bandra, Mumbai, MH 400001. Can you look into it?"
        regexp = "[0-9]{1,3} .+, .+, [A-Z]{2} [0-9]{6}"
        address = re.findall(regexp, txt)
        return listToString(address)
    
    def get_human_names(txt):
        tokens = nltk.tokenize.word_tokenize(txt)
        pos = nltk.pos_tag(tokens)
        sentt = nltk.ne_chunk(pos, binary = False)
        person_list = []
        person = []
        name = ""
        for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
            for leaf in subtree.leaves():
                person.append(leaf[0])
            if len(person) > 1: #avoid grabbing lone surnames
                for part in person:
                    name += part + ' '
                if name[:-1] not in person_list:
                    person_list.append(name[:-1])
                   
                name = ''
            person = []
    
        return (person_list)
    
    li=list(get_human_names(text))
    #print(get_address(text))
    li.append(get_address(text))
    text.replace(get_address(text),' ')
    for word in li:
        text=text.replace(word,"")
    li.append(text[1:-1])
    #print (get_human_names(text))
    return li
