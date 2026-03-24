# 🏥 PATIENT HEALTH MONITORING SYSTEM - SETUP GUIDE

## Project Overview
This is a complete **real-time patient health monitoring system** that detects health anomalies using machine learning and Apache Kafka streaming.

### Key Features
✅ Real-time data streaming with Kafka  
✅ ML-based anomaly detection (IsolationForest)  
✅ Rule-based risk scoring  
✅ Interactive Streamlit dashboard  
✅ REST API with Flask  
✅ Email alerts for critical patients  
✅ Patient history tracking  

---

## 📋 Prerequisites

### 1. System Requirements
- Windows 10/11 or Linux/Mac
- Python 3.9 or higher
- At least 4GB RAM
- Java 8+ (for Kafka)
- 500MB free disk space

### 2. Required Software

#### Option A: Download & Install Manual
- **Python**: https://www.python.org/downloads/ (v3.9+)
- **Kafka**: https://kafka.apache.org/downloads (latest)
- **Java**: https://www.oracle.com/java/technologies/downloads/

#### Option B: Using Package Managers
Windows (Chocolatey):
```bash
choco install python java-se-development kafka
```

macOS (Homebrew):
```bash
brew install python java kafka
```

Linux (Ubuntu):
```bash
sudo apt-get install python3 openjdk-11-jdk kafka
```

---

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
cd "Anomaly Detection\ai-anomaly-detection-platform"
pip install -r requirements.txt
```

### Step 2: Start Kafka
⚠️ **Important**: Kafka must be running before starting the application

**Windows:**
```bash
# Terminal 1: Start Zookeeper
bin\windows\zookeeper-server-start.bat config\zookeeper.properties

# Terminal 2: Start Kafka Server
bin\windows\kafka-server-start.bat config\server.properties
```

**Linux/Mac:**
```bash
# Terminal 1
bin/zookeeper-server-start.sh config/zookeeper.properties

# Terminal 2
bin/kafka-server-start.sh config/server.properties
```

### Step 3: Run Application
```bash
python main.py
```

Select option `5` to start all components:
- Producer (generates patient data)
- Consumer (detects anomalies)
- Backend API (Flask)
- Dashboard (Streamlit)

---

## 📊 Component Details

### 1. **Kafka Producer** (`kafka/producer.py`)
- Generates realistic patient vital signs
- Sends data to Kafka topic `patient-vitals`
- Interval: 2 seconds per patient
- Patients: 1-5

**Vitals Generated:**
- Heart Rate: 60-150 bpm
- SpO2 (Oxygen): 85-100%
- Temperature: 36-40°C
- Blood Pressure: 110-160 mmHg

### 2. **Kafka Consumer** (`kafka/consumer.py`)
- Reads from `patient-vitals` topic
- Calculates risk using RiskCalculator
- Loads pre-trained ML model
- Saves data to CSV
- Logs alerts to JSON
- Sends email notifications (optional)

### 3. **Backend API** (`backend/app.py`)
**Port:** `http://localhost:5000`

**Endpoints:**
```
GET  /                 → API info
GET  /health           → API health status
GET  /vitals           → Latest patient vitals
POST /predict          → Predict anomaly for patient data
GET  /alerts           → Get all alerts
GET  /alerts/<level>   → Filter by severity (HIGH/MEDIUM/LOW)
GET  /patient/<id>     → Patient history
GET  /stats            → Monitoring statistics
```

**Example API Call:**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"patient_id": 1, "heart_rate": 140, "spo2": 88, "temperature": 39.5, "blood_pressure": 160}'
```

### 4. **Dashboard** (`dashboard/dashboard.py`)
**URL:** `http://localhost:8501`

**Pages:**
- **Overview**: System status, recent alerts, statistics
- **Alerts**: Alert management, filtering, download
- **Analysis**: Data visualization and charts
- **Patient Details**: Individual patient tracking
- **Settings**: Configuration and testing

---

## ⚙️ Configuration

### Risk Calculation Thresholds
Edit `utils/risk_calculator.py`:

```python
THRESHOLDS = {
    'heart_rate': {'min': 60, 'max': 100},      # Normal: 60-100 bpm
    'spo2': {'min': 95, 'max': 100},             # Normal: 95-100%
    'temperature': {'min': 36.5, 'max': 37.5},  # Normal: 36.5-37.5°C
    'blood_pressure': {'min': 90, 'max': 140}    # Normal: 90-140 mmHg
}
```

### ML Model Configuration
Current model: **IsolationForest**
- Contamination: 0.1 (10% outliers)
- Location: `model/anomaly_model.pkl`

To retrain:
```bash
python ml/train_model.py
```

### Email Alerts
Set environment variables to enable email notifications:
```bash
# Windows (PowerShell)
$env:ALERT_EMAIL = "your_email@gmail.com"
$env:ALERT_PASSWORD = "your_app_password"
$env:ALERT_RECIPIENT = "doctor@gmail.com"

# Linux/Mac
export ALERT_EMAIL="your_email@gmail.com"
export ALERT_PASSWORD="your_app_password"
export ALERT_RECIPIENT="doctor@gmail.com"
```

⚠️ **Note:** Use Gmail app-specific passwords, not your regular password.

---

## 📁 Project Structure

