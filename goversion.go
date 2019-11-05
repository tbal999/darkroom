//WORK IN PROGRESS
package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
)

//This is the player character
type Player struct {
	name   string
	health int
	attack int
}

//These are the monsters in the game
type Monster struct {
	name   []string
	health []int
	attack []int
}

func initialiseMap(ysize, xsize int, i *[][]int, i2 *[]int) {
	fmt.Println("initialiseMap-" + strconv.Itoa(xsize) + strconv.Itoa(ysize))
	a := *i2
	b := 0
	c := 0
	d := *i
	a = []int{0}
	e := make([]int, len(a))
	copy(e, a)
	for b = 0; b < xsize; b++ {
		e = append(e, 0)
	}
	*i2 = a
	d = [][]int{}
	*i = d
	for c = 0; c < ysize; c++ {
		initialiseMap2(ysize, xsize, i, &e)
	}
	f := *i
	f[0][0] = 1
	*i = f
}

func initialiseMap2(ysize, xsize int, i *[][]int, i2 *[]int) {
	fmt.Println("initialiseMap2-" + strconv.Itoa(xsize) + strconv.Itoa(ysize))
	a := *i
	b := *i2
	a = append(a, b)
	*i = a
	*i2 = b
}

func printMap(i [][]int) {
	for yindex := range i {
		fmt.Println(i[yindex])
	}
}

func find(m [][]int) (i, j int) {
	for i = range m {
		for j = range m[i] {
			if m[i][j] == 1 {
				return i, j
			}
		}
	}
	return i, j
}

func Move(cmd string, m [][]int) {
	//if len(m) <= 1 {
	//	return
	//}
	i, j := find(m)

	fmt.Println(i, j)
	if i >= len(m) || j >= len(m[0]) {
		return
	}
	switch cmd {
	case "w":
		if i <= 0 {
			return
		}
		m[i][j], m[i-1][j] = m[i-1][j], m[i][j]
	case "s":
		if i == len(m)-1 {
			return
		}
		m[i][j], m[i+1][j] = m[i+1][j], m[i][j]
	case "a":
		if j <= 0 {
			return
		}
		m[i][j], m[i][j-1] = m[i][j-1], m[i][j]
	case "d":
		if j == len(m)-1 {
			return
		}
		m[i][j], m[i][j+1] = m[i][j+1], m[i][j]
	default:
		return
	}
}

func seedMap(realmap *[][]int, gamemap [][]int, cmd string) {
	a := *realmap
	a = [][]int{}
	*realmap = a
	for range gamemap {
		seedMap2(realmap, gamemap, cmd)
	}
}

func seedMap2(realmap *[][]int, gamemap [][]int, cmd string) {
	a := *realmap
	nest := []int{}
	for range gamemap {
		switch cmd {
		case "real":
			nest = append(nest, rand.Intn(11))
		case "zeros":
			nest = append(nest, 0)
		}
	}
	a = append(a, nest)
	switch cmd {
	case "zeros":
		a[0][0] = 1
	}
	*realmap = a
}

func main() {
	//you := Player{}
	enemy := Monster{}
	enemy.name = append(enemy.name, "toad", "goblin", "shadowknight", "rogue", "demon")
	enemy.health = append(enemy.health, 10, 15, 20, 25, 30)
	enemy.attack = append(enemy.attack, 1, 2, 4, 6, 8)
	zeronest := []int{}
	zeromap := [][]int{}
	realmap := [][]int{}
	Scanner := bufio.NewScanner(os.Stdin)
	fmt.Println("DUNGEON GAME - IN GO")
	fmt.Println("You are the number 1 on the map. Press w, s, a, d to move around.")
	fmt.Println("Every time you kill a monster, you gain 1 point.")
	fmt.Println("Every time you complete a dungeon, you gain 2 points.")
	fmt.Println("First, type in your name...")
	//Scanner.Scan()
	//you.name = Scanner.Text()
	//you.attack = 2
	//you.health = 100
	//fmt.Println("Good luck " + you.name + "!")
	//fmt.Println("You have " + strconv.Itoa(you.attack) + " attack and " + strconv.Itoa(you.health) + " health.")
	endgame := 0
	difficulty := 0
	//score := 0
	for endgame == 0 {
		fmt.Println(difficulty)
		difficulty = difficulty + 1
		if difficulty > 4 {
			difficulty = 4
		}
		initialiseMap((rand.Intn(difficulty) + 1), (rand.Intn(difficulty) + 1), &zeromap, &zeronest)
		seedMap(&realmap, zeromap, "real")
		seedMap(&zeromap, zeromap, "zeros")
		printMap(realmap)
		printMap(zeromap)
		fmt.Println("Type here: ")
		Scanner.Scan()
		result := Scanner.Text()
		switch result {
		case "w":
			Move(result, zeromap)
		case "s":
			Move(result, zeromap)
		case "a":
			Move(result, zeromap)
		case "d":
			Move(result, zeromap)
		case "q":
			endgame = 1

		}
	}
}
