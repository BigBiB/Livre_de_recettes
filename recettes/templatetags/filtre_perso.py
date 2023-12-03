from django import template

register = template.Library()


@register.filter
def first_letters(iterable):
    result = ""
    result = iterable[:1]
    # print(result)
    return result
