from flask_restful import Resource, reqparse

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
    
class Hotel(Resource):
    
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
            
            return {'message': 'Hotel not found.'}, 404 #not found
    
    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('nome')
        argumentos.add_argument('estrelas')
        argumentos.add_arguments('diaria')
        argumentos.add_arguments('cidade')
        
        dados = argumentos.parse_args()
        
        novo_hotel = {
            "hotel_id": hotel_id,
            "nome": dados['nome'],
            "estrelas" :dados['estrelas'],
            "diaria": dados['diaria'],
            "cidade": dados['cidade']
        }
        
        hoteis.append(novo_hotel)
        return novo_hotel, 200
        
    def put(self, hotel_id):
        pass
    
    def delete(self, hotel_id):
        pass