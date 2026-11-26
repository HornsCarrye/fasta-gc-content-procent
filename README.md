# fasta-gc-content

A small command-line Python tool that reads a FASTA file and reports the GC content (percentage of G and C nucleotides) of every sequence in it.

No external libraries are needed, only Python.

## Features

- Parses multi-sequence FASTA files (sequences may span many lines)
- Case-insensitive: `g`/`c` are counted the same as `G`/`C`
- Shows the sequences with the highest and the lowest GC content
- Shows GC content and length for every sequence

## Usage

```bash
python CG.py
```

An interactive menu opens:

```
--- MENU ---
1. Analyze DNA
2. Exit
Select an action: 1
Enter the FASTA file name: examples/example.fasta

Select analysis mode:
1. Show MAX and MIN GC
2. Show ALL GC values
Your choice: 2

--- ALL GC VALUES ---
gi|186704|Keratin: 54.43% (length 5339)
FASTA: 30.00% (length 10)
```

Mode 1 prints:

```
MAX GC: 54.43% (gi|186704|Keratin)
MIN GC: 30.00% (FASTA)
```

## How GC content is calculated

```
GC% = (G + C) / (A + T + G + C) * 100
```

## Example data

`examples/example.fasta` contains two sequences:

1. A human keratin DNA sequence (`gi|186704|`), taken from the FASTA format example on the DTU Health Tech site: https://services.healthtech.dtu.dk/examples/DNA.fasta.html. Expected GC: 54.43%.
2. A short sequence `ATTCGCTTAA` (3 G/C out of 10 nucleotides). Expected GC: 30.00%.

These two values can be used to check that the tool works correctly.

## Project structure

```
.
├── CG.py
├── examples/
│   └── example.fasta
├── LICENSE
└── README.md
```

## Possible improvements

- Sliding-window GC content along a sequence, with a plot (matplotlib)
- Command-line arguments (`argparse`) instead of the interactive menu
- Unit tests

## License

MIT, see `LICENSE`.
