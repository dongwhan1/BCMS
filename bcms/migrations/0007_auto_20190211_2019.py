# Generated by Django 2.1.5 on 2019-02-11 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcms', '0006_auto_20190210_0123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='board',
        ),
        migrations.AddField(
            model_name='suggest_data',
            name='board',
            field=models.IntegerField(blank=True, choices=[(1, 'BCMS 앱에 관한 건의사항-추가/개선 했으면 하는 기능'), (2, '학교나 기숙사 시설에 관한 건의사항')], default=1),
        ),
    ]