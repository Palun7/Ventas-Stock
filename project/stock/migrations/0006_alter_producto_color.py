# Generated by Django 5.0.4 on 2024-06-05 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_producto_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='color',
            field=models.CharField(max_length=100),
        ),
    ]