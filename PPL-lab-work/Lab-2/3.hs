squares :: [Int] -> [Int]
squares = map(^2)

sumlist :: [Int] -> Int
sumlist []=0
sumlist (x:xs) = x + sumlist xs

ans :: [Int] -> Int
ans = sumlist . squares

main :: IO()
main =do

print(ans [3,5,6])
