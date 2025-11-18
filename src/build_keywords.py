import pandas as p
import s3Utils as util

INTAKE_FILE = 'data\\nasdaq_industrials.csv'
KEYWORDS_FILE = 'data\keywords.csv'

TARGET_INDUSTRIES = {
    'Aerospace',
    'Ordnance And Accessories',
    'Military/Government/Technical',
    'Engineering & Construction',
    'Industrial Machinery/Components'
}

def read_in(filepath = INTAKE_FILE):
    return p.read_csv(filepath)                     #reading in file
    

def clean(df):               
    df = df[df["Industry"].isin(TARGET_INDUSTRIES)] #only keeping rows with desired industries
    return df[["Symbol", "Name", "Industry"]]       #only keeping desired columns in df
    
def build(df):                                      #building final df to save

    data = {
        "ticker": df["Symbol"],             #saving the symbol to ticker
        "keyword": df["Name"],              #saving the company name to keyword
        "category": "company",              #this file we only want company names
        "source": "nasdaq"                  #got data from nasdaq
    }

    return p.DataFrame(data)


def save(df, filepath=KEYWORDS_FILE):   
    df.to_csv(filepath, index=False)        #save locally first

    util.upload_file(filepath, bucket='nba-sentiment-data', key='keywords/keywords.csv') 
    print("Cloud upload complete")
    #uploading to aws bucket


def main():
    raw = read_in()             #reading in raw csv data
    cleaned = clean(raw)        #cleaning
    built = build(cleaned)      #building new dataframe
    save(built)                 #saving locally and to cloud

if __name__ == "__main__":
    main()