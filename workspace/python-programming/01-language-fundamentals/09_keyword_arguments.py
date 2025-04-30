def fn1(x,y, **kwargs):
    print(type(kwargs))
    print(f"X={x}, Y={y}, kwargs={kwargs}")


fn1(23,24,user_name="admin", password="admin123")