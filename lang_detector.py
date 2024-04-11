
import pandas as pd
from langdetect import detect

def detect_language(text):
    try:
        return detect(text)
    except:
        # If detection fails or the text is NaN
        return "Unknown"

def main():
    # Step 1: Read the CSV file
    df = pd.read_csv('data/train.csv', encoding='utf-8')

    # Step 2 and 3: Detect language and create a new column
    df['LANG'] = df['TEXT'].apply(lambda text: detect_language(text) if pd.notnull(text) else "Unknown")

    # Generating summary report
    language_summary = df['LANG'].value_counts().head(5)
    print("Top 5 languages found:")
    print(language_summary)

    # Step 4: Write the dataframe to a new CSV file
    df.to_csv('data/train_lang.csv', index=False, encoding='utf-8')

if __name__ == "__main__":
    main()
