from django import template

register = template.Library()

@register.filter(name='lower')
def lower(value):
    return value.lower()

@register.filter(name='reverse_string')
def reverse_string(value):
    return value[::-1]

@register.filter(name='selam')
def selam(value):
    return f"Selam {value}"