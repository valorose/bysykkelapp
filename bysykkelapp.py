from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load your data
df_csv = pd.read_csv(r'C:\Users\olavr\bysykkelapp\10.csv')

# Example function to calculate speeds for a specific station
def calculate_speeds(selected_station):
    # Process your DataFrame to calculate speeds
    df_csv['speed'] = df_csv['distance'] / df_csv['duration']
    # Filter for the selected station and find the top 3 speeds
    filtered_data = df_csv[df_csv['station_name'] == selected_station]
    top_stations = filtered_data.nlargest(3, 'speed')
    return top_stations

@app.route('/', methods=['GET', 'POST'])
def home():
    selected_station = request.args.get('station', 'Bergen Sentrum')  # Default station
    top_speeds = calculate_speeds(selected_station)
    return render_template('index.html', top_speeds=top_speeds)

if __name__ == '__main__':
    app.run(debug=True)
