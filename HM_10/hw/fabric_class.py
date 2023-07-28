class Fabric:
    

    def __init__(self, obj, *args):   
        self.obj_class = obj
        self.obj_attrs = args

    def do_copy(self):
        return self.obj_class(*self.obj_attrs)