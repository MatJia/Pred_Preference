import pandas as pd
import json
from pathlib import Path


DATA_PATH = Path("./dataset/train.csv")


def parse_text_list(prompt, r1, r2):

    p_l = json.loads(prompt)
    r1_l = json.loads(r1)
    r2_l = json.loads(r2)

    final = []

    for p,r,rr in zip(p_l,r1_l,r2_l):
        final.append({"pr":p,"ra":r, "rb":rr})

    return final


def get_label(w_a, w_b, tie):
    return 'a' if w_a else 'b' if w_b else 't' if tie else 'f'


def organize_data(df):

    data_table = {}

    for idx in range(len(df)):
        label = get_label(
            df.loc[idx, 'winner_model_a'],
            df.loc[idx, 'winner_model_b'],
            df.loc[idx, 'winner_tie']
        )

        conv = parse_text_list(
            df.loc[idx, 'prompt'],
            df.loc[idx, 'response_a'],
            df.loc[idx, 'response_b']
        )

        data_table[idx] = {'label':label, 'conv':conv}

    return data_table


def csv_conversion(csv_path):
    df = pd.read_csv(csv_path)

    data_table = organize_data(df)

    return data_table


if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH)

    df_small = df.head(10)

    data_table = organize_data(df_small)

    print(data_table[0]['label'])
    print(data_table[0]['conv'][0]['pr'])