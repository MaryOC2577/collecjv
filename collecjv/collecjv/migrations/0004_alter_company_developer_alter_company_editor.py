# Generated by Django 4.2.2 on 2023-08-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("collecjv", "0003_alter_game_company_alter_game_state"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="developer",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="company",
            name="editor",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
