package main

import (
	"math/rand"
	"fmt"
	"strings"
)

const maxLength = 8
const words = 50

func genWord(vocals []string, consonances []string, s []string) string {
	// s1 := rand.NewSource(time.Now().UnixNano())
	// r1 := rand.New(s1)
	nbr := (rand.Int() % maxLength) + 1

	startVowel := rand.Int() % 2
	endConsonant := rand.Int() % 2

	var word = ""

	for inx := 0; inx <= nbr; inx++ {
		word += s[ rand.Int() % len(s) ]
	}

	if startVowel == 1 {
		word = consonances[ rand.Int() % len(consonances) ] + word
	}

	if endConsonant == 1 {
		word += vocals[ rand.Int() % len(vocals) ]
	}

	return word
}

func main() {
	vocals := []string{"b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"}
	consonances := []string{"a","e","i","o","u"}

	lenCons := len(consonances)
	s := make([]string, len(vocals) * lenCons)

	for inx, v := range vocals {
		for iny, c := range consonances {
			index := lenCons * inx + iny
			s[ index ] = v+c
		}
	}

	count := 0
	for {
		word := genWord(vocals, consonances, s)

		// if word[ 0 ] == 'x' {
		// 	fmt.Println(word)
		// 	count++
		// }

		if strings.Contains(word, "x") {
			fmt.Println(word)
			count++
		}

		if count >= words {
			break
		}
	}
}
