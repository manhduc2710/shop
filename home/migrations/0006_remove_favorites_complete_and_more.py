# Generated by Django 4.2.4 on 2023-09-14 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_alter_carousel_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='favorites',
            name='transaction_id',
        ),
        migrations.AlterField(
            model_name='favorites',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='favorites',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
    ]