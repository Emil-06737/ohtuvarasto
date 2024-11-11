from varasto import Varasto

# too long line: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
def main():
    mehua, olutta = main1()
    main2(mehua, olutta)

def main1():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    print(f"""Luonnin jälkeen:
Mehuvarasto: {mehua}
Olutvarasto: {olutta}
Olut getterit:
saldo = {olutta.saldo}
tilavuus = {olutta.tilavuus}
paljonko_mahtuu = {olutta.paljonko_mahtuu()}
Mehu setterit:
Lisätään 50.7""")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}\nOtetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)
    return mehua, olutta

def main2(mehua, olutta):
    print(f"Olutvarasto: {olutta}\nolutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}\nMehuvarasto: {mehua}" \
          f"\nmehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}" \
          f"\nOlutvarasto: {olutta}\nolutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}\nOlutvarasto: {olutta}" \
          f"\nMehuvarasto: {mehua}\nmehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}\nMehuvarasto: {mehua}")

if __name__ == "__main__":
    main()
