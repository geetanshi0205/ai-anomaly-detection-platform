from kafka import KafkaProducer
import json
import random
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

while True:

    data = {
        "patient_id": random.randint(1,5),
        "heart_rate": random.randint(60,150),
        "spo2": random.randint(85,100),
        "temperature": round(random.uniform(36,40),2),
        "blood_pressure": random.randint(110,160)
    }

    producer.send("patient-vitals", data)

    print("Sent:", data)

    time.sleep(2)