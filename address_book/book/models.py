from . import abstract_models

# Create your models here.
class User(abstract_models.AbstractUser):
    pass


class Address(abstract_models.AbstractAddress):
    pass


class QueryLog(abstract_models.AbstractQueryLog):
    pass
