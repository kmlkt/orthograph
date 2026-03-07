package main

import (
	"iter"
	"slices"
)

func split(s string, sep ...byte) iter.Seq[string] {
	N := len(s)
	return func(yield func(string) bool) {
		l := 0
		for r := range N {
			if slices.Contains(sep, s[r]) {
				if l != r {
					if !yield(s[l:r]) {
						return
					}
				}
				l = r + 1
			}
		}
		if l != N {
			if !yield(s[l:N]) {
				return
			}
		}
	}
}
