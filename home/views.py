from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout,authenticate,login
import pandas as pd
import numpy as np
from .models import UserProfile

# Create your views here.
def index(request):
    return render(request,'index.html')

def loginUser(request):
    uname=request.POST.get('uname')
    password=request.POST.get('password')
    print(uname,password)
    if request.method == 'POST':
        user = authenticate(username=uname, password=password)
        #print(uname,password)
        if user is not None:
            # A backend authenticated the credentials
            login(request,user)
            return redirect('/')
        else:
            return redirect('/login')
            # No backend authenticated the credentials
    return render(request,'form.html')

def signUp(request):
    if request.method=='POST':
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        pass1=request.POST['p1']
        pass2=request.POST['p2']
        data=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=pass1)
        data.save() 
    return render(request,'form.html')
    
def logoutUser(request):
    logout(request)
    return redirect('/login')

def survey(request):
    if request.method=='POST':
        name=request.user.username
        age=request.POST['age']
        gen=request.POST['gender']
        w=request.POST['weight']
        h=request.POST['height']
        v=request.POST['diet2']
        goal=request.POST['goal']

        up=UserProfile(name=name,age=age,gender=gen,weight=1,height=h,veg=v,goal=goal)
        up.save()
        return redirect('/display')

    return render(request,'survey.html')

