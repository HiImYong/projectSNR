from django.contrib import admin

# Register your models here.
from feedback.models import Question

admin.site.register(Question)