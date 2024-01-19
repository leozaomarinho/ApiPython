from flask_restful import Resource, reqparse
from models.hotel import HotelModel

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
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('estrelas')
    argumentos.add_argument('diaria')
    argumentos.add_argument('cidade')
    
    def get(self, hotel_id):
      hotel = Hotel.find_hotel(hotel_id)
      if hotel :
          return hotel
      return {'message':'Hotel not found.'}, 404
    
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {'message':'Hotel id"{}"already exists.'.format(hotel_id)}, 400
        
        dados = Hotel.argumentos.parse_args()
        novo_hotel = HotelModel(hotel_id,**dados)
        novo_hotel = {"hotel_id": hotel_id, **dados}
        hoteis.append(novo_hotel)
        return novo_hotel, 201
        
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()   
        hotel_objeto = {"hotel_id": hotel_id, **dados}
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return hotel,200
        hoteis.append(novo_hotel), 201#criado    
        return novo_hotel
    
    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message':'Hotel deletado'}, 200