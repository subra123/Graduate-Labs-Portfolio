squar :: [Int] -> [Int]
squar [] = []
squar (x:xs) = (\x -> x*x) x : squar xs 

main::IO()
main=do
print(squar [1,2,3,4,5])
