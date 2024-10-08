gifts_plan = input().split()
command = input()
gift_given = ""
gift_index_given = 0
while command != "No Money":
    for gift in gifts_plan:
        gift_index = gifts_plan.index(gift)
        if command == "OutOfStock " + gift:
            while gift in gifts_plan:
                gifts_plan.remove(gift)
        elif command == "Required  " + gift_given + " " + str(gift_index_given):
            if gift_index_given in gifts_plan:
                gifts_plan[gift_index_given].replace(gift_given)
                print(gifts_plan)



        elif command == "some":
            pass






    command = input()
