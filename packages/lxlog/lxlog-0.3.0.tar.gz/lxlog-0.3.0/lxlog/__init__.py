import subprocess
import pandas as pd
from prettytable import PrettyTable

def log_analysis(start_date, end_date, process_name):
    # Define the Linux command to filter logs for the specified process within the log range
    command = f"journalctl _COMM={process_name} --since='{start_date} 00:00:00' --until='{end_date} 23:59:59'"

    # Execute the command and capture the output
    output = subprocess.check_output(command, shell=True)

    # Decode the output into a string
    output_string = output.decode("utf-8")

    # Split the output into lines and parse them into a pandas DataFrame
    log_data = [line.split(maxsplit=4) for line in output_string.split("\n") if process_name in line]
    df = pd.DataFrame(log_data, columns=["Date", "Time", "Hostname", "Process", "Message"])

    # Create a pretty table and add the data
    table = PrettyTable()
    table.field_names = ["Date", "Time", "Hostname", "Process", "Message"]
    for row in df.itertuples(index=False):
        table.add_row(row)

    # Return the formatted table as a string
    return str(table)

