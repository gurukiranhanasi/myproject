# Generated by Django 4.2.7 on 2023-12-06 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobpost', '0002_remove_submit_user_submit_jobtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='addpost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=200)),
                ('post_type', models.CharField(max_length=200)),
                ('post_title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
