from kafka import KafkaConsumer
import json
import csv

# Create consumer
consumer = KafkaConsumer(
    "patient-vitals",
    bootstrap_servers="localhost:9092",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

# Dictionary to store patient history
patients = {}

# Function for explainable alerts
def explain_alert(hr, spo2, temp):

    reasons = []

    if hr > 130:
        reasons.append("High Heart Rate")

    if spo2 < 90:
        reasons.append("Low Oxygen")

    if temp > 39:
        reasons.append("High Temperature")

    return reasons


# Start consuming messages
for message in consumer:

    data = message.value
    pid = data["patient_id"]

    hr = data["heart_rate"]
    spo2 = data["spo2"]
    temp = data["temperature"]

    print("Received:", data)

    # Patient monitoring
    if pid not in patients:
        patients[pid] = []

    patients[pid].append(data)

    print("Patient", pid, "History:", patients[pid])

    # Save data to CSV
    with open("patient_data.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pid, hr, spo2, temp])

    # Alert detection
    reasons = explain_alert(hr, spo2, temp)

    if reasons:
        print("⚠ ALERT for Patient", pid)
        print("Reasons:", reasons)

    print("----------------------------------")