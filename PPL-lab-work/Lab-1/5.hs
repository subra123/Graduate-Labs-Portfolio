main :: IO()
main =do

print("enter your name")
name <- getLine
print("welcome! " ++ name)
