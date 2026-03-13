import pandas as pd
import os

def load_and_clean_data(filepath):
    if not os.path.exists(filepath):
        df = pd.DataFrame(columns=['Date', 'Description', 'Amount'])
        df.to_csv(filepath, index=False)
        return df

    df = pd.read_csv(filepath)
    
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    
    df = df.dropna(subset=['Date', 'Amount'])
    
    return df