module Main (main) where

import Lib

-- Input
import System.IO

input :: IO [String]
input = do
    handle <- openFile "../input.txt" ReadMode
    contents <- hGetContents handle
    let list = lines contents
    return list

-- Main
main :: IO ()
main = do
    let list = []
    list <- input
    print $ p1 list
    print $ p2 list
