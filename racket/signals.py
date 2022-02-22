from django.db.models import Avg
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from racket.models import Racket
from racketReview.models import RacketReviewModel


@receiver(post_save, sender=RacketReviewModel)
def on_post_product_save(sender, instance: RacketReviewModel, created: bool, raw: bool, using, update_fields, **kwargs):
    racket: Racket = instance.visitorRacket

    getVisitorAvgScore = racket.racketreviewmodel_set.aggregate(Avg('visitorScore'))['visitorScore__avg']
    racket.visitorAvgScore = getVisitorAvgScore
    racket.save()
