# Generated by Django 4.2.2 on 2023-07-22 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rent", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rental",
            name="price",
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6),
        ),
    ]
