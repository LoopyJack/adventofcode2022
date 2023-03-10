package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

type Segment struct {
	pos int
	x int
	y int
}

func abs(x int) int {
	if x > 0 { return x } else { return -x }
}

func NewSegment(pos int) *Segment {
	return &Segment{pos, 0, 0}
}

func Count_locations_visited(filename string, num_body_parts, max_apart int) int {
	file, err := os.ReadFile(filename); if err != nil { panic(err) }
	movements := strings.Split(string(file), "\n")
	
	segments := make([]Segment, num_body_parts)
	locations_visited := map[[2]int]struct{}{}

	for i := 0; i < num_body_parts; i++ {
		segments[i] = *NewSegment(i)

	}
	
	for _, movement := range movements {
		
		distance, err := strconv.Atoi(movement[2:]); if err != nil { panic(err) }

		for i := 0; i < distance; i++ {

			switch direction := string(movement[0]); direction {
				case "R":
					segments[0].x++
				case "L":
					segments[0].x--
				case "U":
					segments[0].y++
				case "D":
					segments[0].y--
				default:
					panic("Invalid direction")
			}

			for i := 1; i < len(segments); i++ {
				diff_x := segments[i-1].x - segments[i].x
				diff_y := segments[i-1].y - segments[i].y

				if abs(diff_x) > max_apart { 
					sign := 1; if diff_x <= 0 { sign = -1 }
					segments[i].x += max_apart * sign
					if diff_y != 0 {
						sign := 1; if diff_y <= 0 { sign = -1 }
						segments[i].y += max_apart * sign
					}
				} else if abs(diff_y) > max_apart {
					sign := 1; if diff_y <= 0 { sign = -1}
					segments[i].y += max_apart * sign
					if diff_x != 0 {
						sign := 1; if diff_x <= 0 { sign = -1 }
						segments[i].x += max_apart * sign
					}
				}
				
				if i == len(segments)-1 {
					locations_visited[[2]int{segments[i].x, segments[i].y}] = struct{}{}
				}
			}
		}
	}
	return len(locations_visited)
}

func main() {
	start_time := time.Now()
	filename := "input.txt"
	ans1 := Count_locations_visited(filename, 2, 1)
	ans2 := Count_locations_visited(filename, 10, 1)

	fmt.Printf("Part 1 answer: %d\n", ans1)
	fmt.Printf("Part 2 answer: %d\n", ans2)
	elapsed := time.Since(start_time)
	fmt.Printf("Time: %s\n", elapsed)
}