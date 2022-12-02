module Lib
    ( p1, p2
    ) where

calc_score :: Int -> Int -> Int
calc_score a b
    | a - b == 1 || a - b == -2 = 0
    | a - b == 0 = 3
    | a - b == -1 || a - b == 2 = 6

p1 :: [(Int, Int)] -> Int
p1 x = sum $ map (\(you, me) -> me + 1 + (calc_score you me)) x

p2 :: [(Int, Int)] -> Int
p2 x = sum $ map (\(you, me) -> (mod ((you + 3) + (me - 1)) 3) + 1 + (me * 3)) x
