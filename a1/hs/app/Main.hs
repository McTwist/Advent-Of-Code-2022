module Main (main) where

import Lib

-- Input
import System.IO
import Data.List.Split (splitOn)

input :: IO [[Int]]
input = do
    handle <- openFile "../input.txt" ReadMode
    contents <- hGetContents handle
    let list = map f (map (splitOn "\n") (splitOn "\n\n" contents))
    return list

f :: [String] -> [Int]
f = map read

-- Main
main :: IO ()
main = do
    list <- input
    print $ p1 list
    print $ p2 list
