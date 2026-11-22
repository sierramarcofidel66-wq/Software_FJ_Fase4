
import logging

logging.basicConfig(
    filename="sistema.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)


def registrar_evento(mensaje):
    logging.info(mensaje)


def registrar_error(error):
    logging.error(
        "Error detectado: %s",
        error,
        exc_info=True
    )
