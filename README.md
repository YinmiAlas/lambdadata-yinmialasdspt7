# lambdadata-yinmialasdspt7
Unit 3 software engineering
Collecting packages

### Installation
pip install -i https://test.pypi.org/simple/ my-lambdadata-yinmialas==2.2

### Usage
    '''Computes a confusion matrix using numpy for true and pred.

Results are identical and similar in computation time to:
from sklearn.metrics import confusion_matrix

However, this function avoids the dependency on sklearn. ''

compute_confusion_matrix(true, pred)

----------------------------------------------------------------

Create a python file package with a name you prefer ussing code below:
def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

lets take the sum using the created package above 

import unittest
from fractions import Fraction
from my_lambdadata.def_sum_unittest1 import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_bad_type(self):
        data = "banana"
        with self.assertRaises(TypeError):
            result = sum(data)
            self.assertRaises(result)

if __name__ == '__main__':
    unittest.main()