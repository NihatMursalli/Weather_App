🌦️ Weather App

AI-powered weather forecasting app built with Streamlit, scikit-learn, and OpenWeather API.
Shows real-time weather, predicts future temperatures, and displays interactive city maps.

🚀 Features

🌤️ Live weather (temperature, humidity, wind, pressure, visibility)

🔮 Next-day prediction using a trained ML model

📈 7-day forecast visualized in a line chart

🌍 City map with Folium integration

🛠️ Tech Stack

UI: Streamlit

ML: scikit-learn (RandomForestRegressor)

API: OpenWeatherMap

Maps: Folium + Geopy

📂 Project Structure
Weather-App/
│── app.py              # Main Streamlit app
│── train_model.py      # Script to train dummy model
│── model.pkl           # Saved ML model
│── requirements.txt    # Dependencies
│── README.md           # Documentation
│
└── utils/
    └── weather.py      # API + geocoding + map helpers

⚡ Installation & Setup
# 1. Clone repo
git clone https://github.com/NihatMursalli/Weather-App.git
cd Weather-App

# 2. (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your OpenWeather API key in utils/weather.py
API_KEY = "YOUR_API_KEY"

# 5. Train model
python train_model.py

# 6. Run the app
streamlit run app.py

📸 Example Output

Weather stats card with today + tomorrow’s temperature

7-day forecast line chart

Map marker of entered city

🤝 Contributing

Pull requests and feature suggestions welcome!
