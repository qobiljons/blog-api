# Generated by Django 5.0.7 on 2024-07-15 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_author_alter_blog_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogs', to='blogs.author'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='published',
            field=models.CharField(choices=[('draft', '❌'), ('published', '✅')], default='draft', max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='blog',
            unique_together={('title', 'author')},
        ),
    ]