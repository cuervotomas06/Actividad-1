# Bitácora - Actividad 1

## Qué estructuras usé y por qué
Usé diccionarios para todo. Para `columnas`, cada columna es una clave y adentro tiene su tipo y completitud. Para `roles`, cada rol es una clave y adentro tiene sus columnas de interés, cómo ordenar y el umbral. Elegí diccionarios porque permiten buscar directo por nombre (por ejemplo `columnas["EDAD"]`) sin tener que recorrer toda una lista buscando cuál es cuál.

## Valores que elegí para los roles
- `docente`: EDAD, PONDERA, ANO4, TRIMESTRE — orden alfabético ascendente, umbral 90%.
- `investigador`: ESTADO, REGION, CAT_OCUP, GDECCFR, ITF — orden por completitud descendente, umbral 80%.
- `analista`: EDAD, MAS_500, ESTADO, ITF — orden por completitud descendente, umbral 75%.

Elegí umbrales distintos en cada rol para poder probar que el filtro realmente funciona: por ejemplo, en `investigador` las columnas GDECCFR (70%) e ITF (60%) quedan afuera porque no llegan al 80% mínimo.

## Por qué separar `roles` de la función
Si algún día quiero cambiar qué columnas ve un rol, o agregar un rol nuevo, solo tengo que editar el diccionario `roles`, sin tocar la función `generar_informe`. La función queda genérica y sirve para cualquier rol que le pase.

## Parámetros con valor por defecto
En `informar()`, `nombre_rol' tiene default `None` (así, si no le paso nada, informa todas las columnas). También `roles` y `columnas` tienen como default los diccionarios globales, así no tengo que escribirlos cada vez que llamo a la función.

## Qué pasa si agrego una columna nueva
Solo agrego una entrada nueva al diccionario `columnas`. Si además quiero que un rol la vea, agrego su nombre a la lista `columnas_interes` de ese rol. No hay que tocar ninguna función.

## Qué pasa si un rol tiene un criterio de orden raro (ej. "promedio")
Con el código actual, el programa fallaría al intentar ordenar (porque `key=lambda col: col["nombre"] if criterio == "nombre" else col["completitud"]` asume que si no es "nombre" es "completitud"). Una mejora sería agregar una validación al principio que chequee que `criterio_orden` sea "nombre" o "completitud", y si no, avisar con un mensaje claro en vez de que falle de forma confusa.

## Errores que tuve y cómo los resolví
- Al principio, `filter()` me devolvía un objeto `filter` (no una lista), y como en un momento lo recorrí dos veces para revisar el resultado, la segunda vez me aparecía vacío — un objeto `filter` se "consume" al iterarlo una sola vez. Lo resolví envolviendo el resultado con `list()` inmediatamente después de aplicar `filter()`, tal como quedó en el código final.
- Al definir `completitud_minima` como opcional, usar acceso directo `rol["completitud_minima"]` habría lanzado `KeyError` en un rol que no la tuviera definida. Lo resolví usando `dict.get("completitud_minima")`, que devuelve `None` si la clave no existe, y tratando ese `None` como "sin filtro".



## Modificaciones
- Previo al inicio de la actividad mi `analista` no incluia ni `PONDERA` ni `ANO4` por lo tanto modifique manualmente `analista` con una lista mas amplia excluyendo a proposito `PONDERA` y `ANO4`
- Modifique la estructura `columnas` agregando `NIVEL_ED` con su respectivo `tipo` y `completitud` sin intervenir con los roles existentes. `NIVEL_ED` aparece unicamente en el informe general el cual muestra las 12 `columnas` y no va a aparecer en ningun rol ya que al `generar_informe()` buscas las columnas explicitamente listadas en `columnas_interes` de ese rol y al no haber editado ningun rol no se muestra en ninguno. En cambio cuando `nombre_rol is None`, el codigo recorre todo el diccionario `columnas` por lo tanto lo incluye.
- En `generar_informe` uso `map()` para transformar cada nombre de `columnas` en un diccionario con sus datos completos; y uso `filter()` para descartar las `columnas` que no llegan al umbral de `completitud_minima`. Y su ventaja frente a un for es que utilizando un for deberia declarar una lista vacia antes y dentro del bucle usar `.append()` en cada vuelta.