module Lib
    ( p1, p2
    ) where

import Data.Char (ord)
import Data.List (intersect)

calc_priority :: Char -> Int
calc_priority a
    | a `elem` ['a'..'z'] = ord a - ord 'a' + 1
    | a `elem` ['A'..'Z'] = ord a - ord 'A' + 27

p1 :: [String] -> Int
p1 x = sum $ map (\a -> calc_priority $ head ((uncurry intersect) $ splitAt (length a `div` 2) a)) x

p2 :: [String] -> Int
p2 x = p2' 0 x
    where
        p2' s (a:b:c:x) = p2' (s + (calc_priority $ head (intersect (intersect a b) c))) x
        p2' s [] = s
