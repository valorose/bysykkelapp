from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the CSV file and parse timestamps
file_path = r'C:\Users\olavr\bysykkelapp\10.csv'
df_csv = pd.read_csv(file_path, parse_dates=['started_at', 'ended_at'])

# Extract one example ride for display
example_ride = df_csv.iloc[0]  # Select the first ride in the CSV for now

# Prepare the details of the example ride
example_ride_details = {
    'start_station_name': example_ride['start_station_name'],
    'end_station_name': example_ride['end_station_name'],
    'started_at': example_ride['started_at'],
    'ended_at': example_ride['ended_at']
}

@app.route('/')
def home():
    # Pass the example ride details to the template
    return render_template('example_ride.html', ride=example_ride_details)

if __name__ == '__main__':
    app.run(debug=True)
