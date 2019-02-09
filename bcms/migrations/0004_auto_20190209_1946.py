# Generated by Django 2.1.5 on 2019-02-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcms', '0003_map_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggest_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='map_data',
            old_name='imformation',
            new_name='information',
        ),
        migrations.AlterField(
            model_name='map_data',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]