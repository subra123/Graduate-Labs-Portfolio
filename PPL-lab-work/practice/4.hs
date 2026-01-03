rmap :: ( a-> a) -> [a] -> [a]
rmap _ [] = [] 
rmap op (x:xs) =  op x : rmap op xs


main::IO()
main=do
print(rmap (*2) [1,2,3,4])
print(rmap (+2) [1,2,3,4])
