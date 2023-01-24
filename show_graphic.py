import instaloader

from model.LoadData import LoadData
from datetime import date

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Config Instagram
bot = instaloader.Instaloader()
# bot.interactive_login('irineu.almeida.jr@icloud.com')


profile = instaloader.Profile
# brothers = LoadData.load_data_intagram()
brothers = LoadData.load_data_file()

dataframe_name = pd.DataFrame(list(map(lambda b: [b.Name, b.Followers], brothers)))
dataframe_name.columns = ['Nome', 'Seguidores']

print(dataframe_name)

dataframe_name_img = pd.DataFrame(list(map(lambda b: [b.Name, (int(b.Followers/1000))], brothers)))
dataframe_name_img.columns = ['Nome', 'Seguidores']
sns.set(rc={'figure.figsize': (20, 10)})
graphic = sns.barplot(
    x=dataframe_name_img["Seguidores"],
    y=dataframe_name_img['Nome'],
    data=dataframe_name_img
)
graphic.bar_label(graphic.containers[0])
figure = graphic.get_figure()

# Write Files
current_date = date.today()

with open(f'data/bbb_instagram_{current_date}.txt', "w") as file:
    for item in brothers:
        file.write(f'{item}\n')

dataframe_name.to_excel(f'data/bbb_instagram_{current_date}.xlsx', index=False)
figure.savefig(f'data/bbb_instagram_{current_date}.png')

plt.show()
