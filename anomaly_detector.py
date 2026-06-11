from data_loader import load_data

df = load_data()

def detect_anomalies():

    anomalies = []

    # 1. Critical unresolved tickets
    critical_unresolved = df[
        (df["priority"] == "Critical") &
        (df["status"] != "Resolved")
    ]

    for _, row in critical_unresolved.iterrows():

        anomalies.append({
            "ticket_id": row["ticket_id"],
            "issue": "Critical unresolved ticket",
            "priority": row["priority"],
            "status": row["status"],
            "agent_id": row["agent_id"],
            "type": "critical" 
        })

    # 2. Long resolution time
    long_resolution = df[
        df["resolution_time_hrs"].fillna(0) > 20
    ]

    for _, row in long_resolution.iterrows():

        anomalies.append({
            "ticket_id": row["ticket_id"],
            "issue": "Abnormally long resolution time",
            "resolution_time_hrs": row["resolution_time_hrs"],
            "agent_id": row["agent_id"],
            "type": "slowres"
        })

    # 3. Poor customer ratings
    poor_ratings = df[
        df["customer_rating"].fillna(5) <= 2
    ]

    for _, row in poor_ratings.iterrows():

        anomalies.append({
            "ticket_id": row["ticket_id"],
            "issue": "Poor customer rating",
            "customer_rating": row["customer_rating"],
            "agent_id": row["agent_id"],
            "type": "rating"
        })

    return anomalies