# Generated by Django 5.0.7 on 2024-07-20 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_alter_author_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]