from django import template

register = template.Library()

@register.filter
def sortSectionByDayOfWeek(sections):
    for section in sections:
        section.day_of_week_num = section.dayOfWeek()
    return sections

@register.filter
def changePhoneNumber(number):
    if number.find('-') <= 0 and len(number) >= 10:
        first = number[:3]
        center = number[3:6]
        last = number[6:]
        
        return f'{first}-{center}-{last}'
    return number
