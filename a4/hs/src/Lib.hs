module Lib
    ( p1, p2
    ) where

contains :: (Int, Int) -> (Int, Int) -> Bool
contains (a,b) (c,d) = a <= c && b >= d

overlap :: (Int, Int) -> (Int, Int) -> Bool
overlap (a,b) (c,d) = contains (a,b) (c,d) || (a <= d && b >= d)

p1 :: [((Int, Int), (Int, Int))] -> Int
p1 x = length $ filter (\(y,z) -> contains y z || contains z y) x

p2 :: [((Int, Int), (Int, Int))] -> Int
p2 x = length $ filter (\(y,z) -> overlap y z || overlap z y) x
