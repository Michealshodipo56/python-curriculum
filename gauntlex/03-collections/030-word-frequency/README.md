# wordfrequency

## Description
Read one line of space-separated words. Print each word and its count in first-appearance order, one per line.

## Requirements
Each output line uses `WORD: COUNT`. Matching is case-sensitive.

## Examples
Input: "cat dog cat\n" → output: "cat: 2\ndog: 1\n"

Input: "a a b a\n" → output: "a: 3\nb: 1\n"

## Tips
A dictionary can map a word to how often it has appeared; insertion order is retained in modern Python.
