from datetime import datetime
from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def format_created_date(created):
    if created.date() == timezone.now().date():
        return created.strftime('Today %I:%M %p')
    return created.strftime("%b %d, %Y %I:%M %p")