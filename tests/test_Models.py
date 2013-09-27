###
### a class test case, with test fixtures.
###
from .. import src

class TestUser:
    def __init__(self):
        self.is_setup = False

    def setUp(self):
        assert not self.is_setup
        self.is_setup = True

    def tearDown(self):
        assert self.is_setup
        self.is_setup = False

    def test_get_rating_average(self):
        user = src.Models.User()
        user.ratings = {}
        for i in range(1,10):
            r = src.Models.Rating()
            r.value = i
            user.ratings[i] = r
        assert user.test_get_rating_average() == 5

