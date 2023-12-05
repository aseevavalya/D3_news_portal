from django import template

register = template.Library()


@register.filter()
def censor(text):
    bad_words = ['аннексии', 'кровь']
    words = text.split()
    censor_list = []
    for word in words:
        if word.lower() in bad_words:
            censor_word = word[0] + '*' * (len(word) - 1)
            censor_list.append(censor_word)
        else:
            censor_list.append(word)
    return ' '.join(censor_list)
