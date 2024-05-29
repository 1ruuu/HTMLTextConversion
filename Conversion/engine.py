# engine.py


from Conversion.conversion import Chineseconversion

class Tools:
    """
    A class to Tools

    Methods
    -------
    get_news_info()
        Get ETtoday news
    save_to_database()
        Save to BigQuery DB
    """

    def __init__(self) -> None:

        self.conversion = Chineseconversion()

    def chinese_conversion(self, file_path: str):

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        result = self.conversion.prase(content)
        new_file_path = file_path.split('.')[0]+'_conversion.html'
        with open(new_file_path, 'w', encoding='utf-8') as file:
            file.write(result)

        return (f'Conversion successful, file path is {new_file_path}')

        


        

    
