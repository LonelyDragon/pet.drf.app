from django.contrib import admin
from .models import Pool, Choice
# Register your models here.

models = [Pool, Choice]
for model in models:
    admin.site.register(model)