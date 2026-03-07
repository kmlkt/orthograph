package main

import (
	"iter"
)

func product[T any](groups ...[]T) iter.Seq[[]T] {
	N := len(groups)
	res := make([]T, N)
	total := 1
	for i := range N {
		total *= len(groups[i])
	}
	return func(yield func([]T) bool) {
		for x := range total {
			for i := range N {
				res[i] = groups[i][x%len(groups[i])]
				x /= len(groups[i])
			}

			if !yield(res) {
				return
			}
		}
	}
}
