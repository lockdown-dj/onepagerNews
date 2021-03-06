# Generated by Django 3.2.5 on 2021-08-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_eight',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='news',
            name='image_nine',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='news',
            name='image_seven',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='news',
            name='image_six',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AddField(
            model_name='news',
            name='para_nine',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='heading_three',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='news',
            name='heading_two',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_five',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_four',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_one',
            field=models.ImageField(upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_three',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image_two',
            field=models.ImageField(upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='news',
            name='para_eight',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='para_five',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='para_four',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='para_seven',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='para_six',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='para_three',
            field=models.TextField(blank=True),
        ),
    ]
