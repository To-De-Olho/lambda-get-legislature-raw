from app.src.LambdaFunction.function import lambda_handler

def test_function(event):
   response = lambda_handler(event, None)

   assert response == event