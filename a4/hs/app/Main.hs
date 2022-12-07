module Main (main) where

import Lib

-- Input
import System.IO
import Data.List.Split (splitOn)

input :: IO [((Int, Int), (Int, Int))]
input = do
    handle <- openFile "../input.txt" ReadMode
    contents <- hGetContents handle
    let list = map (\x -> tuplify $ map (\y -> tuplify $ map read (splitOn "-" y)) (splitOn "," x)) (lines contents)
    return list

tuplify :: [a] -> (a,a)
tuplify [x,y] = (x,y)

-- Main
main :: IO ()
main = do
    list <- input
    print $ p1 list
    print $ p2 list
