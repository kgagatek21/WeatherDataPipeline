import pandas as pd
from api import api_data
from logs import quality_log_append


# df = pd.DataFrame(api_data())
# print(df.head(10).to_string(index=False))
# print(df.shape)


def null_values_handle(df):

    numeric_columns = df.select_dtypes(include="number").columns
    text_columns = df.select_dtypes(include="object").columns

    df[numeric_columns] = df[numeric_columns].fillna(
        df[numeric_columns].mean()
    )

    df[text_columns] = df[text_columns].fillna("Unknown")

    print("Missing numbers replaced with mean, \nMissing strings and objects replaced with unknown")


def duplicate_value_handle(df):
    if df.duplicated().sum():
        print(f"Duplicates found: {df.duplicated().sum()}")
        df = df.drop_duplicates()
        print("Duplicates dropped")
    else:
        print("No duplicates found")


def basic_statistics(df):
    return df.describe()


def change_dtype(df):
    for column in df:
        if column != "date":
            df[column] = df[column].astype(int)
        else:
            df[column] = df[column].dt.strftime("%Y-%m-%d %H:%M:%S")


def transform_data(df, logs, run_id):
    quality_log_append(
        logs,
        run_id,
        "row_count",
        len(df),
        len(df) > 0
    )
    missing_dates = df["date"].isna().sum()

    quality_log_append(
        logs,
        run_id,
        "missing_dates",
        missing_dates,
        missing_dates == 0
    )

    duplicates = df["date"].duplicated().sum()

    quality_log_append(
        logs,
        run_id,
        "duplicate_dates",
        duplicates,
        duplicates == 0
    )

    null_values_handle(df)
    duplicate_value_handle(df)
    change_dtype(df)
    # print(df.head(10).to_string(index=False))
    # df.to_excel("output.xlsx", index=False)
    return df
