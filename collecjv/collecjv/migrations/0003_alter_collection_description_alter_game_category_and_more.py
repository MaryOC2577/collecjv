# Generated by Django 4.2.2 on 2024-01-15 17:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collecjv", "0002_alter_gamecompany_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="collection",
            name="description",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="game",
            name="category",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="game",
            name="description",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name="platform",
            name="description",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
