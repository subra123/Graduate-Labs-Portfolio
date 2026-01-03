evenorodd :: Int -> Bool
evenorodd x=(x `mod` 2) == 0 
evenorodd x=(x `mod` 2) == 1 

main :: IO()
main=do


print(evenorodd 6)
print(evenorodd 5)
