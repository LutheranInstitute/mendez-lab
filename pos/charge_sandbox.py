"""BOCETO — sin ejecutar. Cobro de prueba en el sandbox de Authorize.net.

Usa una tarjeta de prueba pública; nunca datos reales. En producción la tarjeta
llega como token de Accept.js (opaqueData), no como número.
"""
import os
from decimal import Decimal

from dotenv import load_dotenv
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import createTransactionController

load_dotenv()


def charge(amount: Decimal, ref_id: str = "POS-0001"):
    auth = apicontractsv1.merchantAuthenticationType()
    auth.name = os.environ["AUTHNET_API_LOGIN_ID"]
    auth.transactionKey = os.environ["AUTHNET_TRANSACTION_KEY"]

    card = apicontractsv1.creditCardType()
    card.cardNumber = "4111111111111111"  # tarjeta de prueba Visa
    card.expirationDate = "2030-12"
    card.cardCode = "123"

    payment = apicontractsv1.paymentType()
    payment.creditCard = card

    tx = apicontractsv1.transactionRequestType()
    tx.transactionType = "authCaptureTransaction"
    tx.amount = amount
    tx.payment = payment

    req = apicontractsv1.createTransactionRequest()
    req.merchantAuthentication = auth
    req.refId = ref_id
    req.transactionRequest = tx

    ctrl = createTransactionController(req)  # sandbox es el entorno por defecto
    ctrl.execute()
    res = ctrl.getresponse()

    if res is not None and res.messages.resultCode == "Ok" and hasattr(res.transactionResponse, "transId"):
        print("✓ recibo", ref_id, "transId", res.transactionResponse.transId)
        return str(res.transactionResponse.transId)
    print("✗ falló", res.messages.message[0]["text"].text if res is not None else "sin respuesta")
    return None


if __name__ == "__main__":
    charge(Decimal("1.00"))
