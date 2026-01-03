larger :: Int->Int->Int
larger a b
    | a > b = a
    | a == b = "equla"
    | otherwise = b

main :: IO()
main = do

print(larger 4 5)
print(larger 10 9)
print(larger 5 5)
