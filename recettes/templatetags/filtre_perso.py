from django import template
import random

register = template.Library()


@register.filter
def first_letters(iterable):
    result = ""
    result = iterable[:1]
    # print(result)
    return result


@register.simple_tag
def random_photo(a, b):
    photo = [a, b]
    return random.choice(photo)


