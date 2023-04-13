import pandas as pd

class NJCleaner():
    def __init__(self, csv_path:str) -> None:
        self.data = pd.read_csv(csv_path)

    def order_by_scheduled_time(self) -> pd.DataFrame:
        order = self.data.sort_values(by=['scheduled_time'])
        return order
    
    def drop_columns_and_nan(self) -> pd.DataFrame:
        dropped = self.data.drop(["from", "to"], axis=1)
        return dropped.dropna()
    
    def convert_date_to_day(self) -> pd.DataFrame:
        dataframe = self.data
        dataframe["date"] = pd.to_datetime(dataframe["date"])
        dataframe["day"] = dataframe["date"].dt.day_name()
        dataframe.drop("date", axis=1, inplace=True)
        return dataframe
    
    def convert_scheduled_time_to_part_of_the_day(self) -> pd.DataFrame:
        dataframe = self.data
        dataframe['scheduled_time'] = pd.to_datetime(dataframe['scheduled_time'])
        dataframe["part_of_the_day"] = dataframe['scheduled_time'].apply(lambda x: 
            'early_morning' if x.hour >= 4 and x.hour <= 7
            else 'morning' if x.hour >= 8 and x.hour <= 11
            else 'afternoon' if x.hour >= 12 and x.hour <= 15
            else 'evening' if x.hour >= 16 and x.hour <= 19
            else 'night' if x.hour >= 20 and x.hour <= 23
            else 'late_night'
        )
        return dataframe.drop(["scheduled_time"], axis=1)

    def convert_delay(self) -> pd.DataFrame:
        dataframe = self.data
        dataframe["delay"] = dataframe['delay_minutes'].apply(lambda x: 1 if x >= 5 else 0)
        return dataframe
    
    def drop_unnecessary_columns(self) -> pd.DataFrame:
        dropped = self.data.drop(['train_id', 'actual_time', 'delay_minutes'], axis=1)
        return dropped
    
    def save_first_60k(self, path:str):
        self.data.head(60000).to_csv(path, index=False)

    def prep_df(self, path:str = 'data/NJ.csv'):
        self.data = self.order_by_scheduled_time()
        self.data = self.drop_columns_and_nan()
        self.data = self.convert_date_to_day()
        self.data = self.convert_scheduled_time_to_part_of_the_day()
        self.data = self.convert_delay()
        self.data = self.drop_unnecessary_columns()
        self.save_first_60k(path)