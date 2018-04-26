# python web services
# gunicorn app:app --bind 0.0.0.0:8801 --worker-class sanic.worker.GunicornWorker --workers=<Worker>
# ==============================================================================

from sanic import Sanic
from sanic import response
import time
import uuid
import ujson

from confluent_kafka import Producer,Consumer
from config import settings, logger_settings
from cassandra.cluster import Cluster

cluster = Cluster([settings.CASSANDRA_HOST])

app = Sanic("CODA")
# to add before start and after start connector
# app.blueprint(kafka_bp)

application_logger = logger_settings.application_logger
confluent_producer = Producer(settings.KAFKA_PRODUCER_SETTINGS)


@app.route('/coda/v0.01/helloWorld', methods=['GET'])
async def ping(request):
    """
    API to check web service status.
    :param request:
    :return: return static message
    """
    result = {
            "message": "Hello World, This is Python!!",
    		"code": 200
            }
    return response.json(result)

#@app.route('coda/{}/stream-data/'.format(settings.API_VERSION),methods=['POST'])
@app.route('coda/v0.01/stream-data/',methods=['POST'])
async def publish_data_to_kafka(request):
    """
    API to publish message to kafka
    :param request: api payload data
    :return: return message
    """
    message = ""
    try:
        query = request.json
        data = query.get('content',{})
        topic = query.get('topic',settings.KAFKA_DATA_TOPIC)
        record_id = uuid.uuid1().hex
        transaction_id = uuid.uuid1().hex
        customer_id = uuid.uuid1().hex
        data_type = "json"
        size = len(data)
        path = "na"
        contents = data
        created_on = str(time.time()).split(".")[0]

        published_data = {"id": record_id, "transaction_id": transaction_id, "customer_id": customer_id, \
                          "data_type": data_type, "size": size, "path": path, \
                          "contents": contents,"created_on":created_on}
        published_data = ujson.dumps(published_data)

        # publish_message(topic= topic,data= published_data )

        published_data = published_data.encode()
        confluent_producer.produce(topic, published_data)
        confluent_producer.flush()
        #confluent_producer.poll(0)

        # app.producer.produce(settings.KAFKA_DATA_TOPIC, processed_data)
        # app.producer.flush()
        # app.producer.poll(0)

        message = "success"
    except Exception as error:
        data = {}
        application_logger.error("%s" %(error))
        message = "Please look into error :  %s" %(error)

    return response.json({'message': message})


SERVER_HOST = settings.SERVER_HOST
SERVER_PORT = settings.SERVER_PORT
SERVER_WORKER = settings.SERVER_WORKER
SERVER_DEBUG = settings.SERVER_DEBUG

if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT,workers=SERVER_WORKER,debug=SERVER_DEBUG)