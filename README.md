# Cliente - Servidor. Guardería de mascotas

## Objetivo
- Explicar el patrón de diseño por Cliente-Servidor mediante un sistema de información para una guardería de mascotas.

## Particularidades
- Como este caso pretende manejar las interacciones con los usuarios finales, no está habilitada la opción de crear servicios. Estos podrán ser añadidos modificando directamente el servidor.
- Usamos `threading` para que varios clientes puedan ser atendidos al mismo tiempo.

## `server.py`
- El programa arranca con dos listas `customers` y `services` que almacenarán los clientes a medida que vayan siendo añadidos y una serie de servicios pre-definidos

### `handle-client()`
- Maneja las interacciones de los clientes a nivel individual
- Permite ver los clientes, añadir un cliente, o ver los servicios

## `start-server()`
- Inicializa el servidor y lo deja a la espera de conexiones con clientes