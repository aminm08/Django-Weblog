# Generated by Django 4.1.1 on 2022-09-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_post_blogpost_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='short_description',
            field=models.TextField(default='blank', verbose_name='short description'),
            preserve_default=False,
        ),
    ]
