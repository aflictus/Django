from django import template

register = template.Library()


@register.filter
def pop_space(value):
    value = value.replace("Space", "")
    return value

@register.filter
def del_space(value):
    value = value.replace(" ", "")
    return value
