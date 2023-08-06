import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

def encode(data, colnames, method, drop_after = True):
    if any(not isinstance(item, pd.DataFrame) for item in data):
        raise TypeError("Expected a list of pd.Dataframe.")
    
    if any(not isinstance(item, str) for item in colnames):
        raise TypeError("Expected a list of strings containing column names.")

    if method not in ['ohe', 'le']:
        raise KeyError("Expected either 'ohe' for (One Hot Encoding) or 'le' for (Label Encoding)")

    dataVert = pd.concat(data, ignore_index = True, sort = False)

    res = []

    if method == 'ohe':
        ohe = OneHotEncoder()
        for colname in colnames:
            ohe.fit(dataVert[[colname]])
            for df in data:
                newCols = (ohe.transform(df[[colname]]))
                df[ohe.categories_[0]] = newCols.toarray()
                if drop_after:
                    df.drop(columns = [colname], inplace=True)
                res.append(df)

    else:
        le = LabelEncoder()
        for colname in colnames:
            le.fit(dataVert[colname])
            for df in data:
                df[colname] = le.transform(df[colname])
                if drop_after:
                    df.drop(columns = [colname], inplace=True)
                res.append(df)
    return res