from fastapi import HTTPException
from .schemas import ClienteCreate

_clientes: list[dict] = [
    {"id": 1, "nombre": "Ana García",    "email": "ana@gmail.com",   "telefono": "2614001111"},
    {"id": 2, "nombre": "Luis Pérez",    "email": "luis@gmail.com",  "telefono": "2614002222"},
    {"id": 3, "nombre": "Marta López",   "email": "marta@gmail.com", "telefono": "2614003333"},
]
_next_id = 4


def obtener_todos(nombre: str | None, email: str | None) -> list[dict]:
    resultado = _clientes
    if nombre:
        resultado = [c for c in resultado if nombre.lower() in c["nombre"].lower()]
    if email:
        resultado = [c for c in resultado if email.lower() in c["email"].lower()]
    return resultado


def obtener_por_id(cliente_id: int) -> dict:
    for c in _clientes:
        if c["id"] == cliente_id:
            return c
    raise HTTPException(status_code=404, detail=f"Cliente con id {cliente_id} no encontrado")


def crear(datos: ClienteCreate) -> dict:
    global _next_id
    nuevo = {"id": _next_id, **datos.model_dump()}
    _clientes.append(nuevo)
    _next_id += 1
    return nuevo


def actualizar(cliente_id: int, datos: ClienteCreate) -> dict:
    cliente = obtener_por_id(cliente_id)
    cliente.update(datos.model_dump())
    return cliente


def eliminar(cliente_id: int) -> dict:
    cliente = obtener_por_id(cliente_id)
    _clientes.remove(cliente)
    return {"mensaje": f"Cliente '{cliente['nombre']}' eliminado correctamente"}