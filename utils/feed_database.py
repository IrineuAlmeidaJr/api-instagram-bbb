import os
from datetime import date

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from utils.LoadData import LoadData


def create_dataframe(current_date, brothers):
    dir_file = '../data/bbb_instagram.xlsx'
    if os.path.isfile(dir_file):
        df = pd.read_excel('../data/bbb_instagram.xlsx')
        new_df = pd.DataFrame(list(map(lambda b: [b.Id, b.Name, b.Followers], brothers)))
        df[current_date] = new_df[2]
    else:
        df = pd.DataFrame(list(map(lambda b: [b.Id, b.Name.strip(), b.Followers], brothers)))
        df.columns = ['Id', 'Nome', '2024-01-08']

    print(df)
    return df


def create_graphic(brothers):
    dataframe_name_img = pd.DataFrame(list(map(lambda b: [b.Name, (int(b.Followers / 1000))], brothers)))
    dataframe_name_img.columns = ['Nome', 'Seguidores']
    sns.set(rc={'figure.figsize': (20, 10)})
    graphic = sns.barplot(
        x=dataframe_name_img["Seguidores"],
        y=dataframe_name_img['Nome'],
        data=dataframe_name_img
    )
    graphic.bar_label(graphic.containers[0])
    plt.show()
    return graphic.get_figure()


def write_documents(current_date, brothers, dataframe, graphic_figure):
    dataframe.to_excel('../data/bbb_instagram.xlsx', index=False)
    graphic_figure.savefig(f'../data/bbb_instagram.png')
    with open(f'../data/bbb_instagram.txt', "w") as file:
        for item in brothers:
            file.write(f'{item.Id},{item.Name},{item.Instagram_username},{item.Followers},{item.Url_image}')
    with open(f'../backup/bbb_instagram_{current_date}.txt', "w") as file:
        for item in brothers:
            file.write(f'{item.Id},{item.Name},{item.Instagram_username},{item.Followers},{item.Url_image}')


def execute():
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    current_date = str(date.today())
    #brothers = LoadData.load_data_file()
    brothers = LoadData.load_data_intagram()
    dataframe = create_dataframe(current_date, brothers)
    graphic_figure = create_graphic(brothers)
    write_documents(current_date, brothers, dataframe, graphic_figure)


execute()
