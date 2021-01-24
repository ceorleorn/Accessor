from django import template
from django.db.models import Count
from django.db.models.functions import TruncMonth

register = template.Library()
