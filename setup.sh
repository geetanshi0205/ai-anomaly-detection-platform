#!/bin/bash
# Patient Health Monitoring System - Setup Script for Linux/Mac

echo "==============================================================================="
echo "        PATIENT HEALTH MONITORING SYSTEM - Unix Setup"
echo "==============================================================================="
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.9+ and try again"
    exit 1
fi

echo "[OK] Python is installed"
python3 --version
echo ""

# Install requirements
echo "==============================================================================="
echo "Installing Python Dependencies..."
echo "==============================================================================="
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo ""
echo "==============================================================================="
echo "[SUCCESS] Setup Complete!"
echo "==============================================================================="
echo ""
echo "To start the system, run:"
echo "   python3 main.py"
echo ""
