# Generated by Django 5.0.6 on 2024-06-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='Breakfast',
            field=models.IntegerField(verbose_name='Breakfast'),
        ),
        migrations.AlterField(
            model_name='food',
            name='Dinner',
            field=models.IntegerField(verbose_name='Dinner'),
        ),
        migrations.AlterField(
            model_name='food',
            name='Food_items',
            field=models.TextField(max_length=255, verbose_name='Food_items'),
        ),
        migrations.AlterField(
            model_name='food',
            name='Lunch',
            field=models.IntegerField(verbose_name='Lunch'),
        ),
        migrations.AlterField(
            model_name='food',
            name='VegNonVeg',
            field=models.IntegerField(verbose_name='VegNonVeg'),
        ),
    ]