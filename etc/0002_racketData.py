import requests
from django.db import migrations

from racket.models import Racket


def gen_master(apps, schema_editor):
    r = requests.get('https://api.racketlogger.com/rackets')
    data = r.json()
    for element in data:
        Racket(name=element['model'], weight=element['weight']*28.35, pattern=element['pattern'], headsize=element['head_size'],
               length=27, balance=element['balance'], regDateInt=0, visitorAvgScore=0, countLike=0, brand_id=1).save()

class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('racket', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(gen_master)
    ]
