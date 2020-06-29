def function(self):
    print("x")

TypeClass = type("typeClass", (object,),{"x": 5, "xy": function})

t = TypeClass()

t.xy()