from unittest import TestCase


class TestPowerset(TestCase):
    def test_powerset(self):
        try:
            from build import powerset
        except ImportError:
            self.assertFalse("No function found")


        result = powerset([2, 3, 4])


        self.assertNotEqual(None, result)

        self.assertEqual((), next(result))
        self.assertEqual((2, ), next(result))
        self.assertEqual((3, ), next(result))
        self.assertEqual((4, ), next(result))
        self.assertEqual((2,3), next(result))
        self.assertEqual((2,4), next(result))
        self.assertEqual((3,4), next(result))
        self.assertEqual((2,3,4), next(result))


