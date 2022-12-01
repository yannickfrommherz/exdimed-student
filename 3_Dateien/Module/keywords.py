def get_freqs(text, stopwords):
    """Takes in text as string and stopwords as list, returns frequency for all types in text, excluding stopwords."""

    words = text.split()

    preprocessed_words = []

    for word in words:
        word = word.lower() 
        word = word.strip(".,():")
        if word in stopwords:
            continue
        preprocessed_words.append(word)

    types = set(preprocessed_words)

    freq_dict = {} 

    for type_ in types:
        freq_dict[type_] = preprocessed_words.count(type_)

    freq_sorted = sorted(freq_dict.items(), key = lambda x: x[1], reverse=True)

    return(freq_sorted)