# CRUD - C: create, R: read(listing, details), U: update, D: delete

class CreateMixin:
    def _get_or_set_objects(self):
        try:
            self.id
            self.objects
        except (NameError, AttributeError):
            self.objects = []
            self.id = 0

    def __init__(self) -> None:
        self._get_or_set_objects()

    def post(self, **kwargs):
        self.id += 1
        obj = dict(id = self.id, **kwargs)
        self.objects.append(obj)
        return {'status': '201 created', 'mag': obj}

class ReadMixin:
    def list(self):
        res = [{'id': obj['id'], 'title': obj['title']}for obj in self.objects]
        return {'status': '200 OK', 'msg': res}

    def detail(self, id, **kwargs):
        object_id = [x['id'] for x in self.objects] 
        left = 0
        right  = len(self.objects) - 1
        mid = len(self.objects) // 2

        while object_id[mid] != id and left <= right:
            if id < object_id[mid]:
                right = mid -1
            else:
                left = mid +1
            mid = (left + right) // 2
            
        if left > right:
            return {'status': '404 Not Found'}
        return {'status': '200 OK', 'msg': self.object[id]}



    




# obj = CreateMixin()
# obj.post(title = 'Apple', description = 'Phone', qty = 10, price = 250)


