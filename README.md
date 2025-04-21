this is a simple python script for the sonnen data chalenge.
it loads a csv file with battery measurments that had some issues like missing values, n/a, nulls and wrong data types like strings instead of numbers.

so i cleaned it using pandas and made sure timestamps where converted to datetime, 
then extracted the hour so i could group the data by hour and calculate the total grid_purchase and grid_feedin. 
also added a colum called is_max_hour to indicate if that hour had the highest feedin for that day (true or false). 
the output is saved in cleaned_measurements.csv and hourly_summary.csv. to run it you can just do python main.py after installing pandas. 
or you can use docker by building the image with docker build -t sonnen-pipeline .
and then run it with docker run --rm -v $(pwd):/app sonnen-pipeline. the csv files will be created in your current folder after running.



## What It Does

- Cleans missing and bad data
- Converts types (like timestamps and numbers)
- Removes duplicated rows
- Adds a column to show the max grid_feedin hour for each day
- Outputs cleaned data + hourly summaries

## How to Run (Local)

1. Make sure you have Python 3 installed.
2. Install pandas:




3. Place `main.py` and `measurements_coding_challenge.csv` in the same folder.

## How to Run (With Docker)

4. Build the docker image:

docker build -t sonnen-pipeline .


5 Run the container (make sure you're in the folder with the files):



docker run --rm -v $(pwd):/app sonnen-pipeline

markdown


This will create 2 output files:
- `cleaned_measurements.csv`
- `hourly_summary.csv`

## Notes

- The script looks for `measurements_coding_challenge.csv` in the same directory.
- A column called `is_max_hour` will show True for the hour of the day with highest grid_feedin per day.


