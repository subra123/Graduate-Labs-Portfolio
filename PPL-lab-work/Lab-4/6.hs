averagemarks :: (String,Int,[Int])->(String,Double)
averagemarks (name, _, marks) = 
    let total = sum marks
        no = length  marks
    in (name, if no==0 then 0 else fromIntegral total / fromIntegral no)

ans :: [(String,Int,[Int])] -> [(String,Double)]
ans = map averagemarks

main :: IO()
main = do
     let students=[("Alice", 101, [85, 90, 78]),("Bob", 102, [76, 88, 91]),("Charlie", 103, [92, 80, 85])]
     print(ans  students)


