def count_words(text):
    return len(text.split())

def count_characters(text):
    text = text.lower()
    count = {}
    for ch in text:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return count

def dict_to_sorted_list(ch_dict):
    ch_list = []
    for ch in ch_dict:
        ch_list.append({"char": ch, "num": ch_dict[ch]})
    ch_list.sort(reverse=True, key=lambda item: item["num"])
    return ch_list