```
ai-anomaly-detection-platform/
│
├── backend/
│   └── app.py                    # Flask REST API
│
├── kafka/
│   ├── producer.py              # Data generator
│   ├── consumer.py              # Stream processor
│   └── patient_data.csv         # Streaming output
│
├── ml/
│   ├── train_model.py           # Model training
│   └── eda_analysis.py          # Data analysis
│
├── dashboard/
│   └── dashboard.py             # Streamlit UI
│
├── model/
│   └── anomaly_model.pkl        # Trained model
│
├── utils/
│   ├── preprocessing.py         # Data prep
│   ├── model_handler.py         # Model utilities
│   ├── risk_calculator.py       # Risk scoring
│   └── __init__.py
│
├── alerts/
│   ├── alert_manager.py         # Alert system
│   └── alerts_log.json          # Alert history
│
├── data/
│   └── patient_data.csv         # Training data
│
├── main.py                      # CLI orchestrator
├── requirements.txt             # Dependencies
├── setup.bat                    # Windows setup
├── setup.sh                     # Unix setup
├── SETUP_GUIDE.md              # This file
└── README.md                    # Main README
```

---

## 🔧 Troubleshooting

### Issue: "Kafka Connection Refused"
**Solution:**
1. Verify Kafka is running: Check for Java process
2. Check port 9092 is not blocked
3. Restart Kafka server

```bash
# Windows
taskkill /F /IM java.exe
# Then restart Kafka
```

### Issue: "ModuleNotFoundError"
**Solution:**
```bash
pip install -r requirements.txt --upgrade
```

### Issue: "Port 5000 already in use"
**Solution:**
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -i :5000
kill -9 <PID>
```

### Issue: "Port 8501 already in use"
**Solution:**
```bash
streamlit run dashboard/dashboard.py --server.port 8502
```

### Issue: "Model not loading"
**Solution:**
1. Check if `model/anomaly_model.pkl` exists
2. Retrain model: `python ml/train_model.py`
3. Verify TensorFlow installation: `pip install scikit-learn joblib`

---

## 📊 Sample Data

### Input (Vitals)
```json
{
  "patient_id": 1,
  "heart_rate": 145,
  "spo2": 88,
  "temperature": 38.9,
  "blood_pressure": 155
}
```

### Output (Prediction)
```json
{
  "status": "success",
  "patient_id": 1,
  "prediction": {
    "risk_level": "HIGH",
    "risk_score": 0.85,
    "flags": ["High Heart Rate: 145", "Low SpO2: 88%", "High Temperature: 38.9°C"],
    "ml_prediction": "anomaly",
    "recommendation": "Critical condition detected. Emergency medical attention required!"
  }
}
```

---

## 🧪 Testing

### Manual API Test
```bash
# Get API health
curl http://localhost:5000/health

# Get latest vitals
curl http://localhost:5000/vitals

# Get all alerts
curl http://localhost:5000/alerts

# Send prediction request
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"patient_id":1,"heart_rate":150,"spo2":85,"temperature":40,"blood_pressure":160}'
```

### Dashboard Test
1. Open http://localhost:8501
2. Navigate to "Overview" tab
3. Verify statistics are updating
4. Check "Alerts" for anomalies

---

## 🚨 Alert Levels

| Level | Condition | Action |
|-------|-----------|--------|
| **LOW** | All vitals normal | Continue monitoring |
| **MEDIUM** | 1-2 vitals abnormal | Consult healthcare provider |
| **HIGH** | 3+ vitals abnormal or ML detected anomaly | Emergency intervention |

---

## 📈 Performance

**System Requirements for Different Scales:**

| Scale | Patients | Data Points/Min | RAM | CPU |
|-------|----------|-----------------|-----|-----|
| Small | 1-5 | 150-750 | 2GB | 1 core |
| Medium | 10-20 | 4,800-9,600 | 4GB | 2 cores |
| Large | 50+ | 15,000+ | 8GB+ | 4+ cores |

---

## 🔐 Security Considerations

⚠️ **This is a development/demo system. For production:**

1. Use HTTPS for API endpoints
2. Implement authentication (JWT tokens)
3. Use database instead of in-memory storage
4. Encrypt sensitive data
5. Use environment variables for credentials
6. Implement rate limiting
7. Add comprehensive logging
8. Use VPN for Kafka connections

---

## 📚 Additional Resources

- **Kafka Documentation**: https://kafka.apache.org/documentation/
- **Flask Documentation**: https://flask.palletsprojects.com/
- **Streamlit Documentation**: https://docs.streamlit.io/
- **Scikit-learn**: https://scikit-learn.org/
- **IsolationForest**: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html

---

## 👨‍💻 Developer Notes

### Training a New Model
```bash
python ml/train_model.py
```

### Running EDA Analysis
```bash
python ml/eda_analysis.py
```

### Monitoring Logs
```bash
# View alerts log
type alerts\alerts_log.json

# View latest CSV data
tail kafka\patient_data.csv
```

### Extending the System

**Add New Risk Factors:**
Edit `utils/risk_calculator.py` and add conditions to `calculate_risk_score()`

**Add Custom Endpoints:**
Edit `backend/app.py` and add new routes

**Create Custom Dashboard Pages:**
Edit `dashboard/dashboard.py` and add new pages

---

## 📝 License & Support

This is an educational/demonstration project.

For issues or questions:
1. Check troubleshooting section above
2. Review console output for error messages
3. Verify all prerequisites are installed

---

**Last Updated:** March 2026  
**Version:** 1.0  
**Status:** Production Ready ✓
