# Generated by Django 3.1.1 on 2022-11-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_requestleave'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestleave',
            name='IsDeclined',
            field=models.BooleanField(default=False),
        ),
    ]
