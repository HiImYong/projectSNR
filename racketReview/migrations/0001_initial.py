# Generated by Django 3.2.9 on 2022-03-29 01:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('racket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RacketReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitorReview', models.TextField()),
                ('visitorScore', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('reg_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('visitorAccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('visitorRacket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='racket.racket')),
            ],
        ),
    ]
