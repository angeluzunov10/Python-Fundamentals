days_of_trip = int(input())
budget = float(input())
number_of_people = int(input())
price_of_fuel_per_kilometer = float(input())
food_expenses_per_person_per_day = float(input())
room_price_per_person_per_night = float(input())
total_price_for_food_and_accommodation = days_of_trip * \
                                         (number_of_people *
                                          (food_expenses_per_person_per_day + room_price_per_person_per_night))
if number_of_people > 10:
    total_price_for_food_and_accommodation -= total_price_for_food_and_accommodation * 0.25

total_expenses = total_price_for_food_and_accommodation

for day in range(1, days_of_trip + 1):
    traveled_distance_for_current_day = float(input())
    travel_expenses = traveled_distance_for_current_day * price_of_fuel_per_kilometer
    total_expenses += travel_expenses
    current_expenses = total_expenses
    budget = budget - total_expenses
    if budget < 0:
        needed_money = total_expenses - budget
        print(f"Not enough money to continue the trip. You need {needed_money:.2f}$ more.")
        break
    if day % 7 == 0:
        budget += current_expenses / number_of_people
    if day % 5 == 0:
        additional_expenses = current_expenses * 0.4
        total_expenses += additional_expenses
    if day % 3 == 0:
        additional_expenses = current_expenses * 0.4
        total_expenses += additional_expenses
    if budget < total_expenses:
        needed_money = total_expenses - budget
        print(f"Not enough money to continue the trip. You need {needed_money:.2f}$ more.")
        break
if budget >= total_expenses:
    money_left = budget - total_expenses
    print(f"You have reached the destination. You have {money_left:.2f}$ budget left.")

