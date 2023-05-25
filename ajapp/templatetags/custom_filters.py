from django import template

register = template.Library()

@register.filter
def get_by_key(dictionary, key):
    return dictionary.get(key)