def display(request):
    df=pd.read_csv('static/food_items.csv')

    def get_user_input():
        user_data = {}

        user_data['age'] = int(input("Enter your age: "))
        user_data['gender'] = int(input("Enter your gender: "))
        user_data['weight'] = float(input("Enter your weight (in kg): "))
        user_data['height'] = float(input("Enter your height (in cm): "))
        user_data['dietary_preferences'] = input("Enter your dietary preferences: ")
        user_data['allergies'] = input("Enter your allergies (if any): ")
        user_data['health_goals'] = int(input("Enter your health goals:(0 for decreasing weight and 1 for increasing weight) "))
        user_data['weight-gainLoss'] = int(input("Enter your gain or loss weight per week"))
        user_data['activity'] = int(input('Enter your activity levels in (0,1,2)'))

        return user_data

    def calc_bmr(weight, height, age, gender):
        #calculate bmr will allow us to further know if the 
        if gender == 0: #if the user is male
            bmr = 10*weight + 6.25*height - 5*age + 5
        else:
            bmr = 10*weight + 6.25*height - 5*age - 161
        return bmr 


    def cacl_calories(bmr, exercise_duration):
        #we gonna calculate the needed caloried to be observed per day when 
        #wanting the maintaining weight

        # little to no exercise 
        if exercise_duration == 0:
            calories_per_day  = bmr * 1.2
        # light exercise --> 1 to 3 times per week
        elif exercise_duration == 1:
            calories_per_day  = bmr * 1.35
        elif exercise_duration == 2: #Moderate exercise 
            calories_per_day = bmr * 1.5
        else: #active/intense exercise 
            calories_per_day = bmr * 1.5

        return calories_per_day

    def cacl_calories(bmr, exercise_duration):
            #we gonna calculate the needed caloried to be observed per day when 
            #wanting the maintaining weight

            # little to no exercise 
            if exercise_duration == 0:
                calories_per_day  = bmr * 1.2
            # light exercise --> 1 to 3 times per week
            elif exercise_duration == 1:
                calories_per_day  = bmr * 1.35
            elif exercise_duration == 2: #Moderate exercise 
                calories_per_day = bmr * 1.5
            else: #active/intense exercise 
                calories_per_day = bmr * 1.5

            return calories_per_day

    def bmi_cal(weight, height):
        bmi = weight/((height/100)**2) 
        if ( bmi < 18.5):
            print('your are underweight')
            print()
            return 2
        elif ( bmi >= 18.5 and bmi < 25):
            print('you are healthy')
            print()
            return 1
        elif ( bmi >=25):
            print('you are obese')
            print()
            return 0 

    def bmi_result(bmi):
        if ( bmi == 2):
            # underweight
            print("Based on the BMI calculation: You are underweight -- Recommend Increase Weight to Maintain the Healthy Condition")
            return "underweight"
        elif ( bmi == 1):
            #healthy
            print
            return "Based on the BMI calculation: You are healthy -- -- Recommend Maintain Weight to Maintain the Healthy Condition"
        elif ( bmi == 0):
            #healthy
            return "Based on the BMI calculation: You are overweight -- Recommend Decrease Weight to Maintain the Healthy Condition"

    user_data = {'age': 19, 'gender': 0, 'weight': 100.0, 'height': 190.0, 'dietary_preferences': 'na', 'allergies': 'na', 'weight-gainLoss':5,'health_goals': 0, 'activity': 2}

    def decrease_weight(current_calories, desire_weight_decrease):

        calories_per_kilogram = 5500

        # Calculate weekly and daily surplus
        weekly_surplus_calories = desire_weight_decrease * calories_per_kilogram
        daily_surplus_calories = weekly_surplus_calories / 7
        target_calorie = current_calories - daily_surplus_calories
        #distribute the distribution between breakfast, lunch and dinner (20 - 40 - 40)
        bf_calorie  = target_calorie * 0.2
        lch_calorie = target_calorie * 0.35
        din_calorie = target_calorie * 0.45

        return abs(bf_calorie), abs(lch_calorie), abs(din_calorie)
    def increase_weight(current_calories, desire_weight_gain):

        calories_per_kilogram = 7700

        # Calculate weekly and daily surplus
        weekly_surplus_calories = desire_weight_gain * calories_per_kilogram
        daily_surplus_calories = weekly_surplus_calories / 7
        target_calorie = current_calories + daily_surplus_calories
        # diverse the the probability of calories consumption of 3 meals accordingly 
        bf_calorie  = target_calorie * 0.2
        lch_calorie = target_calorie * 0.35
        din_calorie = target_calorie * 0.45

        return abs(bf_calorie), abs(lch_calorie), abs(din_calorie)

    def calculate_meal_plan(cal_di_pday):
        # Read the dataset
        df = pd.read_csv('static/food_items.csv')

        # Create temporary dataframes for each meal
        df_temp_breakfast = df[df['Breakfast'] == 1]
        df_temp_lunch = df[df['Lunch'] == 1]
        df_temp_dinner = df[df['Dinner'] == 1]



        # breakfast
        indices = np.random.choice(df_temp_breakfast.index, size=10, replace=False)
        df_temp_breakfast = df_temp_breakfast.loc[indices]

        # lunch
        indices = np.random.choice(df_temp_lunch.index, size=10, replace=False)
        df_temp_lunch = df_temp_lunch.loc[indices]
        # dinner
        indices = np.random.choice(df_temp_dinner.index, size=10, replace=False)
        df_temp_dinner = df_temp_dinner.loc[indices]


        # Variables to store the selected foods
        breakfast_food = []
        lunch_food = []
        dinner_food = []

        # Helper function to process each meal
        def process_meal(df_temp, meal_index):
            meal_food = []
            for values in df_temp['Calories']:
                if cal_di_pday[meal_index] > 0:
                    meal_food.append(df_temp[df_temp['Calories'] == values]['Food_items'].iloc[0])
                    cal_di_pday[meal_index] =  cal_di_pday[meal_index] - values
                    if cal_di_pday[meal_index] <= 0:
                        break
            return meal_food

        # Process each meal
        breakfast_food = process_meal(df_temp_breakfast, 0)
        lunch_food = process_meal(df_temp_lunch, 1)
        dinner_food = process_meal(df_temp_dinner, 2)

        # Return the food lists
        return breakfast_food, lunch_food, dinner_food

    bmr = calc_bmr(user_data['weight'], user_data['height'], user_data['age'], user_data['gender'])

    calories_per_day = cacl_calories(bmr, user_data['activity'])
    bmi = bmi_cal(user_data['weight'],user_data['height'])

    print()
    print(bmi_result(bmi))
    print()

    if(user_data['health_goals'] == 0):
        cal_di_pday = decrease_weight(calories_per_day,user_data['weight-gainLoss'])
    else:
        cal_di_pday = increase_weight(calories_per_day,user_data['weight-gainLoss'])

    # print(cal_di_pday)

    breakfast_food, lunch_food, dinner_food = calculate_meal_plan(list(cal_di_pday))

    bf = ' '.join(breakfast_food)
    lf = ' '.join(lunch_food)
    df = ' '.join(dinner_food)
    context={'v1':bf,'v2':lf,'v3':df}



    return render(request,'display.html',context)
