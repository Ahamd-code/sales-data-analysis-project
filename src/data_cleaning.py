import pandas as pd

def load_and_clean(filepath):
    # Load data
    df = pd.read_csv(filepath, encoding='latin1')

    # Fix date columns
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    # Remove duplicates
    df = df.drop_duplicates()

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    print(f"Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

if __name__ == "__main__":
    df = load_and_clean('data/raw/superstore.csv')
    df.to_csv('data/processed/cleaned_superstore.csv', index=False)
    print("Cleaned data saved to data/processed/")