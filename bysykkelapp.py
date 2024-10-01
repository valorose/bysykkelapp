from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load your data (use a raw string or double backslashes for Windows paths)
df_csv = pd.read_csv(r'C:\Users\olavr\bysykkelapp\10.csv')  # Use r'' to avoid escape issues

# Example function to calculate speeds
def calculate_speeds():
    # Process your DataFrame to calculate speeds and find top 3
    # Adjust these calculations based on your actual CSV structure
    df_csv['speed'] = df_csv['distance'] / df_csv['duration']  # Example calculation
    # Group by station_name and find the top 3 speeds
    top_stations = df_csv.groupby('station_name')['speed'].nlargest(3).reset_index()
    return top_stations

@app.route('/')
def home():
    top_speeds = calculate_speeds()
    return render_template('index.html', top_speeds=top_speeds)

if __name__ == '__main__':
    app.run(debug=True)
