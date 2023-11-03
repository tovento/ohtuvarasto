from varasto import Varasto

MEHUA = Varasto(100.0)
OLUTTA = Varasto(100.0, 20.2)

def main():
    """TODO"""
    luonnin_jalkeen()
    olut_getterit()
    mehu_setterit()
    virhetilanteita1()
    virhetilanteita2()
    virhetilanteita3()

def luonnin_jalkeen():
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {MEHUA}")
    print(f"Olutvarasto: {OLUTTA}")

def olut_getterit():
    print("Olut getterit:")
    print(f"saldo = {OLUTTA.saldo}")
    print(f"tilavuus = {OLUTTA.tilavuus}")
    print(f"paljonko_mahtuu = {OLUTTA.paljonko_mahtuu()}")

def mehu_setterit():
    print("Mehu setterit:")
    print("Lisätään 50.7")
    MEHUA.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {MEHUA}")
    print("Otetaan 3.14")
    MEHUA.ota_varastosta(3.14)
    print(f"Mehuvarasto: {MEHUA}")

def virhetilanteita1():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def virhetilanteita2():
    print(f"Olutvarasto: {OLUTTA}")
    print("OLUTTA.lisaa_varastoon(1000.0)")
    OLUTTA.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {OLUTTA}")

    print(f"Mehuvarasto: {MEHUA}")
    print("MEHUA.lisaa_varastoon(-666.0)")
    MEHUA.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {MEHUA}")

def virhetilanteita3():
    print(f"Olutvarasto: {OLUTTA}")
    print("OLUTTA.ota_varastosta(1000.0)")
    saatiin = OLUTTA.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {OLUTTA}")

    print(f"Mehuvarasto: {MEHUA}")
    print("MEHUA.otaVarastosta(-32.9)")
    saatiin = MEHUA.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {MEHUA}")


if __name__ == "__main__":
    main()
