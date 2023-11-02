from aws_lambda_powertools import Logger
from Adapters import parameter_store, repository,get_data_service
from sqlalchemy.orm import Session
from Ports import mapper_legislature
from aws_lambda_powertools.utilities.typing import LambdaContext

PARAMETERS = parameter_store.get_parameters(["UrlDadosAbertos","ConnectionString"])
CONNECTION = repository.conn(PARAMETERS["ConnectionString"])

logger = Logger("get-legislature-raw")

@logger.inject_lambda_context
def lambda_handler(event, context: LambdaContext):
    logger.info(event)
    try:
        with Session(CONNECTION) as session:
            get_data_recursive(PARAMETERS['UrlDadosAbertos'] + event, session)
        
        return {
            "statuscode": 200
        }

    except Exception as err:
        logger.exception(err)
        raise err

def get_data_recursive(url, session):
    response = get_data_service.get_data(url)
    response = response.json()
    legislatures = mapper_legislature.mapper(response)
    repository.save_legislatures(session, legislatures)
    logger.info(f"Pagination: {response['links']}")

    for values in response['links']:
        if values['rel'] == 'next':
            get_data_recursive(values['href'], session)
         