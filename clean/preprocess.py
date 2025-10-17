import pandas as pd
import numpy as np


def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """"
      This function is used to encode the incoming data
    """

    nominal_columns = ['Product_Category', 'Region']
    high_cardinality_columns = ['Product_Name']

    for col in nominal_columns:
        if col in data.columns:
            dummies = pd.get_dummies(data[col], prefix=col)
            dummies = dummies.astype(int)
            data = pd.concat([data, dummies], axis=1)
            data.drop(col, axis=1, inplace=True)

    for col in high_cardinality_columns:
        mean_encode = data.groupby(col)['Price'].mean()
        data[col] = data[col].map(mean_encode)

    return data