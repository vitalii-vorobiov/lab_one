def count_chars(sen):
    import string
    if len(sen) > 0:
        if sen[0] in string.ascii_uppercase:
            return [1+count_chars(sen[1:])[0], count_chars(sen[1:])[1]]
        elif sen[0] in string.ascii_lowercase:
            return [count_chars(sen[1:])[0], 1+count_chars(sen[1:])[1]]
        else:
            return count_chars(sen.replace(sen[0], ''))
    else:
        return [0, 0]

print(count_chars(("wAt’rh7rJjoa")))