from django.db.models import Avg
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from racket.models import Racket
from visitor.models import VisitorReview


@receiver(post_save, sender=VisitorReview)
def on_post_product_save(sender, instance: VisitorReview, created: bool, raw: bool, using, update_fields, **kwargs):
    racket: Racket = instance.visitorRacket

    getVisitorAvgScore = racket.visitorreview_set.aggregate(Avg('visitorScore'))['visitorScore__avg']
    racket.visitorAvgScore = getVisitorAvgScore
    racket.save()
