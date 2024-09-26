import unittest
from exo1 import Item

class Exo1Test(unittest.TestCase):

    def test_item_construction(self):
        # Test de la création d'un item avec des valeurs spécifiques
        item = Item(10, 20)

        # Vérification de la valeur du poids
        self.assertEqual(20, item.weight)

        # Vérification de la valeur du prix
        self.assertEqual(10, item.price)

    def test_item_with_different_values(self):
        # Test avec des valeurs différentes pour l'item
        item = Item(50, 100)

        # Vérification de la valeur du poids
        self.assertEqual(100, item.weight)

        # Vérification de la valeur du prix
        self.assertEqual(50, item.price)

    def test_item_type_errors(self):
        # Test pour s'assurer que les valeurs fournies sont correctes (par exemple, pas de chaînes ou de valeurs incorrectes)
        with self.assertRaises(TypeError):
            Item("ten", 20)  # Cela doit lever une erreur TypeError
        with self.assertRaises(TypeError):
            Item(10, "twenty")  # Cela doit lever une erreur TypeError

if __name__ == '__main__':
    unittest.main()
