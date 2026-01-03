power :: Int -> Int -> Int
power 0 _ = 0
power _ 0 = 1
power x y = x * power x (y-1)

main :: IO()
main = do

print(power 2 4)
