hea :: [a] -> Maybe a
hea []    = Nothing
hea (x:_) = Just x

main :: IO ()
main = do
    case hea ([] :: [Int]) of
        Nothing -> return ()
        Just x  -> print x

    case hea [1, 2, 3] of
        Nothing -> return ()
        Just x  -> print x

