columnas = {
    "PONDERA":    {"tipo": "int",    "completitud": 95},
    "ESTADO":     {"tipo": "int",    "completitud": 100},
    "CAT_OCUP":   {"tipo": "int",    "completitud": 80},
    "EDAD":       {"tipo": "int",    "completitud": 98},
    "REGION":     {"tipo": "int",    "completitud": 100},
    "AGLOMERADO": {"tipo": "int",    "completitud": 90},
    "ANO4":       {"tipo": "int",    "completitud": 100},
    "TRIMESTRE":  {"tipo": "int",    "completitud": 100},
    "ITF":        {"tipo": "int",    "completitud": 60},
    "MAS_500":    {"tipo": "string", "completitud": 85},
    "GDECCFR":    {"tipo": "int",    "completitud": 70},
    "NIVEL_ED":   {"tipo": "int",    "completitud": 88},
}

roles = {
    "docente": {
        "columnas_interes": ["EDAD", "PONDERA", "ANO4", "TRIMESTRE"],
        "criterio_orden": "nombre",
        "orden": "A",
        "completitud_minima": 90
    },
    "investigador": {
        "columnas_interes": ["ESTADO", "REGION", "CAT_OCUP", "GDECCFR", "ITF"],
        "criterio_orden": "completitud",
        "orden": "D",
        "completitud_minima": 80
    },
    "analista": {
    "columnas_interes": ["ESTADO", "CAT_OCUP", "EDAD", "REGION", "AGLOMERADO", "TRIMESTRE", "ITF", "MAS_500", "GDECCFR"],
    "criterio_orden": "completitud",
    "orden": "D",
    "completitud_minima": 75
}
}


def generar_informe(nombre_rol, roles, columnas):
    """
    Genera el informe de columnas correspondiente a un rol.

    Args:
        nombre_rol (str): nombre del rol a informar ('docente', 'investigador', 'analista').
        roles (dict): configuración de roles.
        columnas (dict): información base de cada columna (tipo, completitud).

    Returns:
        list[dict]: columnas de interés del rol, filtradas y ordenadas.
    """
    config_rol = roles[nombre_rol]
    nombres_interes = config_rol["columnas_interes"]

    datos_columnas = list(map(
        lambda nombre: {"nombre": nombre, **columnas[nombre]},
        nombres_interes
    ))

    umbral = config_rol.get("completitud_minima")
    if umbral is not None:
        datos_columnas = list(filter(
            lambda col: col["completitud"] >= umbral,
            datos_columnas
        ))

    criterio = config_rol["criterio_orden"]
    descendente = config_rol["orden"] == "D"
    datos_columnas = sorted(
        datos_columnas,
        key=lambda col: col["nombre"] if criterio == "nombre" else col["completitud"],
        reverse=descendente
    )

    return datos_columnas


def informar(nombre_rol=None, roles=roles, columnas=columnas):
    """
    Informa según el rol solicitado. Si no se especifica rol, informa
    todas las columnas ordenadas por completitud de forma descendente.

    Args:
        nombre_rol (str | None): rol a informar, o None para todas las columnas.
        roles (dict): configuración de roles.
        columnas (dict): información base de columnas.

    Returns:
        list[dict]: columnas resultantes.
    """
    if nombre_rol is None:
        datos_columnas = [{"nombre": nombre, **datos} for nombre, datos in columnas.items()]
        return sorted(datos_columnas, key=lambda col: col["completitud"], reverse=True)

    return generar_informe(nombre_rol, roles, columnas)

