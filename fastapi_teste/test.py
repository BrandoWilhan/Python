from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def mostra_pedido():
    return {
      "id": 1,
      "cliente": "Larissa Silva",
      "produto": "Camarão Internacional",
      "valor": 136.0,
      "entregue": True,
      "estado": "DELIVERED",
      "timestamp": "2021-05-02T19:48:09.765Z"
    }

@app.post("/")
async def registra_pedido(payload: dict):
    return payload