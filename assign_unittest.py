import unittest 
import assign as ss
class SimpleTest(unittest.TestCase): 
   
    def test(self):         
        self.assertTrue(True)
        
    def test_isupper(self):
        self.assertTrue(ss.Z.isupper())
        self.assertTrue(ss.Z, '')
        
    # Check for these expected result if the result is not euals to expected then the test will fail    
    def test_isoutput(self):
        self.assertEqual(ss.cartvalue('AAAAAAA'), 310, "should be 310")
        self.assertEqual(ss.cartvalue('DABABA'), 190, "should be 190")
        self.assertEqual(ss.cartvalue('AAABB'), 175, "should be 175")  
        self.assertEqual(ss.cartvalue('CDBA'), 115, "should be 115") 
        self.assertEqual(ss.cartvalue('AAABBD'), 190, "should be 190")  
        self.assertEqual(ss.cartvalue(''), 0, "should be 0")  
        self.assertEqual(ss.cartvalue('AAAA'), 180, "should be 180")   
        self.assertEqual(ss.cartvalue('A'), 50, "should be 50")  
        self.assertEqual(ss.cartvalue('AA'), 100, "should be 100")  
        self.assertEqual(ss.cartvalue('AAA'), 130, "should be 130")  
        self.assertEqual(ss.cartvalue('AAAB'), 160, "should be 160")  
        self.assertEqual(ss.cartvalue('AB'), 80, "should be 80")                 
  
if __name__ == '__main__': 
    unittest.main() 