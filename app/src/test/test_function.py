from unittest.mock import patch
from aws_lambda_powertools.utilities.typing import LambdaContext
class Response:
   pass

   def json():
      return {
         "dados": [
            {
               "id": 57,
               "uri": "https://dadosabertos.camara.leg.br/api/v2/legislaturas/57",
               "dataInicio": "2023-02-01",
               "dataFim": "2027-01-31"
            }
         ],
         "links": []
      }

@patch("app.src.LambdaFunction.Adapters.Adapters.get_data_service.get_data")
@patch("app.src.LambdaFunction.Adapters.Adapters.repository.save_legislatures")
def test_function_return_200(
   save_legislatures,
   get_data
):

   with patch("app.src.LambdaFunction.Adapters.parameter_store.get_parameters") as parameters,\
      patch("app.src.LambdaFunction.Adapters.Adapters.repository.conn") as conn:
      from app.src.LambdaFunction.function import lambda_handler
      
      save_legislatures.return_value = None
      get_data.return_value = Response

      response = lambda_handler("event", LambdaContext)

      assert response == {'statuscode': 200}

     