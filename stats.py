def get_num_words (book):
    words = book.split()
    count = len(words)
    return count

def get_char_count (text):
    text_lower = text.lower()
    char_freq = {}
    
    for char in text_lower:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1

    return char_freq

def sort_on(items):
    return items["count"]

def sort_char (freq):
    char_dict = []
    for key in freq:
         if(key.isalpha()):
            char_dict.append({"char":key, "count":freq[key]})

    char_dict.sort(reverse=True,key=sort_on)
    return char_dict
