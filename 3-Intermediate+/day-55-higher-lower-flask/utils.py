def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return "<em>" + func() + "</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper
