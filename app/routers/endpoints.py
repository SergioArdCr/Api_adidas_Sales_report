from fastapi import APIRouter, Depends
from app.db.database import get_db
from app.models.ventas import Venta, VentaCreate, VentaUpdate
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.services.auth_services import get_current_user

router = APIRouter()

@router.get("/regiones")
def get_regiones(db: Session = Depends(get_db), user=Depends(get_current_user)):
    resultado = db.query(Venta.region).distinct().all()
    return [{"Region": r.region} for r in resultado]

@router.get("/venta/{id}")
def get_venta(id: int, db: Session = Depends(get_db)):
    return db.query(Venta).filter(Venta.id == id).first()

@router.get("/ventas/{region}")
def get_ventas(region: str, db: Session = Depends(get_db)):
    return db.query(Venta).filter(Venta.region == region).all()

@router.get("/ventas/producto/{region}")
def get_ventas_producto(region: str, db: Session = Depends(get_db)):
    resultado = db.query(
        Venta.product, 
        func.sum(Venta.total_sales).label("Total")
    ).filter(Venta.region == region).group_by(Venta.product).all()
    return [{"Product": r.product, "Total": r.Total} for r in resultado]

@router.get("/ventas/estado/{region}")
def get_ventas_estados(region: str, db: Session = Depends(get_db)):
    resultado = db.query(
        Venta.state, 
        func.sum(Venta.total_sales).label("Total")
    ).filter(Venta.region == region).group_by(Venta.state).all()
    return [{"State": r.state, "Total": r.Total} for r in resultado]

@router.post("/ventas")
def crear_venta(venta: VentaCreate, db: Session = Depends(get_db)):
    nueva = Venta(**venta.model_dump())
    db.add(nueva)
    db.commit()
    return {"mensaje": "Venta creada correctamente"}

@router.put("/ventas/{id}")
def actualizar_venta(id: int, venta: VentaUpdate, db: Session = Depends(get_db)):
    db.query(Venta).filter(Venta.id == id).update({"total_sales" : venta.total_sales})
    db.commit()
    return {"mensaje": f"Venta {id} actualizada correctamente"}

@router.delete("/ventas/{id}")
def eliminar_venta(id: int, db: Session = Depends(get_db)):
    db.query(Venta).filter(Venta.id == id).delete()
    db.commit()
    return {"mensaje": f"Venta {id} eliminada correctamente"}