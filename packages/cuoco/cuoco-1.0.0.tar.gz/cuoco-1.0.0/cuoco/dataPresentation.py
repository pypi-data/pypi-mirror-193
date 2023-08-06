# Count number of nans
def countNans(df):
    nan_count = df.isna().sum().sum()
    return nan_count

def summary(json_file):
    print("*************************")
    print("** SUMMARY             **")
    print("")
    print("· Name of the preprocessed data file: " + json_file['new_fileName'])
    print("· Route of the preprocessed data file: " + json_file['new_file_route'])
    print("· Output format: " + json_file['output_format'])
    print("· Applied normalization: " + json_file['normalize_method'])
    print("· Applied balance method: " + json_file['balance_data'])
    print("")
    print("")


def showStats(original_df, actual_df, json_file, y_col):
    # Dataset information
    print("*************************")
    print("** DATASET INFORMATION **")
    print("")
    print("- Number of rows: " + str(len(actual_df)))
    print("")
    print("- Columns: " + actual_df.columns)

    print("")
    print("-------------------------")
    print("DATASET STATISTICS")
    print("")

    # NANS
    print("· Count of NANS in the raw dataset:")
    print(countNans(original_df))
    print(" ")

    # Removed rows
    print("· Number of removed rows:")
    print(len(original_df) - len(actual_df))
    print(" ")

    if json_file['balance_data'] != "no":
        # Count of classes before oversampling
        print("· Original data distribution (on the y_col column)")
        original_df[y_col].value_counts().plot.bar()

        print("//")

        print("· Actual data distribution (on the y_col column)")
        actual_df[y_col].value_counts().plot.bar()


def writeDF(df, route, name, output_format, index_format):
    if output_format == "csv" or output_format == "txt":
        df.to_csv(route + name + "." + output_format, index=index_format)
    elif output_format == "orc":
        df.to_orc(route + name + "." + output_format, index=index_format)
    elif output_format == "parquet":
        df.to_parquet(route + name + "." + output_format, index=index_format)
