import sys
from datetime import datetime
from simulator import Simulator

def parse_arguments():
    if len(sys.argv) < 5 or sys.argv[1] not in ['FCFS', 'PB', 'RR']:
        print("Usage: python main.py <Scheduling Algorithm> <number of CPU> <number of IO> <input file> [<Time Quantum for RR>]")
        print("Scheduling Algorithms: FCFS, PB, RR")
        sys.exit(1)

    algorithm = sys.argv[1]
    num_cpus = int(sys.argv[2])
    num_ios = int(sys.argv[3])
    input_file = sys.argv[4]
    time_quantum = int(sys.argv[5]) if len(sys.argv) > 5 and algorithm == "RR" else None

    return algorithm, num_cpus, num_ios, input_file, time_quantum

def main():
    algorithm, num_cpus, num_ios, input_file, time_quantum = parse_arguments()

    # Generate a unique filename using the current date and time
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"output_{current_time}.txt"

    # Initialize and run the simulator
    simulator = Simulator(input_file, num_cpus, num_ios)

    # Redirecting output to both the console and the file
    with open(output_filename, "w") as output_file:
        if algorithm == "FCFS":
            print(f"Running FCFS Simulation...")
            output_file.write("Running FCFS Simulation...\n")
            simulator.FCFS()
        elif algorithm == "PB":
            print(f"Running Priority-Based Simulation...")
            output_file.write("Running Priority-Based Simulation...\n")
            simulator.PB()
        elif algorithm == "RR":
            print(f"Running Round-Robin Simulation with Time Quantum: {time_quantum}")
            output_file.write(f"Running Round-Robin Simulation with Time Quantum: {time_quantum}\n")
            simulator.RR(time_quantum)

        # The final statistics will be displayed and written within each scheduling method

    print(f"Simulation complete. Output stored in '{output_filename}'.")

if __name__ == '__main__':
    main()
