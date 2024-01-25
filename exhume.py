from modelos.char import Char
def chargen():
    import random

    # GENERADOR DE NOMBRE Y TITULOS
    random_name = ["Verdu", "Graham", "Kardak", "Ambul" "Sieger", "Guntram", "Hademar", "Anselm", "Hartmut",
                   "Hemma",
                   "Ishilde", "Asgard", "Diemut", "Livina"]
    titulos = ("Acechadxr de Sombras",
               "Esencia Maldita",
               "Vagabundx de la Niebla",
               "Arpía Silenciosa",
               "Verdugo Desvanecido",
               "Brujx Sin Rostro",
               "Espectro Olvidado",
               "Hereje Errante",
               "Sombra Eterna",
               "Azote de las Pesadillas",
               "Hoja en la oscuridad",
               "Luz en las tinieblas,"
               "Puño de hierro",
               "Escudo implacable",
               "Amx de los secretos")

    pers = Char(random.choice(random_name), random.choice(titulos))
    # GENERADOR DE STATS
    fue = random.randint(2, 5)
    des = random.randint(2, 5)
    vol = random.randint(2, 5)

    pers.setStats(fue, des, vol)

    if fue > des and fue > vol:
        pers.setClase('Guerrero', 'Puedes atacar 2 veces')
    elif des > fue and des > vol:
        pers.setClase('Ladron', 'Puedes ocultarte de inmediato')
    elif vol > fue and vol > des:
        pers.setClase('Mago', 'Puedes manipular un elemento')
    else:
        pers.setClase('La suerte te sonrie, tienes un personaje raro', "Inventa tu clase y habilidad especial.")
    # GENERADOR DE EQUIPO
    oro = random.randint(2, 12) * 5
    pers.setInv(oro)

    return pers