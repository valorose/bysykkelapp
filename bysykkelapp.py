from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load your data
df_csv = pd.read_csv(r'C:\Users\olavr\bysykkelapp\10.csv')

# Define destinations
destinations = ["Fløyen", "Bryggen", "Festplassen"]

# Example function to calculate top speeds for each destination
def calculate_speeds():
    # Calculate speed (assuming distance is in meters and duration is in seconds)
    # This assumes you have a distance column; if not, you'll need to adapt this logic
    df_csv['speed'] = df_csv['distance'] / (df_csv['duration'] / 3600)  # Speed in km/h

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
