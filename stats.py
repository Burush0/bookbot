def get_word_count(contents):
    lst = contents.split()
    return len(lst)

def get_char_freq(contents):
    lowercase = contents.lower()
    freq = {}
    for char in lowercase:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1
    return freq

def sort_on(dict):
    return dict["freq"]

def sort_freq(dict):
    lst = []
    for key in dict:
        lst.append({"char": key, "freq": dict[key]})
    lst.sort(reverse=True, key=sort_on)
    return lst