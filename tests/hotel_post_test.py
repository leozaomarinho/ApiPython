from unittest.mock import patch
from resource.hotel import Hotel

def test_post_new_hotel():
    with patch('HotelModel.find_hotel') as mock_find_hotel:
        mock_find_hotel.return_value = None  # Simula que o hotel não existe ainda

        # Crie uma instância da sua aplicação Flask (se você não tiver uma já configurada)
        app = create_flask_app()

        # Use o FlaskClient para testar a rota
        with app.test_client() as client:
            # Simule uma solicitação POST com dados
            response = client.post('/hotels/1', json={'nome': 'NovoHotel', 'estrelas': 3, 'diaria': 150, 'cidade': 'NovaCidade'})

            # Verifique se o código de status é 200 OK
            assert response.status_code == 200

            # Verifique se o conteúdo da resposta é o esperado
            assert 'nome' in response.json
            assert response.json['nome'] == 'NovoHotel'
            assert response.json['estrelas'] == 3
            # Adicione mais verificações conforme necessário
