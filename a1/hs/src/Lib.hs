module Lib
    ( p1, p2
    ) where

import Data.List (sort)

p1 :: [[Int]] -> Int
p1 l = foldl max 0 (map sum l)

p2 :: [[Int]] -> Int
p2 l = foldl (+) 0 (three (foldl (flip (:)) [] (sort (map sum l))))

three :: [Int] -> [Int]
three (a:b:c:_) = [a,b,c]
