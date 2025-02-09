import datetime
from django import template

register = template.Library()

@register.simple_tag
def get_thursdays():
    today = datetime.date.today()
    thursdays = []
    for i in range(12):  # 12 weeks for 3 months
        next_thursday = today + datetime.timedelta((3 - today.weekday() + 7) % 7 + i * 7)
        thursdays.append(next_thursday.strftime('%B %d, %Y'))
    return thursdays