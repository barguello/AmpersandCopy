from django import template

register = template.Library()

@register.filter(name = "format_number")
def format_number(number):
    return str(('%f' % number).rstrip('0').rstrip('.'))
