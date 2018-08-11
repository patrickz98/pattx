package main

import (
	"math/rand"
	"time"
	"strings"
	"fmt"
)

const maxLength = 8
const words = 300
const contains = "qu"

func genWord(vocals []string, consonances []string, s []string) string {
	s1 := rand.NewSource(time.Now().UnixNano())
	r1 := rand.New(s1)
	nbr := r1.Intn(maxLength) + 1

	startVowel := r1.Intn(2)
	endConsonant := r1.Intn(2)

	var word = ""

	for inx := 0; inx <= nbr; inx++ {
		word += s[ r1.Int() % len(s) ]
	}

	if startVowel == 1 {
		word = consonances[ r1.Int() % len(consonances) ] + word
	}

	if endConsonant == 1 {
		word += vocals[ r1.Int() % len(vocals) ]
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

		// fmt.Println(word)
		// count++

		// if word[ 0 ] == 'x' {
		// 	fmt.Println(word)
		// 	count++
		// }

		if strings.HasPrefix(word, contains) && strings.Contains(word, "z"){
			fmt.Println(word)
			count++
		}

		// if strings.Contains(word, contains) {
		// 	fmt.Println(word)
		// 	count++
		// }

		if count >= words {
			break
		}
	}
}
