from datetime import date

from model.LoadData import LoadData

brothers = LoadData.load_data()

current_date = date.today()
with open(f'data/bbb_instagram_{current_date}.txt', "w") as file:
    for item in brothers:
        file.write(f'{item}\n')

