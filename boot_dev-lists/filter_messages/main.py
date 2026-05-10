def filter_messages(messages):
    filtered_messages = []
    dang_counts = []

    for message in messages:
        words = message.split()
        dangs = 0
        good_words = []
        # good_words = [word for word in words if word != "dang"]
        
        
        for word in words:
            if word == "dang":
                dangs += 1
            else:
                good_words.append(word)
                
        filtered_messages.append(" ".join(good_words))
        dang_counts.append(dangs)

    return filtered_messages, dang_counts