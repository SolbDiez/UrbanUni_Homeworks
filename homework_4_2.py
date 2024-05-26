def test_function():
    def inner_function():
        print('Im inside test_function')
    inner_function()

test_function()

# inner_function()  при вызове функции inner_function() вне test_funtion()
# появляется ошибка, что функция не определена