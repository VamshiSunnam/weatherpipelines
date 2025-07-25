```markdown
# 🌦️ NYC Weather Dashboard – CSV Based

This project is a simple weather data visualization dashboard built using Streamlit. It allows users to manually upload a CSV file containing historical weather information for New York City and view trends such as temperature, humidity, and wind speed over time.

Originally designed to work with live data from the OpenWeatherMap API, this version uses static or manually updated CSV files for flexibility and easy testing.

---

## 📌 Features

- 📁 Upload your own weather CSV file
- 📊 Visualizes:
  - Temperature over time
  - Humidity over time
  - Wind speed
- 🧾 Displays current (latest) weather record from your file
- ✅ Simple to run locally or deploy on Streamlit Cloud

---

## 🗂 Project Structure

```

weather\_dashboard/
├── dashboard.py           # Streamlit app code
├── data/
│   └── weather\_log.csv    # Your manually uploaded weather data
├── requirements.txt       # Python dependencies
└── README.md              # This file

````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/VamshiSunnam/weatherpipelines.git
cd weatherpipelines
````

### 2. Set Up Environment

(Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Prepare the Data

Replace or edit the sample file at:

```
data/weather_log.csv
```

Make sure it has the following structure:

```csv
city,temperature,humidity,description,wind_speed,timestamp
New York,25.4,60,clear sky,3.1,2025-07-19 09:00:00
New York,26.7,55,few clouds,4.2,2025-07-19 12:00:00
...
```

📌 Tip: You can generate your own rows using Excel, Notepad, or Python.

---

## 🖥️ Run the Streamlit App

```bash
streamlit run dashboard.py
```

It will open in your browser at: [http://localhost:8501](http://localhost:8501)

---

## 🌐 Deploy to Streamlit Community Cloud (Optional)

1. Push this project to a public GitHub repository.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Click "New App" and connect your repo.
4. Set main file path to: dashboard.py
5. Click “Deploy”

---

## 🧠 How It Works

The dashboard reads your CSV and:

* Displays the latest weather record (temp, humidity, wind, condition)
* Plots temperature and humidity as time-series line charts
* Optionally supports enhancements like uploading a new CSV file live

---

## 🛠 Future Ideas

* Add CSV upload directly in dashboard
* Filter data by date range
* Store in SQLite or PostgreSQL
* Add multi-city support
* Add real-time alerts for extreme weather

---

## 🤝 Author

Built with ❤️ by Vamshi Sunnam
GitHub: [https://github.com/VamshiSunnam](https://github.com/VamshiSunnam)
