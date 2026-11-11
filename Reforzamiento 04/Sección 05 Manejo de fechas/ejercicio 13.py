from datetime import datetime, timedelta


def calcular_vencimiento(fecha_inicial_str, plazo_dias):
    fecha_inicial = datetime.strptime(fecha_inicial_str, "%d/%m/%Y")
    fecha_vencimiento = fecha_inicial + timedelta(days=plazo_dias)
    return fecha_vencimiento


def evaluar_vencimiento(fecha_vencimiento):
    # Normalizamos la fecha actual a medianoche para comparar solo días exactos
    hoy = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    fv = fecha_vencimiento.replace(hour=0, minute=0, second=0, microsecond=0)

    diferencia = (fv - hoy).days

    if diferencia > 0:
        return f"Pendiente (Faltan {diferencia} días para el vencimiento)"
    elif diferencia == 0:
        return "Vence hoy"
    else:
        diferencia_abs = abs(diferencia)
        return f"Ya venció (Han transcurrido {diferencia_abs} días desde el vencimiento)"


# Pruebas dinámicas relativas a la fecha de hoy
hoy_str = datetime.now().strftime("%d/%m/%Y")
ayer_str = (datetime.now() - timedelta(days=5)).strftime("%d/%m/%Y")
futuro_str = (datetime.now() - timedelta(days=10)).strftime("%d/%m/%Y")

casos = [
    (futuro_str, 15),  # Vencimiento futuro
    (ayer_str, 5),  # Vence hoy
    (futuro_str, 2)  # Ya vencido
]

print("--- SEGUIMIENTO DE VENCIMIENTOS ---")
for f_ini, plazo in casos:
    f_venc = calcular_vencimiento(f_ini, plazo)
    estado = evaluar_vencimiento(f_venc)

    print(f"\nFecha inicial: {f_ini} | Plazo: {plazo} días")
    print(f"Fecha de vencimiento: {f_venc.strftime('%d/%m/%Y')}")
    print(f"Fecha actual del sistema: {hoy_str}")
    print(f"Resultado de evaluación: {estado}")