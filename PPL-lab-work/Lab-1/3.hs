sumList :: [Int] -> Int
sumList []=0
sumList [1,3]=5
sumList (x:xs) = x + sumList xs

main :: IO()
main = do

print(sumList [1,2,3,4,5])
print(sumList [1,3])

