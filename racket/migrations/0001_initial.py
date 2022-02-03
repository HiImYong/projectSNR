# Generated by Django 3.2.9 on 2022-02-03 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Racket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='라켓이름')),
                ('weight', models.IntegerField(default=0, verbose_name='라켓무게')),
                ('pattern', models.CharField(max_length=20, verbose_name='라켓스트링패턴')),
                ('headsize', models.IntegerField(default=0, verbose_name='라켓헤드사이즈')),
                ('length', models.FloatField(default=0, verbose_name='라켓길이')),
                ('balance', models.IntegerField(default=0, verbose_name='라켓밸런스')),
                ('regDateInt', models.IntegerField(default=0, verbose_name='라켓생산년도')),
                ('manufacturer', models.CharField(default='등록전', max_length=20, verbose_name='제조사')),
                ('like', models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RacketDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminReview', models.TextField()),
                ('adminPower', models.FloatField(default=0, verbose_name='운영자파워평점')),
                ('adminSpin', models.FloatField(default=0, verbose_name='운영자스핀평점')),
                ('adminManeuverability', models.FloatField(default=0, verbose_name='운영자조작성평점')),
                ('adminStability', models.FloatField(default=0, verbose_name='운영자면안정성평점')),
                ('adminComfort', models.FloatField(default=0, verbose_name='운영자안락함평점')),
                ('adminAvgScore', models.FloatField(default=0, verbose_name='평점평균')),
                ('racket', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='detail', to='racket.racket')),
            ],
        ),
    ]
