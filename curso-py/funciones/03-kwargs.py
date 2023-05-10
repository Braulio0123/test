def get_producto(**datos):
    print(datos["id"], datos["name"])

get_producto(id="1",
             name="pistola",
             desc="Arma de fuego")