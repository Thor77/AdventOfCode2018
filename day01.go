package main

import (
	"io/ioutil"
	"log"
	"strconv"
	"strings"
	"time"
)

func part1(lines []int) int {
	result := 0
	for _, line := range lines {
		result += line
	}
	return result
}

func part2(lines []int) int {
	frequencies := make(map[int]struct{})
	result := 0
	for {
		for _, line := range lines {
			result += line
			if _, ok := frequencies[result]; ok {
				return result
			}
			frequencies[result] = struct{}{}
		}
	}
}

func main() {
	content, err := ioutil.ReadFile("inputs/01")
	if err != nil {
		log.Fatal(err)
	}
	lines := strings.Split(string(content), "\n")
	linesInt := make([]int, 0)
	for _, line := range lines {
		i, err := strconv.Atoi(line)
		if err != nil {
			continue
		}
		linesInt = append(linesInt, i)
	}
	log.Println(part1(linesInt))
	var sum float64
	for i := 0; i < 100; i++ {
		start := time.Now()
		part2(linesInt)
		sum += time.Now().Sub(start).Seconds()
	}
	log.Printf("Mean over 100 runs: %fms\n", (sum/100)*1000)
}
