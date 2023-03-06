package main

import (
	"fmt"
	"os"
	"time"
)

func main() {
	start_time := time.Now()
	file, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	data := []rune(string(file))
	fmt.Printf("Part 1 answer: %d\n", find_start_idx(4, data))
	fmt.Printf("Part 2 answer: %d\n", find_start_idx(14, data))
	elapsed := time.Since(start_time)
	fmt.Printf("Time: %s\n", elapsed)
}


func find_start_idx(start_length int, data []rune) int {
	for i := start_length-1; i < len(data); i++ {
		chars := make(map[rune]bool)
		for j := i; j >= i - start_length; j-- {
			_, ok := chars[data[j]] 
			if ok { 
				i = j + start_length-1 // skip ahead to look past first duplicate
				break 
			} 
			if j == i-start_length+1 {
				return i+1
			} 
			chars[data[j]] = true
		}
	}
	return -1
}