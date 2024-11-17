import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
 def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(15), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(30), 150)

    def test_senior_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(70), 100)

    # Grouped test cases for boundary values
    def test_boundary_values(self):#age boundaries#
        # Child boundaries
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

        # Teen boundaries
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

        # Adult boundaries
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

        # Senior boundaries
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

    # if invalid input like negative age entered
    def test_invalid_inputs(self):
        
        self.assertEqual(self.zoo.get_ticket_price(-1), "invalid")

        # if user enters non-integer value
        with self.assertRaises(TypeError):
            self.zoo.get_ticket_price("twenty")
        with self.assertRaises(TypeError):
            self.zoo.get_ticket_price(25.5)
if __name__ == '__main__':
    unittest.main()