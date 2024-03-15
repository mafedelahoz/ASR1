from ..models import Variable

def get_variables():
    queryset = Variable.objects.all()
    return (queryset)

def create_variable(str):
    measurement = str.save()
    measurement.save()
    return ()