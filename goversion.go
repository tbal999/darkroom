package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strconv"
)

func generateNest(x, cmd int) []int {
	xindex := 0
	nest := make([]int, 0)
	for xindex = 0; xindex < x; xindex++ {
		nest = append(nest, 0)
	}
	switch cmd {
	case 1:
		for xindex = 0; xindex < x; xindex++ {
			nest[randomNumber(0, x)] = randomNumber(0, 11)
		}
	}
	return nest
}

func generateSlice(x, y, cmd int) [][]int {
	yindex := 0
	slice := make([][]int, 0, 0)
	for yindex = 0; yindex < y; yindex++ {
		slice = append(slice, generateNest(x, cmd))
	}
	switch cmd {
	case 0:
		slice[0][0] = 2
	}
	return slice
}

func printSlice(x [][]int) {
	for i := range x {
		fmt.Println(x[i])
	}
}

func randomNumber(min, max int) int {
	z := rand.Intn(max)
	if z < min {
		z = min
	}
	return z
}

func resetSlice(a int, b int, zeros, ones *[][]int) {
	i := *zeros
	j := *ones
	i = generateSlice(a, b, 0)
	j = generateSlice(a, b, 1)
	*zeros = i
	*ones = j
}

func Move(c *[][]int, s string) { //Moves the number 2 in the slice around, up,down,left,right
	i := *c
	switch s {
	case "w":
		// MOVE UP
		fmt.Println("Moving Up")
		for a := range i {
			if a == 0 {
				for b := range i[a] {
					if i[a+1][b] == 2 {
						i[a+1][b] = 0
						i[a][b] = 2
						*c = i
						return
					}
					if i[a][b] == 2 {
						i[a][b] = 0
						i[len(i)-1][b] = 2
						*c = i
						return
					}
				}
			}
			if a != 0 {
				for b := range i[a] {
					if i[a][b] == 2 {
						i[a-1][b] = 2
						i[a][b] = 0
						*c = i
						return
					}
				}
			}

		} // END MOVE UP
	case "s":
		// MOVE DOWN
		fmt.Println("Moving Down")
		for a := range i {
			if a != len(i)-1 {
				for b := range i[a] {
					if i[a][b] == 2 {
						i[a][b] = 0
						i[a+1][b] = 2
						*c = i
						return
					}
				}
			}
			if a == len(i)-1 {
				for b := range i[a] {
					if i[a][b] == 2 {
						i[a][b] = 0
						i[0][b] = 2
						*c = i
						return
					}
				}
			}

		} // END MOVE DOWN
	case "a":
		// MOVE LEFT
		fmt.Println("Moving Left")
		for a := range i {
			for b := range i[a] {
				if b == 0 {
					if i[a][b] == 2 {
						i[a][b] = 0
						i[a][len(i[b])-1] = 2
						*c = i
						return
					}
				}
				if b != 0 {
					if i[a][b] == 2 {
						i[a][b] = 0
						i[a][b-1] = 2
						*c = i
						return
					}
				}
			}
		} //END MOVE LEFT
	case "d":
		// MOVE RIGHT
		fmt.Println("Moving Right")
		for a := range i {
			for b := range i[a] {
				if b == len(i[0])-1 {
					if i[a][b] == 2 {
						i[a][b] = 0
						i[a][0] = 2
						*c = i
						return
					}
				}
				if b != len(i[0])-1 {
					if i[a][b] == 2 {
						i[a][b] = 0
						i[a][b+1] = 2
						*c = i
						return
					}
				}
			}
		} //END MOVE RIGHT
	} //END CASES
	return
} // END FUNCTION

func main() {
	gameover := 0
	difficulty := 0
	zeroslice := generateSlice(2, 2, 0)
	gameslice := generateSlice(2, 2, 1)
	for gameover != 1 {
		difficulty = difficulty + 1
		mapx, mapy := randomNumber(2, 5), randomNumber(2, 5)
		fmt.Println("Difficulty:" + strconv.Itoa(difficulty))
		printSlice(zeroslice)
		fmt.Println("")
		printSlice(gameslice)
		Scanner := bufio.NewScanner(os.Stdin)
		fmt.Println("Type here:")
		Scanner.Scan()
		result := Scanner.Text()
		switch result {
		case "q":
			gameover = 1
		case "n":
			resetSlice(mapx, mapy, &zeroslice, &gameslice)
		case "w":
			Move(&zeroslice, "w")
		case "s":
			Move(&zeroslice, "s")
		case "a":
			Move(&zeroslice, "a")
		case "d":
			Move(&zeroslice, "d")
		}
	}
}
