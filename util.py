def fieldTypes(df, fields):
    for field in fields:
        print(type(df[field][0]))