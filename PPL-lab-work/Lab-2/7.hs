firstn :: Int -> [Int] -> [Int]
firstn n=take n

main::IO()
main =do

print (firstn 3 [1,2,3,4,5,6])
