from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the CSV file and parse timestamps
file_path = r'C:\Users\olavr\bysykkelapp\10.csv'
df_csv = pd.read_csv(file_path, parse_dates=['started_at', 'ended_at'])

# Calculate the duration in seconds if it's not present
df_csv['duration_seconds'] = (df_csv['ended_at'] - df_csv['started_at']).dt.total_seconds()

# Function to get the fastest duration between Festplassen and C. Sundts gate
def get_fastest_duration():
    # Filter data for the specific route
    route_data = df_csv[(df_csv['start_station_name'] == 'Festplassen') & 
                        (df_csv['end_station_name'] == 'C. Sundts gate')]
    
    # Check if there are any trips for this route
    if not route_data.empty:
        # Get the fastest duration in seconds
        fastest_trip = route_data.loc[route_data['duration_seconds'].idxmin()]
        return fastest_trip['duration_seconds']
    else:
        return None

@app.route('/')
def home():
    # Get the fastest duration between Festplassen and C. Sundts gate
    fastest_duration_seconds = get_fastest_duration()
    
    return render_template('index.html', fastest_duration_seconds=fastest_duration_seconds)

if __name__ == '__main__':
    app.run(debug=True)
