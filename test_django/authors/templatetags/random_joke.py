from random import choice
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


jokes = [
    'asd',
    'qwe',
    'zxc',
]


@register.simple_tag()
def joke(index=None):
    if index is None or not isinstance(index, int) or index >= len(jokes):
        a_joke = choice(jokes)
    else:
        a_joke = jokes[index]
    return mark_safe(f'<p>{a_joke}</p>')
