""" data set """
import zipfile
import os
import kaggle
import pandas as pd

class DataSet:
    """ Data Source for NCAA Compeition
    """
    def __init__(self, data_path=None):
        if data_path is None:
            self.data_path = os.path.abspath(os.path.join(os.path.expanduser('~'), 'kaggle-ncaa-2019-data'))
            print(f'default path used {self.data_path}') 
        else:
            self.data_path = os.path.abspath(data_path)
            
        self.competition = 'mens-machine-learning-competition-2019'
        self.zip_file_list = ['DataFiles.zip', 'MasseyOrdinals.zip']
        data_dir = self.data_path
        self.csv_files = dict(
            city = "Cities.csv",
            conf = "Conferences.csv",
            conftour = "ConferenceTourneyGames.csv",
            gamecity = "GameCities.csv",
            massey = "MasseyOrdinals.csv",
            t_compact_result = "NCAATourneyCompactResults.csv",
            t_detail_result = "NCAATourneyDetailedResults.csv",
            t_seed_slot = "NCAATourneySeedRoundSlots.csv",
            t_seed = "NCAATourneySeeds.csv",
            t_slot = "NCAATourneySlots.csv",
            r_compact_result = "RegularSeasonCompactResults.csv",
            r_detail_result = "RegularSeasonDetailedResults.csv",
            season = "Seasons.csv",
            st_compact_result = "SecondaryTourneyCompactResults.csv",
            st_team = "SecondaryTourneyTeams.csv",
            team = "Teams.csv",
            coache = "TeamCoaches.csv",
            team_conf = "TeamConferences.csv",
            team_spelling = "TeamSpellings.csv",
        )
        self.codec=dict(
            team_spelling="ISO-8859-1"
        )
        
    def cache_data_exist_(self):
        """ check whether cache data are OK
        """
        if not os.path.exists(self.data_path):
            return False
        else:
            return all([self.get_file_path(key) for key in self.list_raw_keys()])
                
    
    def fetch_from_remote_(self):
        print('Fetch data from kaggle website')
        for file in self.zip_file_list:
            print(f'File: {file}')
            kaggle.api.competition_download_file(competition = self.competition,
                                                 file_name = file, 
                                                 path = self.data_path)
            if not os.path.exists(os.path.join(self.data_path, file)):
                raise FileNotFoundError(f'Can not find the downloaded file {os.path.join(self.data_path, file)}')
        
            # extract csvs
            print(f'Unzip')
            zipfile.ZipFile(os.path.join(self.data_path, file)).extractall(path=self.data_path)
            
        if not self.cache_data_exist_():
            raise ValueError('Unable to fetch all csv data')
    
    def get_file_path(self, key):
        return os.path.normpath(os.path.join(self.data_path, self.csv_files[key]))
    
    def list_raw_keys(self):
        return list(self.csv_files.keys())
    
    def get_raw_data(self, key):
        """ Get data for a certain key
        """
        if not self.cache_data_exist_():
            print(f"cache can not be found at {self.data_path}.")
            self.fetch_from_remote_()
        data = pd.read_csv(self.get_file_path(key),  encoding = self.codec[key] if key in self.codec else None)
        return data
            
            