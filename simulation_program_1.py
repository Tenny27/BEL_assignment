from datetime import datetime


def simulation_program_1(main_analyzer):
    user_id = int(input("Enter user ID: "))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    # Add a prompt for the status input
    status = int(input(f"Enter status for user {user_id} at {timestamp}: "))

    main_analyzer.insert_record(user_id, timestamp, status)
