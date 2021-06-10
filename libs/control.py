def control_age(func):
    def wrapper(*args, **kwargs):
        if str(args[0].age).isdigit():
            if args[0].age < 55:
                func(*args, **kwargs)
        else:
            pass
    return wrapper

def control_name(func):
    def wrapper(*args, **kwargs):
        if not 'fuck' in str(args[0].name):
            func(*args, **kwargs)
        else:
            pass
    return wrapper

@control_age
@control_name
def check(obj):
    print(obj.name)
    print(obj.age)