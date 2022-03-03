from decouple import config

# Obtenha seu token em OpenWeatherMap.org
# Crie um arquivo .env e escreva dessa forma: TOKEN={seu_token}
TOKEN = config('TOKEN')

class Queries:
    def __init__(self):
        self.city  = ""
        self.token = ""
        self.lang  = ""
        self.unit  = ""
    # Construtor Padrão

    def __init__(self, city):
        self.city  = city
        self.lang  = 'pt_br'
        self.unit  = 'metric'
        self.token = TOKEN
    # Construtor Parametrizado
    
    def getQueries(self):
        return (
            "?q="      + self.city 
            +"&appid=" + self.token
            +"&lang="  + self.lang 
            +"&units=" + self.unit
        )
    # getQueries
# Queries