primet :: Int -> Int -> Bool
primet _ 1 = True 
primet x d = (x `mod` d /= 0) &&  primet x (d-1)

prime :: Int -> (Int,Bool)
prime x
    | x<=1 = (x,False)
    | otherwise = (x,primet x (x-1))

main = do 
    print(prime 7)
    print(prime 9)
    let result = [prime x | x <- [1..10]]
    print(result)
