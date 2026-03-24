import subprocess
import sys
import time
import os
from pathlib import Path
import webbrowser

def run_producer():
    """Start Kafka producer"""
    print("\n" + "="*60)
    print("🚀 Starting Kafka Producer...")
    print("="*60)
    subprocess.Popen([sys.executable, "kafka/producer.py"])
    time.sleep(2)

def run_consumer():
    """Start Kafka consumer"""
    print("\n" + "="*60)
    print("📊 Starting Kafka Consumer...")
    print("="*60)
    subprocess.Popen([sys.executable, "kafka/consumer.py"])
    time.sleep(2)

def run_backend():
    """Start Flask backend"""
    print("\n" + "="*60)
    print("🔧 Starting Flask Backend...")
    print("="*60)
    subprocess.Popen([sys.executable, "backend/app.py"])
    time.sleep(3)

def run_dashboard():
    """Start Streamlit dashboard"""
    print("\n" + "="*60)
    print("📈 Starting Streamlit Dashboard...")
    print("="*60)
    subprocess.Popen([sys.executable, "-m", "streamlit", "run", "dashboard/dashboard.py"])
    time.sleep(3)
    webbrowser.open("http://localhost:8501")

def show_menu():
    """Display main menu"""
    print("\n" + "="*70)
    print("🏥 PATIENT HEALTH MONITORING SYSTEM - SETUP & RUNNER")
    print("="*70)
    print("\nBefore running, ensure:")
    print("  ✓ Apache Kafka is running (localhost:9092)")
    print("  ✓ Python 3.9+ is installed")
    print("  ✓ Dependencies installed: pip install -r requirements.txt")
    print("\n" + "-"*70)
    print("SELECT COMPONENTS TO RUN:")
    print("-"*70)
    print("1. Producer (generates patient data to Kafka)")
    print("2. Consumer (reads from Kafka, detects anomalies)")
    print("3. Backend API (Flask - provides REST endpoints)")
    print("4. Dashboard (Streamlit - visualization)")
    print("5. Run ALL components (recommended)")
    print("6. View Project Structure")
    print("7. Exit")
    print("-"*70)

def show_structure():
    """Display project structure"""
    print("\n" + "="*70)
    print("📂 PROJECT STRUCTURE")
    print("="*70)
    
    structure = """
ai-anomaly-detection-platform/
│
├── backend/
│   └── app.py                    ← Flask API with model integration
│
├── kafka/
│   ├── producer.py              ← Generates patient vitals
│   ├── consumer.py              ← Processes stream & detects anomalies
│   └── patient_data.csv         ← Streaming data output
│
├── ml/
│   ├── train_model.py           ← Train IsolationForest model
│   └── eda_analysis.py          ← Exploratory Data Analysis
│
├── dashboard/
│   └── dashboard.py             ← Streamlit visualization
│
├── model/
│   └── anomaly_model.pkl        ← Pre-trained ML model
│
├── utils/
│   ├── preprocessing.py         ← Data preprocessing utilities
│   ├── model_handler.py         ← Model loading & prediction
│   ├── risk_calculator.py       ← Risk scoring logic
│   └── __init__.py
│
├── alerts/
│   ├── alert_manager.py         ← Alert & email management
│   └── alerts_log.json          ← Alert history
│
├── data/
│   └── patient_data.csv         ← Original training data
│
├── requirements.txt             ← Python dependencies
├── main.py                      ← This file (orchestrator)
└── README.md
    """
    print(structure)
    print("="*70)

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            run_producer()
            input("\n✓ Producer started. Press Enter to continue...")
        
        elif choice == '2':
            run_consumer()
            input("\n✓ Consumer started. Press Enter to continue...")
        
        elif choice == '3':
            run_backend()
            print("\n✓ Backend running at http://localhost:5000")
            input("Press Enter to continue...")
        
        elif choice == '4':
            run_dashboard()
            input("\n✓ Dashboard launched. Press Enter to continue...")
        
        elif choice == '5':
            print("\n" + "🚀 STARTING ALL COMPONENTS...".center(70))
            print("="*70)
            print("\nThis will start:")
            print("  1. Kafka Producer (generates data)")
            print("  2. Kafka Consumer (processes data & detects anomalies)")
            print("  3. Flask Backend API (http://localhost:5000)")
            print("  4. Streamlit Dashboard (http://localhost:8501)")
            print("\n⏳ Starting services...")
            
            run_producer()
            run_consumer()
            run_backend()
            run_dashboard()
            
            print("\n" + "✓ ALL SERVICES STARTED!".center(70))
            print("="*70)
            print("\n📝 QUICK LINKS:")
            print("   • Backend API:     http://localhost:5000")
            print("   • Dashboard:       http://localhost:8501")
            print("   • Kafka Topic:     patient-vitals")
            print("\n📊 NEXT STEPS:")
            print("   1. Open http://localhost:8501 to view dashboard")
            print("   2. Go to 'Overview' tab to see real-time monitoring")
            print("   3. Check 'Alerts' tab for anomalies")
            print("\n⚠️  IMPORTANT: Keep this window open!")
            print("   Services will stop when this window closes.")
            print("\nPress Ctrl+C to stop all services")
            
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\n\n" + "🛑 STOPPING ALL SERVICES...".center(70))
                print("="*70)
        
        elif choice == '6':
            show_structure()
            input("\nPress Enter to continue...")
        
        elif choice == '7':
            print("\n👋 Thank you for using Patient Monitoring System!")
            print("="*70)
            break
        
        else:
            print("\n❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Application terminated.")
