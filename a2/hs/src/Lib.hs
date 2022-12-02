module Lib
    ( p1, p2
    ) where

p1 :: [(Int, Int)] -> Int
p1 x = sum $ map (\(you, me) -> me + 1 + ((2 - (mod ((you - me) + 4) 3)) * 3)) x

p2 :: [(Int, Int)] -> Int
p2 x = sum $ map (\(you, me) -> (mod ((you + 3) + (me - 1)) 3) + 1 + (me * 3)) x
