package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
	"unicode"
)

type stack[T any] struct {
    Push func(T)
    Pop func() T
    Length func() int
	Values func() []T
	Last func() T
}

func Stack[T any]() stack[T] {
    slice := make([]T, 0)
    return stack[T]{
        Push: func(i T) {
            slice = append(slice, i)
        },
        Pop: func() T {
            res := slice[len(slice)-1]
            slice = slice[:len(slice)-1]
            return res
        },
        Length: func() int {
            return len(slice)
        },
		Values: func() []T {
			return slice
		},
		Last: func() T {
			return slice[len(slice)-1]
		},
    }
}

func main() {
	start_time := time.Now()
	file, err  := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}
	data := strings.Split(string(file), "\n\n")
	
	moves := strings.Split(data[1], "\n")
	crane := Stack[rune]()
	
	// Part 1
	stacks := parse_stacks(data[0])
	for _, m := range  moves {
		var num_crates, from, to int
		fmt.Sscanf(m, "move %d from %d to %d", &num_crates, &from, &to)
		for i := 0; i < num_crates; i++ {
			move_crates(stacks, crane, 1, from-1, to-1)
		}
	}
	ans1 := ""
	for _, s := range stacks {
		ans1 += string(s.Last())
	} 
	fmt.Printf("Part 1 answer: %s\n", ans1)

	// Part 2
	stacks = parse_stacks(data[0])
	for _, m := range  moves {
		var num_crates, from, to int
		fmt.Sscanf(m, "move %d from %d to %d", &num_crates, &from, &to)
		move_crates(stacks, crane, num_crates, from-1, to-1)
	}
	ans2 := ""
	for _, s := range stacks {
		ans2 += string(s.Last())
	} 
	fmt.Printf("Part 2 answer: %s\n", ans2)
	elapsed := time.Since(start_time)
	fmt.Printf("Time: %s\n", elapsed)
}


func move_crates(stacks []stack[rune], crane stack[rune], num_crates int, from int, to int) {
	// crane := Stack[rune]()
	for i := 0; i < num_crates; i++ {
		crane.Push(stacks[from].Pop())
	}
	for i := 0; i < num_crates; i++ {
		stacks[to].Push(crane.Pop())
	}
}


func parse_stacks(raw string) []stack[rune] {
	data := strings.Split(raw, "\n")
	raw_stack := data[:len(data)-1]
	last_row := strings.Fields(data[len(data)-1])
	num_stacks, _ := strconv.Atoi(last_row[len(last_row)-1])
	stacks := make([]stack[rune], num_stacks)

	for i := range stacks {
		stacks[i] = Stack[rune]()
	}
	for i := len(raw_stack)-1; i >= 0; i-- {
		row := raw_stack[i]
		for j, r := range row {
			column := j / 4
			if unicode.IsLetter(r) {
				stacks[column].Push(r)
			}
		}
	}
	return stacks
}