from django.contrib import admin

from account.models import User
from player.models import Player, playerCharacteristic
from playerReview.models import PlayerReviewModel
from racket.models import RacketDetail, Racket
from visitor.models import VisitorReview
# Register your models here.

admin.site.register(VisitorReview)
admin.site.register(RacketDetail)
admin.site.register(Player)
admin.site.register(playerCharacteristic)
admin.site.register(Racket)
admin.site.register(User)


