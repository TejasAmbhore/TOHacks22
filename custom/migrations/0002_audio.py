# Generated by Django 3.2.12 on 2022-05-31 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convert_audio', models.FileField(upload_to='audio/')),
            ],
        ),
    ]
