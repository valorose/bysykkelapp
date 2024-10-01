from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load your data using the correct column names
df_csv = pd.read_csv(r'C:\Users\olavr\bysykkelapp\10.csv')

# Define destinations for filtering
destinations = ["Fløyen", "Bryggen", "Festplassen"]

# If there is no `distance` column, calculate it using latitude and longitude (optional)
# This is a placeholder for calculating distance if you need it
# Uncomment the next lines if distance is not present in your CSV

# import geopy.distance
# def calculate_distance(row):
#     coords_1 = (row['start_station_latitude'], row['start_station_longitude'])
#     coords_2 = (row['end_station_latitude'], row['end_station_longitude'])
#     return geopy.distance.distance(coords_1, coords_2).km * 1000  # Distance in meters
# df_csv['distance'] = df_csv.apply(calculate_distance, axis=1)

# Example function to calculate top speeds for each destination
def calculate_speeds():
    # Assuming distance is in meters and duration is in seconds
    if 'distance' in df_csv.columns:
        df_csv['speed'] = df_csv['distance'] / (df_csv['duration'] / 3600)  # Speed in km/h
    else:
        raise ValueError("Distance column is missing from the CSV file")

    # Prepare a dictionary to hold top speeds for each destination
    top_speeds = {}

    # Loop through each destination and get the top 3 speeds
    for destination in destinations:
        filtered_data = df_csv[(df_csv['start_station_name'] == 'Bergen Sentrum') & 
                               (df_csv['end_station_name'] == destination)]
        top = filtered_data.nlargest(3, 'speed')[['end_station_name', 'speed', 'duration']]
        top_speeds[destination] = top

    return top_speeds

@app.route('/')
def home():
    top_speeds = calculate_speeds()
    return render_template('index.html', top_speeds=top_speeds)

if __name__ == '__main__':
    app.run(debug=True)
