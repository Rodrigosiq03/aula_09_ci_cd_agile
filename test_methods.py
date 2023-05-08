import methods

def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10

def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_sub():
    value1 = 10
    value2 = 5
    
    output = methods.sub(value1, value2)
    
    assert output == 5
    
def test_add():
    value1 = 10
    value2 = 5
    
    output = methods.add(value1, value2)
    
    assert output == 15
    
def test_div():
    value1 = 10
    value2 = 5
    
    output = methods.div(value1, value2)
    
    assert output == 2

def test_mult():
    value1 = 10
    value2 = 5
    
    output = methods.mult(value1, value2)
    
    assert output == 50