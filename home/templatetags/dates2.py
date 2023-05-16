import datetime
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_day_month(date):
	print(date.strftime("%d.%m"))
	return date.strftime("%d.%m")

