# Generated by Django 4.1.3 on 2022-12-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='filemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='cbapp/static')),
            ],
        ),
    ]
