# Word wrap kata

A (tested) solution to the word wrap kata [described here](https://codingdojo.org/kata/WordWrap/) (a copy of the problem description is below).

## Problem 
You write a class called Wrapper, that has a single static function named wrap that takes two arguments, a string, and a column number. The function returns the string, but with line breaks inserted at just the right places to make sure that no line is longer than the column number. You try to break lines at word boundaries.

Like a word processor, break the line by replacing the last space in a line with a newline.

### Additional point
In implementing the above, I've assumed that although words should be broken at word boundaries (spaces), words that are longer than the column number will need to be split across multiple lines.

## Technologies used
* Python3 (version 3.8.6), including unittest

## Wrapper
The Wrapper class is found in the file `word_wrap/__init__.py`

## Tests
Tests are found in the file `test.py`. 
Run tests locally with `python test.py`.
All tests should pass.