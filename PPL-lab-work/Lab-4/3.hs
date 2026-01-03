filterEven :: [Int] -> [Int]
filterEven = filter odd

main :: IO ()
main = print $ filterEven [1, 2, 3, 4, 5, 6]
