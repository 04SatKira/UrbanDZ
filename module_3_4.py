def single_root_words(root_word, *other_words):
    same_words =[]
    for item in other_words:
        if root_word.lower() in item.lower() or item.lower() in root_word.lower():
            same_words.append(item)
    print(same_words)
single_root_words('rich', 'rich', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')