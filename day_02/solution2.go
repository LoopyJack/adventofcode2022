package main

import (
	"fmt"
	"log"
	"os"
	"strings"
)

var hands = [3]string{"r", "p", "s"}
var opponent_hands = [3]string{"A", "B", "C"}
var player_hands = [3]string{"X", "Y", "Z"}
var scores = [3]int{1, 2, 3}

type Game struct {
	opponent string
	player string
}

func main() {

	opponent := map[string]string{}
	player := map[string]string{}
	hand_score := make(map[string]int)
	var game_score = map[string]map[string]int{}
	
	for i, h := range hands {
		opponent[opponent_hands[i]] = h
		player[player_hands[i]] = h
		hand_score[h] = scores[i]
		game_score[h] = map[string]int{}
	}

	game_score["r"]["r"] = 3 + hand_score["r"]
	game_score["r"]["p"] = 6 + hand_score["p"]
	game_score["r"]["s"] = 0 + hand_score["s"]
	game_score["p"]["r"] = 0 + hand_score["r"]
	game_score["p"]["p"] = 3 + hand_score["p"]
	game_score["p"]["s"] = 6 + hand_score["s"]
	game_score["s"]["r"] = 6 + hand_score["r"]
	game_score["s"]["p"] = 0 + hand_score["p"]
	game_score["s"]["s"] = 3 + hand_score["s"]

	file, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	games := []Game{}
	total_score := 0
	total_score2 := 0
	
	for _, line := range strings.Split(string(file), "\n") {
		game := Game{line[0:1], line[2:3]}
		total_score += game_score[opponent[line[0:1]]][player[line[2:3]]]
		games = append(games, game)
	}
	fmt.Printf("Part 1 answer: %v\n", total_score)

	// Part 2
	for _, game := range games {
		if game.player == "X" { // lose
			if opponent[game.opponent] == "r" { total_score2 += game_score["r"]["s"] }
			if opponent[game.opponent] == "p" { total_score2 += game_score["p"]["r"] }
			if opponent[game.opponent] == "s" { total_score2 += game_score["s"]["p"] }
		} else if game.player == "Y" { // draw
			if opponent[game.opponent] == "r" { total_score2 += game_score["r"]["r"] }
			if opponent[game.opponent] == "p" { total_score2 += game_score["p"]["p"] }
			if opponent[game.opponent] == "s" { total_score2 += game_score["s"]["s"] }
		} else if game.player == "Z" { // win
			if opponent[game.opponent] == "r" { total_score2 += game_score["r"]["p"] }
			if opponent[game.opponent] == "p" { total_score2 += game_score["p"]["s"] }
			if opponent[game.opponent] == "s" { total_score2 += game_score["s"]["r"] }
		}
	}
	fmt.Printf("Part 2 answer: %v\n", total_score2)

}

