# mendez-lab · Laboratorio de los hermanos Méndez

**Yael · Priscila · Daniel** — un laboratorio de I+D dentro de [LutheranInstitute](https://github.com/LutheranInstitute).

> Evidence ≠ Authority: la supervisión informa, el humano decide.

## Líneas de trabajo

| Carpeta | Qué es | Estado |
|---|---|---|
| [`pos/`](pos/) | Punto de venta propio con el SDK de Authorize.net (sandbox) | 🧪 boceto, sin ejecutar |
| [`pos_reselling/`](pos_reselling/) | Reventa de POS / pagos (programa de resellers de Authorize.net) | 📝 investigación |

## Reglas del laboratorio

1. **Sandbox primero.** Ninguna llave de producción en este repo. Las llaves viven en el vault / variables de entorno (`.env`, ignorado por git).
2. **Sin datos de tarjeta en nuestro servidor.** Tarjeta en línea → Accept.js / Accept Hosted (token). Tarjeta presente → lector + SDK In-Person.
3. **Cada cambio es un commit** y cada cobro de prueba deja recibo.
4. **Código no ejecutado se marca como boceto.**
5. **Un humano autoriza** cualquier paso a producción.

## Equipo

- **Yael Méndez** — arquitectura, agentes, #startabusiness
- **Priscila Méndez**
- **Daniel Méndez**

`#opensourceware` · `#startabusiness`
