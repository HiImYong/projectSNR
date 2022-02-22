from django.contrib import admin

from account.models import User
from player.models import Player, playerCharacteristic
from playerReview.models import PlayerReviewModel
from racket.models import RacketDetail, Racket
from racketReview.models import RacketReviewModel
# Register your models here.

admin.site.register(RacketReviewModel)
admin.site.register(RacketDetail)
admin.site.register(Player)
admin.site.register(playerCharacteristic)
admin.site.register(Racket)
admin.site.register(User)


