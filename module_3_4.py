import re

def single_root_woods(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
    return print(same_words)

single_root_woods('Fruit', 'applefruit', 'hoco', "fruit", "Fruit")
single_root_woods('rich', 'richiest', 'Orichalcum', 'cheeRs', 'riCHies')
