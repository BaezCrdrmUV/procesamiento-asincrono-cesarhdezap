import asyncio
from datetime import datetime


async def main():

    hola = asyncio.create_task(
        decir_hola())

    mundo = asyncio.create_task(
        decir_mundo())


    tiempo = datetime.now()
    print(f"----- Hora comienzo {tiempo.strftime('%H:%M:%S')} -----")

    await hola
    await mundo

    tiempo = datetime.now()
    print(f"----- Hora final {tiempo.strftime('%H:%M:%S')} -----")


async def decir_hola ():
    tiempo = datetime.now()
    print(f"Tarea decir hola empezo: {tiempo.strftime('%H:%M:%S')}")
    print('hola')

async def decir_mundo ():
    tiempo = datetime.now()
    print(f"Tarea decir mundo empezo: {tiempo.strftime('%H:%M:%S')}")
    print('mundo')

asyncio.run(main())