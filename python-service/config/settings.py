# define web server configuration
# ==============================================================================
import redis
import uuid

# API version
API_VERSION = "v0.01"

# web server setting
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8801
SERVER_WORKER = 1
SERVER_DEBUG = False

# kafka settings
KAFKA_HOST = "0.0.0.0:9092"
KAFKA_DATA_TOPIC = "coda"
MESSAGE_MAX_BYTES = 15728640 #15 GB
KAFKA_PRODUCER_SETTINGS = {
                            "bootstrap.servers": KAFKA_HOST,
                            "message.max.bytes": MESSAGE_MAX_BYTES,
                            "queue.buffering.max.messages": 10000000,
                            "queue.buffering.max.ms": 2,
                            "socket.keepalive.enable": True,
                            "socket.blocking.max.ms": 1,
                            "message.send.max.retries": 100,
                            "socket.timeout.ms": 1000,
                            "metadata.request.timeout.ms": 1000,
                            "default.topic.config": {
                                                        "message.timeout.ms": 1000,
                                                        "request.timeout.ms": 1000
                                                    }
                            }

KAFKA_CONSUMER_SETTINGS = {
                            'bootstrap.servers': KAFKA_HOST,
                            'group.id': "coda", #uuid.uuid1().hex
                            'default.topic.config':
                                {
                                    'auto.offset.reset': 'earliest'
                                }
                        }
# cassandra settings
CASSANDRA_HOST = "127.0.0.1"
CASSANDRA_DATA_KEYSAPCE = "coda"
CASSANDRA_TRANSACTION_RAW_DATA = "transaction_raw_data"

# spark settings
SPARK_APP_NAME = "CODA STREAMING"
SPARK_MASTER_CONF = "local[2]"
SPARK_CASSANDRA_CONNECTION_CONF = "0.0.0.0"
STREMAING_WINDOW = 9 # seconds

# file processing settings
FILE_EXTENSIONS_DETAILS = {
    "audio": ["mp3", "mpa", "aif", "cda", "mid", "midi", "ogg", "wav", "wma", "wpl"],
    "video": ["3g2", "3gp", "avi", "flv", "h264", "m4v", "mkv", "mov", "mp4", "mpg", "mpeg", "rm", "swf", "vob", "wmv"],
    "image": ["png", "jpeg", "gif", "bmp", "tiff"],
    "text": ["csv", "log", "doc", "json", "docx", "odt", "pdf", "rtf", "text", "txt", "wks", "wps", "wpd"]
}

# google cloud storage buckte name
GOOGLE_STORAGE_BUCKTE_NAME = "gotest-166812.appspot.com"

# logger settings
LOG_FILE_MAX_BYTES = 102400
LOGS_DIR = "logs"

# API urls
STREAMING_API_URL = "http://%s:%s/stream-data/" %(SERVER_HOST, SERVER_PORT)

# redis Settings
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = ''
REDIS_CACHE_DB = 0
REDIS_AUTH_DB = 1

# connection pool for application cache client
CACHE_REDIS_POOL = redis.ConnectionPool(
    host=REDIS_HOST, port=REDIS_PORT, db=REDIS_CACHE_DB,
    password=REDIS_PASSWORD)
CACHE_REDIS_CLIENT = redis.StrictRedis(connection_pool=CACHE_REDIS_POOL)
# Connection pool for application auth client
AUTH_REDIS_POOL = redis.ConnectionPool(
    host=REDIS_HOST, port=REDIS_PORT, db=REDIS_AUTH_DB,
    password=REDIS_PASSWORD)
AUTH_REDIS_CLIENT = redis.StrictRedis(connection_pool=AUTH_REDIS_POOL)


#JSON Web Token settings
# JWT_SECRET_KEY = "#CodaRocks"
# JWT_ALGORITHM = "HS256"

# Error message
# JSON_ERROR = """Malformed JSON Could not decode the request body.The JSON was
# incorrect or not encoded as UTF-8."""

# Load env
# ROOT_PATH = os.path.abspath('')
# ENV = os.path.join(ROOT_PATH, '.env')
# load_dotenv(ENV)

# MongoDB connection settings
# MONGO_DB = 'coda'
# MONGO_HOST = os.environ.get('MONGO_HOST')
# MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME')
# MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD')
# MONGODB_AUTH_DB = os.environ.get('MONGODB_AUTH_DB')
# base_mongo_client = pymongo.MongoClient(
#     'mongodb://{username}:{password}@{host}:{port}/?'
#     'authSource={authsource}'.format(
#     	username=MONGODB_USERNAME, password=MONGODB_PASSWORD,
#     	host=MONGO_HOST, port=27017, authsource=MONGODB_AUTH_DB
#     	)
#     )
#
# MONGO_URL_CELERY = 'mongodb://{}:{}@{}:{}/celery_retailstack?authSource={}'.format(
#         MONGODB_USERNAME, MONGODB_PASSWORD, MONGO_HOST, 27017, MONGODB_AUTH_DB)
#
# mongo_client = base_mongo_client[MONGO_DB]

# Define collections names
#authinfo = mongo_client.oauth2_client

# -----------------------------END-----------------------------------
