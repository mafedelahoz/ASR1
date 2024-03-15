from ..models import Variable


def get_variables():
    queryset = Variable.objects.all()
    return (queryset)


def create_variable(str):
    measurement = str.save()
    measurement.save()
    return ()


def get_variable_by_name(name):
    try:
        variable = Variable.objects.get(name=name)
        return (variable)
    except:
        variable = None
        return (variable)
