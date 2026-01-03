multiplyElements :: Num a => [a] -> a -> [a]
multiplyElements lst n = [x * n | x <- lst]

main :: IO ()
main = print $ multiplyElements [1, 2, 3, 4] 2
