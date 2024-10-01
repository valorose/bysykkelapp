from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the simplified data
df_csv = pd.read_csv(r'C:\Users\olavr\bysykkelapp\10.csv')

# Function to calculate the fastest time between Festplassen and C. Sundts gate
def get_fastest_duration():
    # Filter data for the specific route
    route_data = df_csv[(df_csv['start_station_name'] == 'Festplassen') & 
                        (df_csv['end_station_name'] == 'C. Sundts gate')]
    
    # Get the fastest duration for this route
    if not route_data.empty:
        fastest_trip = route_data.loc[route_data['duration'].idxmin()]
        return fastest_trip['duration']
    else:
        return None

@app.route('/')
def home():
    # Get the fastest duration between Festplassen and C. Sundts gate
    fastest_duration = get_fastest_duration()
    
    return render_template('index.html', fastest_duration=fastest_duration)

if __name__ == '__main__':
    app.run(debug=True)
