import unittest

class prova():
    x = 5
    def areEquals(self, altro):
        return self.x == altro


class CommonTests(object):
    def testCommon(self):
        print ('Calling BaseTest:testCommon')
        value = 5
        self.assertEquals(value, 5)

class SubTest1(unittest.TestCase, CommonTests):

    def testSub1(self):
        print ('Calling SubTest1:testSub1')
        sub = 3
        self.assertEquals(sub, 3)


class SubTest2(unittest.TestCase, CommonTests):
    """
    Test that numbers between 0 and 5 are all even.
    """
    def testSub2(self):
        print ('Calling SubTest2:testSub2')
        sub = 4
        self.assertEquals(sub, 4)
        mycl = prova()
        self.assertEquals(mycl.areEquals(5), True)
        self.assertEquals(mycl.areEquals(7), True)   #Fail

@unittest.skip("demonstrating skipping")
class SubTest3(unittest.TestCase, CommonTests):
    pass

if __name__ == '__main__':
    unittest.main()