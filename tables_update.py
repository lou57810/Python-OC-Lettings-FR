import os
# from pathlib import Path
import sqlite3
import pandas as pd
import shutil


path_db = "oc-lettings-site.sqlite3"


def create_temp_path():
    path_csv = 'data_csv'
    try:
        os.mkdir(path_csv)
        # print("Folder %s created!" % path_csv)
        # check whether directory already exists
    except FileExistsError:
        print("Folder %s already exists" % path_csv)


def delete_temp_path(folder):
    path = os.path.join(os.getcwd(), folder)
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Le répertoire '{path}' a été supprimé avec succès.")
        else:
            print(f"Le répertoire '{path}' n'existe pas.")
    except Exception as e:
        print(f"Erreur lors de la suppression du répertoire : {e}")


def data_exchange(src, dst):
    path_csv = "data_csv/"
    # Extract :
    connection = sqlite3.connect(path_db)
    data = pd.read_sql_query(f"SELECT * FROM {src}", connection)
    # print('data', data)

    name = src
    new = name.split('_')
    new_name = new[-1]
    csv = path_csv + f'{new_name}.csv'

    # Transform to CSV
    data.to_csv(csv, index=False)

    # Transfer to existing table
    connection = sqlite3.connect(path_db)
    data = pd.read_csv(csv)
    data.to_sql(dst, connection, if_exists='replace', index=False)
    connection.close()


def drop_old_datas():
    # Extract :
    connection = sqlite3.connect(path_db)

    # drop old table
    connection.execute("DROP TABLE oc_lettings_site_address")
    connection.execute("DROP TABLE oc_lettings_site_letting")
    connection.execute("DROP TABLE oc_lettings_site_profile")
    print("data dropped successfully")

    # close the connection
    connection.close()


create_temp_path()
data_exchange('oc_lettings_site_address', 'lettings_address')
data_exchange('oc_lettings_site_profile', 'profiles_profile')
data_exchange('oc_lettings_site_letting', 'lettings_letting')
drop_old_datas()
delete_temp_path('data_csv')
