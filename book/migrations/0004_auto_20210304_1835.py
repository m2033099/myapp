# Generated by Django 3.1.2 on 2021-03-04 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_auto_20210304_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
