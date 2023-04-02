package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
	"time"
)


type Monkey struct {
	num int
	items []int
	op_value int
	op_only_input bool
	op string
	test_div int
	test_if_true int
	test_if_false int
	inspection_count int
}

func NewMonkey(raw string) *Monkey {

	m := Monkey{}
	data := strings.Split(raw, "\n")
	
	m.num, _ = strconv.Atoi(data[0][len(data[0])-2:len(data[0])-1])

	items := strings.Split(data[1][18:], ", ")
	m.items = make([]int, len(items))
	for i, item := range items {
		m.items[i], _ = strconv.Atoi(item)
	}
	operations := strings.Fields(data[2])
	m.op = operations[len(operations)-2]
	if operations[len(operations)-1] == "old" {
		m.op_only_input = true
	} else {
		m.op_value, _ = strconv.Atoi(operations[len(operations)-1])
	}
	test_div := strings.Fields(data[3])
	m.test_div, _ = strconv.Atoi(test_div[len(test_div)-1])
	m.test_if_true, _ = strconv.Atoi(data[4][len(data[4])-1:len(data[4])])
	m.test_if_false, _ = strconv.Atoi(data[5][len(data[5])-1:len(data[5])])
	m.inspection_count = 0
	return &m
} 

func (m *Monkey) Operate(num int) int {
	op_left := num
	op_right := num
	if !m.op_only_input {
		op_right = m.op_value
	}
	res := 0
	switch m.op {
		case "+":
			res = op_left + op_right
		case "-":
			res = op_left - op_right
		case "*":
			res = op_left * op_right
		case "/":
			res = op_left / op_right
		default:
			panic("Unknown operation")
	}
	m.inspection_count += 1
	return res
}

func (m *Monkey) Determine_receiving_monkey(value int) int {
	if value % m.test_div == 0 {
		return m.test_if_true
	} else {
		return m.test_if_false
	}
}

func (m *Monkey) AddItem(num int) {
	m.items = append(m.items, num)
}

func (m *Monkey) ClearItems() {
	m.items = []int{}
}

func (m *Monkey) String() string {
	return fmt.Sprintf("Monkey %d: %v, %d", m.num, m.items, m.inspection_count)
}

func (m *Monkey) ProcessItems(monkies []*Monkey, modulus int, worry_level int) {
	for item_idx, item := range m.items {
		value_to_throw := m.Operate(item) % modulus
		m.items[item_idx] = value_to_throw
		monkey_to_receive := m.Determine_receiving_monkey(value_to_throw / worry_level)
		monkies[monkey_to_receive].AddItem(value_to_throw / worry_level)
	}
	m.ClearItems()
}

func Initialize_monkeys(raw_text string) []*Monkey {
	monkies := []*Monkey{}
	data := strings.Split(raw_text, "\n\n")
	for _, monkey := range data {
		m := NewMonkey(monkey)
		monkies = append(monkies, m)
	}
	return monkies
}

func Run_rounds(monkies []*Monkey, num_rounds int, worry_level int) int {
	modulus := worry_level
	for _, monkey := range monkies {
		modulus *= monkey.test_div
	}
	for round := 0; round < num_rounds; round++ {
		for _, monkey := range monkies {
			monkey.ProcessItems(monkies, modulus, worry_level)
		}
	}
	// find 2 largest monkey inspection counts
	sorted_monkies := make([]*Monkey, len(monkies))
	for _, monkey := range monkies {
		sorted_monkies[monkey.num] = monkey
	}
	sort.Slice(sorted_monkies, func(i, j int) bool {
		return sorted_monkies[i].inspection_count > sorted_monkies[j].inspection_count
	})
	return sorted_monkies[0].inspection_count * sorted_monkies[1].inspection_count
}

func main() {
	start_time := time.Now()
	raw, err := os.ReadFile("input.txt"); if err != nil { panic(err) }
	ans1 := Run_rounds(Initialize_monkeys(string(raw)), 20, 3)
	fmt.Println("Part 1 answer: ", ans1)
	ans2 := Run_rounds(Initialize_monkeys(string(raw)), 10000, 1)
	fmt.Println("Part 2 answer: ", ans2)
	elapsed := time.Since(start_time)
	fmt.Println("Time: ", elapsed)
}















