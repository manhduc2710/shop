# Generated by Django 4.2.4 on 2023-09-11 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_date_order_favorites_date_favorite_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('title', models.CharField(max_length=150)),
                ('sub_title', models.CharField(max_length=100)),
            ],
        ),
    ]
