# main_program.py
from main_analyzer import MainAnalyzer
from simulation_program_1 import simulation_program_1
from simulation_program_2 import simulation_program_2
import threading

def main():
    connection = MainAnalyzer.create_connection()
    main_analyzer = MainAnalyzer(connection)

    # Run simulation programs concurrently using threads
    thread_1 = threading.Thread(target=simulation_program_1, args=(main_analyzer,))
    thread_2 = threading.Thread(target=simulation_program_2, args=(main_analyzer,))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

if __name__ == "__main__":
    main()
