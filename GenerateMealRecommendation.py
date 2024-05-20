import random
import os
from datetime import datetime, timedelta

def select_recommendation():
    # This loop allows the user to select the type of recommendation they want
    while True:
        print("Select the type of recommendation you would like from the numbers 1-5.")
        print("[1] Seafood \n[2] Pork \n[3] Chicken \n[4] Beef \n[5] Sides")

        user_recommendation = input(">>> ")
        if user_recommendation not in "12345":
            print("\nPlease enter a number from 1-5 that corresponds with your selection.")
        else: 
            break

    # These if statements help pick the type of reservations from the reservation list
    if user_recommendation == "1":
        min_recommendation, max_recommendation = 0, 7

    elif user_recommendation == "2":
        min_recommendation, max_recommendation = 8, 10

    elif user_recommendation == "3":
        min_recommendation, max_recommendation = 11, 13

    elif user_recommendation == "4":
        min_recommendation, max_recommendation = 14, 18

    elif user_recommendation == "5":
        min_recommendation, max_recommendation = 19, 21

    return min_recommendation, max_recommendation

def recommendation_loop(menu_contents, min_recommendation, max_recommendation):
    recommendation_loop = True
    previous_recommendation = ""
    while recommendation_loop:
        print("\n--------------------------------------------------------------------------------\n")
        recommendation, previous_recommendation = meal_recommendation_generator(menu_contents, min_recommendation, max_recommendation, previous_recommendation)
        print(f"We recommend {recommendation}")
        recommendation_loop_question = "Would you like a new recommendation? Enter a number (1-2) to select your option \n[1] Another recommendation \n[2] Exit \n>>> "
        recommendation_loop = menu_exit(recommendation_loop_question)

# This function generates a meal recommendation
def meal_recommendation_generator(menu_contents, min, max, previous_recommendation):
    # This for loop helps ensure that recommendations of the same type are selected
    menu_recommendation = []
    for i in range(len(menu_contents)):
        if i >= min and i <= max:
            menu_recommendation.append(menu_contents[i])
    recommendation = random.choice(menu_recommendation)
    # This ensures that the same recommendation won't be selected twice in a row
    while recommendation == previous_recommendation:
        recommendation = random.choice(menu_recommendation)
    previous_recommendation = recommendation
    return recommendation, previous_recommendation

# This function will determine if the user continues with their process or return to the main menu
def menu_exit(question):
    loop = True
    while loop:
        answer = input(f"{question}")
        if answer in "12":
            loop = False
        else:
            print("Please enter the number (1-2) that corresponds with your selection.")
    if answer == "1":
        loop = True
        return loop
    elif answer == "2":
        loop = False
        return loop