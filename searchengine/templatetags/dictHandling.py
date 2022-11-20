from django import template
from django.template.defaulttags import register
from datetime import datetime
from random import randrange

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if dictionary.get(key) != None:
        return dictionary.get(key)
    else:
        return ''

@register.filter
def is_selected_Roomtype(dictionary, compare):
    if dictionary.get('roomtype') != None and dictionary.get('roomtype') == compare:
        return 'selected'

@register.filter
def is_selected_Mealtype(dictionary, compare):
    if dictionary.get('mealtype') != None and dictionary.get('mealtype') == compare:
        return 'selected'

@register.filter
def get_duration(begin, ende):
    duration = str(ende - begin)
    return duration[0:2]

@register.filter
def random_rating(max):
    max = int(max)
    return range(randrange(0, max))

@register.filter
def get_name_rating(number):
    match number:
        case 0:
            return 'oneStars'
        case 1:
            return 'twoStars'
        case 2:
            return 'threeStars'
        case 3:
            return 'fourStars'
        case 4:
            return 'fiveStars'
        case _:
            pass