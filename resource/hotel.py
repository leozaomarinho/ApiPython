from flask_restful import Resource

hoteis = [
    {'hotel_id': 'alpha',
     'nome':'Alpha Hotel',
     'estrelas': 4.3,
     'diaria':420.34,
     'cidade':'Rio de janeiro'},
    
     {'hotel_id': 'beira-mar',
     'nome':'Beira-Mar Hotel',
     'estrelas': 4.5,
     'diaria':450.00,
     'cidade':'Florianopolis'}, 
     
     {'hotel_id': 'paraiso',
     'nome':'Paraiso Hotel',
     'estrelas': 4.9,
     'diaria':500.00,
     'cidade':'Porto de Galinas'}
]

class Hoteis(Resource):
    def get(self):
        return{'Hoteis':hoteis}
    #a library do flask converte o dict automaticamente para json
