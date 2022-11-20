from django import template
from django.template.defaultfilters import register
from datetime import datetime


register = template.Library()

@register.filter(name="translatedName")
def get_translated_name(strg):
    match strg:
        #roomtype
        case 'double':
            return 'Doppelzimmer'
        case 'triple':
            return 'Dreibettenzimmer'
        case 'single':
            return 'Einzelbettzimmer'
        case 'apartment':
            return 'Apartment'
        case 'suit':
            return 'suit'
        case 'family':
            return 'Familienzimmer'
        case 'studio':
            return 'Atelier'
        case 'villa':
            return 'Villa'
        #Mealtypes
        case 'none':
            return 'ohne Allem'
        case 'breakfast':
            return 'Frühstück'
        case 'allinclusiv':
            return 'Allinclusive'
        case 'halfboard':
            return 'Halbpension'
        case 'half':
            return 'Halbpension'
        case 'halfboeardplus':
            return 'Halbpension Plus'
        case _:
            print(strg)
            return strg

@register.filter(name="dateFormat")
def date_format(date, strg):
    if isinstance(date, datetime):
        return datetime.strftime(date, strg)
    else:
        return str("{date} is no instance of datetime!").format(date=date)

@register.filter(name="duration_delta")
def get_duration(begin, ende):
    duration = ende - begin
    return str(duration)[:4]

@register.filter(name="duration_delta_format")
def duration_delta_format(duration, digit):
    return duration[:digit]