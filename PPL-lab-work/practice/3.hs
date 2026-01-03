palin :: String -> String
palin []=[]
palin (x:xs) = palin xs ++ [x]

check :: String -> Bool
check x = if x==palin x then True else False 

main::IO()
main=do
print(palin "subramanian")
print(check "amma")
