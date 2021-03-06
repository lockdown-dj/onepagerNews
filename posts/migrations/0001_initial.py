# Generated by Django 3.2.6 on 2021-08-17 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_news', models.BooleanField(default=False)),
                ('heading_one', models.CharField(max_length=250)),
                ('heading_two', models.CharField(max_length=250)),
                ('heading_three', models.CharField(max_length=250)),
                ('image_one', models.ImageField(upload_to='static/images/')),
                ('image_two', models.ImageField(upload_to='static/images/')),
                ('image_three', models.ImageField(upload_to='static/images/')),
                ('image_four', models.ImageField(upload_to='static/images/')),
                ('image_five', models.ImageField(upload_to='static/images/')),
                ('para_one', models.TextField()),
                ('para_two', models.TextField()),
                ('para_three', models.TextField()),
                ('para_four', models.TextField()),
                ('para_five', models.TextField()),
                ('para_six', models.TextField()),
                ('para_seven', models.TextField()),
                ('para_eight', models.TextField()),
            ],
        ),
    ]
