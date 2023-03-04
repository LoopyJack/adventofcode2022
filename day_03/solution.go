package main

import (
	"fmt"
	"os"
	"strings"
	"unicode"
)

func main() {

	file, err := os.ReadFile("input.txt")
	if err != nil {
		fmt.Println(err)
	}	
	data := strings.Split(string(file), "\n")

	// Part 1
	commons := ""
	for _, line := range data {
		r1 := to_set(line[:len(line)/2])
		r2 := to_set(line[len(line)/2:])
		common := intersection(r1, r2)
		commons += to_string(common)
		
	}
	score := calc_score(commons)
	fmt.Printf("Part 1 answer: %d\n", score)
	
	// Part 2
	badges := ""
	for i := 0; i < len(data)-2; i += 3 {
		l1, l2, l3 := to_set(data[i]), to_set(data[i+1]), to_set(data[i+2])
		common := intersection(l1, l2)
		common = intersection(common, l3)
		badges += to_string(common)
	}
	score2 := calc_score(badges)
	fmt.Printf("Part 2 answer: %d\n", score2)

}

func calc_score(line string) int {
	score := 0
	for _, char := range line {
		if unicode.IsUpper(char) {
			score += int(char) - 38
		} else if unicode.IsLower(char) {
			score += int(char) - 96
		}
	}
	return score
}

func to_set(line string) map[rune]struct{} {
	set := make(map[rune]struct{})
	for _, char := range line {
		set[char] = struct{}{}
	}
	return set
}

func to_string(set map[rune]struct{}) string {
	line := ""
	for r := range set {
		line += string(r)
	}
	return line
}

func intersection(s1, s2 map[rune]struct{}) map[rune]struct{} {
	common := make(map[rune]struct{})
	for item1 := range s1 {
		for item2 := range s2 {
			if item1 == item2 {
				common[item1] = struct{}{}
			}
		}
	}
	return common 
}
