main :: IO()
main = do
    putStrLn "Enter the first Number: "
    input1 <- getLine

    putStrLn "Enter the Second Number: "
    input2 <- getLine

    
    putStrLn "Enter the operator(-,+,*,/): "
    op <- getLine

    let a = read input1 :: Double
    let b = read input2 :: Double 

    let result = case op of 
                    "+" -> a+b
                    "-" -> a-b
                    "*" -> a*b
                    "/" -> if b /= 0 then a/b else error "Division error by 0" 
                    _ -> error "Invalid Operation"
    putStrLn ("The Result of the operation is: " ++ show result)

