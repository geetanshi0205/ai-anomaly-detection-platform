#!/usr/bin/env python3
"""
🏥 Project Verification & Setup Tool
Verifies all components are properly configured
"""

import os
import sys
import json
from pathlib import Path

class ProjectVerifier:
    def __init__(self):
        self.project_root = os.path.dirname(os.path.abspath(__file__))
        self.issues = []
        self.warnings = []
        self.successes = []
    
    def check_python_version(self):
        """Check Python version"""
        if sys.version_info >= (3, 9):
            self.successes.append(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} (required: 3.9+)")
            return True
        else:
            self.issues.append(f"✗ Python {sys.version_info.major}.{sys.version_info.minor} (required: 3.9+)")
            return False
    
    def check_directories(self):
        """Check required directories exist"""
        required_dirs = [
            'backend', 'kafka', 'ml', 'dashboard', 'model', 
            'utils', 'alerts', 'data'
        ]
        
        for dir_name in required_dirs:
            dir_path = os.path.join(self.project_root, dir_name)
            if os.path.isdir(dir_path):
                self.successes.append(f"✓ Directory: {dir_name}/")
            else:
                self.issues.append(f"✗ Missing directory: {dir_name}/")
    
    def check_files(self):
        """Check required files exist"""
        required_files = {
            'backend/app.py': 'Backend API',
            'kafka/producer.py': 'Kafka Producer',
            'kafka/consumer.py': 'Kafka Consumer',
            'dashboard/dashboard.py': 'Streamlit Dashboard',
            'model/anomaly_model.pkl': 'ML Model',
            'utils/preprocessing.py': 'Data Preprocessing',
            'utils/model_handler.py': 'Model Handler',
            'utils/risk_calculator.py': 'Risk Calculator',
            'alerts/alert_manager.py': 'Alert Manager',
            'requirements.txt': 'Dependencies',
            'main.py': 'Main Orchestrator'
        }
        
        for file_path, description in required_files.items():
            full_path = os.path.join(self.project_root, file_path)
            if os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                if size > 0:
                    self.successes.append(f"✓ {description}: {file_path}")
                else:
                    self.warnings.append(f"⚠ Empty file: {file_path}")
            else:
                self.issues.append(f"✗ Missing file: {file_path}")
    
    def check_packages(self):
        """Check required packages are installed"""
        required_packages = [
            'kafka', 'flask', 'streamlit', 'pandas', 
            'sklearn', 'plotly', 'joblib'
        ]
        
        missing = []
        for package in required_packages:
            try:
                __import__(package)
                self.successes.append(f"✓ Package: {package}")
            except ImportError:
                missing.append(package)
        
        if missing:
            self.warnings.append(f"⚠ Missing packages: {', '.join(missing)}")
            return False
        return True
    
    def check_data_files(self):
        """Check data files"""
        data_files = {
            'data/patient_data.csv': 'Training Data',
            'kafka/patient_data.csv': 'Streaming Data (generated after run)',
            'alerts/alerts_log.json': 'Alerts Log (generated after run)'
        }
        
        for file_path, description in data_files.items():
            full_path = os.path.join(self.project_root, file_path)
            if os.path.isfile(full_path):
                self.successes.append(f"✓ {description}: {file_path}")
            else:
                self.warnings.append(f"⚠ {description} not found (will be created at runtime): {file_path}")
    
    def verify_model_file(self):
        """Check model file integrity"""
        model_path = os.path.join(self.project_root, 'model/anomaly_model.pkl')
        if os.path.isfile(model_path):
            try:
                import joblib
                model = joblib.load(model_path)
                self.successes.append(f"✓ ML Model loaded successfully ({os.path.getsize(model_path)} bytes)")
                return True
            except Exception as e:
                self.issues.append(f"✗ Model load error: {e}")
                return False
        else:
            self.issues.append("✗ Model file not found")
            return False
    
    def print_report(self):
        """Print verification report"""
        print("\n" + "="*70)
        print("🏥 PROJECT VERIFICATION REPORT".center(70))
        print("="*70 + "\n")
        
        # Successes
        if self.successes:
            print("✓ VERIFIED COMPONENTS:")
            print("-" * 70)
            for item in self.successes:
                print(f"  {item}")
            print()
        
        # Warnings
        if self.warnings:
            print("⚠ WARNINGS:")
            print("-" * 70)
            for item in self.warnings:
                print(f"  {item}")
            print()
        
        # Issues
        if self.issues:
            print("✗ ISSUES TO FIX:")
            print("-" * 70)
            for item in self.issues:
                print(f"  {item}")
            print()
        
        # Summary
        print("="*70)
        status = "✓ READY" if not self.issues else "✗ NOT READY"
        print(f"Status: {status}".center(70))
        print("="*70)
        
        if self.issues:
            print("\n💡 NEXT STEPS:")
            print("  1. Install dependencies: pip install -r requirements.txt")
            print("  2. Start Kafka server")
            print("  3. Verify all required files are present")
            print("  4. Run verification again: python verify_setup.py")
            return False
        else:
            print("\n✓ System is ready to run!")
            print("  Run: python main.py")
            return True
    
    def run_all_checks(self):
        """Run all verification checks"""
        print("\n🔍 Running verification checks...\n")
        
        self.check_python_version()
        self.check_directories()
        self.check_files()
        self.check_packages()
        self.check_data_files()
        self.verify_model_file()
        
        return self.print_report()

def main():
    verifier = ProjectVerifier()
    success = verifier.run_all_checks()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
