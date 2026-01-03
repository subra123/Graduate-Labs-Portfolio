multiply :: Int -> [Int] -> [Int]
multiply x [] = []
multiply x (y:ys) = x*y : multiply x ys

main :: IO()
main = do

print(multiply 2 [1,2,3])
