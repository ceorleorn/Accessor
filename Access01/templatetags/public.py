from django import template
from django.db.models import Count
from django.db.models.functions import TruncMonth

register = template.Library()

@register.inclusion_tag('components/public/navbar.html')
def get_navbar_header():

    return locals()