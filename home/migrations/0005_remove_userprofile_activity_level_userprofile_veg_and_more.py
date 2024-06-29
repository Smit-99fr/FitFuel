# Generated by Django 5.0.6 on 2024-06-29 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_food_breakfast_alter_food_dinner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='activity_level',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='veg',
            field=models.CharField(choices=[('veg', 'Veg'), ('nonveg', 'Non-veg')], default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='goal',
            field=models.CharField(choices=[('l_weight', 'Weight Loss'), ('g_weight', 'Weight Gain')], max_length=20),
        ),
    ]