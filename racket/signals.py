from django.db.models import Avg
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver

from racket.models import Racket
from racketReview.models import RacketReviewModel


@receiver(post_save, sender=RacketReviewModel)
def on_post_product_save(sender, instance: RacketReviewModel, created: bool, raw: bool, using, update_fields, **kwargs):
    racket: Racket = instance.visitorRacket

    getVisitorAvgScore = racket.racketreviewmodel_set.aggregate(Avg('visitorScore'))['visitorScore__avg']
    racket.visitorAvgScore = getVisitorAvgScore
    racket.save()


@receiver(post_delete, sender=RacketReviewModel)
def delete_review(sender, instance, **kwargs):
    racket: Racket = instance.visitorRacket
    getVisitorAvgScore = racket.racketreviewmodel_set.aggregate(Avg('visitorScore'))['visitorScore__avg']
    racket.visitorAvgScore = getVisitorAvgScore
    racket.save()