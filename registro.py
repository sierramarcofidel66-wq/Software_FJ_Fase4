
"""Registro de eventos y errores de Software FJ."""

import logging
from pathlib import Path

logger = logging.getLogger("software_fj")
logger.setLevel(logging.INFO)

if not logger.handlers:
    ruta = Path(__file__).with_name("sistema.log")

    handler = logging.FileHandler(
        ruta,
        encoding="utf-8"
    )

    formato = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    handler.setFormatter(formato)
    logger.addHandler(handler)
    logger.propagate = False


def registrar_evento(mensaje):
    """Guarda información sobre eventos del sistema."""
    logger.info("%s", mensaje)


def registrar_error(error):
    """Registra los errores y sus detalles."""
    logger.error(
        "Error detectado: %s",
        error,
        exc_info=True
    )

