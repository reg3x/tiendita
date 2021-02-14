

class BaseService(object):

    def save(self, instance):
        self.instance.save()


class ProductService(BaseService):

    def save(self, instance):
        super().save(instance)
