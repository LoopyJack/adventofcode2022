package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

func incr_cycle1(x, cycle int, result string) (int, string) {
	i_result, err := strconv.Atoi(result); if err != nil { panic(err) }
	cycle += 1
	if cycle == 20 || (cycle-20) % 40 == 0 {
		i_result += cycle*x
	}
	return cycle, strconv.Itoa(i_result)
}

func incr_cycle2(x, cycle int, result string) (int, string) {
	if cycle % 40 == 0 { result += "\n"	}
	eol := cycle - (cycle/40)*40 
	if eol == x-1 || eol == x || eol == x+1 { 
		result += "#" 
	} else {
		result += "."
	}
	cycle += 1
	return cycle, result
}

func run_cycles(fname string, incrementer func(int, int, string) (int, string), result string) string {
	x, cycle := 1, 0
	file, err := os.ReadFile(fname); if err != nil { panic(err) }
	data := strings.Split(string(file), "\n")

	for _, line := range data {
		tokens := strings.Fields(line)
		cmd := tokens[0]
		if cmd == "addx" {
			val, err := strconv.Atoi(tokens[1]); if err != nil { panic(err) }
			cycle, result = incrementer(x, cycle, result)
			cycle, result = incrementer(x, cycle, result)
			x += val
		} else if cmd == "noop" {
			cycle, result = incrementer(x, cycle, result)
		}
	}
	return result
}

func main() {
	start_time := time.Now()

	fname := "input.txt"
	ans1 := run_cycles(fname, incr_cycle1, "0")
	ans2 := run_cycles(fname, incr_cycle2, "")

	fmt.Printf("Part 1 answer: %s\n", ans1)
	fmt.Printf("Part 2 answer: %s\n", ans2)


	elapsed := time.Since(start_time)
	fmt.Printf("Time: %s\n", elapsed)
}