import pandas as pd

def load_data():
    df = pd.read_csv("support_tickets.csv")

    # clean column names
    df.columns = df.columns.str.strip()

    return df