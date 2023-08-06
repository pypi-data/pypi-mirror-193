lxlog

lxlog is a Python package for analyzing logs in Linux systems. It provides a command-line interface for filtering log data for a specified process or mail logs within a specified date range. The filtered log data is then formatted into a pretty table using the pandas and prettytable libraries.
Installation

You can install lxlog using pip:

pip install lxlog
Usage

To use lxlog, you can import the main function and call it with the required parameters:

python

from lxlog import main
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")
log_type = input("Enter log_type: ")
result = main(start_date, end_date, log_type)
print(result)

The main function accepts three parameters:

    start_date: The start date of the log data to analyze in the format YYYY-MM-DD.
    end_date: The end date of the log data to analyze in the format YYYY-MM-DD.
    log_type: The type of log data to analyze, either syslog or maillog.

If log_type is syslog, the function will prompt for the name of the process to filter for. The function returns a string containing the formatted log data.
Some examples:

To get Input form user

python code

from lxlog import main
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")
log_type = input("Enter log_type: ")
result = main(start_date, end_date, log_type)
print(result)

In log_type use either syslog or maillog as input.

Filter syslog data for the sshd process between January 1st and January 7th, 2022:

python code

from lxlog import main
result = main("2022-01-01", "2022-01-07", "syslog", process_name="sshd")
print(result) 

Filter maillog data between January 1st and January 7th, 2022:
python code

 from lxlog import main
    result = main("2022-01-01", "2022-01-07", "maillog")
    print(result)


