# coding=utf-8


def digger(item_name, item_info, freq=None, method='last'):

    # get data from excel files

    import pandas as pd

    [wbname, shtname, time_column, time_s_row, item_column]=item_info
    df_item = pd.read_excel(wbname, sheetname=shtname, parse_cols=[time_column-1, item_column-1],
                            header=None, skiprows=time_s_row-1, index_col=0)
    df_item.columns = [item_name]

    if freq is None:
        return df_item
    else:
        return df_item.resample(freq).agg(method)


def sniffer(item_name):

    # get item information from item list

    import pandas as pd

    df_list = pd.read_excel('z:\国内经济数据\指标列表.xlsx', index_col=0)

    item_info = df_list.loc[item_name].values

    return item_info


def datamagnet(item_name, freq=None, method='last'):

    # combine sniffer and digger

    import pandas as pd

    if type(item_name)==list:
        df = []
        for item in item_name:
            item_info = sniffer(item)
            df.append(digger(item, item_info, freq, method))
        return pd.concat(df, axis=1)
    else:
        item_info = sniffer(item_name)
        return digger(item_name, item_info, freq, method)
