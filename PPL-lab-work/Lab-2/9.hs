addpair :: [(Int, Int)] -> [Int]
addpair xs = map (\(a,b) -> a+b) xs

main::IO()
main = do

print(addpair [(3,4),(4,3)])
