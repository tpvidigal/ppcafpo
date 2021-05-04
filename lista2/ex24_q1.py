import pandas as pd

def optimal_solution(df):
    cycle_count = 0

    while True:
        df_coefs = df[df.columns[2:]]
        pivot_col = None

        # Get pivot column of that cycle
        for coef in df_coefs.loc[[0]]:
            if df_coefs.loc[df_coefs.index[0], coef] < 0:
                pivot_col = coef
                break

        # If no pivot candidate, optimal solution found
        if pivot_col is None: break
        cycle_count += 1

        # Get pivot line of that cycle
        df_lines = df_coefs[df_coefs[pivot_col] > 0]
        divisao = df_lines.apply(lambda row: row["const"] / row[pivot_col], axis=1)
        pivot_row = divisao.idxmin()

        # Updating table: Change base
        print("< Cycle", cycle_count, "> Pivot: Column", pivot_col, ", Row", pivot_row)
        df.at[pivot_row, "Variável básica"] = pivot_col
        pivot_num = df.at[pivot_row, pivot_col]
        pivot_coefs = df_coefs.loc[df_coefs.index[pivot_row]].to_numpy() / pivot_num

        # Updating table: Substituting pivot variable on rows
        df_ups = df_coefs.drop(pivot_row)
        df_ups = df_ups.apply(lambda row: row.add(pivot_coefs * -1 * row[pivot_col]), axis=1)
        df.update(df_ups)
        print(df)

    return df


df_dict = {
    "Variável básica": ["Z", "x_3", "x_4", "x_5", "x_6"],
    "Z": [1, 0, 0, 0, 0],
    "x_1": [-4, 1, 2, 1, 0],
    "x_2": [-3, 3, 2, 1, 1],
    "x_3": [0, 1, 0, 0, 0],
    "x_4": [0, 0, 1, 0, 0],
    "x_5": [0, 0, 0, 1, 0],
    "x_6": [0, 0, 0, 0, 1],
    "const": [0, 7, 8, 3, 2]
}

df = pd.DataFrame(df_dict)
print(df)
optimal_solution(df)
