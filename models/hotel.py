from sqlalchemy import banco
__tablename__ = 'hoteis'
    
hotel_id = banco.Columns(banco.String, primary_key=True)
nome = banco.Columns(banco.String(80))
estrelas = banco.Columns(banco.Float(precision=1))
diaria = banco.Columns(banco.Float(precision=2))
cidade = banco.Columns(banco.String(40))

class Hotel(banco.Model):    
    def __init__(self,hotel_id, nome, estrelas,diaria,cidade):
            self.hotel_id = hotel_id
            self.nome = nome
            self.estrelas = estrelas
            self.diaria = diaria
            self.cidade = cidade
            
    def json(self):
            return {
                'hotel_id': self.hotel_id,
                'nome':self.nome,
                'estrelas': self.estrelas,
                'diaria':self.diaria,
                'cidade':self.cidade
            }
    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id=hotel_id).first() #SELECT * FROM hoteis WHERE hotel_id = $hotel_id
        if hotel :
            return hotel
        return None
    
    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()