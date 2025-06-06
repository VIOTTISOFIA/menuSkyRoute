import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from menuSkyRoute.gestion_clientes import listar_clientes

clientes = listar_clientes()

print("🧾 Lista de clientes:")
print("-" * 40)

for cliente in clientes:
    print(f"🆔 ID Cliente: {cliente['ID_Cliente']}")
    print(f"🏢 Razón Social: {cliente['Razon_Social']}")
    print(f"💼 CUIT: {cliente['CUIT']}")
    print(f"📧 Correo: {cliente['Correo']}")
    print("-" * 40)  # Línea para separar cada cliente

