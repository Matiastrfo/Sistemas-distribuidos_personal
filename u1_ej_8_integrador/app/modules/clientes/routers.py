from fastapi import APIRouter
from typing import Optional
from .schemas import ClienteCreate, ClienteResponse
from . import services

router = APIRouter(prefix="/clientes", tags=["Clientes"])


@router.get("/", response_model=list[ClienteResponse])
def listar_clientes(
    nombre: Optional[str] = None,
    email: Optional[str] = None,
):
    return services.obtener_todos(nombre, email)


@router.get("/{cliente_id}", response_model=ClienteResponse)
def obtener_cliente(cliente_id: int):
    return services.obtener_por_id(cliente_id)


@router.post("/", response_model=ClienteResponse, status_code=201)
def crear_cliente(datos: ClienteCreate):
    return services.crear(datos)


@router.put("/{cliente_id}", response_model=ClienteResponse)
def actualizar_cliente(cliente_id: int, datos: ClienteCreate):
    return services.actualizar(cliente_id, datos)


@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int):
    return services.eliminar(cliente_id)