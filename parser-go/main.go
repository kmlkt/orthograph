package main

import (
	"fmt"
	"os"
	"runtime"
)

func main() {
	b, err := os.ReadFile("../sources/vim12.txt")
	fmt.Println(err)
	var m1 runtime.MemStats
	var m2 runtime.MemStats
	var m3 runtime.MemStats
	s := string(b)
	runtime.ReadMemStats(&m1)
	sentences := split(s, '.', '-', '\n')
	koras := buildKoras(product([]string{"Н", "н"}, []string{"е", "и"}, []string{" ", "с"}))
	runtime.ReadMemStats(&m2)
	fmt.Println(m2.Alloc - m1.Alloc)
	for sent := range sentences {
		for _, p := range koras.Find(sent) {
			fmt.Println(sent[p.Start:p.End])
		}
	}
	runtime.ReadMemStats(&m3)
	fmt.Println(m3.Alloc - m2.Alloc)
}
