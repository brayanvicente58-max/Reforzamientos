class CuentaBancaria:
    # Constructor
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        self.titular = titular
        self.saldo = saldo_inicial

    # Implementación con validaciones
    def depositar(self, monto: float):
        if monto <= 0:
            print(f"[ERROR] El monto a depositar debe ser mayor a 0. Intentado: S/ {monto}")
        else:
            self.saldo += monto
            print(f"Depósito exitoso de S/ {monto:.2f}. Nuevo saldo: S/ {self.saldo:.2f}")

    def retirar(self, monto: float):
        if monto <= 0:
            print(f"[ERROR] El monto a retirar debe ser mayor a 0. Intentado: S/ {monto}")
        elif monto > self.saldo:
            print(f"[RECHAZADO] Fondos insuficientes. Intenta retirar S/ {monto:.2f}, pero tu saldo es S/ {self.saldo:.2f}")
        else:
            self.saldo -= monto
            print(f"Retiro exitoso de S/ {monto:.2f}. Saldo restante: S/ {self.saldo:.2f}")

    def mostrar_saldo(self):
        print(f"\n--> Saldo final de {self.titular}: S/ {self.saldo:.2f}")


# Prueba con cuenta, depósitos y retiros
cuenta = CuentaBancaria("David Morales", 300.0)

print(f"--- Cuenta de {cuenta.titular} ---")
# Depósitos
cuenta.depositar(100.0)
cuenta.depositar(-50.0)  # Inválido
cuenta.depositar(200.0)

print()
# Intentos de retiro
cuenta.retirar(150.0)
cuenta.retirar(600.0)  # Excede saldo
cuenta.retirar(-20.0)   # Inválido

# Saldo final
cuenta.mostrar_saldo()