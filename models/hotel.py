from sql_alchemy import banco
__tablename__ = 'hoteis'
    
hotel_id = banco.Columns(banco.String, primary_key=True)
nome = banco.Columns(banco.String(80))
estrelas = banco.Columns(banco.Float(precision=1))
diaria = banco.Columns(banco.Float(precision=2))
cidade = banco.Columns(banco.String(40))
    
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