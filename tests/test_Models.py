###
### a class test case, with test fixtures.
###
from src.movielens import models


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
        user = models.User()
        user.id = 1242
        user.ratings = {}
        for i in range(1, 10):
            r = models.Rating()
            r.value = i
            user.ratings[i] = r
        assert user.get_rating_average() == 5

