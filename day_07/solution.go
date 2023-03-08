package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)


func main() {
	
	file, err := os.ReadFile("input.txt"); if err != nil { panic(err) }
	data := string(file)
	lines  := strings.Split(data, "\n")
	
	dir_stack := []string{}
	dir_sizes := map[string]int{}

	for _, line := range lines {
		if line == "$ ls" || strings.Contains(line, "dir") { continue}
		if strings.Contains(line, "$ cd") {
			cd_cmd := strings.Split(line, " ")
			dir := cd_cmd[len(cd_cmd)-1]
			if dir == "/" { 
				dir_stack = []string{"/"}
			} else if dir == ".." {
				dir_stack = dir_stack[:len(dir_stack)-1]
			} else {
				dir_stack = append(dir_stack, dir_stack[len(dir_stack)-1] + dir + "/")
			}
		} else {
			file_info := strings.Split(line, " ")
			size, err := strconv.Atoi(file_info[0]); if err != nil { panic(err) }
			for _, d := range dir_stack {
				dir_sizes[d] += size
			}
		}
	}
	
	ans1 := 0
	ans2 := math.MaxInt32
	size_to_delete := 30000000 - (70000000 - dir_sizes["/"])
	for _, size := range dir_sizes {
		if size < 100000 {
			ans1 += size
		}
		if size > size_to_delete && size < ans2 {
			ans2 = size
		}
	}
	
	fmt.Printf("Part 1 answer: %v\n", ans1)
	fmt.Printf("Part 2 answer: %v\n", ans2)

	

}