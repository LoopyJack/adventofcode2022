package main

import (
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {

	
	file2, err := os.ReadFile("data.txt")
	if err != nil {
		log.Fatal(err)
	}

	d2 := string(file2)
	s := strings.Split(d2, "\n\n")

	int_groups := [][]int{}
	
	for _, str_array := range s {
		group := strings.Split(str_array, "\n")
		int_group := []int{}
		for _, v := range group {
			res, err := strconv.Atoi(v)
			if err != nil {
				log.Fatal(err)
			}
			int_group = append(int_group, res)
		}
		int_groups = append(int_groups, int_group)
	}
	
	group_sums := []int{}
	for _, group := range int_groups {
		sum := 0
		for _, v := range group {
			sum += v
		}
		group_sums = append(group_sums, sum)
	}
	sort.Slice(group_sums, func(i, j int) bool {
		return group_sums[i] > group_sums[j]
	})
	fmt.Printf("The highest sum is %d\n", group_sums[0])
	fmt.Printf("The first 3 sum is %d\n", group_sums[0]+group_sums[1]+group_sums[2])

		
}