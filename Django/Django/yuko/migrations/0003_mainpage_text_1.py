# Generated by Django 4.0.5 on 2022-07-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuko', '0002_alter_mainpage_description_alter_mainpage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpage',
            name='text_1',
            field=models.CharField(blank=True, max_length=200, verbose_name='картка 1'),
        ),
    ]
