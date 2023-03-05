package main

import (
	"fmt"
	"os"
	"strings"
)

type Assignment struct {
	start int
	end   int
}

func main() {

	file, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println(err)
	}
	lines := strings.Split(string(file), "\n")

	cnt_contained := 0
	cnt_overlapped := 0
	for _, line := range lines {
		var a1, a2 Assignment
		fmt.Sscanf(line, "%d-%d,%d-%d", &a1.start, &a1.end, &a2.start, &a2.end)
		if contained(a1, a2) {
			cnt_contained++
		}
		if overlapped(a1, a2) {
			cnt_overlapped++
		}
	}
	fmt.Printf("Part 1 answer: %d\n", cnt_contained)
	fmt.Printf("Part 2 answer: %d\n", cnt_overlapped)
}


func contained(a, b Assignment) bool {
	return (a.start >= b.start && a.end <= b.end) || (b.start >= a.start && b.end <= a.end)
}

func overlapped(a, b Assignment) bool {
	return (a.end >= b.start && a.start <= b.end) || (b.end >= a.start && b.start <= a.end)
}