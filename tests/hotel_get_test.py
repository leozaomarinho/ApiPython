from unittest.mock import patch
from resource.hotel import Hotel
from flask.testing import FlaskClient

def test_get_hotel_list():
    with patch('HotelModel.query') as mock_query:
        # Mock o retorno do HotelModel.query.all()
        mock_query.all.return_value = [HotelModel(nome='Hotel1', estrelas=4, diaria=200, cidade='Cidade1')]

        # Crie uma instância da sua aplicação Flask (se você não tiver uma já configurada)
        app = create_flask_app()

        # Use o FlaskClient para testar a rota
        with app.test_client() as client:
            response = client.get('/hotels/1')  # Substitua o endpoint conforme necessário

            # Verifique se o código de status é 200 OK
            assert response.status_code == 200

            # Verifique se o conteúdo da resposta é o esperado
            assert 'hoteis' in response.json
            assert len(response.json['hoteis']) == 1
            assert response.json['hoteis'][0]['nome'] == 'Hotel1'
            assert response.json['hoteis'][0]['estrelas'] == 4
            # Adicione mais verificações conforme necessário

# Função auxiliar para criar uma instância da aplicação Flask
def create_flask_app():
    app = Flask(__name__)
    app.add_url_rule('/hotels/<int:hotel_id>', view_func=Hotel.as_view('hotel'))
    return app


