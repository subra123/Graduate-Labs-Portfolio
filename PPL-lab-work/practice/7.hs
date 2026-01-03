data Shape =Circle Float
    | Rectangle Float Float  
    deriving Show 

area:: Shape -> Float
area (Circle r) = pi * r *r
area (Rectangle w l) = w* l 

main = do
    let a = Circle 3
    let b = Rectangle 3 3 
    print(area a)
    print(area b)
