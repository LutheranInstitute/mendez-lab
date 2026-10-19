# pos · Punto de venta con Authorize.net

🧪 **Boceto, sin ejecutar.** Sandbox únicamente.

## Piezas

| Pieza | Para qué | SDK |
|---|---|---|
| Servidor de cobro | Crear transacciones (auth/capture, refund, void) | `authorizenet` (Python) |
| Tarjeta en línea | El cliente escribe la tarjeta en el navegador, nosotros solo recibimos un token | Accept.js / Accept Hosted |
| Tarjeta presente | Lector físico en la tienda | Authorize.net In-Person SDK (iOS / Android) |
| Webhooks | Confirmar pagos, reembolsos y fraudes | Webhooks API |

## Arranque (sandbox)

1. Crear cuenta sandbox en developer.authorize.net → obtener **API Login ID** y **Transaction Key**.
2. Guardarlas en el vault / `.env` (ver `.env.example`). Nunca en el repo.
3. `pip install -r requirements.txt`
4. `python charge_sandbox.py` → cobro de prueba con tarjeta de prueba de Visa.

## Pendiente de decidir

- ¿Qué vende el POS y dónde (tienda física, evento, en línea)?
- ¿Lector de tarjeta? (define si usamos In-Person SDK)
- Cuenta de comerciante real (gateway + merchant account) — decisión humana.
