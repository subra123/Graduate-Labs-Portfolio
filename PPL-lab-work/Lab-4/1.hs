swapTuple :: (a, b) -> (b, a)
swapTuple (a, b) = (b, a)

main :: IO ()
main = print $ swapTuple (10, "Hello")
