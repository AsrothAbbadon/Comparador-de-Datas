import pytz
from dateutil.parser import parse
from datetime import datetime

class Converter:

        def __init__(self, canvas_date, db_date) -> None:
            self.timezone: str = 'America/Sao_Paulo'
            self.canvas_date: str = canvas_date
            self.canvas_date_converted: str = self.__canvas_date_converter()
            self.db_date:str = db_date
            self.formatter: str = '%Y-%m-%d %H:%M:%S.%f'
            self.db_date_formatted: str = self.__db_data_formartter()
            self.__check_data()
        
        def __canvas_date_converter(self) -> str:
            date = parse(self.canvas_date)
            date_converted = date.astimezone(pytz.timezone(self.timezone)).replace(tzinfo=None)
            return date_converted
            
            
        def __db_data_formartter(self) -> str:
            db_date = self.db_date
            formatter = self.formatter
            db_date_formatted = datetime.strptime(db_date, formatter)
            return db_date_formatted
            
        def __check_data(self) -> str:
            if self.canvas_date_converted == self.db_date_formatted:
                print('As datas são iguais')
            else:
                print('Datas diferentes')
            

data = Converter()