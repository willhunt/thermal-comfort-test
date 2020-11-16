# Generated by Django 3.1.3 on 2020-11-16 11:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjectivetest', '0002_auto_20201116_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]
