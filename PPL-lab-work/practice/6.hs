fizzbuzz :: Int -> String
fizzbuzz x
    | x `mod` 3 == 0 && x `mod` 5 == 0 = "fizzbuzz" 
    | x `mod` 3 == 0 = "fizz"
    | x `mod` 5 == 0 = "buzz"
    | otherwise = show x
    


main::IO()
main=do
print(fizzbuzz 20)
print(fizzbuzz 15)
print(fizzbuzz 12)
print(fizzbuzz 1)

let result = [fizzbuzz x | x <- [1..100]]
print(result)
