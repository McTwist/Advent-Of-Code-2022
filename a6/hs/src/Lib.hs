module Lib
    ( p1, p2
    ) where

distinct :: Eq a => [a] -> Bool
distinct [] = True
distinct (s:xs) = not (s `elem` xs) && (distinct xs)

marker :: String -> Int -> Int
marker d u = marker' d u 0
    where
        marker' :: String -> Int -> Int -> Int
        marker' [] _ l = l
        marker' s i l
            | distinct $ take u s = i
            | otherwise = marker' (drop 1 s) (i+1) l

p1 :: String -> Int
p1 d = marker d 4

p2 :: String -> Int
p2 d = marker d 14
