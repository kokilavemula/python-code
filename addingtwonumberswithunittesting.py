x = 6
y = 5
  
# Adding two nos 
add = x + y 
  
# printing values 
print("Sum of {0} and {1} is {2}" .format(x, y, add)) 


class AdditionTestSuite(unittest.TestCase):
    def setup(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def tearDown(self):
        """ Executed after every test case """
        print("\ntearDown executing after the test case. Result:")

    def test_addition_two_integers(self):
        result = self.calculator.sum(6, 5)
        self.assertEqual(result, 11)

    def test_addition_integer_string(self):
        result = self.calculator.sum(6, "5")
        self.assertEqual(result, "ERROR")

    def test_addition_negative_integers(self):
        result = self.calculator.sum(-6, -5)
        self.assertEqual(result, -11)
        self.assertNotEqual(result, 11)

    def test_addition_negative_positive_integers(self):
        result = self.calculator.sum(-6, 5)
        self.assertEqual(result, -1)

    def test_addition_positive_negative_integers(self):
        result = self.calculator.sum(6, -5)
        self.assertEqual(result, 1)    
    

    
           

# Execute all the tests when the file is executed
if __name__ == "__main__":
    
    
    unittest.main()