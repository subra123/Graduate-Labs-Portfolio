removeodd :: [Int]->[Int]
removeodd = filter even

main :: IO()
main = do

print(removeodd [1,2,3,4,5])
