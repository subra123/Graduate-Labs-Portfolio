reverselist :: [Int]->[Int]
reverselist [] = []
reverselist (x:xs) = reverselist xs ++ [x]

main :: IO()
main =do

print(reverselist [1,2,3,4])
