from datetime import datetime


def simulation_program_2(main_analyzer,user_id):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    
    status = int(input(f"\nEnter status for user {user_id} at {timestamp}: "))
    if(status==1):
        main_analyzer.insert_record(user_id, timestamp, status)

    elif(status==0):
        main_analyzer.insert_record(user_id, timestamp, status)

    elif(status==-1):
        q=[]
        q.append(user_id)
        print(q)
    else:
         print("Wrong input")
