double :: [Int] -> [Int]
double = map(*2)

incerement :: [Int] -> [Int]
incerement = map(+1)




doubleAndIncrement :: [Int] -> [Int]
doubleAndIncrement = incerement . double 

main :: IO()
main = do

print(doubleAndIncrement [1,2,3])
print(doubleAndIncrement [2,4,6])
