# Procesamiento Asincrono
- ¿Qué es el procesamiento asíncrono?
El procesamiento asincrónico es una forma de distribuir el procesamiento de una aplicación entre sistemas conectados. Las solicitudes y respuestas se transmiten en diferentes sesiones. No existe dependencia de procesamiento entre una solicitud y una respuesta, y no se hacen suposiciones sobre el momento de la respuesta.


- ¿En qué escenarios se utiliza?
En general, el procesamiento asincrónico es aplicable a cualquier situación en la que no sea necesario o deseable vincular recursos locales mientras se procesa una solicitud remota.
El procesamiento asincrónico no es adecuado para aplicaciones que requieren cambios sincronizados en recursos locales y remotos; por ejemplo, no se puede usar para procesar actualizaciones simultáneas relacionadas con la información de datos en diferentes sistemas.

- Ejemplo en lenguaje de programación favorito.
Ejemplo en el archivo ProcesamientoAsincrono.py, crea dos tareas que imprimen al mismo tiempo.