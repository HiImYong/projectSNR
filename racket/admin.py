from django.contrib import admin

from racket.models import RacketDetail
from visitor.models import VisitorReview
# Register your models here.

admin.site.register(VisitorReview)
admin.site.register(RacketDetail)

