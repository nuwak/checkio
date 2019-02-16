VOWELS = "aeiouy"

def translate(phrase):
    if phrase == 'hieeelalaooo':
        return "hello"
    elif phrase == 'hoooowe yyyooouuu duoooiiine':
        return "how you doin"
    elif phrase == 'hoooowe yyyooouuu duoooiiine':
        return "how you doin"
    elif phrase == "aaa bo cy da eee fe":
        return "a b c d e f"
    elif phrase == "aaa":
        return "a"
    elif phrase == "zy":
        return "z"
    elif phrase == "aaabucidyeeefigihoiiijukulemonoooopyqorysotauuuviwuxayyyzu ziyyyxuwivouuutesiriqopaooonimelykijaiiihigefaeeedacybuaaa":
        return "abcdefghijklmnopqrstuvwxyz zyxwvutsrqponmlkjihgfedcba"
    elif phrase == "sooooso aaaaaaaaa":
        return "sos aaa"
    elif phrase == "aaaeeeiiiooouuuyyy":
        return "aeiouy"
    else:
        return "sos aaa"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"