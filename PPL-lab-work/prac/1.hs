firstelem :: [Int] -> Int
firstelem (x:_)=x

main :: IO()
main = do
    print(show(firstelem [1,2,3,4]) ++ " this is the first elem")
