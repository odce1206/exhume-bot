class Char:
    def __init__(self, pname: str, titulo: str):
        self.charName = pname
        self.titulo = titulo

    def setStats(self, fue: int, des: int, vol: int):
        self.fuerza = fue
        self.destreza = des
        self.voluntad = vol
        self.hp = fue + vol + des

    def setClase(self, tipo: str, habEsp: str):
        self.tipo = tipo
        self.habEsp = habEsp

    def setInv(self, oro: int):
        self.oro = oro

    def getInfo(self):
        text = f"""**========= PERSONAJE CREADO =========**
        **Nombre:** {self.charName}
        **Titulo:** {self.titulo}
        ---
        **HP**: {self.hp}
        **Fuerza:** {self.fuerza}
        **Destreza:** {self.destreza}
        **Voluntad:** {self.voluntad}
        **Equipo:** 
        \n  - 1 Arma(1d6) \n  - 1 Pedazo de Armadura \n  - 2 Antorchas \n  - 3 Raciones de Comida \n  - 4 Puntos de equipo \n  - {self.oro} monedas de oro
        ---
        
        """
        return text