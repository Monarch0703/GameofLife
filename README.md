# Conway's Game of Life 🧬

A terminal-based implementation of Conway's Game of Life written in Python — built step by step as a learning project.

---

## What is it?

Conway's Game of Life is a **cellular automaton** invented by mathematician John Conway in 1970. It runs on a 2D grid of cells, each either **alive** (`#`) or **dead** (`.`). You set an initial state, and the simulation evolves on its own — no player input required. It's a *zero-player game*.

Simple rules produce remarkably complex, emergent behaviour.

---

## The Rules

Every cell examines its 8 neighbours (horizontal, vertical, and diagonal) each generation:

| Current State | Live Neighbours | Next State | Reason         |
|---------------|-----------------|------------|----------------|
| Alive         | < 2             | Dies       | Underpopulation |
| Alive         | 2 or 3          | Survives   | Stable          |
| Alive         | > 3             | Dies       | Overpopulation  |
| Dead          | exactly 3       | Born       | Reproduction    |

---

## Features

- Randomly seeded grid with configurable density
- Terminal animation using screen-clearing
- Finite grid (out-of-bounds cells treated as dead)
- Configurable grid size and number of generations
- Clean, readable code written function by function

---

## How to Run

**Requirements:** Python 3.x (no external libraries needed)

```bash
python conway_gof.py
```

The simulation runs for 50 generations by default, with a 0.2s delay between frames.

---

## Code Structure

```
game_of_life.py
│
├── make_grid(rows, cols)
│     Returns a 2D list of zeros (all dead cells)
│
├── print_grid(grid)
│     Prints the grid using '#' for alive, '.' for dead
│
├── count_neighbours(grid, row, col)
│     Returns the number of live neighbours around a cell
│
├── next_generation(grid)
│     Applies the 4 rules and returns the new grid
│
└── random_seed(grid, prob=0.3)
      Sets each cell alive with the given probability
```

---

## Design Decisions

- **Finite grid** — cells outside the boundary are treated as dead (simplest approach)
- **New grid per generation** — the next state is always computed from the current state; the grid is never mutated mid-computation
- **`random.random() < prob`** — the standard idiom for probabilistic cell seeding

---
