package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)

type Cell struct {
	x, y int
	height int
	vis_from_left bool 
	vis_from_right bool
	vis_from_top bool
	vis_from_bottom bool
	visible_area_score int
}

func NewCell(x, y, height int) *Cell {
	return &Cell{x, y, height, false, false, false, false, 0}
}

func (c *Cell) ViewToRight(grid [][]Cell) int {
	dist := 0
	for i := 1; i < len(grid[c.y])-c.x; i++ {
		dist = i
		if grid[c.y][c.x+i].height >= c.height {
			break
		}
	}
	return dist
}

func (c *Cell) ViewToLeft(grid [][]Cell) int {
	dist := 0
	for i := 1; i < c.x+1; i++ {
		dist = i
		if grid[c.y][c.x-i].height >= c.height {
			break
		}
	}
	return dist
}

func (c *Cell) ViewToTop(grid [][]Cell) int {
	dist := 0
	for i := 1; i < c.y+1; i++ {
		dist = i
		if grid[c.y-i][c.x].height >= c.height {
			break
		}
	}
	return dist
}

func (c *Cell) ViewToBottom(grid [][]Cell) int {
	dist := 0
	for i := 1; i < len(grid)-c.y; i++ {
		dist = i
		if grid[c.y+i][c.x].height >= c.height {
			break
		}
	}
	return dist
}

func (c *Cell) VisibleArea(grid [][]Cell) int {
	return c.ViewToRight(grid) * c.ViewToLeft(grid) * c.ViewToTop(grid) * c.ViewToBottom(grid)
}


func main() {
	start_time := time.Now()
	grid := [][]Cell{}

	file, err := os.ReadFile("input.txt"); if err != nil { panic(err) }
	lines := strings.Split(string(file), "\n")
	for y, line := range lines {
		row := []Cell{}
		for x, char := range line {
			height, err := strconv.Atoi(string(char)); if err != nil { panic(err) }
			newCell := NewCell(x, y, height)
			row = append(row, *newCell)
		}
		grid = append(grid, row)
	} 

	/* visible from left */
	for y, row := range grid {
		max_height := 0
		for x, cell := range row {
			if cell.height > max_height || x == 0 {
				grid[y][x].vis_from_left = true
				max_height = cell.height
			}
		}
	}
	
	/* visible from right */
	for _, row := range grid {
		max_height := 0
		for x := len(row)-1; x >= 0; x-- {
			if row[x].height > max_height || x == len(row)-1 {
				row[x].vis_from_right = true
				max_height = row[x].height
			}
		}
	}
	
	/* visible from top */
	for x := 0; x < len(grid[0]); x++ {
		max_height := 0
		for y := 0; y < len(grid); y++ {
			if grid[y][x].height > max_height || y == 0 {
				grid[y][x].vis_from_top = true
				max_height = grid[y][x].height
			}
		}
	}

	/* visible from bottom */
	for x := 0; x < len(grid[len(grid)-1]); x++ {
		max_height := 0
		for y := len(grid)-1; y >= 0; y-- {
			if grid[y][x].height > max_height || y == len(grid)-1 {
				grid[y][x].vis_from_bottom = true
				max_height = grid[y][x].height
			}
		}
	}

	/* count visible cells and find cell with max visibility */
	visible_cells := 0
	max_visible_area_score := 0
	for _, row := range grid {
		for _, cell := range row {
			cell.visible_area_score = cell.VisibleArea(grid)
			if cell.vis_from_left || cell.vis_from_right || cell.vis_from_top || cell.vis_from_bottom {
				visible_cells++
			}
			if cell.visible_area_score > max_visible_area_score {
				max_visible_area_score = cell.visible_area_score
			}
		}
	}
	fmt.Printf("Part 1 answer: %d\n", visible_cells)
	fmt.Printf("Part 2 answer: %d\n", max_visible_area_score)
	elapsed := time.Since(start_time)
	fmt.Printf("Time: %s\n", elapsed)
}