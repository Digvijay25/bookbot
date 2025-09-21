def get_num_words(text):
    word_count = len(text.split())
    return word_count

def get_character_count(text):
    lower_text = text.lower()
    word_count = {}
    
    for i in lower_text: 
        if i in word_count:
            word_count[i] += 1 
        else: 
            word_count[i] = 1
        
    return word_count

def sorted_dictionary(d):
    final_list = []
    for i in d:
        if i.isalpha():
            final_list.append({"char": i, "num": d[i]})
    final_list.sort(reverse=True, key=lambda x: x["num"])
    return final_list


    
    
        


        
    

    