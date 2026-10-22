# Exact Transmitter Placement on a Circular Road

This repository contains the report and implementation of our project in Design and Analysis of Algorithms course in Indian Statistical Institute.

A circular road of length `c` is surrounded by a military complex. There are `n` check posts on the road and `m` candidate sites where a transmitter may be built. Every check post must have **exactly one** transmitter within `250` metres (measured along the shorter arc of the circle), because two transmitters in range would cause interference. The program prints a minimum-size valid set of transmitter sites, or reports that no such placement exists.

The radius `R = 250` is fixed in `main.py`.

## Running the program

The program reads the input from standard input, so a prepared input file can be piped in:

```
git clone https://github.com/Sai-Prabhav/daa_project.git
cd daa_project
python main.py < sample.txt
```

`sample.txt` contains a sample example.

## Input format

The input consists of exactly **three lines**, read in this order:

| Line | Contents                                                        | Notes                                |
| ---- | --------------------------------------------------------------- | ------------------------------------ |
| 1    | `n` integers — the positions of the check posts                 | one line, separated by single spaces |
| 2    | `m` integers — the positions of the candidate transmitter sites | one line, separated by single spaces |
| 3    | `c` — the circumference of the road                             | a single integer                     |
