# Generated by Django 3.0.3 on 2022-03-15 02:55

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
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='선수이름')),
                ('birth', models.DateTimeField(default='0000.00.00', verbose_name='생일')),
                ('turnPro', models.IntegerField(default=0, verbose_name='프로전향')),
                ('weight', models.IntegerField(default=0, verbose_name='몸무게')),
                ('height', models.FloatField(default=0, verbose_name='키')),
                ('country', models.CharField(default='등록전', max_length=20, verbose_name='국가')),
                ('forehand', models.CharField(default='등록전', max_length=20, verbose_name='포핸드사용손')),
                ('backhand', models.CharField(default='등록전', max_length=20, verbose_name='백핸드종류')),
                ('racketBrand', models.CharField(default='등록전', max_length=20, verbose_name='선수이름')),
                ('racketUse', models.CharField(default='등록전', max_length=20, verbose_name='사용라켓')),
                ('racketWeight', models.IntegerField(default=0, verbose_name='라켓무게')),
                ('countLike', models.IntegerField(default=0, verbose_name='좋아요개수')),
                ('like', models.ManyToManyField(related_name='likePlayer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='playerCharacteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Characteristic', models.CharField(max_length=20, verbose_name='선수특성')),
                ('aboutCharacteristic', models.CharField(max_length=20, verbose_name='선수특성설명')),
                ('playerJoin', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Player', to='player.Player')),
            ],
        ),
    ]
