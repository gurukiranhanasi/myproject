# Generated by Django 4.2.7 on 2023-12-06 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost', '0003_addpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='addpost',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
