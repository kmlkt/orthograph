package main

import "iter"

type koras struct {
	to   map[byte]*koras
	walk map[byte]*koras
	p    *koras
	link *koras
	size int
	c    byte
	root bool
	term bool
}

func newKoras(c byte, p *koras) *koras {
	size := 0
	if p != nil {
		size = p.size + 1
	}
	return &koras{
		c:    c,
		p:    p,
		to:   map[byte]*koras{},
		walk: map[byte]*koras{},
		link: nil,
		root: p == nil,
		term: false,
		size: size,
	}
}

func buildKoras(strings iter.Seq[[]string]) *koras {
	root := newKoras('$', nil)
	for s := range strings {
		k := root
		for i, p := range s {
			k = k.Add(p, i == len(s)-1)
		}
	}
	return root
}

func (k *koras) Link() *koras {
	if k.link == nil {
		if k.root {
			k.link = k
		} else if k.p.root {
			k.link = k.p
		} else {
			k.link = k.p.Link().Walk(k.c)
		}
	}
	return k.link
}

func (k *koras) Walk(c byte) *koras {
	if _, exists := k.walk[c]; !exists {
		if _, exists := k.to[c]; exists {
			k.walk[c] = k.to[c]
		} else if k.root {
			k.walk[c] = k
		} else {
			k.walk[c] = k.Link().Walk(c)
		}
	}
	return k.walk[c]
}

func (k *koras) Add(s string, term bool) *koras {
	if len(s) == 0 {
		k.term = term
		return k
	}
	if _, exists := k.to[s[0]]; !exists {
		k.to[s[0]] = newKoras(s[0], k)
	}
	return k.to[s[0]].Add(s[1:], term)
}

type detection struct {
	Start   int
	End     int
	Pattern *koras
}

func (k *koras) find(s string, i int, yield func(detection)) {
	if k.term {
		yield(detection{i - k.size, i, k})
	}
	if i != len(s) {
		k.Walk(s[i]).find(s, i+1, yield)
	}
}

func (k *koras) Find(s string) []detection {
	accumulator := []detection{}
	k.find(s, 0, func(d detection) {
		accumulator = append(accumulator, d)
	})
	return accumulator
}

func (k *koras) Path() []byte {
	if k.p == nil {
		return []byte{}
	}
	return append(k.p.Path(), k.c)
}

func (k *koras) String() string {
	return string(k.Path())
}
