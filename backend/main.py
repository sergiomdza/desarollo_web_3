import logging
import time

from fastapi import FastAPI, HTTPException, Request
from fastapi.exception_handlers import http_exception_handler
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ExecutionTimeout, OperationFailure, PyMongoError
from prometheus_fastapi_instrumentator import Instrumentator
from pythonjsonlogger.json import JsonFormatter
from starlette.exceptions import HTTPException as StarletteHTTPException

# --- Logs en formato JSON para poder filtrarlos en Loki/Grafana ---
handler = logging.StreamHandler()
handler.setFormatter(JsonFormatter("{asctime}{levelname}{name}{message}", style="{"))

# Nuestro logger y el de uvicorn (arranque y errores no controlados) usan el mismo formato
for name in ("backend", "uvicorn"):
    logging.getLogger(name).handlers = [handler]

logger = logging.getLogger("backend")
logger.setLevel(logging.INFO)

# Sin log por cada petición: los errores HTTP los registra log_http_exception
# y el conteo/latencia de peticiones ya lo tenemos en Prometheus
logging.getLogger("uvicorn.access").disabled = True

app = FastAPI()
Instrumentator().instrument(app).expose(app, endpoint="/metrics")


# Registra el mensaje (detail) de cada HTTPException, incluidos los 404 de rutas inexistentes
@app.exception_handler(StarletteHTTPException)
async def log_http_exception(request: Request, exc: StarletteHTTPException):
    nivel = logging.ERROR if exc.status_code >= 500 else logging.WARNING
    logger.log(nivel, exc.detail, extra={"path": request.url.path, "status_code": exc.status_code})
    return await http_exception_handler(request, exc)

def datos_error_mongo(exc: PyMongoError) -> dict:
    """Campos útiles de un error de Mongo para el log, sin el traceback completo."""
    detalles = exc.details if isinstance(exc, OperationFailure) and exc.details else {}
    return {
        "error_type": type(exc).__name__,
        "mongo_code": getattr(exc, "code", None),
        "mongo_code_name": detalles.get("codeName"),  # p. ej. "AuthenticationFailed"
        "timeout": exc.timeout,
        # En errores de conexión, str(exc) incluye la topología completa del cluster; solo dejamos la primera parte
        "error_detail": str(exc).split(", Topology Description")[0],
    }


# Mongo DB connection
mongo_client = MongoClient("mongodb://admin:web3@mongo-service.default.svc.cluster.local:27017/")
database = mongo_client["desarrollo_web_3"]
productos = database["productos"]

@app.get("/")
def default():
    return {"message": "HOLA MUNDO!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/productos")
def get_productos():
    contexto = {"operacion": "find", "coleccion": "productos"}
    try:
        return list(productos.find({}, {"_id": 0}))
    # Va primero: ExecutionTimeout también es OperationFailure
    except (ConnectionFailure, ExecutionTimeout) as exc:  # Mongo caído, inalcanzable o lento
        logger.error("Mongo no disponible", extra={**contexto, **datos_error_mongo(exc)})
        raise HTTPException(status_code=503, detail="La base de datos no está disponible, no se pudo obtener los productos") from exc
    except OperationFailure as exc:  # Mongo respondió con un error (auth, permisos, consulta inválida)
        nivel = logging.CRITICAL if exc.code in (13, 18) else logging.ERROR  # 13 = Unauthorized, 18 = AuthenticationFailed
        logger.log(nivel, "Mongo rechazó la operación", extra={**contexto, **datos_error_mongo(exc)})
        raise HTTPException(status_code=500, detail="Error interno del servidor") from exc

@app.get("/error_400")
def get_error():
    raise HTTPException(status_code=400, detail="El ID no puede ser cero")
    return []

@app.get("/error_500")
def get_error():
    raise HTTPException(status_code=500, detail="Error en la conexión a la DB")
    return []

@app.get("/logins")
def get_error():
    return [1,2,3,4,5]

@app.get("/wait")
def get_error():
    time.sleep(3)
    return "Respuesta despues de 3 segundos"