"""
Crear una lista con el contenido de esta tabla
Accion  Aventura          Deportes
GTA     Assasins creed    Fifa 21
COD     Crash             Pes 21
PUBG    POP               F1 21


"""

tabla = [
    {
        "categoria": "Accion",
        "juegos": [
            "GTA",
            "COD",
            "PUBG"
        ]
    },
    {
        "categoria": "Aventura",
        "juegos": [
            "Assasins creed",
            "Crash",
            "POP"
        ]
    },
    {
        "categoria": "Deportes",
        "juegos": [
            "Fifa 21",
            "PES 21",
            "F1 21"
        ]
    }
]

for categoria in tabla:
    print(f"---------- {categoria['categoria']} ----------")
    for juego in categoria['juegos']:
        print(juego)
