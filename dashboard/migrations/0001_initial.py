# Generated by Django 4.2.1 on 2023-06-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='wa_camp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('camp_name', models.CharField(max_length=50)),
                ('response', models.TextField(blank=True, null=True)),
                ('numbers', models.CharField(max_length=15)),
            ],
        ),
    ]
