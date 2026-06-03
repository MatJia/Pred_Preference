from parser import csv_conversion, DATA_PATH

def acc_count(data_table, label):
    if data_table is None:
        raise ValueError("Data table is empty")

    acc = 0

    for idx in range(len(data_table)):
        if data_table[idx]['label'] == label:
            acc += 1

    return acc / len(data_table)


if __name__ == '__main__':
    data_table = csv_conversion(DATA_PATH)

    print(acc_count(data_table, 'a'))
    print(acc_count(data_table, 'b'))
    print(acc_count(data_table, 't'))
    print(acc_count(data_table, 'f'))

    print("majority baseline accuracy =", max(
        acc_count(data_table, 'a'),
        acc_count(data_table, 'b'),
        acc_count(data_table, 't')
    ))