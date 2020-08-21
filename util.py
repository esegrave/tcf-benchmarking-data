import pandas as pd

def fieldTypes(df, fields):
    for field in fields:
        print(type(df[field][0]))

def view(df):
    df.to_csv('temp.csv', index=False)
    
def toFloat(row, column):
    try:
        return float(row[column])
    except:
        return np.nan

def toInt(row, column):
    try:
        return int(row[column])
    except:
        return np.nan
    
def cleanString(row, column):
    try:
        return str(int(row[column]))
    except:
        return row[column]

# enrollment dtypes
# dtype={'year': str,'district_id': str,'district': str,'school_id': str,'school': str,'grade': str,'group_state': str,'num': np.int64}

# proficiency dtypes
# dtype={'year': str,'district_id': str,'district': str,'school_id': str,'school': str,'grade': str,'group_state': str,'subject': str,'proficient_tf': bool,'num_at_level': np.float64,'num_tested': np.float64,'pct_at_level': np.float64}