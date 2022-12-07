module Main (main) where

import Lib

-- Input
import System.IO
import Data.Char (ord)

input :: IO [(Int, Int)]
input = do
    handle <- openFile "../input.txt" ReadMode
    contents <- hGetContents handle
    let list = f $ lines contents
    return list

f :: [String] -> [(Int, Int)]
f x = map (g . words) x

g :: [String] -> (Int, Int)
g [[a], [b]] = (ord a - ord 'A', ord b - ord 'X')

-- Main
main :: IO ()
main = do
    list <- input
    print $ p1 list
    print $ p2 list
