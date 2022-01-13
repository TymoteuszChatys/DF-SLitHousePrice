import pickle
import pandas as pd

def get_price(model,type,station,beds,baths,receptions,postcode,pc_df):


    price_12_months = pc_df.loc[pc_df['post_code'] == (postcode.upper()), 'avg_sold_price_12months'].iloc[0]

    if type == "detached":
            price_type = pc_df.loc[pc_df['post_code'] == (postcode.upper()), 'detached_12months'].iloc[0]
    elif type == "semi-detached":
            price_type = pc_df.loc[pc_df['post_code'] == (postcode.upper()), 'semi_detached_12months'].iloc[0]
    elif type == "terraced":
            price_type = pc_df.loc[pc_df['post_code'] == (postcode.upper()), 'terraced_12months'].iloc[0]
    elif type == "flat":
            price_type = pc_df.loc[pc_df['post_code'] == (postcode.upper()), 'flat_12months'].iloc[0]

    data = {'type' : type,
            'station' : station,
            'beds' : beds,
            'baths' : baths,
            'receptions' : receptions,
            'avg_sold_price_12months' : price_12_months,
            'avg_type' : price_type
    }

    df = pd.DataFrame(data, index=[0])

    categorical_columns = ['type']
    category_ids = [df.columns.get_loc(col) for col in categorical_columns]
    category_ids

    for column in categorical_columns:
            df[column] = pd.Categorical(df[column])

    

    return float(model.predict(df)[0])


