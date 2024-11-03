import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_kostruktorissa_negatiivinen_tilavuus_nollataan(self):
        self.varasto = Varasto(-1)
        self.assertEqual(self.varasto.tilavuus, 0)

    def test_konstruktorissa_negatiivinen_saldo_nollataan(self):
        self.varasto = Varasto(10, -1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_konstruktorissa_saldosta_tulee_enimmillaan_tilavuus(self):
        self.varasto = Varasto(10, 12)
        self.assertEqual(self.varasto.saldo, 10)

    def test_lisays_ei_lisaa_negatiivista(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisayksessa_saldosta_tulee_enimmillaan_tilavuus(self):
        self.varasto.lisaa_varastoon(12)
        self.assertEqual(self.varasto.saldo, 10)

    def test_ottamisessa_negatiivinen_ottaa_nolla(self):
        self.assertEqual(self.varasto.ota_varastosta(-1), 0)

    def test_ottaminen_ottaa_enimmillaan_saldon(self):
        self.varasto = Varasto(10, 5)
        saldo = self.varasto.saldo
        self.assertEqual(self.varasto.ota_varastosta(12), saldo)

    def test_ottamisessa_saldon_ylittyessa_saldo_nollaantuu(self):
        self.varasto = Varasto(10, 5)
        self.varasto.ota_varastosta(12)
        self.assertEqual(self.varasto.saldo, 0)

    def test_merkkijono_oikeaa_muotoa(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")