from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class UserProfile(models.Model):
    ACTIVITY_LEVEL_CHOICES = [
        ('sedentary', 'Sedentary'),
        ('lightly_active', 'Lightly Active'),
        ('active', 'Active'),
        ('very_active', 'Very Active')
    ]
    
    GOAL_CHOICES = [
        ('l_weight', 'Weight Loss'),
        ('g_weight', 'Weight Gain'),
    ]

    #user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
   
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    weight = models.FloatField()
    height = models.FloatField()
    veg=models.CharField(max_length=10,choices=[('veg','Veg'),('nonveg','Non-veg')])
    goal = models.CharField(max_length=20, choices=GOAL_CHOICES)

    def _str_(self):
        return self.name
    
class food(models.Model):
    Food_items=models.TextField(_('Food_items'),max_length=255)
    Breakfast=models.IntegerField(_('Breakfast'))
    Lunch=models.IntegerField(_('Lunch'))
    Dinner=models.IntegerField(_('Dinner'))
    VegNonVeg=models.IntegerField(_('VegNonVeg'))
    Calories=models.FloatField(_('Calories'))
    Fats=models.FloatField(_('Fats'))
    Proteins=models.FloatField(_('Proteins'))
    Iron=models.FloatField(_('Iron'))
    Calcium=models.FloatField(_('Calcium'))
    Sodium=models.FloatField(_('Sodium'))
    Potassium=models.FloatField(_('Potassium'))
    Carbohydrates=models.FloatField(_('Carbohydrates'))
    Fibre=models.FloatField(_('Fibre'))
    VitaminD=models.FloatField(_('VitaminD'))
    Sugars=models.FloatField(_('Sugars'))


    



