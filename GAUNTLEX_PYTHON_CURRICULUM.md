# Gauntlex Python Curriculum

> Single-file learner-facing curriculum assembled from rewritten exercise briefs.
> Order is provisional pending full prerequisite and source coverage review.
> No solutions or answer keys are included.

**Total exercises: 409**

---

## Foundations

*Source: gauntlex/01-foundations/001-hello/README.md*

### 001 — First Signal

## Description
Every program begins with an observable result. In this challenge, create a Python script that sends a welcome message to the terminal. The goal is to understand what happens when the interpreter runs a source file and how a program communicates through standard output.

## Requirements
- Use the provided `main.py` file.
- When the program runs, display the exact message `Hello, world!`.
- Display the message once, followed by a newline.
- Do not request input or display any other text.

## Tips
- Find out how to run a Python source file from a terminal.
- What does *standard output* mean, and where does its content appear?
- Pay attention to capitalization, punctuation, and spaces: a computer compares characters exactly.

## Example Output
```text
Hello, world!
```

*Source: gauntlex/01-foundations/002-displaynumber/README.md*

### 002 — The Answer

## Description
Programs can represent information as numbers as well as words. In this challenge, display a specific whole number and explore why the value a program works with is not necessarily the same thing as the characters a person sees on screen.

## Requirements
- Use the provided `main.py` file.
- Display the number `42` on one line.
- End the output with a newline.
- Do not add a label, prompt, or any additional text.

## Tips
- Investigate the difference between an integer and text made of digit characters.
- Can two different kinds of values produce identical terminal output?
- Check that the terminal shows only the required number.

## Example Output
```text
42
```

*Source: gauntlex/01-foundations/003-two-lines/README.md*

### 003 — Two Signals

## Description
A terminal program can communicate a sequence of messages, not just one. Build a script that displays two separate lines in the correct order. This challenge focuses on line boundaries and precise output formatting.

## Requirements
- Use the provided `main.py` file.
- Display `Python` on the first line.
- Display `Gauntlex` on the second line.
- End the second line with a newline.
- Do not add blank lines, labels, or other output.

## Tips
- How does the terminal know where one line ends and the next begins?
- Consider the difference between a space and a line break.
- Compare the displayed output character by character with the expected result.

## Example Output
```text
Python
Gauntlex
```

*Source: gauntlex/01-foundations/004-addition/README.md*

### 004 — Combine Values

## Description
A program can transform information instead of simply displaying it. Create a program that receives two whole numbers and produces their sum. This challenge introduces the distinction between text received from standard input and numeric values used in arithmetic.

## Requirements
- Read two integers from standard input, one per line.
- Display their arithmetic sum on one line, followed by a newline.
- Handle positive numbers, negative numbers, and zero.
- Do not display prompts, labels, or explanations.

## Tips
- Investigate the type of data received when a program reads a line of input.
- What happens when two text values are combined? How is that different from arithmetic addition?
- Think about how negative values affect the result.

## Example Input
```text
7
5
```

## Example Output
```text
12
```

*Source: gauntlex/01-foundations/005-greeting/README.md*

### 005 — A Personal Greeting

## Description
A useful program can respond to information it receives instead of producing the same message every time. Build a greeting that incorporates a person's name exactly as entered. The challenge introduces input-driven output and combining fixed text with changing information.

## Requirements
- Read one line containing a name from standard input.
- Display `Hello, NAME!`, replacing `NAME` with the name received.
- Preserve the input name's spelling, capitalization, and spaces.
- Display exactly one line followed by a newline, without a prompt or additional output.

## Tips
- Which part of the greeting stays the same for every person?
- Which part must come from the input rather than being written in advance?
- Check the punctuation and spacing around the name.

## Example Input
```text
Ada
```

## Example Output
```text
Hello, Ada!
```

*Source: gauntlex/01-foundations/006-name-card/README.md*

### 006 — Identity Card

## Description
Programs often collect several pieces of information and present them in a consistent format. Build a small identity card from a name and a city. This challenge practices reading inputs in sequence and matching each value to the correct output label.

## Requirements
- Read a name on the first input line and a city on the second.
- Display the name in the format `Name: VALUE`.
- Display the city in the format `City: VALUE`.
- Preserve the text supplied for both values.
- Print exactly two lines, each ending with a newline, and no prompts or extra output.

## Tips
- Consider how to keep the first and second inputs distinct.
- What would happen if the city and name were displayed in the wrong order?
- Compare the labels, capitalization, and spaces with the expected output.

## Example Input
```text
Ada
Lagos
```

## Example Output
```text
Name: Ada
City: Lagos
```

*Source: gauntlex/01-foundations/007-rectangle/README.md*

### 007 — Measure a Rectangle

## Description
A rectangle has an interior and a boundary, and each is measured differently. Build a calculator that uses its width and height to report both its area and its perimeter. This challenge develops arithmetic reasoning and precise formatting.

## Requirements
- Read a positive integer width, followed by a positive integer height, each on its own line.
- Display the area in the format `Area: N`.
- Display the perimeter in the format `Perimeter: N` on the next line.
- End each output line with a newline.
- Do not print prompts or other text.

## Tips
- Sketch a rectangle and identify what the two measurements represent.
- Consider how the width and height contribute to the interior versus the boundary.
- Verify your reasoning with a rectangle whose sides have different lengths.

## Example Input
```text
4
3
```

## Example Output
```text
Area: 12
Perimeter: 14
```

*Source: gauntlex/01-foundations/008-remainder/README.md*

### 008 — Share Into Groups

## Description
Suppose a collection of items must be divided into groups of equal size. Some items may remain after forming every possible complete group. Build a program that reports both the number of complete groups and the leftover items.

## Requirements
- Read a nonnegative integer item count on the first line.
- Read a positive integer group size on the second line.
- Display `Groups: N` for the number of complete groups.
- Display `Leftover: N` for the unused items on the next line.
- Print no prompts or additional messages.

## Tips
- Try distributing a small number of objects by hand.
- How can you tell whether another complete group can be formed?
- Consider the cases where the item count is zero or smaller than the group size.

## Example Input
```text
17
5
```

## Example Output
```text
Groups: 3
Leftover: 2
```

*Source: gauntlex/01-foundations/009-initials/README.md*

### 009 — Name Initials

## Description
Names can be represented in shorter forms while retaining identifying information. Read two names and transform their first letters into a compact set of initials. This challenge practices accessing characters in text and handling capitalization.

## Requirements
- Read a nonempty first name and a nonempty last name, each on its own line.
- Take the first character of each name and display it in uppercase.
- Follow each initial with a period, without spaces between the initials.
- Display exactly one line and no prompts or extra output.

## Tips
- Explore how to access an individual character within a string.
- Consider what happens when the supplied names use lowercase letters.
- Check that both initials appear in the same order as the input.

## Example Input
```text
ada
lovelace
```

## Example Output
```text
A.L.
```

*Source: gauntlex/01-foundations/010-shout/README.md*

### 010 — Clean Announcement

## Description
Messages received from users may contain unwanted whitespace at their boundaries and inconsistent capitalization. Prepare a message for announcement by normalizing its appearance without changing the spaces between its words.

## Requirements
- Read one line of text from standard input.
- Remove leading and trailing whitespace.
- Convert all remaining letters to uppercase.
- Preserve any whitespace that remains between characters.
- Display the resulting message on one line without prompts.

## Tips
- Investigate how leading and trailing whitespace differs from spaces inside a sentence.
- Think about the order in which text transformations can be applied.
- Consider what should be displayed when the input contains only whitespace.

## Example Input
```text
  hello Gauntlex  
```

## Example Output
```text
HELLO GAUNTLEX
```

*Source: gauntlex/01-foundations/011-next-year/README.md*

### 011 — One Year Later

## Description
Programs often combine descriptive information with calculations. Read a person's name and current age, then produce a sentence describing their age one year later. This challenge connects numeric input with formatted text.

## Requirements
- Read a name on the first line and a nonnegative integer age on the second.
- Calculate the person's age one year later.
- Display exactly `NAME will be AGE next year.` with the supplied name and calculated age.
- Print one line, with no prompts or additional messages.

## Tips
- Which input is used as text, and which is used in arithmetic?
- Think about when a value must change representation to be included in a sentence.
- Verify the exact spacing and punctuation in the final message.

## Example Input
```text
Mira
19
```

## Example Output
```text
Mira will be 20 next year.
```

*Source: gauntlex/01-foundations/012-even-or-odd/README.md*

### 012 — Even or Odd

## Description
An integer is even when it can be separated into pairs without a remainder; otherwise, it is odd. Build a program that classifies any integer, including zero and negative values. This challenge introduces decision-making based on a numeric property.

## Requirements
- Read one integer from standard input.
- Display `even` if it is even or `odd` if it is odd.
- Use lowercase letters exactly as shown.
- Display only the classification on one line, without a prompt.

## Tips
- What property distinguishes integers that can be split into pairs evenly?
- Check whether your reasoning still works for zero and negative values.
- Consider what information a conditional decision needs.

## Example Input
```text
-3
```

## Example Output
```text
odd
```

*Source: gauntlex/01-foundations/013-larger/README.md*

### 013 — Choose the Larger

## Description
When two numbers are supplied, a program can compare them and select one based on their relative values. Build a program that displays the greater integer. Equal values should produce that shared number rather than a special message.

## Requirements
- Read two integers, one per line.
- Display the greater of the two integers.
- If the values are equal, display that value once.
- Support positive values, negative values, and zero.
- Print exactly one line without prompts or additional text.

## Tips
- Consider the three possible relationships between two values: greater, smaller, and equal.
- Check cases involving two negative numbers.
- What should happen when neither value is greater than the other?

## Example Input
```text
-2
5
```

## Example Output
```text
5
```

---

## Control Flow

*Source: gauntlex/02-control-flow/014-grade/README.md*

### 014 — Score Boundaries

## Description
A grading system converts a numeric score into a letter category. Build a program that selects the correct grade for every valid score. This challenge focuses on ordered decisions and boundary values.

## Requirements
- Read one integer score between 0 and 100, inclusive.
- Assign `A` to 90–100, `B` to 80–89, `C` to 70–79, `D` to 60–69, and `F` to 0–59.
- Display the result exactly as `Grade: X`, where `X` is the letter.
- Print one line without prompts or additional output.

## Tips
- List the score ranges and make sure none overlap or leave gaps.
- Consider values immediately above and below each boundary.
- How can the program ensure that exactly one category is chosen?

## Example Input
```text
90
```

## Example Output
```text
Grade: A
```

*Source: gauntlex/02-control-flow/015-access/README.md*

### 015 — Permission Gate

## Description
Some decisions depend on more than one requirement. A supervised driving session is available only to participants who meet an age threshold and have the required license status. Build a program that evaluates both conditions together.

## Requirements
- Read an integer age on the first line.
- Read a lowercase license status, either `yes` or `no`, on the second line.
- Display `allowed` only when the age is at least 16 and the license status is `yes`.
- Display `denied` in every other case.
- Use lowercase output and do not print prompts or explanations.

## Tips
- Check each condition independently before considering the combined decision.
- What happens when only one requirement is met?
- Think about ages immediately below and at the threshold.

## Example Input
```text
16
yes
```

## Example Output
```text
allowed
```

*Source: gauntlex/02-control-flow/016-count/README.md*

### 016 — Count Forward

## Description
Repeating a task manually works for a few steps but not for an input-dependent sequence. Build a program that displays consecutive numbers starting at one and stopping at a supplied limit. This challenge introduces repetition with a defined boundary.

## Requirements
- Read a nonnegative integer `N`.
- Display each integer from 1 through `N`, in ascending order.
- Put each number on its own line.
- If `N` is zero, produce no output.
- Do not print prompts or other text.

## Tips
- Identify the first value, the last value, and how the sequence changes.
- Investigate whether the upper boundary of a repetition construct is included.
- Consider how the program behaves when there are no numbers to display.

## Example Input
```text
3
```

## Example Output
```text
1
2
3
```

*Source: gauntlex/02-control-flow/017-sum-range/README.md*

### 017 — Running Total

## Description
A running total changes as new values are considered. Build a program that adds the consecutive integers from one through a supplied limit. The number of values to include depends on the input.

## Requirements
- Read a nonnegative integer `N`.
- Display the sum of all integers from 1 through `N`, inclusive.
- If `N` is zero, display `0`.
- Display one integer on one line without prompts or additional text.

## Tips
- Work through a small example by hand and track how the total changes.
- What total should you begin with before adding any values?
- Consider how the stopping boundary affects which numbers are included.

## Example Input
```text
5
```

## Example Output
```text
15
```

*Source: gauntlex/02-control-flow/018-countdown/README.md*

### 018 — Launch Countdown

## Description
A countdown is a sequence that moves toward a stopping point. Build a program that counts backward from a supplied number and finishes with a launch message. This challenge develops control over decreasing sequences and their termination.

## Requirements
- Read a nonnegative integer `N`.
- Display the integers from `N` down to 1, one per line.
- After the numbers, display `Go!` on its own line.
- If `N` is zero, display only `Go!`.
- Do not print prompts or other text.

## Tips
- Determine how the current number changes after each step.
- What condition tells the program to stop counting?
- Check the zero case so the final message is still displayed.

## Example Input
```text
3
```

## Example Output
```text
3
2
1
Go!
```

*Source: gauntlex/02-control-flow/019-even-sum/README.md*

### 019 — Even Accumulator

## Description
A running total does not always include every value. Build a program that considers the integers in a range but adds only those that are even. This challenge combines repetition, selection, and accumulation.

## Requirements
- Read a nonnegative integer `N`.
- Add all even integers from 1 through `N`, inclusive.
- Display the total as one integer on one line.
- If `N` is zero or one, display `0`.
- Do not print prompts or other text.

## Tips
- Separate the decision to include a number from the action of adding it.
- Think about how to recognize even values.
- Check whether the upper limit itself should contribute to the total.

## Example Input
```text
6
```

## Example Output
```text
12
```

*Source: gauntlex/02-control-flow/020-multiplication-table/README.md*

### 020 — Times Table

## Description
A multiplication table follows the same pattern across several rows. Build a program that produces ten rows for an input number, keeping the calculation and text formatting consistent. This challenge practices repetition with changing values.

## Requirements
- Read one integer `N`.
- Display ten rows for multipliers 1 through 10, in ascending order.
- Format every row exactly as `N x I = RESULT`, with single spaces around `x` and `=`.
- Use the input number in every row, including when it is zero or negative.
- Do not display prompts or additional lines.

## Tips
- Identify which parts of each row remain constant and which change.
- How can the same calculation be repeated for each multiplier?
- Check the first and last rows and the spaces around the symbols.

## Example Input
```text
2
```

## Example Output
```text
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
```

*Source: gauntlex/02-control-flow/021-digit-count/README.md*

### 021 — Decimal Length

## Description
The number of digits in an integer depends on its size, not on whether it is positive or negative. Build a program that counts the decimal digits in an input value. This challenge encourages careful handling of zero and sign characters.

## Requirements
- Read one integer from standard input.
- Display the number of decimal digits in its absolute value.
- Count zero as a one-digit number.
- Do not count a leading minus sign as a digit.
- Display one integer on one line without prompts or extra output.

## Tips
- Compare the digit counts of 9, 10, 99, and 100.
- What should happen to the sign of a negative number?
- Consider why zero needs special attention.

## Example Input
```text
-1204
```

## Example Output
```text
4
```

*Source: gauntlex/02-control-flow/022-number-guess/README.md*

### 022 — Find the Secret

## Description
Some programs continue interacting with a user until a particular condition is met. Build a guessing process with a fixed secret number. After each guess, provide feedback and stop immediately when the secret is found. This challenge combines repeated input with conditional decisions.

## Requirements
- Read integer guesses from standard input, one per line.
- The secret number is `7`.
- Display `low` when a guess is below 7 and `high` when it is above 7.
- Display `correct` when the guess is 7, then stop reading input.
- Assume the input eventually contains 7.
- Display one feedback line per processed guess, with no prompts or additional text.

## Tips
- What action must repeat, and what event ends that repetition?
- Think about when feedback should be displayed relative to checking the guess.
- Guesses after the correct answer must not affect the output.

## Example Input
```text
3
9
7
```

## Example Output
```text
low
high
correct
```

---

## Collections

*Source: gauntlex/03-collections/023-list-length/README.md*

### 023 — Count the Collection

## Description
A single line can represent a collection of several numbers or an empty collection. Build a program that counts the values supplied, rather than counting the characters used to write them. This challenge introduces working with sequences.

## Requirements
- Read one line containing space-separated integers.
- Treat an empty line as an empty collection.
- Display the number of integers as one number on one line.
- Display `0` when the collection is empty.
- Do not print prompts or additional text.

## Tips
- How is a collection of values different from the text that represents it?
- Think about what separates one value from the next.
- Check the cases with zero, one, and several elements.

## Example Input
```text
1 2 3
```

## Example Output
```text
3
```

For an empty input line, the output is `0`.

*Source: gauntlex/03-collections/024-list-ends/README.md*

### 024 — At Both Ends

## Description
An ordered collection has a first element and a last element. Build a program that retrieves both boundaries while preserving the values exactly as supplied.

## Requirements
- Read one nonempty line of space-separated words.
- Display the first word on the first output line.
- Display the last word on the second output line.
- If the input contains only one word, display it on both lines.
- Do not print prompts or other text.

## Tips
- Explore how positions identify elements in a sequence.
- Can the last element be found without knowing the collection's length in advance?
- Consider the special case of a one-element collection.

## Example Input
```text
red blue green
```

## Example Output
```text
red
green
```

*Source: gauntlex/03-collections/025-list-total/README.md*

### 025 — Sum the Collection

## Description
A collection of numbers can be reduced to one result by combining its elements. Build a program that finds the arithmetic sum of a sequence of integers, including when the sequence is empty.

## Requirements
- Read one line of space-separated integers; the line may be empty.
- Calculate the arithmetic sum of all supplied integers.
- Display the total on one line.
- If the input line is empty, display `0`.
- Do not print prompts or extra text.

## Tips
- Input arrives as text, but addition works with numeric values.
- What total makes sense before any values have been considered?
- Check collections containing both positive and negative integers.

## Example Input
```text
-5 8 -3
```

## Example Output
```text
0
```

*Source: gauntlex/03-collections/026-list-maximum/README.md*

### 026 — Find the Peak

## Description
Find the greatest number in a collection without assuming the values are positive, different, or already ordered. This challenge develops comparison across a sequence.

## Requirements
- Read one nonempty line of space-separated integers.
- Display the greatest integer on one line.
- Handle negative numbers and repeated maximum values.
- Do not print prompts or additional text.

## Tips
- Consider how to choose a starting candidate when every number is negative.
- How should a new value affect the current greatest value?
- Check collections containing a single element.

## Example Input
```text
-7 -2 -9
```

## Example Output
```text
-2
```

*Source: gauntlex/03-collections/027-reverse-words/README.md*

### 027 — Reverse the Sequence

## Description
The order of items in a sequence can change without changing the items themselves. Build a program that reverses the order of words in a line while leaving the characters inside each word unchanged.

## Requirements
- Read one line of space-separated words; the line may be empty.
- Display the words in reverse order.
- Separate displayed words with single spaces.
- If the input is empty, display a blank line.
- Do not print prompts or additional text.

## Tips
- Distinguish reversing a sequence of words from reversing the letters in each word.
- How can the result be converted back into one line of text?
- Consider sequences with one word or no words.

## Example Input
```text
one two three
```

## Example Output
```text
three two one
```

*Source: gauntlex/03-collections/028-filter-even/README.md*

### 028 — Keep the Evens

## Description
Filtering a collection means keeping only elements that satisfy a condition. Build a program that selects even integers without changing their relative order.

## Requirements
- Read one line of space-separated integers; the line may be empty.
- Keep only the even integers.
- Display retained values in their original order, separated by single spaces.
- If there are no even values, display a blank line.
- Do not print prompts or additional text.

## Tips
- Decide how to determine whether each integer qualifies.
- Think about how to preserve the order of retained values.
- Check inputs containing negative even numbers and no qualifying elements.

## Example Input
```text
1 2 3 4 6
```

## Example Output
```text
2 4 6
```

*Source: gauntlex/03-collections/029-unique-order/README.md*

### 029 — First Appearance

## Description
A collection can contain the same word more than once. Build a program that removes repeated words while keeping the order in which each distinct word first appeared.

## Requirements
- Read one line of space-separated words; the line may be empty.
- Display each distinct word exactly once.
- Preserve the order of first appearance.
- Treat uppercase and lowercase versions as different words.
- Separate displayed words with single spaces; display a blank line for empty input.
- Do not print prompts or additional text.

## Tips
- Removing duplicates and preserving order are separate concerns.
- What information must be remembered when a word is encountered?
- Check what happens when every word is the same.

## Example Input
```text
a b a c b
```

## Example Output
```text
a b c
```

*Source: gauntlex/03-collections/030-word-frequency/README.md*

### 030 — Word Tally

## Description
A frequency report records how often each distinct word appears in a collection. Build a report that preserves the order in which words first appeared while counting all occurrences.

## Requirements
- Read one line of space-separated words; the line may be empty.
- Count occurrences of each distinct word using case-sensitive matching.
- Display one line per distinct word in the format `WORD: COUNT`.
- Order the lines by each word's first appearance.
- If the input is empty, produce no output.
- Do not print prompts or additional text.

## Tips
- Consider how a word can be associated with a running count.
- How can you avoid printing a word more than once?
- Think about the distinction between counting occurrences and ordering the report.

## Example Input
```text
cat dog cat
```

## Example Output
```text
cat: 2
dog: 1
```

*Source: gauntlex/03-collections/031-sort-numbers/README.md*

### 031 — Numeric Order

## Description
A collection of integers may arrive in any order. Build a program that arranges them from smallest to largest. Numeric order is different from the alphabetical order of the characters used to write numbers.

## Requirements
- Read one line of space-separated integers; the line may be empty.
- Display all integers in ascending numeric order.
- Preserve repeated values.
- Separate output values with single spaces.
- If the input is empty, display a blank line.
- Do not print prompts or additional text.

## Tips
- Compare the ordering of the text values `10` and `2` with the ordering of the numbers they represent.
- Consider what should happen to duplicate values.
- Check an input containing negative numbers.

## Example Input
```text
9 2 10 2
```

## Example Output
```text
2 2 9 10
```

*Source: gauntlex/03-collections/032-middle-slice/README.md*

### 032 — Inside the Boundaries

## Description
Sometimes only the middle part of a sequence is needed. Build a program that excludes the first and last words and displays everything between them in the original order.

## Requirements
- Read one line of space-separated words; the line may be empty.
- Exclude the first and last word.
- Display the remaining words in their original order, separated by single spaces.
- If the input has fewer than three words, display a blank line.
- Do not print prompts or additional text.

## Tips
- Identify the positions that mark the beginning and end of the desired region.
- Consider whether those boundary positions belong in the result.
- What happens when the region contains no elements?

## Example Input
```text
a b c d
```

## Example Output
```text
b c
```

*Source: gauntlex/03-collections/033-set-overlap/README.md*

### 033 — Shared Vocabulary

## Description
Two collections may contain some of the same words. Build a program that finds the distinct words shared by both collections and reports them in alphabetical order.

## Requirements
- Read two lines of space-separated words.
- Find words that occur in both lines, using case-sensitive matching.
- Display each common word at most once.
- Sort the common words alphabetically and separate them with single spaces.
- If no words are shared, display a blank line.
- Do not print prompts or additional text.

## Tips
- Think about how to check whether a word belongs to both collections.
- Why must repeated words not appear multiple times in the result?
- Consider the difference between the order words appear in the input and alphabetical order.

## Example Input
```text
red blue green
blue yellow red
```

## Example Output
```text
blue red
```

*Source: gauntlex/03-collections/034-pair-count/README.md*

### 034 — Matching Pairs

## Description
Repeated values can form pairs of matching positions. Build a program that counts every pair of distinct positions containing the same integer. A value appearing several times can contribute multiple pairs.

## Requirements
- Read one line of space-separated integers; the line may be empty.
- Count each pair of distinct positions with equal values exactly once.
- Display the total number of matching pairs on one line.
- If the input is empty or has no matching positions, display `0`.
- Do not print prompts or additional text.

## Tips
- Work through a collection with three copies of the same value.
- When a new copy appears, how many earlier copies could it pair with?
- Be careful not to count the same two positions in both orders.

## Example Input
```text
2 2 2
```

## Example Output
```text
3
```

---

## Functions

*Source: gauntlex/04-functions/035-sum-function/README.md*

### 035 — Return a Sum

## Description
A function makes a calculation reusable by other parts of a program. Create an operation that receives two numbers and gives their sum back to its caller rather than displaying it.

## Requirements
- Implement `sum_two(a, b)` in `solution.py`.
- Accept two integers, including negative values and zero.
- Return their arithmetic sum.
- Do not print the result or execute input-handling code when the module is imported.

## Tips
- What does a caller receive when a function returns a value?
- How is returning different from printing?
- Try values with different signs.

## Example Behavior
`sum_two(2, 3)` → `5`; `sum_two(-4, 7)` → `3`.

*Source: gauntlex/04-functions/036-absolute-function/README.md*

### 036 — Distance from Zero

## Description
The absolute value of an integer describes its distance from zero, regardless of direction. Write a reusable function that produces this nonnegative quantity.

## Requirements
- Implement `absolute(n)` in `solution.py`.
- Return the absolute value of integer `n`.
- Handle negative values, zero, and positive values.
- Return the result without printing or running input-handling code on import.

## Tips
- Which inputs already represent a nonnegative distance?
- What should change when the input is negative?
- Consider the boundary at zero.

## Example Behavior
`absolute(-7)` → `7`; `absolute(0)` → `0`.

*Source: gauntlex/04-functions/037-factorial/README.md*

### 037 — Factorial Product

## Description
A factorial combines a sequence of positive integers through multiplication. Implement this operation as a function and account for the empty product at zero.

## Requirements
- Implement `factorial(n)` in `solution.py`.
- Assume `n` is a nonnegative integer.
- Return the product of the positive integers from 1 through `n`.
- Return `1` when `n` is zero.
- Do not print or execute input-handling code on import.

## Tips
- What value should a running product begin with?
- Why does the zero case return one?
- Trace the result for a small input by hand.

## Example Behavior
`factorial(0)` → `1`; `factorial(4)` → `24`.

*Source: gauntlex/04-functions/038-palindrome/README.md*

### 038 — Mirror Text

## Description
Some strings read the same forward and backward. Build a function that checks this property using an exact character comparison; capitalization, spaces, and punctuation all matter.

## Requirements
- Implement `is_palindrome(text)` in `solution.py`.
- Return a boolean indicating whether the string reads identically in both directions.
- Compare characters exactly, including case and whitespace.
- Treat the empty string and a one-character string as palindromes.
- Do not print or execute input-handling code on import.

## Tips
- What positions correspond when reading from opposite ends?
- How would a single differing character affect the answer?
- Check strings with spaces and mixed case.

## Example Behavior
`is_palindrome('level')` → `True`; `is_palindrome('Level')` → `False`.

*Source: gauntlex/04-functions/039-vowel-count/README.md*

### 039 — Vowel Census

## Description
Count how many English vowels appear in a piece of text. The count must include repeated vowels and treat uppercase and lowercase forms equally.

## Requirements
- Implement `count_vowels(text)` in `solution.py`.
- Count occurrences of `a`, `e`, `i`, `o`, and `u`, regardless of case.
- Do not count `y` as a vowel.
- Return an integer, including zero for text without vowels.
- Do not print or execute input-handling code on import.

## Tips
- How can characters be compared consistently despite capitalization?
- Does counting distinct vowel types give the same result as counting occurrences?
- Consider an empty string.

## Example Behavior
`count_vowels('Gauntlex')` → `3`; `count_vowels('WHY')` → `0`.

*Source: gauntlex/04-functions/040-prime-check/README.md*

### 040 — Prime or Composite

## Description
Prime numbers have exactly two positive divisors: one and themselves. Build a function that identifies primes while correctly rejecting zero, one, and negative integers.

## Requirements
- Implement `is_prime(n)` in `solution.py`.
- Return `True` exactly when integer `n` is prime.
- Return `False` for every integer below 2.
- Return a boolean without printing or executing input-handling code on import.

## Tips
- What does finding one divisor other than one and the number prove?
- Can you avoid checking every smaller integer?
- Consider 2, 4, 9, and 17.

## Example Behavior
`is_prime(2)` → `True`; `is_prime(17)` → `True`; `is_prime(1)` → `False`.

*Source: gauntlex/04-functions/041-fibonacci/README.md*

### 041 — Sequence Memory

## Description
In the Fibonacci sequence, each term after the first two is the sum of the two preceding terms. Write a function that finds a requested term without displaying intermediate values.

## Requirements
- Implement `fibonacci(n)` in `solution.py`.
- Assume `n` is a nonnegative integer.
- Use the definition F(0) = 0, F(1) = 1, and F(n) = F(n−1) + F(n−2).
- Return the nth term as an integer.
- Do not print or execute input-handling code on import.

## Tips
- Which previous terms are needed to determine the next one?
- Why are the first two terms special?
- Trace a short sequence before generalizing.

## Example Behavior
`fibonacci(0)` → `0`; `fibonacci(1)` → `1`; `fibonacci(6)` → `8`.

*Source: gauntlex/04-functions/042-anagram/README.md*

### 042 — Same Letters, Different Order

## Description
Two strings are anagrams when they contain the same characters with the same frequencies, even if their orders differ. Write a function that checks this exact relationship.

## Requirements
- Implement `are_anagrams(a, b)` in `solution.py`.
- Return `True` when both strings have identical character frequencies.
- Treat uppercase and lowercase as different characters.
- Include spaces and punctuation in the comparison.
- Return a boolean without printing or executing input-handling code on import.

## Tips
- Why is comparing only the set of characters insufficient?
- What happens when one letter appears twice in one string?
- Consider strings of different lengths.

## Example Behavior
`are_anagrams('listen', 'silent')` → `True`; `are_anagrams('aab', 'abb')` → `False`.

*Source: gauntlex/04-functions/043-flatten-once/README.md*

### 043 — One Level Down

## Description
A list can contain several smaller lists. Combine their elements into one new list while preserving encounter order. This task flattens exactly one level of nesting.

## Requirements
- Implement `flatten_once(groups)` in `solution.py`.
- Accept a list of lists.
- Return a new list containing the inner elements in their original order.
- Handle empty inner lists and an empty outer list.
- Do not mutate the supplied lists, print, or execute input-handling code on import.

## Tips
- How does combining inner lists differ from recursively flattening arbitrary nesting?
- What should an empty inner list contribute?
- Consider how to preserve element order.

## Example Behavior
`flatten_once([[1, 2], [3], []])` → `[1, 2, 3]`.

*Source: gauntlex/04-functions/044-first-unique/README.md*

### 044 — First Unrepeated Character

## Description
A character that appears once may be useful as a unique marker. Find the earliest character whose total frequency in the complete string is exactly one.

## Requirements
- Implement `first_unique(text)` in `solution.py`.
- Return the first character occurring exactly once in the entire string.
- Return `None` when no such character exists.
- Treat uppercase and lowercase characters as distinct.
- Do not print or execute input-handling code on import.

## Tips
- Why might a character that seems unique at first turn out to repeat later?
- How can frequency and original order both matter?
- Consider empty input.

## Example Behavior
`first_unique('swiss')` → `'w'`; `first_unique('aabb')` → `None`.

*Source: gauntlex/04-functions/045-chunk-list/README.md*

### 045 — Divide Into Chunks

## Description
Partition a sequence into consecutive groups of a requested maximum size. Preserve the order of elements, and allow the final group to be shorter.

## Requirements
- Implement `chunks(items, size)` in `solution.py`.
- Assume `size` is a positive integer.
- Return a new list of consecutive sublists, each containing at most `size` elements.
- Preserve input order, return an empty list for empty input, and do not modify `items`.
- Return the result without printing or running input-handling code on import.

## Tips
- What happens when the input length is not divisible by the chunk size?
- How do you identify consecutive group boundaries?
- Consider when the group size is larger than the entire collection.

## Example Behavior
`chunks([1, 2, 3, 4, 5], 2)` → `[[1, 2], [3, 4], [5]]`.

*Source: gauntlex/04-functions/046-gcd/README.md*

### 046 — Greatest Shared Divisor

## Description
Find the greatest nonnegative integer that divides two integers without a remainder. The function must handle negative inputs and zero correctly.

## Requirements
- Implement `gcd(a, b)` in `solution.py`.
- Accept any two integers, including negative values and zero.
- Return a nonnegative greatest common divisor.
- Return `0` for two zero arguments.
- Return the result without printing or running input-handling code on import.

## Tips
- How does the remainder of two numbers relate to their common divisors?
- Why does changing a number's sign not change the answer?
- Consider when one argument is zero.

## Example Behavior
`gcd(12, 18)` → `6`; `gcd(-8, 12)` → `4`; `gcd(0, 0)` → `0`.

---

## Algorithms

*Source: gauntlex/05-algorithms/047-word-count/README.md*

### 047 — Count the Words

## Description
Words may be separated by spaces, tabs, or other whitespace. Determine how many words appear in a text without counting empty gaps.

## Requirements
- Implement `word_count(text)` in `solution.py`.
- Count nonempty words separated by whitespace.
- Return `0` for empty or whitespace-only input.
- Return an integer; do not print or execute code on import.

## Tips
- How does repeated whitespace affect word boundaries?
- Check leading and trailing spaces, tabs, and empty text.

## Example Behavior
`word_count('one two three')` → `3`; `word_count('  a  b  ')` → `2`.

*Source: gauntlex/05-algorithms/048-longest-word/README.md*

### 048 — Longest in the Line

## Description
Find the longest word in a text. If several words have the same maximum length, keep the first one encountered.

## Requirements
- Implement `longest_word(text)` in `solution.py`.
- Treat words as nonempty whitespace-separated tokens.
- Return the longest word; for ties return the earliest.
- Return an empty string if there are no words.
- Do not print or execute code on import.

## Tips
- How should the current winner change when a longer word appears?
- Why should a tie not replace the earlier winner?

## Example Behavior
`longest_word('cat elephant dog')` → `'elephant'`; `longest_word('aa bb')` → `'aa'`.

*Source: gauntlex/05-algorithms/049-rotate-list/README.md*

### 049 — Circular Shift

## Description
A rotation moves items from the end of a list to the beginning while preserving their relative order. Build a function that handles shifts longer than the list itself.

## Requirements
- Implement `rotate_right(items, k)` in `solution.py`.
- Assume `k` is a nonnegative integer.
- Return a new list rotated right by `k` positions.
- Return an empty list for empty input and do not modify `items`.
- Do not print or execute code on import.

## Tips
- What happens after a full rotation?
- How can a large shift be related to the list length?
- Consider zero shifts.

## Example Behavior
`rotate_right([1, 2, 3, 4], 1)` → `[4, 1, 2, 3]`; `rotate_right([1, 2], 5)` → `[2, 1]`.

*Source: gauntlex/05-algorithms/050-merge-sorted/README.md*

### 050 — Two Ordered Streams

## Description
Combine two already sorted lists into one sorted list. Preserve every value, including duplicates, without changing the original inputs.

## Requirements
- Implement `merge_sorted(left, right)` in `solution.py`.
- Assume both input lists are sorted in ascending numeric order.
- Return a new ascending list containing every element of both inputs.
- Preserve duplicates and handle empty lists.
- Do not modify inputs, print, or execute code on import.

## Tips
- Compare the next unconsumed values from each list.
- What happens when one list has no elements left?
- How should equal values be handled?

## Example Behavior
`merge_sorted([1, 3, 5], [2, 4])` → `[1, 2, 3, 4, 5]`; `merge_sorted([], [-1, 2])` → `[-1, 2]`.

*Source: gauntlex/05-algorithms/051-balanced-brackets/README.md*

### 051 — Nested Delimiters

## Description
Brackets must close in the reverse order in which they open. Determine whether a string has correctly matched and nested parentheses, square brackets, and braces.

## Requirements
- Implement `balanced_brackets(text)` in `solution.py`.
- Recognize `()`, `[]`, and `{}` as matching pairs.
- Return `True` only when all brackets are correctly nested and closed.
- Ignore characters that are not brackets; an empty string is valid.
- Return a boolean without printing or executing code on import.

## Tips
- Why are equal counts of opening and closing brackets insufficient?
- Which opening bracket should match the next closing bracket?
- Consider mismatched nesting.

## Example Behavior
`balanced_brackets('([]{})')` → `True`; `balanced_brackets('([)]')` → `False`.

*Source: gauntlex/05-algorithms/052-run-length/README.md*

### 052 — Compress Repeated Runs

## Description
Represent a string as consecutive runs of identical characters. Each run records the character and the number of times it appears without interruption.

## Requirements
- Implement `run_length(text)` in `solution.py`.
- Return a list of two-element lists in the form `[character, count]`.
- Create a separate entry for each consecutive run, preserving order.
- Return an empty list for empty input.
- Do not print or execute code on import.

## Tips
- How can you tell when one run ends and the next begins?
- Why must separated runs of the same character remain distinct?

## Example Behavior
`run_length('aaabb')` → `[['a', 3], ['b', 2]]`; `run_length('abc')` → `[['a', 1], ['b', 1], ['c', 1]]`.

*Source: gauntlex/05-algorithms/053-caesar/README.md*

### 053 — Alphabet Rotation

## Description
Shift each English letter by a specified number of positions, wrapping around the alphabet. Preserve case and leave nonletters unchanged.

## Requirements
- Implement `caesar(text, k)` in `solution.py`.
- Shift ASCII letters `A`–`Z` and `a`–`z` forward by integer `k` positions.
- Wrap around each alphabet; support zero, negative, and large shifts.
- Preserve case and leave all non-ASCII letters, digits, spaces, and punctuation unchanged.
- Return the transformed string without printing or executing code on import.

## Tips
- What happens when a shift crosses `z` or `Z`?
- How does a full alphabet rotation affect the result?
- Think about negative shifts.

## Example Behavior
`caesar('Abc-Z!', 2)` → `'Cde-B!'`; `caesar('xyz', 3)` → `'abc'`.

*Source: gauntlex/05-algorithms/054-common-prefix/README.md*

### 054 — Shared Beginning

## Description
Several words may begin with the same sequence of characters. Find the longest prefix shared by every word in the input collection.

## Requirements
- Implement `common_prefix(words)` in `solution.py`.
- Return the longest initial substring shared by all input strings.
- Compare characters exactly, including case.
- Return an empty string for an empty list or when no common prefix exists.
- Do not mutate input, print, or execute code on import.

## Tips
- How does the shortest word limit the possible prefix?
- What happens at the first mismatch?
- Consider a list containing one word.

## Example Behavior
`common_prefix(['flower', 'flow', 'flight'])` → `'fl'`; `common_prefix(['dog', 'cat'])` → `''`.

*Source: gauntlex/05-algorithms/055-matrix-transpose/README.md*

### 055 — Rows Become Columns

## Description
Transposing a matrix exchanges its rows and columns. Build a function that returns a new matrix with each element moved to its corresponding transposed position.

## Requirements
- Implement `transpose(matrix)` in `solution.py`.
- Assume a rectangular list of rows, all of equal length.
- Return a new matrix whose rows correspond to the original columns.
- Return `[]` for an empty matrix or a matrix with zero columns.
- Do not modify input, print, or execute code on import.

## Tips
- Draw a small rectangular grid and track the row and column of one element.
- How do the dimensions change after transposition?

## Example Behavior
`transpose([[1, 2], [3, 4]])` → `[[1, 3], [2, 4]]`; `transpose([[1, 2, 3]])` → `[[1], [2], [3]]`.

*Source: gauntlex/05-algorithms/056-binary-search/README.md*

### 056 — Halve the Search

## Description
A sorted collection can be searched efficiently by repeatedly ruling out half of the remaining candidates. Find the index of a target value using this approach.

## Requirements
- Implement `binary_search(items, target)` in `solution.py`.
- Assume `items` is sorted in ascending order and contains distinct integers.
- Return the zero-based index of `target`, or `-1` when absent.
- Use a search that narrows the candidate interval rather than checking every item in order.
- Do not modify input, print, or execute code on import.

## Tips
- How does a comparison with the middle value eliminate part of the search space?
- What does it mean when no candidate positions remain?

## Example Behavior
`binary_search([1, 3, 5, 7], 5)` → `2`; `binary_search([1, 3, 5], 2)` → `-1`.

*Source: gauntlex/05-algorithms/057-second-largest/README.md*

### 057 — Runner-Up Value

## Description
The second-largest distinct value is not always the second item in descending order. Find the runner-up value while ignoring repeated copies of the maximum.

## Requirements
- Implement `second_largest(items)` in `solution.py`.
- Return the second-largest distinct integer.
- Return `None` when fewer than two distinct values exist.
- Support negative integers and duplicate values.
- Do not modify input, print, or execute code on import.

## Tips
- Why should two copies of the maximum not occupy both ranks?
- Consider an all-equal list and a list of negative numbers.

## Example Behavior
`second_largest([3, 1, 3, 2])` → `2`; `second_largest([5, 5])` → `None`.

*Source: gauntlex/05-algorithms/058-group-by-length/README.md*

### 058 — Group by Size

## Description
Organize words into groups according to their lengths. Each group must retain the original encounter order of the words it contains.

## Requirements
- Implement `group_by_length(words)` in `solution.py`.
- Return a dictionary mapping integer word lengths to lists of words.
- Preserve the original order within each length group.
- Include empty strings under length zero; return `{}` for empty input.
- Do not modify input, print, or execute code on import.

## Tips
- Which data structure can associate one length with several words?
- What should happen when another word has a length already seen?

## Example Behavior
`group_by_length(['a', 'cat', 'be', 'dog'])` → `{1: ['a'], 2: ['be'], 3: ['cat', 'dog']}`; `group_by_length([])` → `{}`.

*Source: gauntlex/05-algorithms/059-valid-parentheses/README.md*

### 059 — Balance the Parentheses

## Description
A sequence of parentheses is valid only if every opening parenthesis is closed in the correct order. Detect invalid prefixes as well as unclosed parentheses at the end.

## Requirements
- Implement `valid_parentheses(text)` in `solution.py`.
- Assume `text` contains only `(` and `)` characters.
- Return `True` only if the parentheses form complete, correctly ordered pairs.
- Return `True` for an empty string.
- Return a boolean without printing or executing code on import.

## Tips
- Why can equal counts still describe an invalid sequence?
- What must remain true at every point while reading from left to right?

## Example Behavior
`valid_parentheses('(())')` → `True`; `valid_parentheses('())(')` → `False`.

*Source: gauntlex/05-algorithms/060-move-zeros/README.md*

### 060 — Zeros to the Back

## Description
Rearrange a sequence so that all numeric zeros appear after the nonzero values. Preserve the original order of nonzero elements.

## Requirements
- Implement `move_zeros(items)` in `solution.py`.
- Accept a list of integers.
- Return a new list containing all nonzero elements in original order, followed by the same number of zeros.
- Preserve the input length and do not mutate `items`.
- Do not print or execute code on import.

## Tips
- What information must be preserved about the nonzero values?
- Consider all-zero, no-zero, and empty inputs.

## Example Behavior
`move_zeros([0, 1, 0, 3, 12])` → `[1, 3, 12, 0, 0]`; `move_zeros([0, 0])` → `[0, 0]`.

*Source: gauntlex/05-algorithms/061-pascal-row/README.md*

### 061 — Build Pascal's Row

## Description
Pascal's triangle grows one row at a time. Every row begins and ends with one, while interior entries are formed from neighboring values in the preceding row.

## Requirements
- Implement `pascal_row(n)` in `solution.py`.
- Assume `n` is a nonnegative integer and row numbering begins at zero.
- Return the full nth row as a list of integers.
- Row zero is `[1]`; each later row contains `n + 1` entries.
- Do not print or execute code on import.

## Tips
- How do the first and last values differ from the interior values?
- Trace the first few rows and identify how their lengths change.

## Example Behavior
`pascal_row(0)` → `[1]`; `pascal_row(1)` → `[1, 1]`; `pascal_row(4)` → `[1, 4, 6, 4, 1]`.

*Source: gauntlex/05-algorithms/062-flatten-recursive/README.md*

### 062 — Unfold Nested Lists

## Description
A nested list may contain integers and more lists at arbitrary depths. Traverse the structure and return all integers in their original left-to-right order.

## Requirements
- Implement `flatten_recursive(items)` in `solution.py`.
- Assume elements are integers or lists following the same rule at any depth.
- Return a new flat list containing every integer in encounter order.
- Handle empty lists at any depth.
- Do not modify input, print, or execute code on import.

## Tips
- What is the difference between encountering an integer and encountering another list?
- How does the same decision recur inside nested lists?

## Example Behavior
`flatten_recursive([1, [2, [3]], 4])` → `[1, 2, 3, 4]`; `flatten_recursive([])` → `[]`.

---

## Text Files

*Source: gauntlex/06-text-files/063-normalize-spaces/README.md*

### 063 — One Space Apart

## Description
A message copied from different sources may contain tabs, newlines, and repeated spaces. Produce a clean single-line representation without losing or rearranging words.

## Requirements
- Implement `normalize_spaces(text)` in `starter/solution.py`.
- Treat consecutive whitespace characters as a single separator between words.
- Remove leading and trailing whitespace; return an empty string when no words remain.
- Preserve the order and spelling of nonwhitespace characters.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- What happens when the input contains only tabs and spaces?
- Why should a newline between two words become a separator rather than joining the words?

## Example Behavior
`normalize_spaces("  hello   world \n")` → `"hello world"`

`normalize_spaces("\tA \t B\t")` → `"A B"`

*Source: gauntlex/06-text-files/064-line-count/README.md*

### 064 — Count the Lines

## Description
Text records can end at a newline or at the end of the string. Count logical lines consistently, without inventing an extra record merely because the text ends in a line break.

## Requirements
- Implement `line_count(text)` in `starter/solution.py`.
- Return the number of logical lines represented by the supplied text.
- Count a final nonempty line even when it has no trailing newline.
- Do not count a phantom extra line after a trailing newline; empty text contains zero lines.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- Compare an empty string, a single word, and a word followed by a newline.
- Why is counting separators alone not sufficient?

## Example Behavior
`line_count("one\ntwo\n")` → `2`

`line_count("single")` → `1`

*Source: gauntlex/06-text-files/065-safe-integer/README.md*

### 065 — Parse With Care

## Description
User-entered numbers are not always valid integers. Convert valid base-ten integer text while giving callers a predictable nonexceptional result for invalid input.

## Requirements
- Implement `parse_integer(text)` in `starter/solution.py`.
- Accept surrounding whitespace and an optional leading sign on a valid integer.
- Return the parsed integer for valid decimal integer text.
- Return `None` for text that cannot be interpreted as a base-ten integer, including fractional notation.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- How should `-12` differ from `3.5`?
- What should happen with empty or whitespace-only input?

## Example Behavior
`parse_integer("  -12 ")` → `-12`

`parse_integer("3.5")` → `None`

*Source: gauntlex/06-text-files/066-extract-numbers/README.md*

### 066 — Numbers Hidden in Text

## Description
Logs and messages often mix words with numeric identifiers. Extract every consecutive run of ASCII digits and represent each run as an integer.

## Requirements
- Implement `extract_numbers(text)` in `starter/solution.py`.
- Find nonoverlapping runs of ASCII digits `0` through `9` in input order.
- Convert each run to an integer; leading zeros do not survive numeric conversion.
- Return an empty list when no qualifying digit runs occur.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- What ends one digit run and starts the next?
- Should a leading minus sign be part of a run of digits under this contract?

## Example Behavior
`extract_numbers("a12 b003 c")` → `[12, 3]`

`extract_numbers("no digits")` → `[]`

*Source: gauntlex/06-text-files/067-mask-email/README.md*

### 067 — Protect the Address

## Description
When displaying an address publicly, conceal most of the local part while keeping its first character and domain recognizable.

## Requirements
- Implement `mask_email(email)` in `starter/solution.py`.
- Preserve the domain and `@` separator in the returned address.
- For a local part longer than one character, keep its first character and replace each remaining character with `*`.
- Keep a one-character local part visible as shown in the examples.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- Which characters identify the domain and must remain unchanged?
- How does the result differ for a one-character local part?

## Example Behavior
`mask_email("alice@example.com")` → `"a****@example.com"`

`mask_email("x@y.io")` → `"x@y.io"`

*Source: gauntlex/06-text-files/068-slugify/README.md*

### 068 — URL-Friendly Words

## Description
Page titles are often turned into compact URL identifiers. Normalize casing and separate words consistently, even when punctuation and whitespace appear together.

## Requirements
- Implement `slugify(text)` in `starter/solution.py`.
- Return a lowercase, hyphen-separated identifier based on the supplied title.
- Treat punctuation, whitespace, and underscores as boundaries between retained word content.
- Avoid leading, trailing, or repeated hyphens; return an empty slug if nothing remains.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- What happens when several separators occur consecutively?
- How should leading or trailing punctuation affect the output?

## Example Behavior
`slugify("Hello, Python World!")` → `"hello-python-world"`

`slugify("  A__B  ")` → `"a-b"`

*Source: gauntlex/06-text-files/069-csv-row/README.md*

### 069 — Fields and Quotes

## Description
A comma-separated row may contain quoted fields whose commas are data rather than separators. Interpret one complete record using CSV quoting conventions.

## Requirements
- Implement `parse_csv_row(line)` in `starter/solution.py`.
- Return the parsed fields of the supplied CSV record as a list of strings.
- Respect quoted commas and doubled quotation marks inside quoted fields.
- Preserve empty fields and their positions; use Python's standard library.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- Why does splitting on every comma fail for a quoted field?
- How are quotation marks represented inside a quoted CSV value?

## Example Behavior
`parse_csv_row("a,b,c")` → `["a", "b", "c"]`

`parse_csv_row("\"a,b\",c")` → `["a,b", "c"]`

*Source: gauntlex/06-text-files/070-json-value/README.md*

### 070 — Find a JSON Field

## Description
Applications frequently receive structured JSON text but need only one field. Parse the document and retrieve the requested object key while handling absent keys.

## Requirements
- Implement `json_value(text, key)` in `starter/solution.py`.
- Decode the supplied JSON text using standard JSON rules.
- Return the value associated with the requested key in the decoded object.
- Return `None` when the requested key is missing; JSON `null` also maps to Python `None`.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- Why can missing keys and explicit JSON `null` produce the same result?
- Why is manual string searching unreliable for JSON values?

## Example Behavior
`json_value("{\"a\":1,\"b\":2}", "a")` → `1`

`json_value("{\"x\":null}", "x")` → `None`

*Source: gauntlex/06-text-files/071-json-compact/README.md*

### 071 — Canonical JSON Text

## Description
A canonical JSON representation makes output stable for comparison and storage. Convert JSON-compatible Python values into compact text with predictable object key order.

## Requirements
- Implement `compact_json(value)` in `starter/solution.py`.
- Serialize the supplied JSON-compatible value as a string, not bytes.
- Sort dictionary keys and omit unnecessary spaces between JSON tokens.
- Preserve the data's JSON meaning, including nested values and arrays.
- Use Python's standard library only. Return values without printing or requesting input; do not mutate caller-owned inputs.

## Tips
- Why can two equivalent dictionaries serialize differently without canonical key ordering?
- Which spaces are structural formatting rather than part of string values?

## Example Behavior
`compact_json({"b": 2, "a": 1})` → `"{\"a\":1,\"b\":2}"`

`compact_json([1, 2, 3])` → `"[1,2,3]"`

*Source: gauntlex/06-text-files/072-path-extension/README.md*

### 072 — Final File Suffix

## Description
A filename can contain several dots or none at all. Identify its final suffix without confusing earlier filename segments with the extension.

## Requirements
- Implement `path_extension(path)` in `starter/solution.py`.
- Inspect the final filename component of the supplied POSIX path.
- Return the final extension in lowercase without the leading dot.
- Return an empty string when there is no extension; do not treat a lone leading dot as an ordinary extension.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- Why is the final dot more relevant than the first dot?
- How should a hidden file without a second dot be treated?

## Example Behavior
`path_extension("notes.TXT")` → `"txt"`

`path_extension("archive.tar.gz")` → `"gz"`

*Source: gauntlex/06-text-files/073-safe-divide/README.md*

### 073 — Division Without Failure

## Description
A reusable numeric operation should handle an expected zero divisor without crashing the caller. Preserve ordinary division behavior for valid divisors.

## Requirements
- Implement `safe_divide(a, b)` in `starter/solution.py`.
- Return the result of dividing `a` by `b` when the divisor is nonzero.
- Return `None` when `b` is zero rather than raising a division-by-zero exception.
- Do not change the operands or print a result.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- What is the difference between a valid zero quotient and an invalid zero divisor?
- Which failure condition does this function explicitly handle?

## Example Behavior
`safe_divide(8, 2)` → `4`

`safe_divide(3, 0)` → `None`

*Source: gauntlex/06-text-files/074-parse-date/README.md*

### 074 — Real Calendar Dates

## Description
A date-like string is not necessarily a real date. Validate calendar rules, including month lengths and leap years, before accepting it.

## Requirements
- Implement `parse_date(text)` in `starter/solution.py`.
- Interpret date text in the `YYYY-MM-DD` calendar format.
- Return the validated date string for a real date.
- Return `None` when the date is invalid, including impossible days such as February 29 in a nonleap year.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- Why does a matching pattern not prove that a date exists?
- Which years permit February 29?

## Example Behavior
`parse_date("2024-02-29")` → `"2024-02-29"`

`parse_date("2023-02-29")` → `None`

*Source: gauntlex/06-text-files/075-days-between/README.md*

### 075 — Calendar Distance

## Description
Calendar arithmetic must account for varying month lengths and leap years. Determine the absolute number of days separating two supplied dates.

## Requirements
- Implement `days_between(a, b)` in `starter/solution.py`.
- Accept two valid date strings in `YYYY-MM-DD` format.
- Return the nonnegative count of whole calendar days between them.
- Return `0` for the same date, and produce the same distance when arguments are reversed.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- Why is subtracting day-of-month numbers insufficient?
- What changes when the interval crosses February in a leap year?

## Example Behavior
`days_between("2024-01-01", "2024-01-03")` → `2`

`days_between("2024-03-01", "2024-02-28")` → `2`

*Source: gauntlex/06-text-files/076-iso-weekday/README.md*

### 076 — Day of the Week

## Description
Scheduling systems often represent weekdays numerically. Translate a valid calendar date to the ISO convention instead of relying on locale-specific weekday names.

## Requirements
- Implement `iso_weekday(text)` in `starter/solution.py`.
- Accept a valid date string in `YYYY-MM-DD` format.
- Return the ISO weekday as an integer from `1` (Monday) through `7` (Sunday).
- Use the actual calendar date rather than inferring weekdays from the day-of-month number.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- How does ISO numbering differ from systems that start weeks on Sunday?
- What weekday value should consecutive dates produce?

## Example Behavior
`iso_weekday("2024-01-01")` → `1`

`iso_weekday("2024-01-07")` → `7`

*Source: gauntlex/06-text-files/077-clean-records/README.md*

### 077 — Keep Valid Records

## Description
Imported records may have missing names or names containing only whitespace. Keep usable records while normalizing their names and preserving other fields.

## Requirements
- Implement `clean_records(records)` in `starter/solution.py`.
- Accept a sequence of record dictionaries.
- Discard records without a meaningful `name` value after trimming surrounding whitespace.
- Return cleaned records in their original order, trimming retained names and preserving their other fields.
- Do not modify any original record dictionaries.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- How can you check whether a name remains meaningful after trimming?
- Why should output records be distinct from caller-owned dictionaries?

## Example Behavior
`clean_records([{"name": " Ada ", "age": 3}, {"name": " "}, {"age": 4}])` → `[{"name": "Ada", "age": 3}]`

`clean_records([])` → `[]`

*Source: gauntlex/06-text-files/078-count-file-lines/README.md*

### 078 — Read the Line Count

## Description
A file can contain empty lines, a trailing newline, or a final line with no terminator. Read the caller's UTF-8 text file and count its logical lines.

## Requirements
- Implement `count_file_lines(path)` in `starter/solution.py`.
- Accept a file path supplied by the caller and open that file using UTF-8.
- Return the number of logical text lines as an integer.
- An empty file has zero lines; a final nonempty line without a newline still counts.
- Do not hardcode a filename or print the count.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- Why does counting newline characters alone miss a final unterminated line?
- How do you distinguish an empty file from a file containing one blank line?

*Source: gauntlex/06-text-files/079-read-json-file/README.md*

### 079 — Load Structured Data

## Description
Structured configuration and data files may contain objects, arrays, or scalar JSON values. Load the actual Python value rather than returning unparsed text.

## Requirements
- Implement `read_json_file(path)` in `starter/solution.py`.
- Accept a caller-supplied file path and read it as UTF-8 text.
- Parse the file as JSON and return the decoded Python value.
- Support any valid JSON root type, including objects, arrays, strings, numbers, booleans, and null.
- Do not hardcode paths or print the parsed result.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- Why should the function not assume that every JSON document starts with `{`?
- What Python values correspond to JSON booleans and null?

*Source: gauntlex/06-text-files/080-csv-column-total/README.md*

### 080 — Sum a CSV Column

## Description
CSV reports often reorder columns and contain cells that cannot be used as numbers. Locate the requested column by its header and accumulate valid integer values.

## Requirements
- Implement `csv_column_total(path, column)` in `starter/solution.py`.
- Accept the CSV file path and the name of the column to total.
- Read the CSV with UTF-8 encoding and identify the target column by its header, not a fixed index.
- Add valid integer values from that column and return the numeric total.
- Do not hardcode paths, print results, or alter the input file.
- Use Python's standard library only. Do not mutate caller-owned inputs.

## Tips
- What happens when the requested column moves to another position?
- How should empty or noninteger cells affect the running total?

---

## Objects

*Source: gauntlex/07-objects/081-stack/README.md*

### 081 — Last In, First Out

## Description
A stack stores values so the newest addition is the first one removed. Model this behavior as an object whose state changes across method calls.

## Requirements
- Define `Stack` in `starter/solution.py`.
- Provide `push(value)` to add an item and `pop()` to remove and return the newest item.
- Provide `peek()` to return the newest item without removing it.
- Provide `is_empty()` to report whether any items remain.
- Raise `IndexError` for `pop()` or `peek()` on an empty stack.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- How does the most recent addition affect the next removal?
- What should change after a peek compared with a pop?
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
After pushing `4` and then `9`, `peek()` returns `9`; `pop()` returns `9`, then `4`.

*Source: gauntlex/07-objects/082-queue/README.md*

### 082 — First In, First Out

## Description
A queue represents a waiting line: items leave in the same order in which they arrive. Build an object that maintains that order through repeated operations.

## Requirements
- Define `Queue` in `starter/solution.py`.
- Provide `enqueue(value)` to add an item at the back.
- Provide `dequeue()` to remove and return the oldest waiting item.
- Provide `is_empty()` to report whether the queue contains items.
- Raise `IndexError` when `dequeue()` is called on an empty queue.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- How does this removal order differ from a stack?
- Consider what happens when several items are added before any are removed.
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
After enqueuing `'A'` and `'B'`, successive calls to `dequeue()` return `'A'` and `'B'`.

*Source: gauntlex/07-objects/083-counter/README.md*

### 083 — Count by Key

## Description
A counter can record how often different values are observed. Design an object that tracks counts by key and also remembers the total number of recorded observations.

## Requirements
- Define `CounterMap` in `starter/solution.py`.
- Implement `add(key)` to increase that key's count by one.
- Implement `count(key)` to return the recorded count, or `0` for an unseen key.
- Implement `total()` to return the number of `add` calls across all keys.
- Maintain the state between calls without requiring interactive input.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- How should an unseen key be treated?
- Why is the overall total different from the number of distinct keys?
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
After `add('red')`, `add('blue')`, and `add('red')`, `count('red')` is `2` and `total()` is `3`.

*Source: gauntlex/07-objects/084-bank-account/README.md*

### 084 — Guard the Balance

## Description
A bank account must protect its balance against invalid operations. Model deposits and withdrawals so the object remains consistent even when a transaction is rejected.

## Requirements
- Define `BankAccount(initial_balance=0)` in `starter/solution.py`.
- Expose the current amount through a `balance` property.
- Implement `deposit(amount)` and `withdraw(amount)` to change the balance.
- Raise `ValueError` for a negative initial balance or any nonpositive transaction amount.
- Raise `ValueError` when a withdrawal exceeds the available balance.
- Keep the balance unchanged when an operation fails.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- Why should validation happen before changing the stored balance?
- Consider zero-value transactions and withdrawals exceeding the balance.
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
An account initialized with `10` has balance `15` after depositing `5`; withdrawing `20` raises `ValueError`.

*Source: gauntlex/07-objects/085-temperature/README.md*

### 085 — Two Scales, One Value

## Description
A temperature can be represented in Celsius or Fahrenheit without storing two independent mutable values. Design a class that exposes both scales consistently.

## Requirements
- Define `Temperature(celsius)` in `starter/solution.py`.
- Provide read-only `celsius` and `fahrenheit` properties.
- Ensure the Fahrenheit value reflects the same temperature as the Celsius value.
- Provide `from_fahrenheit(cls, value)` as a class method returning a `Temperature` instance.
- Do not require input or produce output when imported.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- What relationship connects the two temperature scales?
- Why might storing both values independently lead to inconsistencies?
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
`Temperature(0).fahrenheit` is `32`; `Temperature.from_fahrenheit(212).celsius` is `100`.

*Source: gauntlex/07-objects/086-rectangle-class/README.md*

### 086 — Shape Invariants

## Description
An object representing a rectangle should begin in a valid state. Require valid dimensions during construction so subsequent calculations can rely on them.

## Requirements
- Define `Rectangle(width, height)` in `starter/solution.py`.
- Accept positive numeric width and height values.
- Raise `ValueError` if either dimension is zero or negative.
- Implement `area()` to return the rectangle's area.
- Implement `perimeter()` to return the total boundary length.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- Which rules belong in object construction?
- How does enforcing valid dimensions simplify later calculations?
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
For `Rectangle(4, 3)`, `area()` returns `12` and `perimeter()` returns `14`.

*Source: gauntlex/07-objects/087-todo-list/README.md*

### 087 — Track the Work

## Description
A to-do list needs to preserve the order tasks were added while tracking whether each one has been completed. Build a stateful task manager.

## Requirements
- Define `TodoList` in `starter/solution.py`.
- Implement `add(title)` and reject titles that are empty after trimming whitespace.
- Implement `complete(index)` using zero-based insertion positions.
- Raise `IndexError` for invalid task positions.
- Implement `pending()` and `completed()` to return lists of task titles in insertion order.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- Why is a task's original position different from its completion state?
- What should happen when an invalid index is supplied?
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
After adding `'Read'` and `'Write'`, completing index `0` leaves `'Write'` pending and `'Read'` completed.

*Source: gauntlex/07-objects/088-point/README.md*

### 088 — Immutable Coordinates

## Description
A point identifies a fixed location in two-dimensional space. Create a class whose coordinates cannot be reassigned after construction and that can measure distance to another point.

## Requirements
- Define `Point(x, y)` in `starter/solution.py`.
- Store the point's `x` and `y` coordinates.
- Prevent assignments that change either coordinate after construction.
- Implement `distance_to(other)` to return the Euclidean distance to another point.
- Keep the original point unchanged during distance calculations.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- What distinguishes an immutable object from an ordinary mutable one?
- How can horizontal and vertical differences determine distance?
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
The distance from `Point(0, 0)` to `Point(3, 4)` is `5`; assigning a new `x` afterward must fail.

*Source: gauntlex/07-objects/089-inventory/README.md*

### 089 — Stock Ledger

## Description
An inventory tracks how many units of each product are available. Model stock additions and sales without permitting impossible transactions.

## Requirements
- Define `Inventory` in `starter/solution.py`.
- Implement `stock(name, quantity)` to increase a product's quantity.
- Implement `sell(name, quantity)` to decrease the available quantity.
- Require positive integer quantities for both operations.
- Raise `ValueError` for invalid quantities or sales exceeding available stock.
- Implement `quantity(name)` and return `0` for unknown products.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- What state must remain unchanged after a failed sale?
- How should a product with no prior stock be treated?
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
After stocking `'pen'` with `5` units and selling `2`, `quantity('pen')` returns `3`.

*Source: gauntlex/07-objects/090-gradebook/README.md*

### 090 — Student Averages

## Description
A gradebook records multiple scores for each student and reports their average. Distinguish students with no recorded scores from those with a genuine average of zero.

## Requirements
- Define `Gradebook` in `starter/solution.py`.
- Implement `add_score(student, score)` to record a score for a student.
- Accept scores only from `0` through `100`, inclusive.
- Implement `average(student)` to return the arithmetic mean of recorded scores.
- Return `None` when the student has no scores.
- Use Python's standard library only and do not print or request input at import time.

## Tips
- Why does a missing average differ from an average of zero?
- How should repeated scores for one student affect the result?
- Think through the object's state before and after each operation; implement the behavior without using the examples as solution code.

## Example Behavior
After adding scores `80` and `100` for `'Ada'`, `average('Ada')` returns `90`; an unknown student returns `None`.

*Source: gauntlex/07-objects/091-event-emitter/README.md*

### 091 — Publish and Listen

## Description
Build an event emitter that associates named events with callback functions and dispatches notifications in registration order.

## Requirements
- Implement `EventEmitter` in `starter/solution.py`.
- Provide `on(event, callback)` to register a callback.
- Provide `off(event, callback)` to remove one matching registration, if present.
- Provide `emit(event, *args)` to call listeners in registration order and return their results as a list.
- Use the Python standard library only. Do not print or request input at import time.

## Tips
- What happens if a callback is registered twice but removed only once?
- Why does listener order matter?
- Think through valid and invalid operations and their effects on object state.

## Example Behavior
If two callbacks return `1` and `2`, emitting their event returns `[1, 2]`.

*Source: gauntlex/07-objects/092-lru-cache/README.md*

### 092 — Remember the Recent

## Description
Create a capacity-limited cache that discards its least recently used entry when another entry must be stored.

## Requirements
- Implement `LRUCache(capacity)` in `starter/solution.py`.
- Require positive capacity.
- Provide `get(key)` returning the value or `None` for a missing key.
- Provide `put(key, value)` to add or update an entry.
- Make successful reads and updates count as recent use.
- Evict the least recently used entry when insertion exceeds capacity.
- Use the Python standard library only. Do not print or request input at import time.

## Tips
- Why should a read change the order of future eviction?
- What happens when an existing key is updated?
- Think through valid and invalid operations and their effects on object state.

## Example Behavior
With capacity `2`, storing `a` and `b`, reading `a`, then storing `c` evicts `b`.

*Source: gauntlex/07-objects/093-undo-history/README.md*

### 093 — Step Back in Time

## Description
Maintain a current value together with enough history to restore earlier values, one change at a time.

## Requirements
- Implement `UndoHistory(initial)` in `starter/solution.py`.
- Provide `set(value)` to replace the current value and preserve the previous one.
- Expose the active value through the `current` property.
- Provide `undo()` to restore the preceding value.
- Raise `IndexError` when there is no earlier state.
- Use the Python standard library only. Do not print or request input at import time.

## Tips
- What should be saved before each change?
- How does the history change after an undo?
- Think through valid and invalid operations and their effects on object state.

## Example Behavior
Starting at `'A'`, setting `'B'` then `'C'` and undoing once restores `'B'`.

*Source: gauntlex/07-objects/094-shopping-cart/README.md*

### 094 — Cart Rules

## Description
Maintain products, prices, and quantities in a shopping cart without accepting contradictory entries.

## Requirements
- Implement `ShoppingCart` in `starter/solution.py`.
- Provide `add(name, price, quantity=1)` with nonnegative prices and positive integer quantities.
- Increase quantity when an existing name is added at the same price.
- Raise `ValueError` if an existing name is added with a different price.
- Provide `remove(name)` to delete the entire item; raise `KeyError` if missing.
- Provide `total()` to calculate the sum of price times quantity.
- Use the Python standard library only. Do not print or request input at import time.

## Tips
- Why should an existing product not silently change its price?
- What should happen to a cart's total after removal?
- Think through valid and invalid operations and their effects on object state.

## Example Behavior
Adding two items at price `3` and one more at the same price produces a total of `9`.

*Source: gauntlex/07-objects/095-task-priority/README.md*

### 095 — Serve by Priority

## Description
Schedule tasks by urgency while preserving arrival order when two tasks have the same priority.

## Requirements
- Implement `PriorityTasks` in `starter/solution.py`.
- Provide `add(title, priority)` with integer priority values.
- Provide `pop()` returning the title with the lowest numeric priority.
- For equal priorities, return tasks in their insertion order.
- Raise `IndexError` when popping an empty collection.
- Use the Python standard library only. Do not print or request input at import time.

## Tips
- Why is a numeric priority alone insufficient to distinguish ties?
- What information preserves fairness for equally urgent tasks?
- Think through valid and invalid operations and their effects on object state.

## Example Behavior
Adding `A` at priority `2`, `B` at priority `1`, and `C` at priority `1` yields pops `B`, `C`, `A`.

---

## Problem Solving

*Source: gauntlex/08-problem-solving/096-two-sum/README.md*

### 096 — Find the Pair

## Description
Find two different positions in an integer list whose values add to a target. When several answers exist, the order in which pairs finish determines which answer is chosen.

## Requirements
- Implement `two_sum(nums, target)` in `starter/solution.py`.
- Return a list `[i, j]` of zero-based indices where `i < j` and `nums[i] + nums[j] == target`.
- If multiple pairs exist, choose the smallest `j`, then the smallest `i`.
- Return `[]` when no matching pair exists.
- Never use the same position twice.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why does the pair's second index determine which answer comes first?
- Consider repeated values and negative numbers.

## Example Behavior
`two_sum([2, 7, 11, 15], 9)` → `[0, 1]`; `two_sum([3, 3], 6)` → `[0, 1]`.

*Source: gauntlex/08-problem-solving/097-prefix-sums/README.md*

### 097 — Totals Along the Way

## Description
A prefix includes every value from the beginning of a sequence through a chosen position. Produce the running total at each position.

## Requirements
- Implement `prefix_sums(nums)` in `starter/solution.py`.
- Return a new list containing one sum for every prefix of `nums`.
- Include negative values in the totals.
- Return `[]` when the input list is empty.
- Preserve the input list.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- How does the next total relate to the previous total?
- What should the output length be?

## Example Behavior
`prefix_sums([2, -1, 4])` → `[2, 1, 5]`; `prefix_sums([])` → `[]`.

*Source: gauntlex/08-problem-solving/098-max-subarray/README.md*

### 098 — Best Continuous Segment

## Description
A contiguous subarray is an uninterrupted stretch of a list. Find the largest possible sum of a nonempty stretch, even when every number is negative.

## Requirements
- Implement `max_subarray(nums)` in `starter/solution.py`.
- Assume `nums` is a nonempty list of integers.
- Return the maximum sum among all nonempty contiguous subarrays.
- Do not treat an empty subarray as a candidate.
- Do not modify `nums`.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why can the best answer be negative?
- When can extending a segment make its sum worse?

## Example Behavior
`max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])` → `6`; `max_subarray([-4, -2, -8])` → `-2`.

*Source: gauntlex/08-problem-solving/099-product-except-self/README.md*

### 099 — Everyone Else's Product

## Description
For each position, multiply every other value in the list, excluding the value at that position. This challenge requires reasoning about products without division.

## Requirements
- Implement `product_except_self(nums)` in `starter/solution.py`.
- Return a new list of the same length as `nums`.
- At index `i`, include the product of all values except `nums[i]`.
- Do not use division.
- Handle zeros and negative values correctly without modifying the input.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- What changes when the list contains one zero or several zeros?
- How can values before and after a position contribute separately?

## Example Behavior
`product_except_self([1, 2, 3, 4])` → `[24, 12, 8, 6]`; `product_except_self([0, 1, 2])` → `[2, 0, 0]`.

*Source: gauntlex/08-problem-solving/100-rotate-matrix/README.md*

### 100 — Quarter Turn

## Description
A square matrix can be rotated clockwise by a quarter turn. Return the transformed grid without changing the original rows.

## Requirements
- Implement `rotate_matrix(matrix)` in `starter/solution.py`.
- Assume `matrix` is a square list of lists.
- Return a new matrix rotated exactly 90 degrees clockwise.
- Return `[]` for an empty matrix.
- Do not mutate any original row.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Where does each corner move after one clockwise rotation?
- Consider a one-cell grid and an empty grid.

## Example Behavior
`rotate_matrix([[1, 2], [3, 4]])` → `[[3, 1], [4, 2]]`; `rotate_matrix([])` → `[]`.

*Source: gauntlex/08-problem-solving/101-spiral-order/README.md*

### 101 — Walk the Spiral

## Description
Read a rectangular grid in clockwise spiral order, starting at the top-left corner and moving inward as the outer boundary is exhausted.

## Requirements
- Implement `spiral_order(matrix)` in `starter/solution.py`.
- Assume `matrix` is rectangular.
- Return a flat list of values visited clockwise, starting across the top row.
- Visit every cell exactly once.
- Return `[]` for an empty grid; do not mutate the input.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- How do the unvisited boundaries change after completing each side?
- What if only one row or column remains?

## Example Behavior
`spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])` → `[1, 2, 3, 6, 9, 8, 7, 4, 5]`.

*Source: gauntlex/08-problem-solving/102-binary-conversion/README.md*

### 102 — Write in Base Two

## Description
Represent any integer using base-two digits. Return the representation as plain text without Python's binary prefix.

## Requirements
- Implement `to_binary(n)` in `starter/solution.py`.
- Return a string of binary digits representing integer `n`.
- For negative values, use a leading `-` followed by the magnitude's binary digits.
- Return `'0'` for zero.
- Do not include a `0b` prefix.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why does zero need special attention?
- How does a negative sign relate to the digits of the magnitude?

## Example Behavior
`to_binary(0)` → `'0'`; `to_binary(13)` → `'1101'`; `to_binary(-5)` → `'-101'`.

*Source: gauntlex/08-problem-solving/103-roman-numerals/README.md*

### 103 — Number to Numeral

## Description
Convert a decimal integer to the conventional Roman numeral system, including the subtractive forms used for values such as four and nine.

## Requirements
- Implement `to_roman(n)` in `starter/solution.py`.
- Assume `n` is an integer from `1` through `3999`.
- Return its canonical uppercase Roman numeral representation.
- Use standard symbols `I`, `V`, `X`, `L`, `C`, `D`, and `M` and conventional subtractive pairs.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why are four and nine not written using repeated identical symbols?
- How do larger place values relate to smaller ones?

## Example Behavior
`to_roman(4)` → `'IV'`; `to_roman(58)` → `'LVIII'`.

*Source: gauntlex/08-problem-solving/104-roman-to-int/README.md*

### 104 — Numeral to Number

## Description
Interpret a canonical uppercase Roman numeral as its decimal integer value. Some symbols subtract from the following larger symbol rather than adding.

## Requirements
- Implement `roman_to_int(text)` in `starter/solution.py`.
- Assume `text` is a valid canonical uppercase Roman numeral.
- Return its integer value.
- Account for subtractive pairs without requiring validation of malformed input.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- How can the symbol immediately following another affect its value?
- Consider the difference between `VI` and `IV`.

## Example Behavior
`roman_to_int('IV')` → `4`; `roman_to_int('LVIII')` → `58`.

*Source: gauntlex/08-problem-solving/105-longest-unique-substring/README.md*

### 105 — Longest Without Repeats

## Description
A substring is a contiguous stretch of text. Determine the maximum length of a substring in which no character appears more than once.

## Requirements
- Implement `longest_unique_substring(text)` in `starter/solution.py`.
- Return the length of the longest contiguous substring without repeated characters.
- Treat character comparisons as case-sensitive.
- Return `0` for empty text.
- Do not alter the original string.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why is a substring different from a subsequence?
- What happens to a candidate stretch when a character repeats?

## Example Behavior
`longest_unique_substring('abcabcbb')` → `3`; `longest_unique_substring('bbbbb')` → `1`.

*Source: gauntlex/08-problem-solving/106-min-window-sum/README.md*

### 106 — Smallest Sufficient Window

## Description
Find the shortest uninterrupted group of positive integers whose sum reaches or exceeds a target.

## Requirements
- Implement `min_subarray_len(target, nums)` in `starter/solution.py`.
- Assume `target` and all elements of `nums` are positive integers.
- Return the minimum length of a contiguous subarray with sum at least `target`.
- Return `0` when no qualifying subarray exists.
- Do not mutate the input.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why does the positivity of all numbers matter?
- When might shortening a qualifying window preserve its sum threshold?

## Example Behavior
`min_subarray_len(7, [2, 3, 1, 2, 4, 3])` → `2`; `min_subarray_len(15, [1, 2, 3, 4, 5])` → `5`.

*Source: gauntlex/08-problem-solving/107-group-anagrams/README.md*

### 107 — Families of Letters

## Description
Group words with identical character frequencies while preserving both the first appearance of each group and the original order within that group.

## Requirements
- Implement `group_anagrams(words)` in `starter/solution.py`.
- Return a list of lists of anagram strings.
- Treat case and every character as significant.
- Order groups by the first occurrence of any member.
- Preserve input order within each group.
- Return `[]` for empty input; do not mutate the original list.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why is matching only distinct characters insufficient?
- How do you preserve two different levels of ordering?

## Example Behavior
`group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])` → `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`.

*Source: gauntlex/08-problem-solving/108-top-k-frequent/README.md*

### 108 — Most Common Values

## Description
Rank integer values by frequency. If two values appear equally often, the smaller integer comes first.

## Requirements
- Implement `top_k_frequent(nums, k)` in `starter/solution.py`.
- Assume `0 <= k <=` the number of distinct values in `nums`.
- Return exactly `k` distinct integers.
- Order them by descending frequency, then ascending numeric value.
- Return `[]` when `k` is zero.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why does a frequency ranking need an explicit tie-breaker?
- How should negative values behave when counts tie?

## Example Behavior
`top_k_frequent([1, 1, 1, 2, 2, 3], 2)` → `[1, 2]`; `top_k_frequent([4, 4, 5, 5, 3], 2)` → `[4, 5]`.

*Source: gauntlex/08-problem-solving/109-interval-merge/README.md*

### 109 — Unify Time Ranges

## Description
Intervals may overlap or share an endpoint. Combine them into the smallest sorted collection of disjoint closed intervals.

## Requirements
- Implement `merge_intervals(intervals)` in `starter/solution.py`.
- Each input interval is `[start, end]` with integer endpoints and `start <= end`.
- Merge intervals that overlap or touch at an endpoint.
- Return the resulting intervals sorted by starting point.
- Return `[]` for empty input and do not mutate caller-owned intervals.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- What changes after intervals are ordered by their starts?
- Why should `[1, 3]` and `[3, 5]` combine?

## Example Behavior
`merge_intervals([[1, 3], [2, 6], [8, 10], [10, 12]])` → `[[1, 6], [8, 12]]`.

*Source: gauntlex/08-problem-solving/110-interval-insert/README.md*

### 110 — Add a New Range

## Description
Insert one new closed interval into an already sorted, nonoverlapping collection, merging any ranges it overlaps or touches.

## Requirements
- Implement `insert_interval(intervals, new_interval)` in `starter/solution.py`.
- Assume `intervals` is sorted and contains nonoverlapping closed integer intervals.
- Insert `new_interval` in its correct position.
- Merge any overlapping or endpoint-touching ranges.
- Return sorted nonoverlapping intervals without modifying inputs.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Which existing intervals lie completely before the new interval?
- How do overlapping ranges affect the new interval's boundaries?

## Example Behavior
`insert_interval([[1, 3], [6, 9]], [2, 5])` → `[[1, 5], [6, 9]]`; `insert_interval([], [2, 4])` → `[[2, 4]]`.

*Source: gauntlex/08-problem-solving/111-valid-sudoku/README.md*

### 111 — Sudoku Constraints

## Description
Check whether the currently filled cells in a Sudoku board obey the puzzle's uniqueness rules. Do not attempt to solve the board.

## Requirements
- Implement `valid_sudoku(board)` in `starter/solution.py`.
- Assume a 9-by-9 grid containing digits `'1'` through `'9'` and `'.'` for empty cells.
- Return `True` only if each row, column, and 3-by-3 box contains no repeated filled digit.
- Ignore `'.'` cells; the board need not be complete or solvable.
- Do not modify the board.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why must each filled cell satisfy three different regions?
- Does an unfinished board necessarily violate the rules?

## Example Behavior
A board containing only `'.'` cells returns `True`; repeating `'5'` in one row returns `False`.

*Source: gauntlex/08-problem-solving/112-flood-fill/README.md*

### 112 — Recolor a Region

## Description
Recolor the connected area containing a starting pixel without changing disconnected pixels of the same color.

## Requirements
- Implement `flood_fill(image, sr, sc, color)` in `starter/solution.py`.
- Assume a nonempty rectangular 2D integer image and valid coordinates `(sr, sc)`.
- Find all cells connected to the starting cell in the four cardinal directions that share its original color.
- Return a new image with only that region changed to `color`.
- Do not mutate the input; handle replacement with the original color.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why does diagonal contact not establish connectivity?
- How can already visited cells be distinguished from unvisited ones?

## Example Behavior
`flood_fill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)` → `[[2, 2, 2], [2, 2, 0], [2, 0, 1]]`.

*Source: gauntlex/08-problem-solving/113-islands/README.md*

### 113 — Count the Islands

## Description
A land region is a group of `'1'` cells connected horizontally or vertically. Count the number of separate regions in a grid.

## Requirements
- Implement `count_islands(grid)` in `starter/solution.py`.
- Assume a rectangular grid of `'0'` and `'1'` strings.
- Count distinct four-directionally connected land regions.
- Do not connect cells diagonally.
- Return `0` for an empty grid and do not mutate the input.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- How can one discovered region be counted only once?
- Why do diagonal neighbors remain separate islands?

## Example Behavior
`count_islands([['1', '1', '0'], ['0', '1', '0'], ['0', '0', '1']])` → `2`; `count_islands([])` → `0`.

*Source: gauntlex/08-problem-solving/114-bfs-shortest-path/README.md*

### 114 — Shortest Route

## Description
Find a route with the fewest edges between two graph nodes. When multiple shortest routes exist, neighbor-list order determines the selected route.

## Requirements
- Implement `shortest_path(graph, start, goal)` in `starter/solution.py`.
- Accept a graph mapping nodes to lists of neighbors; interpret edges as specified by the adjacency lists.
- Return a list of nodes from `start` to `goal`, including both endpoints.
- Return `[]` when the goal is unreachable.
- Choose among equal-length paths by exploring neighbors in listed order.
- Do not mutate the graph.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why does exploring paths by number of edges find a shortest route?
- How does neighbor order break ties?

## Example Behavior
`shortest_path({'A': ['B', 'C'], 'B': ['D'], 'C': ['D'], 'D': []}, 'A', 'D')` → `['A', 'B', 'D']`.

*Source: gauntlex/08-problem-solving/115-cycle-detection/README.md*

### 115 — Detect a Loop

## Description
A directed graph contains a cycle if a path of outgoing edges can return to a node already on that same active path.

## Requirements
- Implement `has_cycle(graph)` in `starter/solution.py`.
- Accept a dictionary mapping nodes to lists of outgoing neighbors.
- Return `True` if any directed cycle exists and `False` otherwise.
- Treat neighbor nodes absent from the dictionary as nodes with no outgoing edges.
- Do not mutate the graph.
- Return the result without printing or reading input. Use Python's standard library only.

## Tips
- Why is visiting a node from an earlier completed branch not enough to prove a cycle?
- How does a self-loop differ from a dead end?

## Example Behavior
`has_cycle({'a': ['b'], 'b': ['c'], 'c': ['a']})` → `True`; `has_cycle({'a': ['b'], 'b': []})` → `False`.

---

## Validation

*Source: gauntlex/09-validation/116-dedupe-normalized/README.md*

### 116 — Distinct After Normalization

## Description
Clean strings consistently before deciding which values are duplicates. Keep only meaningful normalized values in their original first-appearance order.

## Requirements
- Implement `dedupe_normalized(items)` in `starter/solution.py`.
- Trim surrounding whitespace and apply Unicode casefolding to each string.
- Discard values that become empty after trimming.
- Keep only the first occurrence of each normalized value.
- Return a new list without modifying `items`.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why must normalization happen before duplicate detection?
- How can casefolding differ from preserving the original spelling?

## Example Behavior
`dedupe_normalized(['  Ada ', 'ada', 'BOB', 'bob', '  '])` → `['ada', 'bob']`; `dedupe_normalized([])` → `[]`.

*Source: gauntlex/09-validation/117-parse-boolean/README.md*

### 117 — Interpret a Boolean

## Description
A configuration value may express yes or no using several text forms. Convert recognized forms to Boolean values and reject unsupported tokens.

## Requirements
- Implement `parse_boolean(text)` in `starter/solution.py`.
- Ignore surrounding whitespace and letter case.
- Return `True` for `true`, `yes`, or `1`.
- Return `False` for `false`, `no`, or `0`.
- Raise `ValueError` for every other string, including an empty value.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why should an unknown token not silently become `False`?
- Consider uppercase words and spaces around input.

## Example Behavior
`parse_boolean(' YES ')` → `True`; `parse_boolean('No')` → `False`; `parse_boolean('maybe')` raises `ValueError`.

*Source: gauntlex/09-validation/118-clamp/README.md*

### 118 — Stay Within Bounds

## Description
Constrain a number to a specified inclusive interval. Values outside the interval should be brought to the nearest boundary, while invalid bounds must be rejected.

## Requirements
- Implement `clamp(value, low, high)` in `starter/solution.py`.
- Accept numeric `value`, `low`, and `high` arguments.
- Return `low` if the value is below it, or `high` if above it.
- Return the original value when it is already within the inclusive interval.
- Raise `ValueError` when `low > high`.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- How do the three possible positions relative to an interval differ?
- What happens when the two bounds are equal?

## Example Behavior
`clamp(12, 0, 10)` → `10`; `clamp(-3, 0, 10)` → `0`.

*Source: gauntlex/09-validation/119-normalize-phone/README.md*

### 119 — Telephone Canonical Form

## Description
Remove permitted visual separators from a telephone number without silently accepting invalid symbols. Preserve a plus sign only when it indicates an international prefix.

## Requirements
- Implement `normalize_phone(text)` in `starter/solution.py`.
- Remove spaces, hyphens, and parentheses.
- Preserve an optional `+` only at the beginning of the normalized number.
- Require at least one digit and reject every remaining character that is not a digit.
- Raise `ValueError` for invalid input.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why must a plus sign be checked for its position?
- Can removing formatting characters hide an invalid symbol?

## Example Behavior
`normalize_phone('+1 (555) 123-4567')` → `'+15551234567'`; `normalize_phone('080-123 456')` → `'080123456'`.

*Source: gauntlex/09-validation/120-validate-password/README.md*

### 120 — Password Rules

## Description
A password validator must check several independent conditions. Determine whether a candidate meets the required minimum length and ASCII character classes.

## Requirements
- Implement `validate_password(text)` in `starter/solution.py`.
- Return a Boolean for the supplied string.
- Require at least eight characters.
- Require at least one ASCII uppercase letter (`A`–`Z`), one ASCII lowercase letter (`a`–`z`), and one ASCII digit (`0`–`9`).
- Return `False` when any condition is missing.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why can a long password still be invalid?
- How are ASCII letters different from arbitrary Unicode letters?

## Example Behavior
`validate_password('Abcdefg1')` → `True`; `validate_password('abcdefg1')` → `False`.

*Source: gauntlex/09-validation/121-parse-query/README.md*

### 121 — Read URL Parameters

## Description
A URL query string can contain encoded characters, blank values, and repeated names. Parse it into a mapping where later occurrences replace earlier values.

## Requirements
- Implement `parse_query(text)` in `starter/solution.py`.
- Return a dictionary of decoded parameter names and values.
- Decode percent escapes and interpret `+` as a space.
- Keep blank values.
- For repeated keys, retain the last decoded value.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why does `%2B` differ from a literal plus sign?
- What should happen when a name occurs more than once?

## Example Behavior
`parse_query('a=1&b=two+words&a=3')` → `{'a': '3', 'b': 'two words'}`; `parse_query('x=&y=%2B')` → `{'x': '', 'y': '+'}`.

*Source: gauntlex/09-validation/122-build-query/README.md*

### 122 — Write URL Parameters

## Description
Convert a mapping of text keys and values into a predictable HTTP query string. The result must not depend on the mapping's insertion order.

## Requirements
- Implement `build_query(params)` in `starter/solution.py`.
- Accept a mapping of string keys to string values.
- Sort keys alphabetically before encoding.
- Percent-encode query components using plus signs for spaces.
- Join encoded pairs with `&`, and return an empty string for an empty mapping.
- Do not modify `params`.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why does sorting keys make output reproducible?
- Which characters require encoding inside query components?

## Example Behavior
`build_query({'b': 'two words', 'a': '1'})` → `'a=1&b=two+words'`; `build_query({})` → `''`.

*Source: gauntlex/09-validation/123-validate-ipv4/README.md*

### 123 — Four Network Octets

## Description
An IPv4 address has four dotted decimal components, but not every four-part numeric string is valid. Validate both the structure and canonical spelling.

## Requirements
- Implement `valid_ipv4(text)` in `starter/solution.py`.
- Return `True` only for exactly four dot-separated decimal components.
- Each component must contain ASCII digits and represent a number from `0` through `255`.
- Reject leading zeros except when a component is exactly `0`.
- Reject whitespace, signs, missing components, and extra components.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why are numeric range checks alone insufficient?
- What distinguishes `0` from `00` in canonical notation?

## Example Behavior
`valid_ipv4('192.168.0.1')` → `True`; `valid_ipv4('256.1.1.1')` → `False`.

*Source: gauntlex/09-validation/124-parse-log-line/README.md*

### 124 — Structured Log Entry

## Description
A log entry combines a severity, a date, and a message. Parse these fields without losing separators that belong to the message itself.

## Requirements
- Implement `parse_log_line(line)` in `starter/solution.py`.
- Accept records formatted `LEVEL
- YYYY-MM-DD
- MESSAGE`.
- Require `LEVEL` to be exactly `INFO`, `WARN`, or `ERROR`.
- Require a real calendar date in the specified format.
- Allow the message to contain additional `
- ` characters.
- Return a dictionary with `level`, `date`, and `message`, or `None` for invalid input.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why is splitting at every delimiter unsafe for the message?
- Why must a date be checked beyond its visual pattern?

## Example Behavior
`parse_log_line('INFO|2024-02-29|Started|ok')` → `{'level': 'INFO', 'date': '2024-02-29', 'message': 'Started|ok'}`; `parse_log_line('DEBUG|2024-01-01|x')` → `None`.

*Source: gauntlex/09-validation/125-count-log-levels/README.md*

### 125 — Log Severity Summary

## Description
Summarize the severity of valid structured log records while ignoring malformed lines. The output must include every supported severity even when its count is zero.

## Requirements
- Implement `count_log_levels(lines)` in `starter/solution.py`.
- Accept a list of log lines formatted `LEVEL
- YYYY-MM-DD
- MESSAGE`.
- Count only valid `INFO`, `WARN`, and `ERROR` records.
- Ignore malformed lines, including invalid calendar dates.
- Return a dictionary containing all three level names with integer counts.
- Do not modify `lines`.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why is checking the prefix alone insufficient to validate a record?
- What should the result contain for an empty list?

## Example Behavior
`count_log_levels(['INFO|2024-01-01|ok', 'WARN|2024-01-02|slow', 'INFO|2024-01-03|ok', 'bad'])` → `{'INFO': 2, 'WARN': 1, 'ERROR': 0}`.

*Source: gauntlex/09-validation/126-chunk-text/README.md*

### 126 — Text Segments

## Description
Divide a string into consecutive pieces of a requested maximum length. Preserve every character and the original order.

## Requirements
- Implement `chunk_text(text, size)` in `starter/solution.py`.
- Return a list of consecutive substrings of length at most `size`.
- Require `size` to be a positive integer; raise `ValueError` otherwise.
- Allow the final piece to be shorter than the others.
- Return `[]` for empty text.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- What happens when the text length is not a multiple of the chunk size?
- Why must zero or negative chunk lengths be rejected?

## Example Behavior
`chunk_text('abcdef', 2)` → `['ab', 'cd', 'ef']`; `chunk_text('abc', 5)` → `['abc']`.

*Source: gauntlex/09-validation/127-parse-env/README.md*

### 127 — Configuration Assignments

## Description
Read configuration assignments from multiline text. Ignore blank and comment lines, normalize surrounding whitespace, and allow later assignments to replace earlier ones.

## Requirements
- Implement `parse_env(text)` in `starter/solution.py`.
- Interpret noncomment lines as `KEY=VALUE` assignments.
- Ignore blank lines and lines whose first nonspace character is `#`.
- Trim whitespace around keys and values.
- Split each assignment at its first `=` so the value may contain additional equals signs.
- Raise `ValueError` for any noncomment, nonblank line without `=`.
- Keep the last value for repeated keys.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why should only the first equals sign separate the key and value?
- What makes a line a comment rather than an assignment?

## Example Behavior
`parse_env('A=1\nB = hello world\n# comment\nA=2')` → `{'A': '2', 'B': 'hello world'}`.

*Source: gauntlex/09-validation/128-redact-secrets/README.md*

### 128 — Hide Sensitive Tokens

## Description
Hide credential values in text while preserving the original capitalization of their keys. Only explicitly recognized assignment forms should be changed.

## Requirements
- Implement `redact_secrets(text)` in `starter/solution.py`.
- Find case-insensitive occurrences of `password=VALUE` or `token=VALUE`.
- Treat `VALUE` as a nonempty consecutive run of nonwhitespace characters.
- Replace each matched value with `[REDACTED]`.
- Preserve the original spelling and capitalization of each key and all unmatched text.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why should the key's original spelling remain unchanged?
- How do spaces and punctuation affect the end of a credential value?

## Example Behavior
`redact_secrets('token=abc password=123')` → `'token=[REDACTED] password=[REDACTED]'`; `redact_secrets('TOKEN=x')` → `'TOKEN=[REDACTED]'`.

*Source: gauntlex/09-validation/129-normalize-url-path/README.md*

### 129 — Canonical URL Paths

## Description
Normalize a POSIX-style URL path into a stable rooted form. Redundant separators and relative segments should not allow the result to escape above the root.

## Requirements
- Implement `normalize_url_path(path)` in `starter/solution.py`.
- Return a path beginning with `/`.
- Collapse repeated slashes and remove `.` segments.
- Resolve `..` segments by removing a preceding ordinary segment when possible.
- Never navigate above the root.
- Remove a trailing slash unless the result is `/`.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- What should happen when a parent segment appears at the root?
- How do `.` and `..` differ?

## Example Behavior
`normalize_url_path('/a//b/./c/../d')` → `'/a/b/d'`; `normalize_url_path('../../x')` → `'/x'`.

*Source: gauntlex/09-validation/130-safe-filename/README.md*

### 130 — Safe File Labels

## Description
Turn a human-readable ASCII label into a predictable lowercase filename stem by replacing disallowed runs with underscores.

## Requirements
- Implement `safe_filename(text)` in `starter/solution.py`.
- Convert ASCII letters to lowercase.
- Keep lowercase `a`–`z`, digits `0`–`9`, underscores, and hyphens.
- Replace each run of other characters with one underscore.
- Remove leading and trailing underscores.
- Return `'untitled'` when no usable stem remains.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why should consecutive punctuation produce one separator?
- What happens when every input character is disallowed?

## Example Behavior
`safe_filename('My Report (2024)')` → `'my_report_2024'`; `safe_filename('!!!')` → `'untitled'`.

*Source: gauntlex/09-validation/131-parse-duration/README.md*

### 131 — Clock Text to Seconds

## Description
Interpret a duration in hours, minutes, and seconds. Reject malformed text and impossible minute or second values.

## Requirements
- Implement `parse_duration(text)` in `starter/solution.py`.
- Accept `H:MM:SS` with a nonnegative integer hour field.
- Require exactly two digits each for minutes and seconds.
- Require minutes and seconds to be between `00` and `59` inclusive.
- Return the total duration in seconds.
- Raise `ValueError` for invalid notation or out-of-range components.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why must minutes and seconds be bounded independently of hours?
- What is the difference between an invalid format and a valid zero duration?

## Example Behavior
`parse_duration('1:02:03')` → `3723`; `parse_duration('0:00:05')` → `5`.

*Source: gauntlex/09-validation/132-format-duration/README.md*

### 132 — Seconds to Clock Text

## Description
Represent a nonnegative number of seconds in a consistent hours-minutes-seconds format.

## Requirements
- Implement `format_duration(seconds)` in `starter/solution.py`.
- Accept a nonnegative integer duration in seconds.
- Return text formatted as `H:MM:SS`.
- Do not pad the hour field; always use exactly two digits for minutes and seconds.
- Raise `ValueError` for a negative duration.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why must minutes and seconds remain below sixty?
- What happens when the hour count has several digits?

## Example Behavior
`format_duration(3723)` → `'1:02:03'`; `format_duration(0)` → `'0:00:00'`.

*Source: gauntlex/09-validation/133-parse-hex-color/README.md*

### 133 — Decode an RGB Color

## Description
A six-digit hexadecimal color stores red, green, and blue intensities in three adjacent pairs. Validate and decode each channel.

## Requirements
- Implement `parse_hex_color(text)` in `starter/solution.py`.
- Accept exactly `#RRGGBB` where each letter is a hexadecimal digit.
- Reject missing `#`, incorrect lengths, and nonhexadecimal characters with `ValueError`.
- Return three integer channel values between `0` and `255`, in red-green-blue order.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why does each color channel occupy two hexadecimal digits?
- Why should the full input be validated before decoding?

## Example Behavior
`parse_hex_color('#FF8000')` → `[255, 128, 0]`; `parse_hex_color('#000000')` → `[0, 0, 0]`.

*Source: gauntlex/09-validation/134-format-hex-color/README.md*

### 134 — Encode an RGB Color

## Description
Encode red, green, and blue channel values as a canonical uppercase hexadecimal color string.

## Requirements
- Implement `format_hex_color(r, g, b)` in `starter/solution.py`.
- Accept three integer channel values `r`, `g`, and `b`.
- Require every component to lie between `0` and `255`; raise `ValueError` otherwise.
- Return a string in uppercase `#RRGGBB` form.
- Represent each channel with exactly two hexadecimal digits.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why do small channel values still require two digits?
- How does channel order affect the resulting color?

## Example Behavior
`format_hex_color(255, 128, 0)` → `'#FF8000'`; `format_hex_color(0, 0, 0)` → `'#000000'`.

*Source: gauntlex/09-validation/135-normalize-tags/README.md*

### 135 — Clean the Tags

## Description
Normalize comma-separated labels into a unique, ordered collection of meaningful tags.

## Requirements
- Implement `normalize_tags(text)` in `starter/solution.py`.
- Split input text at commas.
- Trim surrounding whitespace and lowercase each tag.
- Discard empty tags after trimming.
- Remove duplicates while retaining the first occurrence of each normalized tag.
- Return a list of tags, or `[]` if none remain.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why must normalization happen before duplicate detection?
- What should consecutive commas contribute?

## Example Behavior
`normalize_tags('Python, python, AI, , ai')` → `['python', 'ai']`; `normalize_tags(' , ')` → `[]`.

*Source: gauntlex/09-validation/136-email-domain/README.md*

### 136 — Domain Extraction

## Description
An email address has a local part and a domain separated by `@`. Extract the domain and normalize its capitalization without changing the local part.

## Requirements
- Implement `email_domain(email)` in `starter/solution.py`.
- Assume the input is a valid email address containing exactly one `@`.
- Return the substring after `@`.
- Convert the returned domain to lowercase.
- Do not include the separator or local part in the result.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Which part of an email address identifies its domain?
- Why should only the extracted domain be normalized?

## Example Behavior
`email_domain('User@Example.COM')` → `'example.com'`; `email_domain('a@sub.example.org')` → `'sub.example.org'`.

*Source: gauntlex/09-validation/137-common-keys/README.md*

### 137 — Shared Dictionary Keys

## Description
Two dictionaries may contain some of the same keys even when their values differ. Find the shared keys and return them in a predictable order.

## Requirements
- Implement `common_keys(a, b)` in `starter/solution.py`.
- Accept two dictionaries with sortable string keys.
- Return a sorted list of keys present in both dictionaries.
- Ignore the values associated with those keys.
- Return `[]` when no keys are shared; do not modify either dictionary.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why should different values not affect whether keys match?
- How does sorting remove dependence on insertion order?

## Example Behavior
`common_keys({'x': 1, 'a': 2}, {'a': 3, 'z': 4})` → `['a']`; `common_keys({}, {'x': 1})` → `[]`.

*Source: gauntlex/09-validation/138-invert-mapping/README.md*

### 138 — Reverse a Relationship

## Description
A dictionary can map several keys to the same value. Reverse that relationship while preserving every original key and its encounter order.

## Requirements
- Implement `invert_mapping(mapping)` in `starter/solution.py`.
- Accept a dictionary mapping strings to strings.
- Return a new dictionary whose keys are the original values.
- Associate each new key with a list of original keys having that value.
- Preserve the original dictionary's key insertion order within each list.
- Return `{}` for an empty mapping.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why might an inverted mapping need lists rather than single values?
- What ordering should be preserved when multiple keys share a value?

## Example Behavior
`invert_mapping({'a': 'x', 'b': 'y', 'c': 'x'})` → `{'x': ['a', 'c'], 'y': ['b']}`.

*Source: gauntlex/09-validation/139-diff-sets/README.md*

### 139 — What Changed?

## Description
Compare an older collection of labels with a newer collection. Report which distinct values were introduced, removed, or kept.

## Requirements
- Implement `set_diff(old, new)` in `starter/solution.py`.
- Accept two collections of strings named `old` and `new`.
- Ignore duplicate occurrences within each collection.
- Return a dictionary with exactly `added`, `removed`, and `shared` keys.
- Each value must be a sorted list of strings.
- `added` contains only new values; `removed` contains only old values; `shared` contains values in both.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why does comparison direction matter?
- How should duplicates affect membership and the result?

## Example Behavior
`set_diff(['a', 'b'], ['b', 'c'])` → `{'added': ['c'], 'removed': ['a'], 'shared': ['b']}`.

*Source: gauntlex/09-validation/140-top-words/README.md*

### 140 — Word Leaderboard

## Description
Extract words from text, count how often each appears, and rank them. Equal-frequency words must be ordered alphabetically.

## Requirements
- Implement `top_words(text, n)` in `starter/solution.py`.
- Assume `n` is a nonnegative integer.
- Recognize words as maximal runs of ASCII letters `a`–`z`, ignoring case.
- Count normalized lowercase words, treating punctuation and other characters as separators.
- Return at most `n` distinct words, ordered by descending frequency and then alphabetically.
- Return `[]` when `n` is zero or no words exist.
- Return the specified value without printing or reading standard input. Use Python's standard library only.

## Tips
- Why must case normalization happen before counting?
- How should equal-frequency words be ordered?
- What separates two ASCII words?

## Example Behavior
`top_words('Red red blue!', 2)` → `['red', 'blue']`; `top_words('b a b a', 1)` → `['a']`.

---

## Cli Tools

*Source: gauntlex/10-cli-tools/141-echo-lines/README.md*

### 141 — Reverse the Stream

## Description
Build a command-line program that reverses the order of input lines. The contents of each line must remain unchanged, including blank lines.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read every line from standard input.
- Print the lines in reverse order, preserving each line's text.
- Use exactly one newline after each output line.
- Produce no output when input is empty.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why must all lines be known before the first output line can be chosen?
- How should a blank line behave?

## Example Input and Output
Input: "red\nblue\ngreen\n"

Expected output: "green\nblue\nred\n"

Input: ""

Expected output: ""

*Source: gauntlex/10-cli-tools/142-number-lines/README.md*

### 142 — Line Numbers

## Description
Give every input line a sequential label so that a reader can refer to its position. Blank lines count as lines too.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read text lines from standard input.
- Prefix each line with its one-based line number, a colon, and one space.
- Preserve the content of each line, including empty lines.
- Produce no output for empty input.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why does the first line receive label `1` rather than `0`?
- How can a blank line still receive a label?

## Example Input and Output
Input: "a\nb\n"

Expected output: "1: a\n2: b\n"

Input: "\n"

Expected output: "1: \n"

*Source: gauntlex/10-cli-tools/143-grep-literal/README.md*

### 143 — Find Matching Lines

## Description
Create a simple literal search tool that filters a stream of text lines by a case-sensitive substring.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Treat the first input line as the literal search string.
- Inspect every remaining input line for that exact substring.
- Print matching lines in their original order, once per matching line.
- Do not print the search string itself or lines without a match.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why is a substring match different from a whole-word match?
- What does case-sensitive matching imply?

## Example Input and Output
Input: "cat\ncatapult\ndog\nbobcat\n"

Expected output: "catapult\nbobcat\n"

Input: "z\nabc\n"

Expected output: ""

*Source: gauntlex/10-cli-tools/144-head-lines/README.md*

### 144 — First Lines Only

## Description
Build a tool that selects the earliest requested lines from a text stream and discards the remainder.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read a nonnegative integer `N` from the first line.
- Print at most the first `N` subsequent lines, preserving their order and content.
- Print nothing when `N` is zero.
- If fewer than `N` lines remain, print all of them.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- How does the first line differ from the lines being selected?
- What happens when the requested limit exceeds available data?

## Example Input and Output
Input: "2\na\nb\nc\n"

Expected output: "a\nb\n"

Input: "0\na\n"

Expected output: ""

*Source: gauntlex/10-cli-tools/145-tail-lines/README.md*

### 145 — Last Lines Only

## Description
Build a tool that selects the final requested lines of a stream without reversing their order.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read a nonnegative integer `N` from the first line.
- Print at most the last `N` subsequent lines in their original order.
- Print nothing when `N` is zero.
- If fewer than `N` lines remain, print all of them.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why is choosing the last lines different from reversing the stream?
- What happens when the requested limit is larger than the input?

## Example Input and Output
Input: "2\na\nb\nc\n"

Expected output: "b\nc\n"

Input: "0\na\n"

Expected output: ""

*Source: gauntlex/10-cli-tools/146-sort-lines/README.md*

### 146 — Order the Lines

## Description
Rearrange complete text lines using case-sensitive lexical order while preserving repeated entries.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read all lines from standard input.
- Sort lines lexicographically by Unicode code point.
- Print each sorted line on its own line, preserving duplicates.
- Produce no output for empty input.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why can uppercase and lowercase letters sort differently?
- Why should duplicate lines remain in the output?

## Example Input and Output
Input: "pear\napple\npear\n"

Expected output: "apple\npear\npear\n"

Input: ""

Expected output: ""

*Source: gauntlex/10-cli-tools/147-unique-adjacent/README.md*

### 147 — Collapse Repeated Lines

## Description
Remove duplicates only when they appear consecutively. A value that returns after a different line must appear again.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read all lines from standard input.
- Keep only the first line in each consecutive run of identical lines.
- Preserve the original order of retained lines.
- Treat blank lines as ordinary lines for comparison.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why is this different from removing every duplicate globally?
- What happens when an earlier line reappears after another line?

## Example Input and Output
Input: "a\na\nb\na\na\n"

Expected output: "a\nb\na\n"

Input: "\n\nx\n"

Expected output: "\nx\n"

*Source: gauntlex/10-cli-tools/148-count-occurrences/README.md*

### 148 — Count Matching Lines

## Description
Count the number of input lines containing a literal search string, rather than the total number of occurrences.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Treat the first input line as the case-sensitive search string.
- Count each subsequent line once if it contains the search string as a substring.
- Print the integer count followed by a newline, including `0` when no lines match.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why must a line with several matches count only once?
- How does literal matching differ from regular-expression matching?

## Example Input and Output
Input: "cat\ncat\ndog\nbobcat\n"

Expected output: "2\n"

Input: "x\na\nb\n"

Expected output: "0\n"

*Source: gauntlex/10-cli-tools/149-sum-columns/README.md*

### 149 — Sum the Stream

## Description
Read integer values spread across multiple lines and produce one total for the entire input stream.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read zero or more lines containing whitespace-separated integers.
- Include every integer on every line in the total.
- Print the sum as a single integer followed by a newline.
- Print `0` for an empty input stream.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why should the number of lines not affect the calculation?
- What is the sum of no values?

## Example Input and Output
Input: "1 2\n3 4\n"

Expected output: "10\n"

Input: ""

Expected output: "0\n"

*Source: gauntlex/10-cli-tools/150-csv-to-tsv/README.md*

### 150 — CSV to Tabs

## Description
Convert comma-separated records into tab-separated records without mistaking commas inside quoted fields for separators.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read CSV records from standard input.
- Interpret quoted commas and escaped double quotation marks using CSV rules.
- Output the same fields separated by tabs, one record per line.
- Assume fields contain no tabs or embedded newlines.
- Produce no extra messages or headers.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why is replacing every comma directly unsafe?
- How are quotation marks inside quoted CSV fields represented?

## Example Input and Output
Input: "name,age\nAda,20\n"

Expected output: "name\tage\nAda\t20\n"

Input: "\"a,b\",c\n"

Expected output: "a,b\tc\n"

*Source: gauntlex/10-cli-tools/151-json-pretty/README.md*

### 151 — Readable JSON

## Description
Turn compact JSON into a human-readable representation while preserving its data. The output must use predictable indentation and key ordering.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read one valid JSON value from standard input.
- Print valid JSON with object keys sorted alphabetically and indentation of two spaces.
- End the output with exactly one newline.
- Support JSON arrays, objects, and scalar values.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why can two differently formatted JSON strings represent the same value?
- What makes output formatting predictable?

## Example Input and Output
Input: "{\"b\":2,\"a\":1}\n"

Expected output: "{\n  \"a\": 1,\n  \"b\": 2\n}\n"

Input: "[1,2]\n"

Expected output: "[\n  1,\n  2\n]\n"

*Source: gauntlex/10-cli-tools/152-json-lines/README.md*

### 152 — Compact JSON Stream

## Description
Process a stream of independent JSON values and output one canonical compact representation for each nonblank record.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read one valid JSON value per nonempty input line.
- Ignore blank input lines.
- Print one compact JSON value per record with object keys sorted alphabetically.
- Do not add unnecessary spaces between JSON separators.
- Preserve the order of records.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why must each line be parsed independently?
- What distinguishes an empty line from a JSON string containing empty text?

## Example Input and Output
Input: "{\"b\":2,\"a\":1}\n\n[1, 2]\n"

Expected output: "{\"a\":1,\"b\":2}\n[1,2]\n"

Input: ""

Expected output: ""

*Source: gauntlex/10-cli-tools/153-jsonl-count/README.md*

### 153 — Count Active Records

## Description
Count JSON records that explicitly declare themselves active. Numeric values that resemble Boolean values must not be mistaken for true.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read valid JSON objects, one per nonempty line.
- Count only objects whose `active` key has the Boolean value `true`.
- Do not count numeric `1`, strings, missing keys, or Boolean `false`.
- Print the count as an integer followed by a newline.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why is equality alone potentially misleading when comparing Booleans and integers in Python?
- What happens when a record lacks the key?

## Example Input and Output
Input: "{\"active\":true}\n{\"active\":1}\n{\"active\":false}\n"

Expected output: "1\n"

Input: ""

Expected output: "0\n"

*Source: gauntlex/10-cli-tools/154-jsonl-select/README.md*

### 154 — Extract JSON Fields

## Description
Extract one named field from a stream of JSON objects. Missing fields are skipped, but explicitly null fields must remain in the output.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read the desired key name from the first input line.
- Treat subsequent nonempty lines as valid JSON objects.
- Print the value for the named key as compact JSON, one line per matching object.
- Skip objects without the key, but print `null` when the key is present with a null value.
- Preserve record order.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why is a missing key different from a key containing null?
- Why should strings be printed as JSON strings rather than raw text?

## Example Input and Output
Input: "name\n{\"name\":\"Ada\",\"age\":3}\n{\"age\":4}\n{\"name\":null}\n"

Expected output: "\"Ada\"\nnull\n"

Input: "x\n{}\n"

Expected output: ""

*Source: gauntlex/10-cli-tools/155-csv-row-count/README.md*

### 155 — Count CSV Records

## Description
Count data records in a CSV stream while excluding the header row. The result should reflect CSV records, not merely arbitrary text lines.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read CSV input with a header and zero or more data records.
- Do not include the header in the count.
- Print the number of data records followed by a newline.
- Print `0` for empty input or a header-only file.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why does a header not count as a data record?
- What happens when no data rows follow the header?

## Example Input and Output
Input: "name,age\nAda,20\nBob,30\n"

Expected output: "2\n"

Input: "name\n"

Expected output: "0\n"

*Source: gauntlex/10-cli-tools/156-csv-select-column/README.md*

### 156 — Extract a CSV Column

## Description
Select a CSV column by its header name rather than by a fixed numeric position. Preserve the order of data rows.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read the target column name from the first input line.
- Treat the remaining input as CSV with a header row.
- Assume the named column exists and fields contain no embedded newlines.
- Print that column's value for each data row on its own line, in original row order.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why should the header determine which field is selected?
- How does an empty field affect the output?

## Example Input and Output
Input: "name\nname,age\nAda,20\nBob,30\n"

Expected output: "Ada\nBob\n"

Input: "age\nname,age\nAda,20\n"

Expected output: "20\n"

*Source: gauntlex/10-cli-tools/157-csv-filter-equal/README.md*

### 157 — Filter CSV Records

## Description
Filter CSV data records using an exact field comparison and emit each match as a compact JSON object.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read the column name and exact target value from the first two input lines.
- Treat the remaining input as CSV with a header row.
- Select only records whose named field exactly equals the target.
- Print matching records as compact JSON objects with alphabetically sorted keys, one per line.
- Preserve input record order and print nothing when there are no matches.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why should capitalization and whitespace matter for an exact match?
- How can the header provide JSON field names?

## Example Input and Output
Input: "city\nLagos\nname,city\nAda,Lagos\nBob,Abuja\n"

Expected output: "{\"city\":\"Lagos\",\"name\":\"Ada\"}\n"

Input: "status\nok\nname,status\nx,no\n"

Expected output: ""

*Source: gauntlex/10-cli-tools/158-word-count-cli/README.md*

### 158 — Three Text Measures

## Description
Report three different measurements of an input stream: logical lines, whitespace-separated words, and Unicode characters.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read all text from standard input.
- Print the number of lines as determined by Python's `splitlines()` behavior.
- Print the number of whitespace-separated words.
- Print the total number of Unicode characters, including spaces and newline characters.
- Output the three integers on separate lines, each ending with a newline.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why do spaces and line breaks contribute to the character count?
- How does the number of words differ from the number of lines?

## Example Input and Output
Input: "a b\nc\n"

Expected output: "2\n3\n6\n"

Input: ""

Expected output: "0\n0\n0\n"

*Source: gauntlex/10-cli-tools/159-histogram/README.md*

### 159 — Value Histogram

## Description
Count how often each nonnegative integer occurs in a stream, then display a frequency report sorted by value.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read whitespace-separated nonnegative integers from standard input.
- Count occurrences of each distinct value.
- Print one line per distinct value in ascending numeric order, formatted `VALUE: COUNT`.
- Produce no output for empty input.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why does sorting by value differ from sorting by frequency?
- How should repeated values affect the count?

## Example Input and Output
Input: "3 1 3 2 1 3\n"

Expected output: "1: 2\n2: 1\n3: 3\n"

Input: ""

Expected output: ""

*Source: gauntlex/10-cli-tools/160-stats-cli/README.md*

### 160 — Numeric Stream Summary

## Description
Summarize an integer stream using its count, total, minimum, and maximum. Empty input has a deliberately shorter report.

## Requirements
- Implement the program in `starter/main.py` using standard input and standard output.
- Read whitespace-separated integers from standard input.
- For nonempty input, print four lines in this exact order: `count=N`, `sum=S`, `min=M`, `max=X`.
- For empty input, print only `count=0` and `sum=0`.
- End every printed line with a newline and do not print additional text.
- Use Python's standard library only. Do not print prompts, debugging output, or explanations.
- Match the required output exactly, including newline characters.

## Tips
- Why are minimum and maximum undefined for an empty stream?
- How should negative and repeated values affect each statistic?

## Example Input and Output
Input: "3 1 2\n"

Expected output: "count=3\nsum=6\nmin=1\nmax=3\n"

Input: ""

Expected output: "count=0\nsum=0\n"

---

## Data Analysis

*Source: gauntlex/11-data-analysis/161-median/README.md*

### 161 — The Middle Value

## Description
The median describes the center of a dataset after its observations are arranged in numeric order. The rule differs depending on whether the dataset has an odd or even number of values.

## Requirements
- Implement `median(values)` in `starter/solution.py`.
- Assume `values` is a nonempty list of numbers.
- Return the middle value for an odd number of observations.
- For an even number of observations, return the arithmetic mean of the two middle values.
- Do not change the input order or mutate the list.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why is the original order irrelevant to the median?
- What happens when there are two central observations?

## Example Behavior
`median([3, 1, 2])` → `2`

`median([4, 1, 3, 2])` → `2.5`

*Source: gauntlex/11-data-analysis/162-mode/README.md*

### 162 — Most Frequent Observation

## Description
Find the most frequently observed integer in a dataset. When multiple integers are equally common, choose a deterministic answer.

## Requirements
- Implement `mode(values)` in `starter/solution.py`.
- Assume a nonempty list of integers.
- Return the value with the highest occurrence count.
- When several values tie for the highest count, return the smallest integer.
- Leave the input unchanged.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why is the most frequent value not necessarily the largest?
- What should happen when all observations are distinct?

## Example Behavior
`mode([2, 3, 2, 3])` → `2`

`mode([5, 5, 1])` → `5`

*Source: gauntlex/11-data-analysis/163-variance/README.md*

### 163 — Spread Around the Mean

## Description
Population variance measures how widely observations differ from their average. It uses squared deviations and divides by the number of observations.

## Requirements
- Implement `population_variance(values)` in `starter/solution.py`.
- Assume a nonempty list of numbers representing an entire population.
- Calculate the arithmetic mean and the average squared deviation from it.
- Use the population divisor `N`, not the sample divisor `N - 1`.
- Return the variance without modifying the data.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why are deviations squared rather than simply added?
- What happens when every value equals the mean?

## Example Behavior
`population_variance([1, 2, 3])` → `0.6666666666666666`

`population_variance([5, 5, 5])` → `0`

*Source: gauntlex/11-data-analysis/164-standard-deviation/README.md*

### 164 — Standard Spread

## Description
Population standard deviation describes the spread of values in the original units of the dataset rather than squared units.

## Requirements
- Implement `population_stddev(values)` in `starter/solution.py`.
- Assume a nonempty list of numeric observations.
- Return the square root of the population variance.
- Use the population divisor `N` for variance, not `N - 1`.
- Return zero when all values are equal; do not mutate the input.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- How is standard deviation related to variance?
- Why does taking a square root change the units?

## Example Behavior
`population_stddev([1, 1, 1])` → `0`

`population_stddev([3, 4, 5])` → `0.816496580927726`

*Source: gauntlex/11-data-analysis/165-percentile-nearest/README.md*

### 165 — Nearest-Rank Percentile

## Description
A percentile selects an observation at a specified position in sorted data. Use the nearest-rank definition rather than interpolation.

## Requirements
- Implement `nearest_rank_percentile(values, p)` in `starter/solution.py`.
- Assume `values` is nonempty and `p` is an integer from `1` through `100`.
- Sort the values conceptually in ascending order without mutating the input.
- Choose the one-based rank `ceil(p * N / 100)` for `N` observations.
- Return the value at that rank.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why does the percentile rank start at one rather than zero?
- What does the 100th percentile select?

## Example Behavior
`nearest_rank_percentile([10, 20, 30, 40], 50)` → `20`

`nearest_rank_percentile([10, 20, 30, 40], 100)` → `40`

*Source: gauntlex/11-data-analysis/166-moving-average/README.md*

### 166 — Sliding Average

## Description
A moving average smooths a sequence by averaging every consecutive group of a fixed size. Each neighboring group overlaps the previous one.

## Requirements
- Implement `moving_average(values, k)` in `starter/solution.py`.
- Assume `k` is a positive integer.
- Return one arithmetic average for each contiguous window of `k` values.
- Preserve the left-to-right order of windows.
- Return `[]` if `k` exceeds the number of observations.
- Do not mutate the input.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- How many windows fit in a list of length `N`?
- What changes when the window moves one position?

## Example Behavior
`moving_average([1, 2, 3, 4], 2)` → `[1.5, 2.5, 3.5]`

`moving_average([1, 2], 3)` → `[]`

*Source: gauntlex/11-data-analysis/167-normalize-minmax/README.md*

### 167 — Scale to Unit Range

## Description
Min-max normalization rescales numeric observations relative to their smallest and largest values, preserving their order.

## Requirements
- Implement `minmax_normalize(values)` in `starter/solution.py`.
- Return a new list with each value scaled into the inclusive range `[0, 1]`.
- Map the minimum to `0` and the maximum to `1` using the range between them.
- When every value is equal, return zeros for every position.
- Return `[]` for empty input without mutating it.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why does a constant dataset need a special case?
- What happens to values between the minimum and maximum?

## Example Behavior
`minmax_normalize([2, 4, 6])` → `[0, 0.5, 1]`

`minmax_normalize([3, 3])` → `[0, 0]`

*Source: gauntlex/11-data-analysis/168-dot-product/README.md*

### 168 — Multiply and Accumulate

## Description
The dot product combines two numeric vectors by pairing corresponding positions and adding their products.

## Requirements
- Implement `dot_product(a, b)` in `starter/solution.py`.
- Assume `a` and `b` are equal-length numeric lists.
- Multiply the elements at matching indices and sum those products.
- Return a single numeric result.
- Return `0` for two empty vectors; do not mutate either list.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why must vector elements be paired by position?
- How does the empty case affect the total?

## Example Behavior
`dot_product([1, 2, 3], [4, 5, 6])` → `32`

`dot_product([], [])` → `0`

*Source: gauntlex/11-data-analysis/169-euclidean-distance/README.md*

### 169 — Distance in Many Dimensions

## Description
Generalize the familiar straight-line distance between two points to vectors of any matching dimension.

## Requirements
- Implement `euclidean_distance(a, b)` in `starter/solution.py`.
- Assume two equal-length numeric vectors.
- Return the square root of the sum of squared coordinate differences.
- Return `0` for two empty vectors.
- Do not modify either input.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- How does two-dimensional distance extend to more coordinates?
- Why does changing the order of the vectors not change the distance?

## Example Behavior
`euclidean_distance([0, 0], [3, 4])` → `5`

`euclidean_distance([], [])` → `0`

*Source: gauntlex/11-data-analysis/170-matrix-add/README.md*

### 170 — Add Two Grids

## Description
Matrix addition combines two grids of identical shape by adding entries at matching positions.

## Requirements
- Implement `matrix_add(a, b)` in `starter/solution.py`.
- Assume two equal-shaped rectangular numeric matrices.
- Return a new matrix whose entries are sums of corresponding input entries.
- Return `[]` when both matrices are empty.
- Preserve the structure and contents of both input matrices.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why must the two shapes match?
- What should happen to an empty matrix?

## Example Behavior
`matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]])` → `[[6, 8], [10, 12]]`

`matrix_add([], [])` → `[]`

*Source: gauntlex/11-data-analysis/171-matrix-multiply/README.md*

### 171 — Matrix Composition

## Description
Matrix multiplication combines rows from one matrix with columns from another. The resulting grid has dimensions determined by the outer dimensions of the inputs.

## Requirements
- Implement `matrix_multiply(a, b)` in `starter/solution.py`.
- Assume `a` and `b` are nonempty, rectangular, numeric matrices with compatible dimensions.
- Return a new matrix representing the product `a * b`.
- Each output entry combines one row of `a` with one column of `b`.
- Do not modify either input matrix.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why must the number of columns in the first matrix match the number of rows in the second?
- How is multiplication different from elementwise addition?

## Example Behavior
`matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])` → `[[19, 22], [43, 50]]`

`matrix_multiply([[2]], [[3]])` → `[[6]]`

*Source: gauntlex/11-data-analysis/172-bucket-count/README.md*

### 172 — Build a Histogram

## Description
A fixed-width histogram groups observations into adjacent numeric intervals. Count values that fall into each interval and ignore those outside the supported range.

## Requirements
- Implement `bucket_count(values, width, bucket_count)` in `starter/solution.py`.
- Assume `width > 0` and `bucket_count >= 0`.
- Create `bucket_count` half-open buckets beginning at zero, each of width `width`.
- Count values in `[0, width)`, `[width, 2 * width)`, and subsequent intervals.
- Ignore values below zero or at least `width * bucket_count`.
- Return the counts in bucket order.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why does a value exactly on a boundary belong to the bucket on its right?
- What should happen when no buckets are requested?

## Example Behavior
`bucket_count([0, 1, 2, 3, 4, 5], 2, 3)` → `[2, 2, 2]`

`bucket_count([-1, 0, 10], 5, 2)` → `[1, 0]`

*Source: gauntlex/11-data-analysis/173-pearson-correlation/README.md*

### 173 — Linear Relationship

## Description
Pearson correlation measures the direction and strength of a linear relationship between two paired numeric datasets.

## Requirements
- Implement `pearson_correlation(a, b)` in `starter/solution.py`.
- Assume two equal-length numeric lists containing at least two observations.
- Return the Pearson correlation coefficient of the paired observations.
- Return `None` if either dataset has zero variance.
- Do not mutate either input.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why does a constant dataset prevent correlation from being calculated?
- What do positive and negative correlation indicate?

## Example Behavior
`pearson_correlation([1, 2, 3], [2, 4, 6])` → `1`

`pearson_correlation([1, 1, 1], [2, 3, 4])` → `None`

*Source: gauntlex/11-data-analysis/174-cumulative-product/README.md*

### 174 — Running Products

## Description
Track how the product of a sequence changes as each additional integer is included. Return one product for every prefix.

## Requirements
- Implement `cumulative_product(values)` in `starter/solution.py`.
- Return a new list of running products in input order.
- At each position, include every integer from the beginning through that position.
- Return `[]` for empty input.
- Do not mutate the original list.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- What effect does a zero have on all later running products?
- How is this different from multiplying every value only once for a single result?

## Example Behavior
`cumulative_product([2, 3, 4])` → `[2, 6, 24]`

`cumulative_product([2, 0, 4])` → `[2, 0, 0]`

*Source: gauntlex/11-data-analysis/175-frequency-table/README.md*

### 175 — Observation Counts

## Description
Summarize a collection of integers by recording how many times each distinct value appears.

## Requirements
- Implement `frequency_table(values)` in `starter/solution.py`.
- Return a dictionary mapping each distinct integer to its number of occurrences.
- Include negative, zero, and positive integer keys when present.
- Return `{}` for empty input.
- Do not modify the original observations.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- How does a repeated value change a frequency count?
- What is the natural representation of an empty dataset?

## Example Behavior
`frequency_table([1, 2, 1])` → `{1: 2, 2: 1}`

`frequency_table([])` → `{}`

*Source: gauntlex/11-data-analysis/176-weighted-mean/README.md*

### 176 — Unequal Importance

## Description
A weighted mean lets some observations contribute more than others. Each observation has a corresponding nonnegative weight.

## Requirements
- Implement `weighted_mean(values, weights)` in `starter/solution.py`.
- Assume numeric `values` and `weights` have equal length and every weight is nonnegative.
- Return the weighted average, with each observation contributing in proportion to its weight.
- Return `None` if the total weight is zero.
- Do not mutate either list.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why is a simple arithmetic mean insufficient when weights differ?
- What does a zero weight contribute?

## Example Behavior
`weighted_mean([10, 20], [1, 3])` → `17.5`

`weighted_mean([1, 2], [0, 0])` → `None`

*Source: gauntlex/11-data-analysis/177-rank-values/README.md*

### 177 — Dense Rankings

## Description
Assign ranks to integer observations by their numeric value. Equal values share a rank, and consecutive distinct values receive consecutive ranks without gaps.

## Requirements
- Implement `dense_ranks(values)` in `starter/solution.py`.
- Return a list of ranks in the original input order.
- Assign rank `1` to the smallest distinct value.
- Assign the same rank to equal values.
- Increase ranks by one for each next distinct value, without gaps.
- Return `[]` for empty input.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why must ranking order differ from output order?
- What makes dense ranking different from ranking with skipped positions?

## Example Behavior
`dense_ranks([30, 10, 20, 10])` → `[3, 1, 2, 1]`

`dense_ranks([])` → `[]`

*Source: gauntlex/11-data-analysis/178-quantize/README.md*

### 178 — Round to Steps

## Description
Quantization maps numeric observations to the nearest multiple of a positive step. The rounding rule must follow Python's built-in semantics.

## Requirements
- Implement `quantize(values, step)` in `starter/solution.py`.
- Assume `step` is positive.
- Return a new list with every value rounded to the nearest multiple of `step`.
- Use Python's built-in `round` semantics, including midpoint behavior.
- Preserve input order and do not mutate it.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why can midpoint values behave differently from always rounding upward?
- How does changing the step alter the available results?

## Example Behavior
`quantize([0.2, 0.7, 1.2], 0.5)` → `[0, 0.5, 1]`

`quantize([2, 4], 2)` → `[2, 4]`

*Source: gauntlex/11-data-analysis/179-outlier-iqr/README.md*

### 179 — Outside the Fences

## Description
The interquartile range describes the spread of the middle half of a dataset. Use it to identify observations beyond the standard lower and upper fences.

## Requirements
- Implement `iqr_outliers(values)` in `starter/solution.py`.
- Return `[]` for fewer than four values.
- Determine `Q1` and `Q3` as medians of the lower and upper halves of sorted data.
- For odd-length datasets, exclude the overall median from both halves.
- Define `IQR = Q3 - Q1` and fences at `Q1 - 1.5 * IQR` and `Q3 + 1.5 * IQR`.
- Return only values strictly outside those fences, preserving original input order.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- Why does the quartile definition matter for odd-sized datasets?
- Why are values exactly on a fence not outliers?

## Example Behavior
`iqr_outliers([1, 2, 2, 3, 3, 4, 5, 6, 100])` → `[100]`

`iqr_outliers([1, 2, 3])` → `[]`

*Source: gauntlex/11-data-analysis/180-linear-regression/README.md*

### 180 — Fit a Straight Line

## Description
Find the least-squares straight line that best describes paired numeric observations, expressed as a slope and intercept.

## Requirements
- Implement `linear_regression(xs, ys)` in `starter/solution.py`.
- Assume equal-length numeric `xs` and `ys` containing at least two points.
- Return `[slope, intercept]` for the ordinary least-squares line `y = slope * x + intercept`.
- Return `None` when all `x` values are equal.
- Do not mutate the input lists.
- Return the result without printing or reading standard input. Use only Python's standard library.

## Tips
- What does the slope describe about changes in `x` and `y`?
- Why can a vertical set of observations not be represented by this form?

## Example Behavior
`linear_regression([1, 2, 3], [2, 4, 6])` → `[2, 0]`

`linear_regression([1, 1], [2, 3])` → `None`

---

## Http Security

*Source: gauntlex/12-http-security/181-url-host/README.md*

### 181 — Identify the Host

## Description
An absolute web URL contains a scheme, a network location, and an optional path. Extract the hostname without confusing it with the port or the complete address.

## Requirements
- Implement `url_host(url)` in `starter/solution.py`.
- Accept an absolute HTTP or HTTPS URL.
- Return its hostname in lowercase, excluding the port and path.
- Raise `ValueError` for unsupported schemes or a missing hostname.
- Return the result without printing or making network requests.

## Tips
- Consider how a hostname differs from a network location containing a port.
- A URL may have a path without changing its hostname.

## Example Behavior
`url_host("https://Example.COM:8443/path")` → `"example.com"`

`url_host("http://localhost/x")` → `"localhost"`

*Source: gauntlex/12-http-security/182-url-join/README.md*

### 182 — Resolve a Link

## Description
Resolve a relative link against an absolute base URL using standard URL path rules.

## Requirements
- Implement `resolve_url(base, relative)` in `starter/solution.py`.
- Return the resolved absolute URL.
- Respect parent-directory paths, root-relative paths, and the base URL's trailing slash.
- Do not make network requests.
- Use the Python standard library, without printing or making network requests.

## Tips
- Why does a root-relative link behave differently from a parent-relative link?

## Example Behavior
`resolve_url("https://example.com/a/b", "../c")` → `"https://example.com/c"`

`resolve_url("https://example.com/a/", "/x")` → `"https://example.com/x"`

*Source: gauntlex/12-http-security/183-parse-http-status/README.md*

### 183 — Read the Response Status

## Description
Interpret an HTTP/1.1 response status line as a numeric status and a potentially multiword reason.

## Requirements
- Implement `parse_status_line(line)` in `starter/solution.py`.
- Return a dictionary with integer `status` and string `reason` for valid HTTP/1.1 status lines.
- Return `None` for malformed input.
- Preserve the full reason phrase, including internal spaces.
- Use the Python standard library, without printing or making network requests.

## Tips
- Why is splitting every word insufficient for a reason such as `Not Found`?

## Example Behavior
`parse_status_line("HTTP/1.1 200 OK")` → `{"status": 200, "reason": "OK"}`

`parse_status_line("HTTP/1.1 404 Not Found")` → `{"status": 404, "reason": "Not Found"}`

*Source: gauntlex/12-http-security/184-normalize-headers/README.md*

### 184 — Canonical Header Names

## Description
HTTP header names are case-insensitive. Normalize them while retaining the latest supplied value.

## Requirements
- Implement `normalize_headers(pairs)` in `starter/solution.py`.
- Accept `[name, value]` pairs.
- Return a dictionary with trimmed lowercase names and trimmed values.
- Keep the last value when a normalized name repeats.
- Preserve value capitalization and do not mutate inputs.
- Use Python's standard library without printing or making network requests.

## Tips
- Why are header names and header values normalized differently?

## Example Behavior
`normalize_headers([["Content-Type", " text/plain "], ["X-KEY", " 1 "]])` → `{"content-type": "text/plain", "x-key": "1"}`

`normalize_headers([["X", "1"], ["x", "2"]])` → `{"x": "2"}`

*Source: gauntlex/12-http-security/185-parse-cookie/README.md*

### 185 — Read Cookie Pairs

## Description
Parse semicolon-separated cookie assignments without decoding their contents.

## Requirements
- Implement `parse_cookie(text)` in `starter/solution.py`.
- Ignore empty segments and trim spaces around names and values.
- Split each assignment at its first equals sign.
- Keep the last value for repeated cookie names.
- Do not percent-decode values.
- Use Python's standard library without printing or making network requests.

## Tips
- Why might a cookie value contain an equals sign?

## Example Behavior
`parse_cookie("a=1; theme=dark")` → `{"a": "1", "theme": "dark"}`

`parse_cookie("a=1; a=2; ")` → `{"a": "2"}`

*Source: gauntlex/12-http-security/186-build-cookie/README.md*

### 186 — Assemble a Cookie Header

## Description
Serialize cookie pairs into a predictable header string.

## Requirements
- Implement `build_cookie(cookies)` in `starter/solution.py`.
- Assume valid cookie names and values.
- Sort names alphabetically and join `name=value` entries with `; `.
- Return an empty string for an empty mapping.
- Use Python's standard library without printing or making network requests.

## Tips
- Why does a stable ordering help reproducibility?

## Example Behavior
`build_cookie({"theme": "dark", "a": "1"})` → `"a=1; theme=dark"`

`build_cookie({})` → `""`

*Source: gauntlex/12-http-security/187-http-retry-delay/README.md*

### 187 — Backoff with a Ceiling

## Description
When a request fails, successive retries can wait progressively longer. Calculate an exponential delay without exceeding a maximum permitted interval.

## Requirements
- Implement `retry_delay(attempt, base, cap)` in `starter/solution.py`.
- Assume `attempt` is nonnegative and both `base` and `cap` are positive.
- Return the smaller of `cap` and `base * 2**attempt`, measured in seconds.
- Do not sleep, print, or make any network requests.

## Tips
- The first attempt uses the base delay; each successive attempt doubles the uncapped delay.
- Consider when the cap prevents further growth.

## Example Behavior
`retry_delay(0, 0.5, 10)` → `0.5`

`retry_delay(3, 0.5, 10)` → `4`

*Source: gauntlex/12-http-security/188-pagination-offset/README.md*

### 188 — Page to Offset

## Description
Convert a one-based page number into the zero-based position of its first record.

## Requirements
- Implement `pagination_offset(page, page_size)` in `starter/solution.py`.
- Return the offset for positive `page` and `page_size`.
- Raise `ValueError` if either is nonpositive.
- Page one begins at offset zero.
- Use Python's standard library without printing or making network requests.

## Tips
- Why do two pages precede page three?

## Example Behavior
`pagination_offset(1, 20)` → `0`

`pagination_offset(3, 20)` → `40`

*Source: gauntlex/12-http-security/189-pagination-slice/README.md*

### 189 — One Page of Results

## Description
Select a page of records from a collection without changing the original.

## Requirements
- Implement `paginate(items, page, page_size)` in `starter/solution.py`.
- Accept a one-based page and positive page size.
- Raise `ValueError` for invalid page or size.
- Return the selected items in their original order.
- Return `[]` for a page beyond the available records.
- Do not mutate the collection.
- Use Python's standard library without printing or making network requests.

## Tips
- How should a partially filled final page behave?

## Example Behavior
`paginate([1, 2, 3, 4, 5], 2, 2)` → `[3, 4]`

`paginate([1, 2], 3, 2)` → `[]`

*Source: gauntlex/12-http-security/190-query-filter/README.md*

### 190 — Match Every Field

## Description
Select dictionary records that match every exact field requirement.

## Requirements
- Implement `filter_records(records, filters)` in `starter/solution.py`.
- Return only records matching all key-value pairs in `filters`.
- Preserve original record order.
- Treat empty filters as matching all records.
- Return shallow copies without mutating inputs.
- Use Python's standard library without printing or making network requests.

## Tips
- Why does a single mismatched field disqualify a record?

## Example Behavior
`filter_records([{"x": 1, "y": 2}, {"x": 1, "y": 3}, {"x": 2}], {"x": 1})` → `[{"x": 1, "y": 2}, {"x": 1, "y": 3}]`

`filter_records([{"a": 1}], {})` → `[{"a": 1}]`

*Source: gauntlex/12-http-security/191-json-response/README.md*

### 191 — Build a JSON Response

## Description
Wrap an arbitrary JSON-serializable value in a predictable HTTP-style response object.

## Requirements
- Implement `json_response(value)` in `starter/solution.py`.
- Return a dictionary with `status`, `headers`, and `body`.
- Set status to `200` and `headers` to `{'content-type': 'application/json'}`.
- Encode the body as compact JSON text with sorted object keys.
- Do not return the original value as the body.
- Use Python's standard library without printing or making network requests.

## Tips
- Why is a serialized JSON body different from a Python dictionary?

## Example Behavior
`json_response({"b": 2, "a": 1})` → `{"status": 200, "headers": {"content-type": "application/json"}, "body": "{\"a\":1,\"b\":2}"}`

*Source: gauntlex/12-http-security/192-parse-bearer/README.md*

### 192 — Read a Bearer Token

## Description
Extract one token from an Authorization header while checking its authentication scheme.

## Requirements
- Implement `parse_bearer(header)` in `starter/solution.py`.
- Recognize `Bearer TOKEN` without regard to scheme capitalization.
- Allow extra surrounding and separating whitespace.
- Return the token as written.
- Return `None` for missing tokens, invalid schemes, or malformed headers.
- Use Python's standard library without printing or making network requests.

## Tips
- Why must the scheme be validated before accepting the token?

## Example Behavior
`parse_bearer("Bearer abc123")` → `"abc123"`

`parse_bearer(" bearer   XYZ ")` → `"XYZ"`

*Source: gauntlex/12-http-security/193-constant-time-compare/README.md*

### 193 — Compare Secrets Safely

## Description
Compare Unicode strings using a timing-resistant standard-library primitive rather than an ordinary early-exit comparison.

## Requirements
- Implement `constant_time_compare(a, b)` in `starter/solution.py`.
- Return whether the two strings are equal.
- Support Unicode input by using a consistent byte encoding.
- Use the standard library's timing-resistant comparison facility.
- Do not print or expose intermediate comparison results.
- Use Python's standard library without printing or making network requests.

## Tips
- Why can early-exit comparisons reveal information through timing?

## Example Behavior
`constant_time_compare("abc", "abc")` → `True`

`constant_time_compare("abc", "abd")` → `False`

*Source: gauntlex/12-http-security/194-sha256-hex/README.md*

### 194 — Fingerprint a Message

## Description
A cryptographic digest turns a message into a fixed-length fingerprint. In this challenge, generate the SHA-256 fingerprint of text encoded as UTF-8 and present the digest in a consistent hexadecimal form.

## Requirements
- Implement `sha256_hex(text)` in `starter/solution.py`.
- Encode the input string as UTF-8 before hashing.
- Return the SHA-256 digest as exactly 64 lowercase hexadecimal characters.
- Return the result without printing, prompting, or making network requests.
- Use Python's standard library only.

## Tips
- Hash functions operate on bytes, not directly on Python characters.
- The hexadecimal digest represents the hash output, not the original message.
- Even an empty string has a well-defined digest.

## Example Behavior
`sha256_hex("")` → `"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"`

`sha256_hex("abc")` → `"ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"`

*Source: gauntlex/12-http-security/195-hmac-signature/README.md*

### 195 — Authenticate a Message

## Description
A keyed message authentication code helps verify that a message came from someone holding a shared secret. Produce an HMAC using SHA-256 without exposing the key.

## Requirements
- Implement `hmac_signature(secret, message)` in `starter/solution.py`.
- Encode the secret and message separately as UTF-8.
- Return the lowercase hexadecimal HMAC-SHA256 digest.
- Treat the secret as the authentication key, not as an ordinary prefix or suffix.
- Do not print or expose the secret.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why does a keyed MAC provide different guarantees from an unkeyed hash?
- How would changing the secret affect the result?

## Example Behavior
`hmac_signature("key", "The quick brown fox jumps over the lazy dog")` → `"f7bc83f430538424b13298e6aa6fb143ef4d59a14946175997479dbc2d1a3cd8"`

*Source: gauntlex/12-http-security/196-verify-hmac/README.md*

### 196 — Verify a Signature

## Description
A received message may be accompanied by a claimed HMAC. Determine whether the signature matches the shared secret and message, using a timing-resistant comparison.

## Requirements
- Implement `verify_hmac(secret, message, signature)` in `starter/solution.py`.
- Recompute HMAC-SHA256 for the supplied UTF-8 secret and message.
- Return `True` only if the supplied lowercase hexadecimal signature matches the expected digest.
- Return `False` for malformed or mismatched signatures.
- Use a timing-resistant comparison rather than an ordinary early-exit string check.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why should malformed signatures be treated as invalid?
- Why can comparison timing matter for authentication?

## Example Behavior
`verify_hmac("key", "abc", "wrong")` → `False`

`verify_hmac("key", "abc", "")` → `False`

*Source: gauntlex/12-http-security/197-cors-origin/README.md*

### 197 — Exact Origin Allowlist

## Description
Cross-origin access decisions depend on exact origins, not vaguely similar hostnames. Check whether a request origin is explicitly permitted.

## Requirements
- Implement `allowed_origin(origin, allowed)` in `starter/solution.py`.
- Return `True` only when `origin` exactly equals one of the allowed origins.
- Treat URL scheme and port as significant.
- Do not accept substring, prefix, or suffix matches.
- Return `False` for an empty allowlist.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why is a lookalike domain not the same origin?
- What changes when an HTTPS origin uses a different port?

## Example Behavior
`allowed_origin("https://example.com", ["https://example.com"])` → `True`

`allowed_origin("https://evil-example.com", ["https://example.com"])` → `False`

*Source: gauntlex/12-http-security/198-http-method/README.md*

### 198 — Recognize HTTP Methods

## Description
Normalize a request method to a standard uppercase spelling, then reject names outside a fixed set of supported HTTP methods.

## Requirements
- Implement `normalize_method(text)` in `starter/solution.py`.
- Trim surrounding whitespace and ignore the input's letter case.
- Return the uppercase method if it is GET, POST, PUT, PATCH, DELETE, HEAD, or OPTIONS.
- Raise `ValueError` for all other values, including an empty string.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why is normalization useful before checking allowed methods?
- Why should an unsupported method be rejected explicitly?

## Example Behavior
`normalize_method(" get ")` → `"GET"`

`normalize_method("PaTcH")` → `"PATCH"`

*Source: gauntlex/12-http-security/199-parse-content-type/README.md*

### 199 — Extract the Media Type

## Description
A Content-Type header identifies a representation and may also include parameters such as character encoding. Extract only its media type.

## Requirements
- Implement `media_type(header)` in `starter/solution.py`.
- Return the portion of the header before the first semicolon.
- Trim surrounding whitespace and convert the result to lowercase.
- Ignore parameters after the first semicolon.
- Return an empty string for empty input.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why should a charset parameter not be part of the media type?
- What if no semicolon appears?

## Example Behavior
`media_type("Application/JSON; charset=utf-8")` → `"application/json"`

`media_type("text/plain")` → `"text/plain"`

*Source: gauntlex/12-http-security/200-http-cache-key/README.md*

### 200 — Stable Request Identity

## Description
A cache key should consistently identify the same request inputs. Combine the method, URL, and body into an unambiguous canonical representation before hashing.

## Requirements
- Implement `cache_key(method, url, body)` in `starter/solution.py`.
- Uppercase the request method before serialization.
- Represent the normalized method, URL, and optional body as a three-element JSON list in that order.
- Serialize JSON using compact separators and UTF-8 encoding.
- Return the SHA-256 digest as lowercase hexadecimal text.
- Do not make network requests.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why can directly concatenating fields be ambiguous?
- Why should method capitalization not change the resulting key?

## Example Behavior
See the contract and write additional edge-case tests.

*Source: gauntlex/12-http-security/201-request-id/README.md*

### 201 — Unique Request Identifier

## Description
Distributed systems use request identifiers to connect logs and trace related work. Generate a fresh identifier in canonical UUID version-four form.

## Requirements
- Implement `request_id()` in `starter/solution.py`.
- Return a lowercase UUID version 4 string with hyphens in canonical positions.
- Use a secure standard-library UUID generator.
- Generate a fresh identifier on each call rather than returning a fixed value.
- Do not print or make network requests.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why should the identifier include both a recognizable version and a consistent format?
- Why is a hard-coded identifier unsuitable?

## Example Behavior
See the contract and write additional edge-case tests.

*Source: gauntlex/12-http-security/202-url-encode-component/README.md*

### 202 — Escape One URL Component

## Description
A path component is a single part of a URL, so characters such as spaces and slashes must be encoded rather than interpreted as separators.

## Requirements
- Implement `encode_component(text)` in `starter/solution.py`.
- Encode the input as UTF-8 and percent-escape reserved or unsafe bytes.
- Leave only RFC 3986 unreserved characters (`A`–`Z`, `a`–`z`, digits, `-`, `.`, `_`, `~`) unescaped.
- Encode spaces as `%20`, not `+`.
- Encode `/` as `%2F` because it belongs to the component's data.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why does a slash inside one component need escaping?
- How does URL component encoding differ from form encoding?

## Example Behavior
`encode_component("hello world")` → `"hello%20world"`

`encode_component("a/b")` → `"a%2Fb"`

*Source: gauntlex/12-http-security/203-url-decode-component/README.md*

### 203 — Restore One URL Component

## Description
Recover text from percent-escaped UTF-8 bytes while preserving literal plus signs, which are not spaces in URL path components.

## Requirements
- Implement `decode_component(text)` in `starter/solution.py`.
- Percent-decode the input and interpret the resulting bytes as UTF-8.
- Do not convert literal `+` characters to spaces.
- Preserve unescaped characters as appropriate.
- Return the decoded string.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why does form-style query decoding handle plus signs differently?
- What happens to `%2F` during decoding?

## Example Behavior
`decode_component("hello%20world")` → `"hello world"`

`decode_component("a%2Fb")` → `"a/b"`

*Source: gauntlex/12-http-security/204-parse-basic-auth/README.md*

### 204 — Decode Basic Credentials

## Description
HTTP Basic authorization carries a Base64-encoded username and password separated by a colon. Decode the credentials and reject malformed input without exposing secrets.

## Requirements
- Implement `parse_basic_auth(header)` in `starter/solution.py`.
- Accept an Authorization header using the `Basic` scheme followed by a Base64 payload.
- Decode valid Base64 data as UTF-8.
- Split the decoded credentials at the first colon into username and password; allow additional colons inside the password.
- Return `[username, password]` for valid input.
- Return `None` for an invalid scheme, Base64 payload, UTF-8 sequence, or missing colon.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why must the first colon be the separator?
- Why does Base64 encoding not provide encryption?

## Example Behavior
`parse_basic_auth("Basic YWRhOnNlY3JldA==")` → `["ada", "secret"]`

`parse_basic_auth("Bearer x")` → `None`

*Source: gauntlex/12-http-security/205-header-get/README.md*

### 205 — Find the Last Header

## Description
HTTP headers may repeat, and header names are case-insensitive. Retrieve the last matching value without changing the original list.

## Requirements
- Implement `header_get(headers, name)` in `starter/solution.py`.
- Accept a list of `[name, value]` pairs and a target header name.
- Compare names without regard to letter case.
- Return the value from the last matching pair, unchanged.
- Return `None` when no header matches.
- Do not modify the input.
- Return the result without printing or prompting. Use Python's standard library only; make no network requests.

## Tips
- Why must the last matching value win?
- How does case-insensitive comparison affect repeated names?

## Example Behavior
`header_get([["X-ID", "1"], ["x-id", "2"]], "X-Id")` → `"2"`

`header_get([["A", "b"]], "X")` → `None`

---

## Sqlite

*Source: gauntlex/13-sqlite/206-create-users/README.md*

### 206 — Define the Users Table

## Description
A reliable directory starts with a schema that prevents incomplete records and duplicate email addresses. Define the database constraints before any user records are inserted.

## Requirements
- Implement `create_users(conn)` in `starter/solution.py`.
- Use the supplied live `sqlite3.Connection`; do not open a new connection.
- Create the `users` table only if it does not already exist.
- Use `id INTEGER PRIMARY KEY`, `name TEXT NOT NULL`, and `email TEXT NOT NULL UNIQUE`.
- Do not remove or overwrite an existing table.
- Use the supplied SQLite connection.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Preserve unrelated data and the caller's transaction state.

## Tips
- Which integrity rules belong in the database rather than only in application code?
- What should a second call do when the table already exists?

## Example Behavior
Calling `create_users(conn)` twice leaves one usable table with the required constraints.

*Source: gauntlex/13-sqlite/207-insert-user/README.md*

### 207 — Register a User

## Description
Register one new person in the existing users table and return the database-generated identity of that record.

## Requirements
- Implement `insert_user(conn, name, email)` in `starter/solution.py`.
- Use the supplied live `sqlite3.Connection`; do not open a new connection.
- Assume the `users(id,name,email)` table already exists.
- Insert the supplied name and email without constructing SQL from string concatenation.
- Return the inserted row's integer ID.
- Let database constraints reject invalid or duplicate records.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Preserve unrelated data and the caller's transaction state.

## Tips
- Why should user-supplied text be bound as a parameter?
- How can you identify the row that was just created?

## Example Behavior
After `insert_user(conn, 'Ada', 'ada@example.com')`, the returned integer identifies the new row.

*Source: gauntlex/13-sqlite/208-find-user/README.md*

### 208 — Find One Record

## Description
A user ID identifies at most one directory entry. Retrieve that record in a predictable Python representation, or clearly indicate that it does not exist.

## Requirements
- Implement `find_user(conn, user_id)` in `starter/solution.py`.
- Use the supplied live `sqlite3.Connection`; do not open a new connection.
- Assume the `users(id,name,email)` table exists.
- Find the row with the supplied integer `user_id`.
- Return `[id, name, email]` when found, or `None` otherwise.
- Do not change any database rows.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Preserve unrelated data and the caller's transaction state.

## Tips
- Why is a missing record different from a record with an empty field?
- How should a SQLite row be represented in the return value?

## Example Behavior
`find_user(conn, 999)` → `None` when no row has that ID.

*Source: gauntlex/13-sqlite/209-list-users/README.md*

### 209 — Read the User Directory

## Description
Database queries do not guarantee insertion order. Retrieve the complete user directory in a stable order suitable for display or further processing.

## Requirements
- Implement `list_users(conn)` in `starter/solution.py`.
- Use the supplied live `sqlite3.Connection`; do not open a new connection.
- Read all rows from `users(id,name,email)`.
- Return a list of `[id, name, email]` records.
- Order records by ascending ID.
- Return `[]` when the table is empty.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Preserve unrelated data and the caller's transaction state.

## Tips
- Why should sorting be requested explicitly?
- What is the expected result for an empty directory?

## Example Behavior
An empty `users` table produces `[]`; populated results are ordered by ID.

*Source: gauntlex/13-sqlite/210-update-email/README.md*

### 210 — Change a User Email

## Description
Changing a stored email should affect only the intended user. Report whether the target record existed so callers can distinguish success from a missing ID.

## Requirements
- Implement `update_email(conn, user_id, email)` in `starter/solution.py`.
- Use the supplied live `sqlite3.Connection`; do not open a new connection.
- Update the email of the user identified by `user_id`.
- Assume `users(id,name,email)` exists.
- Return `True` if a row was updated and `False` if none matched.
- Keep all other user records unchanged.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Preserve unrelated data and the caller's transaction state.

## Tips
- How can the number of affected rows tell you whether the user existed?
- Why should the identifier be parameterized?

## Example Behavior
`update_email(conn, 999, 'new@example.com')` → `False` when the user does not exist.

*Source: gauntlex/13-sqlite/211-delete-user/README.md*

### 211 — Remove a User

## Description
Delete a specific directory entry without disturbing other users, and report whether the target was actually present.

## Requirements
- Implement `delete_user(conn, user_id)` in `starter/solution.py` using the caller's live `sqlite3.Connection`.
- Delete only the row with the supplied integer ID.
- Return `True` when a row was deleted, `False` if none matched.
- Leave unrelated records untouched.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or alter unrelated records or transaction state.

## Tips
- How can the affected-row count distinguish a missing user from a successful deletion?

## Example Behavior
Deleting a missing user returns `False`; deleting an existing user returns `True`.

*Source: gauntlex/13-sqlite/212-search-users/README.md*

### 212 — Search Names Literally

## Description
A name search should treat the search term as text, even when it contains characters that SQL ordinarily uses as wildcards.

## Requirements
- Implement `search_users(conn, term)` in `starter/solution.py` using the caller's live `sqlite3.Connection`.
- Search names case-insensitively for the supplied substring.
- Treat `%` and `_` as literal characters, not pattern wildcards.
- Return `[id, name]` rows ordered by ascending ID.
- Return `[]` if no names match.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or alter unrelated records or transaction state.

## Tips
- Why does binding a LIKE pattern not automatically make its wildcard characters literal?|How can a search be case-insensitive without losing the input text?

## Example Behavior
A term containing `%` searches for the percent character itself rather than matching arbitrary text.

*Source: gauntlex/13-sqlite/213-count-users/README.md*

### 213 — Count the Directory

## Description
A directory count should return one number, without loading every user record into Python.

## Requirements
- Implement `count_users(conn)` in `starter/solution.py` using the caller's live `sqlite3.Connection`.
- Return the number of rows in `users(id,name,email)` as an integer.
- Return `0` for an empty table.
- Do not change database contents.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or alter unrelated records or transaction state.

## Tips
- What does a SQL aggregate return when no records exist?

## Example Behavior
An empty directory returns `0`; inserting one user makes the result `1`.

*Source: gauntlex/13-sqlite/214-users-page/README.md*

### 214 — Paginate User Records

## Description
A large directory is easier to consume in pages. Select a consistent slice of users by their IDs.

## Requirements
- Implement `users_page(conn, page, page_size)` in `starter/solution.py` using the caller's live `sqlite3.Connection`.
- Accept a one-based page and a positive page size.
- Raise `ValueError` for nonpositive page or page size.
- Return `[id, name]` rows ordered by ascending ID.
- Return `[]` for a page beyond available records.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or alter unrelated records or transaction state.

## Tips
- Why is an explicit ordering necessary for stable pagination?|What is the offset of the first page?

## Example Behavior
For users with IDs 1–5, page 2 of size 2 returns the records with IDs 3 and 4.

*Source: gauntlex/13-sqlite/215-create-orders/README.md*

### 215 — Define the Orders Table

## Description
Store orders with nonnegative amounts and require the database to enforce that rule, regardless of which caller inserts the record.

## Requirements
- Implement `create_orders(conn)` in `starter/solution.py` using the caller's live `sqlite3.Connection`.
- Create `orders` if absent, with `id INTEGER PRIMARY KEY`, `user_id INTEGER NOT NULL`, and `amount INTEGER NOT NULL CHECK(amount>=0)`.
- Keep an existing table and its data unchanged.
- Make repeated calls safe.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or alter unrelated records or transaction state.

## Tips
- Why should the amount constraint live in the database schema?|What should happen if the setup function runs twice?

## Example Behavior
Calling `create_orders(conn)` again must not erase existing orders.

*Source: gauntlex/13-sqlite/216-order-total/README.md*

### 216 — Sum Customer Orders

## Description
Calculate a customer's total order value using the database, even when that customer has no orders.

## Requirements
- Implement `order_total(conn, user_id)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Read amounts from `orders(id,user_id,amount)` for the supplied user ID.
- Return their numeric sum.
- Return `0` when no orders match.
- Do not alter any records.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- Why might a SQL aggregate over zero matching rows need special handling?

## Example Behavior
`order_total(conn, 42)` → `0` when customer 42 has no orders.

*Source: gauntlex/13-sqlite/217-top-customers/README.md*

### 217 — Rank Customers by Spending

## Description
Build a leaderboard by combining each customer's orders and ranking the resulting totals.

## Requirements
- Implement `top_customers(conn, k)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Aggregate `orders(id,user_id,amount)` by user ID.
- Return `[user_id, total]` rows ordered by total descending, then user ID ascending.
- Return at most `k` rows, assuming `k` is nonnegative.
- Return `[]` when `k` is zero.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- Why does the ranking need a tie-breaker?
- How does grouping differ from sorting?

## Example Behavior
Two customers with the same total appear in ascending user-ID order.

*Source: gauntlex/13-sqlite/218-join-orders/README.md*

### 218 — Orders and Their Owners

## Description
Combine related order and user tables so each order is presented alongside the name of its owner.

## Requirements
- Implement `orders_with_users(conn)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Use `users(id,name,email)` and `orders(id,user_id,amount)`.
- Return `[order_id, user_name, amount]` rows sorted by order ID.
- Exclude orders without a matching user.
- Do not modify either table.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- What makes an order an orphan?
- Why is a matching key needed when joining tables?

## Example Behavior
An order whose `user_id` has no matching user does not appear in the result.

*Source: gauntlex/13-sqlite/219-insert-ignore/README.md*

### 219 — Insert Only Once

## Description
Add a user only when the email is not already registered. A duplicate must leave the existing record intact.

## Requirements
- Implement `insert_email_once(conn, name, email)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Assume `users(id,name,email UNIQUE)` exists.
- Return `True` only if a new row is inserted.
- For an existing email, return `False` without raising or overwriting the record.
- Bind name and email as data parameters.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- How can uniqueness be enforced by the database?
- Why is ignoring a duplicate different from replacing a record?

## Example Behavior
Registering the same email twice returns `True` and then `False`, without changing the first record.

*Source: gauntlex/13-sqlite/220-upsert-score/README.md*

### 220 — Create or Replace a Score

## Description
Maintain exactly one score per student, creating a record on first use and updating it on later submissions.

## Requirements
- Implement `upsert_score(conn, student, score)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Assume `scores(student TEXT PRIMARY KEY,score INTEGER)` exists.
- Insert a new student and score when the student is absent.
- Overwrite the score when that student already exists.
- Do not create duplicate student rows.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- What determines whether the operation is an insert or an update?
- Why is the student key central to the behavior?

## Example Behavior
Calling `upsert_score` twice for one student leaves one row with the newer score.

*Source: gauntlex/13-sqlite/221-transaction-transfer/README.md*

### 221 — Atomic Account Transfer

## Description
A transfer changes two balances that must stay consistent. Treat the debit and credit as one indivisible operation.

## Requirements
- Implement `transfer(conn, source_id, target_id, amount)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Assume `accounts(id INTEGER PRIMARY KEY,balance INTEGER NOT NULL)` exists.
- Transfer a positive integer amount from source to target.
- Raise `ValueError` if the amount is nonpositive, either account is absent, or the source has insufficient funds.
- On failure, leave both balances exactly as they were before the call.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- Why must a debit and credit succeed or fail together?
- What should happen if validation fails after a tentative change?

## Example Behavior
An invalid transfer raises `ValueError` and leaves both account balances unchanged.

*Source: gauntlex/13-sqlite/222-transaction-batch/README.md*

### 222 — All or Nothing

## Description
Import multiple users as one unit of work. If any record violates a database constraint, none of the records from that batch may remain.

## Requirements
- Implement `insert_batch_atomic(conn, records)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Insert each `[name,email]` pair into `users(id,name,email UNIQUE)`.
- Treat the batch atomically, including when an error occurs partway through.
- Propagate `sqlite3.IntegrityError` on a constraint violation.
- On failure, restore the table to its pre-call contents.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- Why is a sequence of independent inserts insufficient?
- What should happen to earlier successful inserts when a later one fails?

## Example Behavior
If the third record repeats an existing unique email, the first two inserts from that batch must also be undone.

*Source: gauntlex/13-sqlite/223-safe-sort/README.md*

### 223 — Allowlisted Sorting

## Description
Caller-selected sorting can be dangerous when SQL identifiers are constructed from untrusted input. Permit only known columns and directions.

## Requirements
- Implement `sorted_users(conn, field, direction)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Accept a sort field of `id` or `name`.
- Accept `asc` or `desc` without regard to case.
- Raise `ValueError` for unsupported fields or directions.
- Return `[id, name]` rows sorted as requested from `users(id,name,email)`.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- Why do SQL value parameters not safely substitute for column identifiers?
- What role does an explicit allowlist play?

## Example Behavior
`sorted_users(conn, 'name', 'DESC')` returns `[id, name]` rows ordered by descending name.

*Source: gauntlex/13-sqlite/224-group-counts/README.md*

### 224 — Count Event Categories

## Description
Summarize event frequencies by category and produce a deterministic ranking even when multiple categories have equal counts.

## Requirements
- Implement `group_counts(conn)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Read from `events(id,category)`.
- Return `[category, count]` for every distinct category.
- Sort by count descending, then category ascending.
- Return `[]` for an empty table.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- Why should a frequency report specify tie-breaking?
- How does grouping combine multiple rows into one result?

## Example Behavior
If two categories have equal counts, their names determine their order.

*Source: gauntlex/13-sqlite/225-date-filter/README.md*

### 225 — Events After a Date

## Description
Canonical ISO dates can be compared lexically when their format is consistent. Select events from a cutoff date onward.

## Requirements
- Implement `events_on_or_after(conn, cutoff)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Assume valid `YYYY-MM-DD` strings in `events(id,event_date TEXT)` and in the cutoff.
- Include events on or after the cutoff date.
- Return `[id, event_date]` rows ordered by event date, then ID.
- Do not modify the table.
- Use parameterized SQL for untrusted values, standard-library modules, and no printed output.
- Do not open a new connection or alter unrelated data or transaction state.

## Tips
- Why do zero-padded ISO dates have useful lexical ordering?
- Why is the cutoff inclusive?

## Example Behavior
An event dated exactly on the cutoff is included; an earlier event is excluded.

*Source: gauntlex/13-sqlite/226-db-schema-check/README.md*

### 226 — Inspect the Schema

## Description
A database can contain tables, views, and indexes. Determine whether a named object is specifically a table, not merely any schema entry.

## Requirements
- Implement `table_exists(conn, table_name)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Check the SQLite schema for the supplied table name.
- Return `True` only if an actual table with that name exists.
- Return `False` for missing names, views, and indexes.
- Treat the name as data rather than interpolating it into arbitrary SQL.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or change unrelated data or transaction state.

## Tips
- Why does the presence of a schema name not guarantee a table exists?
- Which object type must be checked?

## Example Behavior
A named view must produce `False`, even if its name exists in the SQLite schema.

*Source: gauntlex/13-sqlite/227-db-index/README.md*

### 227 — Ensure an Index

## Description
An index can speed up lookups by a frequently searched column. Create a named email index without failing when setup is repeated.

## Requirements
- Implement `ensure_email_index(conn)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Assume `users(email)` exists.
- Ensure an index named `idx_users_email` exists on the `email` column.
- Make repeated calls safe and preserve existing data.
- Do not recreate the table.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or change unrelated data or transaction state.

## Tips
- Why should database setup be idempotent?
- How does an index differ from a table?

## Example Behavior
Calling `ensure_email_index(conn)` twice leaves the named index available without an error.

*Source: gauntlex/13-sqlite/228-db-json/README.md*

### 228 — Store a JSON Document

## Description
Structured Python data can be persisted as JSON text. Use a stable representation so equivalent dictionaries serialize consistently.

## Requirements
- Implement `store_json(conn, value)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Assume `documents(id INTEGER PRIMARY KEY,body TEXT)` exists.
- Serialize the supplied JSON-compatible value with sorted object keys and compact separators.
- Store the resulting JSON string in the `body` column.
- Return the new document's integer row ID.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or change unrelated data or transaction state.

## Tips
- Why is Python's display representation not a substitute for JSON?
- How does stable key ordering help reproducibility?

## Example Behavior
Storing `{'b': 2, 'a': 1}` saves the compact JSON body `{"a":1,"b":2}`.

*Source: gauntlex/13-sqlite/229-db-json-read/README.md*

### 229 — Load a JSON Document

## Description
Retrieve a stored JSON document and restore its structured Python representation rather than returning raw serialized text.

## Requirements
- Implement `load_json(conn, doc_id)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Read the `body` field from `documents(id,body TEXT)` for the requested ID.
- Decode the stored JSON text to a Python value.
- Return `None` if the row does not exist.
- Do not modify the database.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or change unrelated data or transaction state.

## Tips
- Why is a stored JSON string different from its decoded Python value?
- What does a missing record mean?

## Example Behavior
A missing document ID returns `None`; a stored JSON object is returned as a Python dictionary.

*Source: gauntlex/13-sqlite/230-db-report/README.md*

### 230 — Revenue by Category

## Description
Summarize sales performance by grouping amounts into categories, then rank the categories by total revenue.

## Requirements
- Implement `revenue_report(conn)` in `starter/solution.py` using the supplied live `sqlite3.Connection`.
- Read `sales(id,category,amount INTEGER)`.
- Sum amounts for each category.
- Return `[category, total]` rows ordered by total descending and category ascending for ties.
- Return `[]` when there are no sales.
- Use parameterized SQL for untrusted values, Python's standard library, and no printed output.
- Do not open another connection or change unrelated data or transaction state.

## Tips
- Why is the category name needed as a secondary sort key?
- How can aggregation reduce many sales rows to one row per category?

## Example Behavior
Two categories with equal revenue are returned in alphabetical category order.

---

## Async

*Source: gauntlex/14-async/231-async-greeting/README.md*

### 231 — An Awaitable Greeting

## Description
A coroutine is a function whose result can be awaited by an asynchronous caller. Begin with a greeting that returns text rather than printing it.

## Requirements
- Implement `async def greet_async(name)` in `starter/solution.py`.
- Define `async def greet_async(name)`.
- Return the exact string `Hello, NAME!`, substituting the supplied name.
- Do not print, sleep, or block the event loop.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- What is the difference between calling a coroutine function and awaiting it?

## Example Behavior
`await greet_async('Ada')` → `'Hello, Ada!'`

*Source: gauntlex/14-async/232-async-double/README.md*

### 232 — A Coroutine Result

## Description
An asynchronous function can return an ordinary calculated value even when it has no waiting to perform.

## Requirements
- Implement `async def double_async(value)` in `starter/solution.py`.
- Define `async def double_async(value)` for an integer.
- Return twice the input integer.
- Do not print, sleep, or block the event loop.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Does an `async def` function need to await something before it can return a value?

## Example Behavior
`await double_async(7)` → `14`

*Source: gauntlex/14-async/233-async-gather/README.md*

### 233 — Gather in Order

## Description
Several awaitables may finish in an unpredictable order. Collect their results in the original input order, regardless of completion timing.

## Requirements
- Implement `async def gather_results(awaitables)` in `starter/solution.py`.
- Accept a sequence of awaitable objects.
- Run the awaitables concurrently and return a list of results in input order.
- Return `[]` for empty input.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- How can concurrent tasks finish out of order while their results remain ordered?

## Example Behavior
Awaitables returning `3`, `1`, and `2` in that input order produce `[3, 1, 2]` even if they finish in another order.

*Source: gauntlex/14-async/234-async-map/README.md*

### 234 — Concurrent Transformation

## Description
Apply an asynchronous operation to each item without waiting for one item to finish before beginning the next.

## Requirements
- Implement `async def async_map(fn, values)` in `starter/solution.py`.
- Accept an async function `fn` and a sequence of values.
- Invoke `fn(value)` for every value concurrently.
- Return results in input order, including an empty list for empty input.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- What is the difference between creating concurrent work and ordering its results?

## Example Behavior
For an async doubling function and values `[2, 4]`, the result is `[4, 8]`.

*Source: gauntlex/14-async/235-async-timeout/README.md*

### 235 — Set a Deadline

## Description
An asynchronous operation should not be allowed to wait indefinitely when a caller sets a deadline.

## Requirements
- Implement `async def with_timeout(awaitable, seconds)` in `starter/solution.py`.
- Accept an awaitable and a timeout in seconds.
- Return the awaited result if it finishes before the deadline.
- Propagate `asyncio.TimeoutError` when the timeout expires.
- Do not turn a timeout into a successful result.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- What distinguishes a timeout from a normal return value?

## Example Behavior
An operation that finishes within the limit returns normally; an operation exceeding it raises `asyncio.TimeoutError`.

*Source: gauntlex/14-async/236-async-retry/README.md*

### 236 — Try Again

## Description
Transient failures sometimes justify another attempt. Each retry must call the operation again rather than reuse a coroutine that has already failed.

## Requirements
- Implement `async def retry_async(fn, attempts)` in `starter/solution.py`.
- Accept a zero-argument async function and an integer attempt count.
- Raise `ValueError` if attempts is less than one.
- Call the function up to that many times, returning the first successful result.
- Retry only on `Exception` and re-raise the final failure.
- Do not introduce retry delays.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Why must a fresh coroutine be created for each attempt?|Why should the final error remain visible?

## Example Behavior
If the first call fails and the second succeeds with `9`, the result is `9` and no third call is made.

*Source: gauntlex/14-async/237-async-semaphore/README.md*

### 237 — Limit Concurrency

## Description
Launching all work simultaneously can overload a resource. Bound the number of operations running at once while preserving output order.

## Requirements
- Implement `async def limited_map(fn, values, limit)` in `starter/solution.py`.
- Accept an async function, input values, and a positive concurrency limit.
- Never allow more than `limit` calls to run simultaneously.
- Return results in original input order.
- Return `[]` for empty input.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- How is the number of active operations different from the number of total inputs?

## Example Behavior
For five inputs and a limit of two, no more than two calls may be active at any instant.

*Source: gauntlex/14-async/238-async-first/README.md*

### 238 — First to Finish

## Description
When several independent operations can provide the same answer, the earliest completed one may be sufficient. Unfinished operations still require cleanup.

## Requirements
- Implement `async def first_completed(awaitables)` in `starter/solution.py`.
- Accept a nonempty sequence of awaitables, none of which raises.
- Return the result of the first completed awaitable.
- Cancel unfinished tasks once a result is available.
- Do not wait for every operation to finish normally.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Why is cancellation part of correctness rather than just an optimization?

## Example Behavior
If the second operation finishes before the first, return the second result and cancel unfinished work.

*Source: gauntlex/14-async/239-async-queue/README.md*

### 239 — Drain the Queue

## Description
A queue holds work in first-in, first-out order. Collect what is currently waiting without suspending until future items arrive.

## Requirements
- Implement `async def queue_drain(queue)` in `starter/solution.py`.
- Accept an existing `asyncio.Queue`.
- Remove and return all currently queued items in FIFO order.
- Return `[]` if the queue is empty.
- Do not wait for additional items.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Why is draining a queue different from waiting for a producer?

## Example Behavior
A queue holding `['a', 'b']` produces `['a', 'b']` and is empty afterward.

*Source: gauntlex/14-async/240-async-producer/README.md*

### 240 — Produce in Sequence

## Description
A producer adds values to a shared asynchronous queue. When the queue has limited capacity, insertion may need to wait for space.

## Requirements
- Implement `async def produce_items(queue, values)` in `starter/solution.py`.
- Accept an `asyncio.Queue` and a sequence of values.
- Enqueue every value in its original order.
- Return the number of values successfully enqueued.
- Return `0` for empty input.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Why can putting an item into a bounded queue require waiting?

## Example Behavior
Enqueuing three values returns `3`, and the queue receives them in their original order.

*Source: gauntlex/14-async/241-async-consumer/README.md*

### 241 — Consume Exactly N

## Description
Unlike draining a queue, consuming a fixed number of items may require waiting for items that have not arrived yet.

## Requirements
- Implement `async def consume_n(queue, n)` in `starter/solution.py`.
- Accept an `asyncio.Queue` and integer `n`.
- Raise `ValueError` when `n` is negative.
- Remove exactly `n` items, awaiting future arrivals when necessary.
- Return the items in FIFO order; return `[]` for `n == 0`.
- Assume the queue will eventually receive enough items.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Why can a consumer need to wait even when a queue is initially empty?

## Example Behavior
`consume_n(queue, 0)` returns `[]` without removing anything.

*Source: gauntlex/14-async/242-async-event/README.md*

### 242 — Wait for a Signal

## Description
An event coordinates coroutines by letting one wait until another announces that a condition is ready.

## Requirements
- Implement `async def wait_for_event(event)` in `starter/solution.py`.
- Accept an `asyncio.Event`.
- Suspend until the event is set.
- Return `True` after the signal arrives.
- Return promptly if the event is already set.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Why is awaiting a signal preferable to repeatedly polling a flag?

## Example Behavior
An already-set event lets `wait_for_event(event)` return `True` without waiting.

*Source: gauntlex/14-async/243-async-lock/README.md*

### 243 — Protected Increment

## Description
Multiple coroutines may share mutable state. Protect a read-modify-write operation so concurrent updates cannot interfere with one another.

## Requirements
- Implement `async def locked_increment(state, lock)` in `starter/solution.py`.
- Accept a dictionary containing integer key `count` and an `asyncio.Lock`.
- Acquire the lock while reading and incrementing the count by one.
- Update the dictionary and return the new integer count.
- Release the lock even if the operation cannot complete normally.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Why must the read and write occur inside the same protected section?

## Example Behavior
With `state = {'count': 4}`, one protected increment returns `5` and updates the stored count to `5`.

*Source: gauntlex/14-async/244-async-filter/README.md*

### 244 — Concurrent Selection

## Description
Evaluate an asynchronous predicate for every value, then keep only those values whose predicate results are truthy.

## Requirements
- Implement `async def async_filter(predicate, values)` in `starter/solution.py`.
- Accept an async predicate and a sequence of values.
- Evaluate the predicate for each value concurrently.
- Return original input values whose predicate results are truthy.
- Preserve original input order regardless of completion order.
- Return `[]` for empty input.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- Why should filtering retain the original values rather than predicate results?

## Example Behavior
If the predicate accepts even numbers, values `[3, 2, 4]` produce `[2, 4]`.

*Source: gauntlex/14-async/245-async-batch/README.md*

### 245 — Process in Waves

## Description
Divide asynchronous work into consecutive batches. Work within a batch may overlap, but later batches must not begin until earlier batches finish.

## Requirements
- Implement `async def async_batches(fn, values, batch_size)` in `starter/solution.py`.
- Accept an async function, values, and a positive batch size.
- Process consecutive groups of at most `batch_size` items.
- Allow calls within one group to run concurrently.
- Do not start any later group before the previous group finishes.
- Return all results in input order; return `[]` for empty input.
- Use Python's `asyncio` standard library, with no external packages or network access.
- Do not print output or block the event loop with synchronous sleeps.

## Tips
- How do batch boundaries differ from a simple concurrency limit?

## Example Behavior
With five inputs and a batch size of two, batches have sizes 2, 2, and 1, executed in sequence.

---

## Testing

*Source: gauntlex/15-testing/246-assert-equal/README.md*

### 246 — Explain a Mismatch

## Description
A good assertion does more than say a check failed. Compare actual and expected values and report an unambiguous failure message.

## Requirements
- Implement `assert_equal(actual, expected)` in `starter/solution.py`.
- Return `None` when `actual == expected`.
- Otherwise raise `AssertionError` with exact message `expected EXPECTED, got ACTUAL`, where each placeholder uses `repr()`.
- Do not mutate the values.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why is `repr()` more informative than a plain string conversion?

## Example Behavior
`assert_equal(3, 3)` → `None`; `assert_equal('x', 'y')` raises `AssertionError` with `expected 'y', got 'x'`.

*Source: gauntlex/15-testing/247-assert-raises/README.md*

### 247 — Expect a Failure

## Description
Some tests succeed only when a callable raises a particular exception. Validate the exception type and preserve the caught instance.

## Requirements
- Implement `assert_raises(expected_exception, fn)` in `starter/solution.py`.
- Call the zero-argument function `fn`.
- Return the caught exception when it is an instance of `expected_exception`.
- Raise `AssertionError` if `fn` returns normally or raises a different exception type.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why is a normal return a failure for this test?
- What distinguishes an exception instance from its class?

## Example Behavior
A callable raising `ValueError('bad')` passes when `ValueError` is expected and returns that exception instance.

*Source: gauntlex/15-testing/248-approx-equal/README.md*

### 248 — Close Enough

## Description
Floating-point results may differ slightly because of representation and rounding. Compare numbers using an explicit absolute tolerance.

## Requirements
- Implement `approx_equal(a, b, tolerance)` in `starter/solution.py`.
- Accept numeric `a`, `b`, and a nonnegative `tolerance`.
- Return `True` when their absolute difference is at most the tolerance; otherwise return `False`.
- Raise `ValueError` for a negative tolerance.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why is exact equality sometimes inappropriate for floating-point calculations?

## Example Behavior
`approx_equal(1.01, 1.0, 0.02)` → `True`; `approx_equal(1.1, 1.0, 0.01)` → `False`.

*Source: gauntlex/15-testing/249-first-difference/README.md*

### 249 — Find the Divergence

## Description
When comparing two sequences, identify the earliest point where their contents or lengths diverge.

## Requirements
- Implement `first_difference(a, b)` in `starter/solution.py`.
- Return the zero-based index of the first unequal pair.
- Return the shorter length if one sequence is a strict prefix of the other.
- Return `None` when the sequences are identical.
- Do not modify either sequence.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- What happens if every overlapping element matches but one sequence continues?

## Example Behavior
`first_difference([1, 2], [1, 3])` → `1`; `first_difference([1], [1, 2])` → `1`.

*Source: gauntlex/15-testing/250-diff-dicts/README.md*

### 250 — Compare Records

## Description
Two records can differ because a field was added, removed, or changed. Report every difference without losing which side contained which value.

## Requirements
- Implement `diff_dicts(old, new)` in `starter/solution.py`.
- Accept `old` and `new` mappings whose stored values are never `None`.
- Include every key appearing in either mapping whose values differ or whose key is missing on one side.
- Return a dictionary mapping each changed key to `[old_value, new_value]`.
- Use `None` for an absent side; omit unchanged keys.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why is it important to distinguish a missing key from an equal value?

## Example Behavior
`diff_dicts({'a': 1}, {'a': 2, 'b': 3})` → `{'a': [1, 2], 'b': [None, 3]}`.

*Source: gauntlex/15-testing/251-run-cases/README.md*

### 251 — Evaluate Examples

## Description
Turn a collection of expected input-output pairs into a simple test report. Each case should produce one boolean result.

## Requirements
- Implement `run_cases(fn, cases)` in `starter/solution.py`.
- Accept callable `fn` and cases shaped `[args, expected]`, where `args` is a list.
- Call `fn` with each case's positional arguments.
- Return booleans indicating whether the result equals the expected value, in case order.
- Allow exceptions from the callable to propagate.
- Use Python's standard library only; do not print or mutate inputs unless the task explicitly requires capturing output.

## Tips
- Why should the result list preserve the order of the cases?

## Example Behavior
For a function that doubles numbers, cases `[[[2], 4], [[3], 5]]` produce `[True, False]`.

*Source: gauntlex/15-testing/252-capture-output/README.md*

### 252 — Observe Printed Output

## Description
A function's return value and printed output are different observable effects. Capture both while ensuring the global output stream is restored.

## Requirements
- Implement `capture_output(fn)` in `starter/solution.py`.
- Call the supplied zero-argument function once.
- Capture everything it writes to standard output during that call.
- Return `[result, stdout_text]` if the function returns normally.
- Restore standard output even if the function raises, and propagate the exception.
- Use Python's standard library only; do not print or mutate inputs unless the task explicitly requires capturing output.

## Tips
- Why is cleanup necessary even when the callable fails?

## Example Behavior
A callable that prints `Hi` and returns `7` produces `[7, 'Hi\n']`.

*Source: gauntlex/15-testing/253-is-sorted/README.md*

### 253 — Check the Order

## Description
Determine whether a sequence is already in nondecreasing order. Equal neighbors are permitted.

## Requirements
- Implement `is_sorted(values)` in `starter/solution.py`.
- Return `True` if each element is no smaller than the preceding one.
- Return `True` for empty and one-element sequences.
- Return `False` when any adjacent pair decreases.
- Do not sort or mutate the input.
- Use Python's standard library only; do not print or mutate inputs unless the task explicitly requires capturing output.

## Tips
- Why does an empty sequence count as sorted?

## Example Behavior
`is_sorted([1, 1, 3])` → `True`; `is_sorted([2, 1])` → `False`.

*Source: gauntlex/15-testing/254-validate-sorted/README.md*

### 254 — Reject Disorder

## Description
Validation checks a property of existing data; it must not silently repair the data by sorting it.

## Requirements
- Implement `validate_sorted(values)` in `starter/solution.py`.
- Return the original list unchanged when values are nondecreasing.
- Raise `ValueError` if any later value is smaller than the previous one.
- Do not mutate the list or return a sorted copy.
- Use Python's standard library only; do not print or mutate inputs unless the task explicitly requires capturing output.

## Tips
- Why should validation reject rather than repair unordered data?

## Example Behavior
`validate_sorted([1, 2, 2])` returns the original list; `validate_sorted([2, 1])` raises `ValueError`.

*Source: gauntlex/15-testing/255-check-permutation/README.md*

### 255 — Same Elements, New Order

## Description
Two sequences are permutations when they contain the same elements with identical occurrence counts, regardless of position.

## Requirements
- Implement `is_permutation(a, b)` in `starter/solution.py`.
- Accept lists of hashable elements.
- Return `True` only if both lists contain the same values with the same multiplicities.
- Treat ordering as irrelevant but duplicates as significant.
- Do not mutate either list.
- Use Python's standard library only; do not print or mutate inputs unless the task explicitly requires capturing output.

## Tips
- Why is comparing sets alone insufficient when values repeat?

## Example Behavior
`is_permutation([1, 2, 1], [1, 1, 2])` → `True`; `is_permutation([1, 1], [1, 2])` → `False`.

*Source: gauntlex/15-testing/256-invariant-check/README.md*

### 256 — Guard the Nonnegative Invariant

## Description
An invariant is a condition that must remain true for a collection of values. Detect the earliest violation and report its location.

## Requirements
- Implement `check_nonnegative(values)` in `starter/solution.py`.
- Accept a sequence of numeric values.
- Return `True` if every value is nonnegative.
- Otherwise raise `AssertionError` with exact message `negative at INDEX` for the first negative value's zero-based index.
- Do not mutate the sequence.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why should the first violation be reported instead of every violation?

## Example Behavior
`check_nonnegative([0, 3])` → `True`; `check_nonnegative([1, -2, -3])` raises `AssertionError('negative at 1')`.

*Source: gauntlex/15-testing/257-parse-test-report/README.md*

### 257 — Count Test Report Lines

## Description
Textual test reports often mix structured results with unrelated lines. Count only records that match a strict pass-or-fail format.

## Requirements
- Implement `parse_test_report(lines)` in `starter/solution.py`.
- Accept a sequence of lines.
- Count only lines matching `PASS name` or `FAIL name` with exactly one space and a nonempty name.
- Ignore all other lines, including malformed status lines.
- Return `{'passed': N, 'failed': M}` with both keys present.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why is checking only the start of a line insufficient?

## Example Behavior
`parse_test_report(['PASS alpha', 'FAIL beta', 'PASS  extra', 'noise'])` → `{'passed': 1, 'failed': 1}`.

*Source: gauntlex/15-testing/258-flaky-detector/README.md*

### 258 — Measure the Failure Rate

## Description
Repeated test runs can reveal instability. Summarize the proportion of unsuccessful runs rather than the count alone.

## Requirements
- Implement `failure_rate(results)` in `starter/solution.py`.
- Accept a sequence of booleans where `True` means success and `False` means failure.
- Return the number of failures divided by the number of runs.
- Return `0.0` when there are no runs.
- Do not change the results.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why does a fraction make results comparable across different run counts?

## Example Behavior
`failure_rate([True, False, False, True])` → `0.5`; `failure_rate([])` → `0.0`.

*Source: gauntlex/15-testing/259-test-selection/README.md*

### 259 — Select by Name

## Description
Large test suites often need a focused subset. Match a search term within test names without changing their original spelling or order.

## Requirements
- Implement `select_tests(names, pattern)` in `starter/solution.py`.
- Accept test names and a substring pattern.
- Match the pattern case-insensitively anywhere in each name.
- Return matching original names in their input order.
- An empty pattern matches every name.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why should the output preserve the original capitalization?

## Example Behavior
`select_tests(['TestLogin', 'testCart', 'LOGIN_FLOW'], 'login')` → `['TestLogin', 'LOGIN_FLOW']`.

*Source: gauntlex/15-testing/260-test-summary/README.md*

### 260 — Three Outcomes

## Description
Summarize a test run that can pass, fail, or skip individual cases. A complete report includes zero counts for absent outcomes.

## Requirements
- Implement `test_summary(records)` in `starter/solution.py`.
- Accept dictionaries containing a `status` of `pass`, `fail`, or `skip`.
- Count records for each status and the total number of records.
- Return a dictionary with counts for all three statuses and `total`, even when some counts are zero.
- Return all zero counts for empty input.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why are explicit zero counts useful for reporting?

## Example Behavior
One pass and one skip produce counts `pass: 1`, `fail: 0`, `skip: 1`, and `total: 2`.

*Source: gauntlex/15-testing/261-pytest-nodeid/README.md*

### 261 — Identify a Test

## Description
A test identifier combines the file location and test function name. Validate both parts before building the identifier.

## Requirements
- Implement `pytest_nodeid(path, test_name)` in `starter/solution.py`.
- Strip surrounding whitespace from `path` and `test_name`.
- Raise `ValueError` if either is empty after stripping.
- Return the exact form `path::test_name` using the trimmed parts.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why must both parts be validated before joining them?

## Example Behavior
`pytest_nodeid(' tests/test_math.py ', ' test_sum ')` → `'tests/test_math.py::test_sum'`.

*Source: gauntlex/15-testing/262-test-name-normalize/README.md*

### 262 — Name a Test Function

## Description
Turn a human-readable ASCII title into a predictable pytest-style function name, avoiding repeated or trailing separators.

## Requirements
- Implement `normalize_test_name(title)` in `starter/solution.py`.
- Lowercase the ASCII title.
- Replace each run of nonalphanumeric characters with one underscore.
- Trim leading and trailing underscores from the normalized title.
- Prefix the result with `test_`, or return `test_unnamed` when no alphanumeric characters remain.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why should consecutive punctuation marks become a single separator?

## Example Behavior
`normalize_test_name('  Save & Load! ')` → `'test_save_load'`; `normalize_test_name('!!!')` → `'test_unnamed'`.

*Source: gauntlex/15-testing/263-coverage-percent/README.md*

### 263 — Coverage Ratio

## Description
Line coverage reports the fraction of measurable lines exercised by tests. Validate the counts and define what an empty project means.

## Requirements
- Implement `coverage_percent(covered, total)` in `starter/solution.py`.
- Accept nonnegative integer counts `covered` and `total` with `covered <= total`.
- Return the covered percentage as a float between `0.0` and `100.0`.
- Return `100.0` when `total` is zero.
- Raise `ValueError` for negative counts or when covered exceeds total.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why does an empty denominator need an explicit convention?

## Example Behavior
`coverage_percent(3, 4)` → `75.0`; `coverage_percent(0, 0)` → `100.0`.

*Source: gauntlex/15-testing/264-regression-check/README.md*

### 264 — Spot Regressions

## Description
A regression occurs when a previously passing test now fails. Compare two test runs while excluding tests that were not present in both.

## Requirements
- Implement `regressions(baseline, current)` in `starter/solution.py`.
- Accept mappings from test names to boolean pass results for baseline and current runs.
- Include only names present in both mappings that changed from `True` to `False`.
- Return matching test names in sorted order.
- Ignore newly added or removed tests.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why is a new failing test not necessarily a regression relative to the baseline?

## Example Behavior
`regressions({'a': True, 'b': False}, {'a': False, 'b': False})` → `['a']`.

*Source: gauntlex/15-testing/265-test-matrix/README.md*

### 265 — Cross-Platform Failures

## Description
A test suite may run on several platforms. Identify any test that failed on at least one platform, regardless of its results elsewhere.

## Requirements
- Implement `test_matrix(results)` in `starter/solution.py`.
- Accept a mapping from platform names to mappings of test names to boolean results.
- Include a test name if any platform records `False` for that test.
- Return unique failing names sorted alphabetically.
- Return `[]` when no failures are recorded.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why does one failure matter even if other platforms pass?

## Example Behavior
`test_matrix({'linux': {'a': True}, 'windows': {'a': False, 'b': True}})` → `['a']`.

*Source: gauntlex/15-testing/266-mutation-survivors/README.md*

### 266 — Undetected Mutations

## Description
Mutation testing changes a program deliberately to see whether tests detect the change. A mutant survives when every supplied test still passes.

## Requirements
- Implement `surviving_mutants(results)` in `starter/solution.py`.
- Accept a mapping from mutant IDs to lists of boolean test outcomes.
- Return sorted mutant IDs whose entire outcome list contains only `True`.
- Treat an empty outcome list as surviving, because no test detected the mutant.
- Return `[]` when no mutants survive.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why does a mutant with no test outcomes count as undetected?

## Example Behavior
`surviving_mutants({'m1': [True, True], 'm2': [True, False], 'm3': []})` → `['m1', 'm3']`.

*Source: gauntlex/15-testing/267-test-case-ids/README.md*

### 267 — Unique Case Labels

## Description
Repeated test names need distinct identifiers so reports can refer to each occurrence without ambiguity.

## Requirements
- Implement `case_ids(cases)` in `starter/solution.py`.
- Accept test case dictionaries containing a string `name`.
- Assign each name its own one-based occurrence counter.
- Return IDs in original case order, formatted as `name#N`.
- Do not mutate case dictionaries.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why must different names have independent counters?

## Example Behavior
`case_ids([{'name': 'a'}, {'name': 'b'}, {'name': 'a'}])` → `['a#1', 'b#1', 'a#2']`.

*Source: gauntlex/15-testing/268-snapshot-compare/README.md*

### 268 — Compare Stable Snapshots

## Description
Structured snapshots should be compared using a canonical JSON representation so irrelevant object-key ordering does not cause false mismatches.

## Requirements
- Implement `snapshot_matches(actual, expected)` in `starter/solution.py`.
- Accept two JSON-compatible Python values.
- Compare their compact JSON representations with object keys sorted.
- Return `True` only when the canonical representations match exactly.
- Treat dictionary key order as irrelevant but list element order as significant.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why should object keys and array elements be treated differently?

## Example Behavior
`snapshot_matches({'b': 2, 'a': 1}, {'a': 1, 'b': 2})` → `True`.

*Source: gauntlex/15-testing/269-test-duration/README.md*

### 269 — Find Slow Cases

## Description
Performance reports can prioritize slow tests. Select only tests exceeding a threshold and rank them predictably.

## Requirements
- Implement `slow_tests(records, threshold)` in `starter/solution.py`.
- Accept `[name, duration_seconds]` pairs and a nonnegative threshold.
- Include only names whose duration is strictly greater than the threshold.
- Sort qualifying tests by duration descending, then name ascending.
- Return the names only.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why does a duration equal to the threshold not qualify?

## Example Behavior
`slow_tests([['a', 2], ['b', 3], ['c', 3]], 2)` → `['b', 'c']`.

*Source: gauntlex/15-testing/270-assert-subset/README.md*

### 270 — Require Every Item

## Description
An assertion can check whether all expected items appear in an actual collection. When the check fails, report the missing values in a reproducible order.

## Requirements
- Implement `assert_subset(expected_items, actual_items)` in `starter/solution.py`.
- Accept collections of sortable, hashable elements.
- Return `None` if every expected item is present in the actual collection.
- Otherwise raise `AssertionError` whose message includes a sorted list of missing items.
- Do not mutate either input.
- Use Python's standard library only; do not print or mutate inputs.

## Tips
- Why is sorting useful for reproducible failure messages?

## Example Behavior
`assert_subset([1, 2], [1, 2, 3])` → `None`; missing expected items trigger `AssertionError`.

---

## Packaging

*Source: gauntlex/16-packaging/271-semver-parse/README.md*

### 271 — Three-Part Version

## Description
Package releases often use three numeric components: major, minor, and patch. Parse this precise version form without silently accepting ambiguous formatting.

## Requirements
- Implement `parse_version(text)` in `starter/solution.py`.
- Accept exactly `MAJOR.MINOR.PATCH` with three nonnegative decimal integers.
- Reject leading zeros in multi-digit components; `0` itself is valid.
- Return `[major, minor, patch]` as integers.
- Raise `ValueError` for missing, extra, negative, or malformed components.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why is strict validation preferable to guessing what a malformed version means?

## Example Behavior
`parse_version('2.10.3')` → `[2, 10, 3]`; `parse_version('01.2.3')` raises `ValueError`.

*Source: gauntlex/16-packaging/272-semver-compare/README.md*

### 272 — Version Ordering

## Description
Version components represent numeric precedence, not ordinary string order. Compare major, minor, and patch numbers in significance order.

## Requirements
- Implement `compare_version(a, b)` in `starter/solution.py`.
- Accept two valid three-part versions without prerelease or build suffixes.
- Return `-1` if the first version is older, `0` if equal, and `1` if newer.
- Compare components numerically in major, minor, then patch order.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why does `1.10.0` come after `1.9.0`?

## Example Behavior
`compare_version('1.9.0', '1.10.0')` → `-1`; `compare_version('2.0.0', '2.0.0')` → `0`.

*Source: gauntlex/16-packaging/273-dependency-parse/README.md*

### 273 — Pinned Dependency

## Description
A pinned dependency specifies one package and one exact version. Normalize the package name while retaining the version text.

## Requirements
- Implement `parse_requirement(text)` in `starter/solution.py`.
- Accept exactly `name==version`.
- Allow ASCII letters, digits, underscores, and hyphens in the name.
- Require three dot-separated nonnegative integer components in the version.
- Return `[normalized_name, version]` where the name is lowercase and underscores become hyphens.
- Raise `ValueError` for invalid input.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why should package-name normalization be distinct from version validation?

## Example Behavior
`parse_requirement('My_Pkg==1.2.3')` → `['my-pkg', '1.2.3']`.

*Source: gauntlex/16-packaging/274-requirements-sort/README.md*

### 274 — Dependency Order

## Description
A dependency file can be made easier to review by sorting package entries consistently, while preserving their original spelling and version text.

## Requirements
- Implement `sort_requirements(lines)` in `starter/solution.py`.
- Accept valid exact requirement strings `name==version`.
- Sort requirements by their normalized package names.
- Return the original requirement strings, not rewritten versions.
- Do not mutate the original sequence.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why should the comparison key differ from the text returned to the caller?

## Example Behavior
`sort_requirements(['Zed==1.0.0', 'alpha==2.0.0'])` → `['alpha==2.0.0', 'Zed==1.0.0']`.

*Source: gauntlex/16-packaging/275-requirements-dedupe/README.md*

### 275 — One Requirement per Package

## Description
A dependency list may mention the same normalized package multiple times. Keep the final declaration for each package while preserving surviving declaration order.

## Requirements
- Implement `dedupe_requirements(lines)` in `starter/solution.py`.
- Accept valid exact requirement strings.
- Treat names as equivalent after lowercase conversion and replacing underscores with hyphens.
- Keep only the last occurrence of each normalized package name.
- Return surviving original lines ordered by their last positions.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why would keeping the first occurrence violate the intended override behavior?

## Example Behavior
`dedupe_requirements(['A==1.0.0', 'b==1.0.0', 'a==2.0.0'])` → `['b==1.0.0', 'a==2.0.0']`.

*Source: gauntlex/16-packaging/276-env-config/README.md*

### 276 — Read Environment Settings

## Description
Application configuration often arrives as text from environment variables. Interpret the supported values while applying a safe default only when a setting is absent.

## Requirements
- Implement `read_config(env)` in `starter/solution.py`.
- Accept a mapping of environment variable names to strings.
- Return a dictionary with boolean `debug` and integer `port`.
- Set `debug` to `True` for `DEBUG` values `1`, `true`, or `yes`, ignoring case; otherwise `False`.
- Use port `8000` when `PORT` is absent.
- Raise `ValueError` unless a supplied port is an integer from 1 through 65535.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why should an invalid supplied port not silently fall back to the default?

## Example Behavior
`read_config({'DEBUG': 'YES', 'PORT': '9000'})` → `{'debug': True, 'port': 9000}`.

*Source: gauntlex/16-packaging/277-config-merge/README.md*

### 277 — Apply Overrides

## Description
Default configuration defines which settings an application recognizes. Apply only permitted overrides and keep both source mappings intact.

## Requirements
- Implement `merge_config(defaults, overrides)` in `starter/solution.py`.
- Return a new dictionary containing the defaults with recognized overrides applied.
- Allow an override only if its key already exists in `defaults`.
- Ignore unknown override keys.
- Do not mutate either input mapping.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why might allowing unknown keys unexpectedly change application behavior?

## Example Behavior
`merge_config({'port': 8000}, {'port': 9000, 'unknown': 1})` → `{'port': 9000}`.

*Source: gauntlex/16-packaging/278-file-manifest/README.md*

### 278 — Describe Build Files

## Description
A build manifest records the files included in an artifact and their byte counts. Reject paths that could escape the intended relative directory.

## Requirements
- Implement `file_manifest(entries)` in `starter/solution.py`.
- Accept `[relative_path, bytes_count]` pairs.
- Reject absolute paths and paths containing a complete `..` segment with `ValueError`.
- Return sorted strings formatted `path<TAB>bytes`.
- Do not modify the entries.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why is a `..` path component different from two dots inside a filename?

## Example Behavior
`file_manifest([['b.txt', 2], ['a.txt', 5]])` → `['a.txt\t5', 'b.txt\t2']`.

*Source: gauntlex/16-packaging/279-release-notes/README.md*

### 279 — Write a Release Note

## Description
Turn a version identifier and change descriptions into a short, predictable Markdown announcement.

## Requirements
- Implement `release_notes(version, changes)` in `starter/solution.py`.
- Begin with the exact heading `# Release VERSION`.
- When changes exist, follow the heading with a blank line and one `- CHANGE` line per entry.
- End the result with a newline.
- When no changes exist, return only the heading and one newline.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why is the empty-change case formatted differently from a release with entries?

## Example Behavior
`release_notes('1.0.0', ['Initial release'])` → `'# Release 1.0.0\n\n- Initial release\n'`.

*Source: gauntlex/16-packaging/280-changelog-groups/README.md*

### 280 — Organize Changes

## Description
Release changes can be grouped by category for easier reading without changing the order in which changes were supplied.

## Requirements
- Implement `group_changes(entries)` in `starter/solution.py`.
- Accept `[category, description]` pairs.
- Return a dictionary mapping each category to its list of descriptions.
- Preserve original description order within each category.
- Do not discard earlier descriptions when a category repeats.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why does assigning a new list for every repeated category lose information?

## Example Behavior
`group_changes([['fix', 'A'], ['feat', 'B'], ['fix', 'C']])` → `{'fix': ['A', 'C'], 'feat': ['B']}`.

*Source: gauntlex/16-packaging/281-python-entrypoint/README.md*

### 281 — Name the Entry Point

## Description
A command-line entry point refers to a Python module and the function to execute. Validate a dotted module path before adding the function reference.

## Requirements
- Implement `entrypoint_name(module_name)` in `starter/solution.py`.
- Accept a nonempty dotted module name.
- Require every dot-separated component to be a valid Python identifier.
- Return `module.path:main` using the original valid module name.
- Raise `ValueError` for empty names or invalid components.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why is validating each component more reliable than checking only the full string?

## Example Behavior
`entrypoint_name('package.cli')` → `'package.cli:main'`; `entrypoint_name('package..cli')` raises `ValueError`.

*Source: gauntlex/16-packaging/282-module-path/README.md*

### 282 — Module to File

## Description
A Python module's dotted import path corresponds to directories and a source filename. Convert the module name into a relative POSIX file path.

## Requirements
- Implement `module_to_path(module_name)` in `starter/solution.py`.
- Accept a dotted module name.
- Require every component to be a valid Python identifier.
- Replace module separators with forward slashes and append `.py`.
- Raise `ValueError` for empty or invalid components.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why must dots become path separators rather than remain in the filename?

## Example Behavior
`module_to_path('package.tools.cli')` → `'package/tools/cli.py'`.

*Source: gauntlex/16-packaging/283-artifact-name/README.md*

### 283 — Wheel Filename

## Description
A Python wheel filename encodes the distribution, version, and compatibility tags. Assemble the expected filename from trusted components.

## Requirements
- Implement `wheel_name(name, version, python_tag)` in `starter/solution.py`.
- Accept trusted, nonempty package name, version, and Python tag strings.
- Convert hyphens in the package name to underscores.
- Return `NAME-VERSION-TAG-none-any.whl` using the converted name.
- Do not alter the version or Python tag.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why is the distribution name represented differently inside a wheel filename?

## Example Behavior
`wheel_name('my-package', '1.2.0', 'py3')` → `'my_package-1.2.0-py3-none-any.whl'`.

*Source: gauntlex/16-packaging/284-build-metadata/README.md*

### 284 — Package Metadata

## Description
Build a small package metadata record that does not unexpectedly change when the caller later edits its dependency list.

## Requirements
- Implement `build_metadata(name, version, minimum_python, dependencies)` in `starter/solution.py`.
- Return a dictionary with keys `name`, `version`, `requires_python`, and `dependencies`.
- Set `requires_python` from `minimum_python`.
- Copy the supplied dependency list into the result.
- Do not mutate the input list or retain it by reference.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why can sharing a mutable dependency list cause unexpected changes after the function returns?

## Example Behavior
`build_metadata('demo', '1.0.0', '>=3.10', ['requests'])` returns the four metadata fields and an independent dependency list.

*Source: gauntlex/16-packaging/285-release-checklist/README.md*

### 285 — Release Readiness

## Description
A release should proceed only when its required checks are complete. Report missing steps in a consistent order.

## Requirements
- Implement `release_checklist(tests_passed, docs_updated, version_bumped)` in `starter/solution.py`.
- Accept booleans `tests_passed`, `docs_updated`, and `version_bumped`.
- For each false condition, include its corresponding action: `run tests`, `update docs`, or `bump version`.
- Return missing actions in that exact order.
- Return `[]` when every condition is true.
- Use Python's standard library only; do not print or mutate caller-owned collections.

## Tips
- Why is a fixed checklist order useful for repeatable release reviews?

## Example Behavior
`release_checklist(False, True, False)` → `['run tests', 'bump version']`; all true → `[]`.

---

## Architecture

*Source: gauntlex/17-architecture/286-dependency-order/README.md*

### 286 — Build in Dependency Order

## Description
A build system must complete prerequisites before their dependents. Produce a deterministic sequence even when several tasks are ready simultaneously.

## Requirements
- Implement `dependency_order(graph)` in `starter/solution.py`.
- Accept a mapping of task names to prerequisite-name lists.
- Include tasks mentioned only as prerequisites.
- Return a topological ordering with every prerequisite before its dependent.
- When several tasks are ready, choose the lexicographically smallest available name.
- Raise `ValueError` if any cycle makes completion impossible.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
A task mentioned only as a prerequisite must still appear in the final order; disconnected tasks also belong in the result.

## Tips
- Why does choosing among ready tasks require a consistent rule?

## Example Behavior
For `{'app': ['lib'], 'lib': []}`, return `['lib', 'app']`.

*Source: gauntlex/17-architecture/287-dependency-cycles/README.md*

### 287 — Find Dependency Loops

## Description
Circular prerequisites prevent any valid build order. Detect a cycle even when some nodes appear only in other tasks' dependency lists.

## Requirements
- Implement `has_dependency_cycle(graph)` in `starter/solution.py`.
- Accept a directed mapping of tasks to prerequisites.
- Return `True` if any directed cycle exists; otherwise `False`.
- Include names appearing only as prerequisites.
- Do not change the graph.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
A self-dependency is a cycle, while two separate branches that converge on the same prerequisite are not.

## Tips
- Why is revisiting a fully explored node different from revisiting an active path?

## Example Behavior
`has_dependency_cycle({'a': ['b'], 'b': ['a']})` → `True`.

*Source: gauntlex/17-architecture/288-reachable-services/README.md*

### 288 — Downstream Reachability

## Description
A service dependency graph can show which components may be reached from one starting point. Explore transitively without looping forever.

## Requirements
- Implement `reachable_services(graph, start)` in `starter/solution.py`.
- Accept a mapping from service names to lists of downstream services and a start name.
- Include the start itself, even if it is not a graph key.
- Return every reachable service name once, sorted alphabetically.
- Handle cycles without infinite traversal.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
A start node absent from the graph still produces a one-item result containing that start name.

## Tips
- Why must visited services be tracked?

## Example Behavior
`reachable_services({'a': ['b'], 'b': ['c']}, 'a')` → `['a', 'b', 'c']`.

*Source: gauntlex/17-architecture/289-reverse-dependencies/README.md*

### 289 — Who Depends on This?

## Description
A dependency graph points from packages to their requirements. Reverse those relationships to find the direct dependents of each package.

## Requirements
- Implement `reverse_dependencies(graph)` in `starter/solution.py`.
- Accept a mapping from package names to dependency-name lists.
- Include every name occurring as a key or dependency.
- Return a dictionary mapping each name to a sorted list of its direct dependents.
- Include empty lists for names with no dependents.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
A package listed as a prerequisite by several packages must list each direct dependent, not indirect dependents.

## Tips
- Why should a dependency-only package still appear in the result?

## Example Behavior
`reverse_dependencies({'app': ['core'], 'tool': ['core']})` → `{'app': [], 'tool': [], 'core': ['app', 'tool']}`.

*Source: gauntlex/17-architecture/290-service-layers/README.md*

### 290 — Build in Parallel Layers

## Description
Independent services can be built in parallel once all their prerequisites are complete. Group services by the earliest layer in which they become ready.

## Requirements
- Implement `service_layers(graph)` in `starter/solution.py`.
- Accept a mapping of services to prerequisite-name lists.
- Include names that occur only as prerequisites.
- Return successive layers, each a sorted list of all services ready at that stage.
- Place each service after every prerequisite.
- Raise `ValueError` if a dependency cycle exists.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
Independent services are grouped in the same layer; a service may enter only after all its prerequisites are in earlier layers.

## Tips
- Why should all currently ready services share a layer?

## Example Behavior
`service_layers({'app': ['db', 'api'], 'api': []})` → `[['api', 'db'], ['app']]`.

*Source: gauntlex/17-architecture/291-feature-flags/README.md*

### 291 — Transitive Feature Gates

## Description
A feature may be enabled by its own flag yet unavailable because a required feature is disabled. Resolve every prerequisite before reporting usable features.

## Requirements
- Implement `enabled_features(flags, dependencies)` in `starter/solution.py`.
- Accept mappings of feature flags and dependency lists.
- Include a feature only if its own flag and every transitive dependency flag are `True`.
- Treat missing flags as `False`.
- Assume dependencies are acyclic.
- Return sorted enabled feature names.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
A feature's own flag is not sufficient: every dependency in its chain must also be enabled. A missing dependency flag disables the feature.

## Tips
- Why does checking only a feature's own flag miss disabled prerequisites?

## Example Behavior
With `{'a': True, 'b': False}` and `{'a': ['b']}`, feature `a` is not enabled.

*Source: gauntlex/17-architecture/292-route-match/README.md*

### 292 — Capture Route Parameters

## Description
HTTP route templates combine fixed path segments with named placeholders. Match a request path and extract the placeholder values.

## Requirements
- Implement `match_route(template, path)` in `starter/solution.py`.
- Accept a route template and request path.
- Require the same number of path segments.
- Match literal segments exactly; capture segments written `{name}` as dictionary entries.
- Return captured values on a match, or `None` on mismatch.
- Do not percent-decode path text.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
A literal path segment cannot match a different spelling. Capture parameters as raw strings without decoding or numeric conversion.

## Tips
- Why must a literal route segment match exactly?

## Example Behavior
`match_route('/users/{id}', '/users/42')` → `{'id': '42'}`.

*Source: gauntlex/17-architecture/293-route-priority/README.md*

### 293 — Route Specificity

## Description
Routes with more fixed path segments are more specific than routes dominated by placeholders. Calculate a simple specificity score.

## Requirements
- Implement `route_priority(template)` in `starter/solution.py`.
- Split the template into path segments, ignoring empty segments from leading or trailing slashes.
- Count each literal segment as one point.
- Treat a segment as dynamic only when it starts with `{` and ends with `}`.
- Return the integer literal-segment count.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
Count only complete fixed segments. A segment beginning with `{` and ending with `}` is dynamic even when its contents are unusual.

## Tips
- Why is a placeholder less specific than a fixed path segment?

## Example Behavior
`route_priority('/users/{id}/posts')` → `2`.

*Source: gauntlex/17-architecture/294-rate-limit-window/README.md*

### 294 — Requests in a Time Window

## Description
A sliding-window rate limit counts recent requests to decide whether another request is permitted. Boundary handling must be exact.

## Requirements
- Implement `rate_limit_allowed(timestamps, now, window, limit)` in `starter/solution.py`.
- Accept sorted integer timestamps, integer `now`, positive `window`, and nonnegative `limit`.
- Count timestamps in the interval `(now - window, now]`.
- Return `True` only when that count is strictly less than `limit`.
- Do not mutate timestamps.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
A request exactly at `now - window` is outside the window; a request exactly at `now` is inside. The next request is permitted only below the limit.

## Tips
- Why is the lower boundary excluded but the upper included?

## Example Behavior
`rate_limit_allowed([5, 8, 10], 10, 5, 3)` → `True`, because time 5 is excluded.

*Source: gauntlex/17-architecture/295-circuit-state/README.md*

### 295 — Circuit Breaker States

## Description
A circuit breaker tracks consecutive failures and may allow a recovery probe. Classify the state from the failure threshold and probe result.

## Requirements
- Implement `circuit_state(failures, threshold, probe_success)` in `starter/solution.py`.
- Accept a failure count, positive threshold, and boolean `probe_success`.
- Return `'closed'` when failures are below the threshold.
- At or above the threshold, return `'half-open'` for a successful probe, otherwise `'open'`.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
When failures are below threshold, the state remains closed regardless of probe outcome; the probe matters only at or above threshold.

## Tips
- Why must the failure threshold be checked before the probe outcome?

## Example Behavior
`circuit_state(3, 3, False)` → `'open'`; `circuit_state(3, 3, True)` → `'half-open'`.

*Source: gauntlex/17-architecture/296-cache-expiry/README.md*

### 296 — Time to Live

## Description
Cached data has a limited lifetime. Determine whether an entry remains usable at a given moment, including the exact expiry boundary.

## Requirements
- Implement `cache_valid(created_at, ttl, now)` in `starter/solution.py`.
- Accept creation time, positive time-to-live (`ttl`), and current time.
- Return `True` only while `now` is strictly earlier than `created_at + ttl`.
- Return `False` at or after the expiry instant.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
At the precise expiry instant the entry is no longer valid; no grace period is implied.

## Tips
- Why should an entry expire exactly when its lifetime is exhausted?

## Example Behavior
`cache_valid(100, 30, 129)` → `True`; `cache_valid(100, 30, 130)` → `False`.

*Source: gauntlex/17-architecture/297-cache-eviction/README.md*

### 297 — Evict the Oldest

## Description
A bounded cache must discard entries when its capacity is exceeded. Prefer the least recently accessed entries and break ties consistently.

## Requirements
- Implement `eviction_candidates(accesses, max_items)` in `starter/solution.py`.
- Accept a mapping from cache keys to integer last-access timestamps and a nonnegative maximum item count.
- Return only enough keys to reduce the cache to that maximum.
- Order eviction candidates by oldest access time, then alphabetically by key.
- Return `[]` when the cache is already within capacity.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
The number of returned keys is the excess over capacity, not the capacity itself. Tied timestamps use alphabetical key order.

## Tips
- Why must tied access times use a secondary sort order?

## Example Behavior
With `{'b': 1, 'a': 1, 'c': 3}` and a limit of 1, evict `['a', 'b']`.

*Source: gauntlex/17-architecture/298-health-rollup/README.md*

### 298 — Worst Service Health

## Description
A system-wide health summary should reflect its most severe service condition. Combine individual statuses into one result.

## Requirements
- Implement `health_rollup(statuses)` in `starter/solution.py`.
- Accept service statuses `'ok'`, `'degraded'`, and `'down'`.
- Return `'down'` if any service is down.
- Otherwise return `'degraded'` if any service is degraded.
- Return `'ok'` when every service is healthy or the list is empty.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
The summary reflects the most severe status, not the most common one. An empty service list has the defined status `ok`.

## Tips
- Why should one down service dominate the overall status?

## Example Behavior
`health_rollup(['ok', 'degraded'])` → `'degraded'`; `health_rollup([])` → `'ok'`.

*Source: gauntlex/17-architecture/299-retry-budget/README.md*

### 299 — Protect the Retry Budget

## Description
Retries consume resources and should remain proportional to normal request traffic. Calculate how many attempts are still permitted.

## Requirements
- Implement `retry_budget(requests, ratio, retries_used)` in `starter/solution.py`.
- Accept nonnegative request count, retry ratio, and retries already used.
- Compute the allowed retry count as the floor of `requests * ratio`.
- Subtract used retries and never return a negative number.
- Return the remaining retry count as an integer.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
The retry allowance is rounded down before subtracting used attempts; exhausted budgets return zero rather than a negative count.

## Tips
- Why should a retry budget never become negative?

## Example Behavior
`retry_budget(10, 0.3, 1)` → `2`.

*Source: gauntlex/17-architecture/300-idempotency-key/README.md*

### 300 — Identify Duplicate Requests

## Description
Logically identical requests need a stable identifier even when their method capitalization differs. Canonicalize request data before hashing.

## Requirements
- Implement `idempotency_key(method, url, body)` in `starter/solution.py`.
- Accept a method, URL, and request body string.
- Uppercase the method.
- Serialize `[method, url, body]` as compact JSON in that order.
- Hash the UTF-8 JSON bytes with SHA-256.
- Return the lowercase hexadecimal digest.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
The JSON array field order matters. Method case is normalized, but URL and body text remain unchanged.

## Tips
- Why is structured serialization safer than concatenating fields?

## Example Behavior
Requests with methods `'post'` and `'POST'` and otherwise identical inputs must produce the same key.

*Source: gauntlex/17-architecture/301-partition-key/README.md*

### 301 — Choose a Stable Partition

## Description
Distributed storage often assigns records to partitions using a repeatable hash. The same identifier must map to the same partition across processes.

## Requirements
- Implement `partition_key(identifier, partition_count)` in `starter/solution.py`.
- Accept a nonempty identifier string and a positive partition count.
- Hash the identifier's UTF-8 bytes with SHA-256.
- Interpret the digest as one unsigned big-endian integer.
- Return that integer modulo the partition count.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
Use a deterministic byte representation and digest interpretation; the partition number must remain within the valid zero-based range.

## Tips
- Why is Python's built-in hash unsuitable for stable cross-process partitioning?

## Example Behavior
For any valid input, the returned partition is an integer from `0` through `partition_count - 1`.

*Source: gauntlex/17-architecture/302-event-dedup/README.md*

### 302 — Keep First Events

## Description
An event stream may contain duplicate deliveries. Keep the first occurrence of each event ID and preserve event order.

## Requirements
- Implement `deduplicate_events(events)` in `starter/solution.py`.
- Accept event dictionaries with string `id` fields.
- Return the first event for each distinct ID in original order.
- Return shallow copies of retained event dictionaries.
- Do not mutate the original events or allow later duplicates to overwrite earlier ones.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
Retain the first dictionary for each ID as a shallow copy. Changing the returned dictionary must not change the original top-level event.

## Tips
- Why should the first occurrence win rather than the last?

## Example Behavior
Events with IDs `a`, `b`, `a` produce two retained events, ordered `a`, `b`.

*Source: gauntlex/17-architecture/303-event-projection/README.md*

### 303 — Rebuild Account Balances

## Description
Event-sourced state can be rebuilt by applying recorded changes. Derive each account's current balance from its event deltas.

## Requirements
- Implement `project_balances(events)` in `starter/solution.py`.
- Accept events containing `id`, string `account`, and integer `delta` fields; IDs are unique.
- Accumulate deltas for each account in event order, beginning from zero.
- Return a dictionary from account names to integer balances.
- Keep accounts whose net balance is zero in the result.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
A zero net balance is still a meaningful account result. Events are applied in their supplied order without requiring a database.

## Tips
- Why should an account remain present when its total returns to zero?

## Example Behavior
`project_balances([{'id': '1', 'account': 'a', 'delta': 3}, {'id': '2', 'account': 'a', 'delta': -3}])` → `{'a': 0}`.

*Source: gauntlex/17-architecture/304-replay-dedup/README.md*

### 304 — Replay Exactly Once

## Description
Repeated delivery must not apply the same account event more than once. Rebuild balances while treating each event ID as unique.

## Requirements
- Implement `replay_unique(events)` in `starter/solution.py`.
- Accept events with string `id`, account, and integer delta fields.
- Apply only the first occurrence of each event ID.
- Sum retained deltas by account, starting from zero.
- Return final balances, including accounts with zero totals.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
Duplicate event IDs are ignored even if later deliveries contain different account or delta values; the first delivery wins.

## Tips
- Why must deduplication happen before updating balances?

## Example Behavior
Two deliveries of `{'id': 'x', 'account': 'a', 'delta': 5}` produce balance `{'a': 5}`, not `{'a': 10}`.

*Source: gauntlex/17-architecture/305-config-diff/README.md*

### 305 — Configuration Changes

## Description
Configuration drift can come from changed values, added settings, or removed settings. Report every key that differs between two snapshots.

## Requirements
- Implement `config_diff(old, new)` in `starter/solution.py`.
- Accept old and new dictionaries.
- Return sorted keys whose values differ or whose presence differs.
- Treat a missing key as different from a present key whose value is `None`.
- Do not mutate either dictionary.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
A missing key is not equivalent to a present key whose value is `None`; report the key as changed.

## Tips
- Why is missing different from explicitly configured `None`?

## Example Behavior
`config_diff({'a': None}, {})` → `['a']`.

*Source: gauntlex/17-architecture/306-permission-check/README.md*

### 306 — Permission by Role

## Description
Role-based access control grants actions through assigned roles. Determine whether any known role explicitly authorizes a requested permission.

## Requirements
- Implement `has_permission(role_permissions, user_roles, permission)` in `starter/solution.py`.
- Accept a mapping from roles to permission lists, assigned user roles, and a requested permission.
- Return `True` if at least one assigned role includes that permission.
- Treat unknown roles as granting nothing.
- Return `False` when no assigned role grants the permission.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
Permission checks use direct grants from assigned roles only. Unknown roles grant nothing, and a missing permission is denied.

## Tips
- Why must an unknown role never grant permissions by default?

## Example Behavior
`has_permission({'editor': ['write']}, ['editor'], 'write')` → `True`.

*Source: gauntlex/17-architecture/307-permission-inherit/README.md*

### 307 — Inherited Permissions

## Description
Roles can inherit permissions from parent roles. Collect all permissions granted directly or transitively through the hierarchy.

## Requirements
- Implement `effective_permissions(role_permissions, parents, assigned)` in `starter/solution.py`.
- Accept role-to-permissions mapping, role-to-parent-roles mapping, and assigned roles.
- Include permissions of every assigned role and all transitive ancestor roles.
- Assume the parent-role graph is acyclic.
- Return a sorted list of unique permission strings.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
Permissions flow through every ancestor role, not only direct parents. Multiple inheritance paths must not duplicate permissions.

## Tips
- Why can one role inherit permissions through several levels?

## Example Behavior
If `admin` inherits `editor` and `editor` grants `write`, an assigned `admin` role includes `write`.

*Source: gauntlex/17-architecture/308-audit-record/README.md*

### 308 — Record an Action

## Description
Audit records should capture who performed an action, what they did, which resource was involved, and when it occurred. Use caller-supplied facts without inventing new ones.

## Requirements
- Implement `audit_record(actor, action, resource, timestamp)` in `starter/solution.py`.
- Accept `actor`, `action`, `resource`, and `timestamp`.
- Return a dictionary with exactly those four keys and their supplied values.
- Use the caller's timestamp; do not generate the current time.
- Do not modify the supplied values.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
The record contains exactly the supplied four facts. Do not generate a timestamp or add implicit metadata.

## Tips
- Why should the audit function not substitute its own timestamp?

## Example Behavior
`audit_record('ada', 'edit', 'doc-1', '2026-01-01')` → `{'actor': 'ada', 'action': 'edit', 'resource': 'doc-1', 'timestamp': '2026-01-01'}`.

*Source: gauntlex/17-architecture/309-error-envelope/README.md*

### 309 — Structured Errors

## Description
A consistent error response lets callers inspect an error code, message, and optional details without guessing the shape of the result.

## Requirements
- Implement `error_envelope(code, message, details)` in `starter/solution.py`.
- Accept error code, message, and optional details mapping.
- Return `{'error': {'code': code, 'message': message, 'details': details}}`.
- Use an empty dictionary when details is `None`.
- Copy provided details so later caller changes do not alter the returned response.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
The nested `details` mapping must be a new dictionary, even when the caller supplies one; a missing details argument becomes an empty mapping.

## Tips
- Why is sharing a mutable details dictionary risky?

## Example Behavior
`error_envelope('bad', 'Invalid', None)` → `{'error': {'code': 'bad', 'message': 'Invalid', 'details': {}}}`.

*Source: gauntlex/17-architecture/310-pagination-token/README.md*

### 310 — Opaque Page Cursor

## Description
Pagination APIs can encode a numeric offset into a URL-safe cursor. The token is a representation, not a security boundary.

## Requirements
- Implement `encode_cursor(offset)` in `starter/solution.py`.
- Accept a nonnegative integer offset.
- Raise `ValueError` for a negative offset.
- Encode the offset's ASCII decimal text using URL-safe Base64.
- Remove Base64 padding characters from the returned token.
- Return the result without printing; use Python's standard library only and do not mutate caller-owned collections.

## Design Considerations
The cursor is URL-safe Base64 of decimal text with padding removed. It is an encoding, not encryption or authentication.

## Tips
- Why is URL-safe encoding useful for pagination links?
- Why should the cursor not be treated as encrypted?

## Example Behavior
`encode_cursor(0)` → `'MA'`; `encode_cursor(12)` → `'MTI'`.

---

## File Automation

*Source: gauntlex/19-file-automation/315-safe-relative-path/README.md*

### 315 — Safe Relative Paths

## Description
Paths supplied by users must not escape an intended working directory. Normalize harmless separators while rejecting traversal and absolute locations.

## Requirements
- Implement `safe_relative_path(text)` in `starter/solution.py`.
- Reject empty paths, absolute paths, any `..` component, and any backslash with `ValueError`.
- Ignore `.` components and repeated forward slashes.
- Return the remaining components joined as a POSIX relative path.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Validate path components before simplifying them: normalizing away `..` first would hide an explicitly forbidden traversal attempt. Treat the output as a relative POSIX path, not a filesystem existence check.

## Tips
- Why must traversal be checked before normalization?

## Example Behavior
`safe_relative_path('a//./b.txt')` → `'a/b.txt'`; `safe_relative_path('../secret')` raises `ValueError`.

*Source: gauntlex/19-file-automation/316-file-extension/README.md*

### 316 — Recognize File Extensions

## Description
A file's final suffix can identify its type, but hidden files beginning with a dot need careful treatment.

## Requirements
- Implement `file_extension(filename)` in `starter/solution.py`.
- Return the lowercase final extension, including its leading dot.
- Do not count the leading dot of a dotfile as an extension by itself.
- Return `''` when there is no extension.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Distinguish the leading dot used to hide a file from the separator introducing its final suffix. Preserve only the extension in the return value and normalize its case.

## Tips
- How does `.env` differ from `.env.local`?

## Example Behavior
`file_extension('REPORT.CSV')` → `'.csv'`; `file_extension('.env')` → `''`.

*Source: gauntlex/19-file-automation/317-line-ending-normalize/README.md*

### 317 — One Line Ending

## Description
Text copied between operating systems may contain CRLF, CR, or LF line endings. Standardize line boundaries without modifying other content.

## Requirements
- Implement `normalize_line_endings(text)` in `starter/solution.py`.
- Replace every CRLF and standalone CR line ending with LF.
- Preserve all other characters, including existing LF and trailing newlines.
- Return the normalized text without writing to disk.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Treat CRLF as one boundary before processing lone CR characters; otherwise a single Windows newline could become two line breaks. Preserve the presence or absence of a trailing newline.

## Tips
- Why does handling two-character line endings require care?

## Example Behavior
`normalize_line_endings('a\r\nb\rc\n')` → `'a\nb\nc\n'`.

*Source: gauntlex/19-file-automation/318-parse-ini-section/README.md*

### 318 — Read an INI Section

## Description
Configuration files group assignments under named sections. Read only one section while respecting whitespace and comments.

## Requirements
- Implement `parse_ini_section(text, section)` in `starter/solution.py`.
- Recognize section headers `[name]` and assignments `key=value` in well-formed text.
- Trim surrounding whitespace from keys and values.
- Ignore blank lines and lines beginning `#` or `;`.
- Return entries from the requested section, with later duplicate keys overriding earlier ones.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Track the active section as lines are read, and apply assignments only while the requested section is active. Later duplicate keys in that section replace earlier values.

## Tips
- How can the current section be tracked while reading line by line?

## Example Behavior
`parse_ini_section('[db]\nhost=local\n[app]\nmode=dev', 'db')` → `{'host': 'local'}`.

*Source: gauntlex/19-file-automation/319-json-path-get/README.md*

### 319 — Follow Nested Keys

## Description
Structured data often contains nested mappings. Navigate a dot-separated key path without assuming list indices are supported.

## Requirements
- Implement `json_path_get(data, path)` in `starter/solution.py`.
- An empty path returns the original object.
- For a nonempty path, interpret each dot-separated component as a dictionary key.
- Return `None` when a required key is missing or traversal cannot continue through a dictionary.
- Do not interpret numeric components as list indices.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
At each path component, verify that the current value is a dictionary before attempting key lookup. A dictionary key containing digits is still a key, never a list position.

## Tips
- Why should a missing intermediate key stop traversal?

## Example Behavior
`json_path_get({'user': {'name': 'Ada'}}, 'user.name')` → `'Ada'`; missing path → `None`.

*Source: gauntlex/19-file-automation/320-flatten-json/README.md*

### 320 — Flatten a JSON Tree

## Description
Nested dictionaries can be represented by dotted paths to their leaf values. Flatten the structure without treating lists as subtrees.

## Requirements
- Implement `flatten_json(data)` in `starter/solution.py`.
- Return a dictionary mapping dotted key paths to leaf values.
- Recursively traverse dictionaries, but treat lists and empty dictionaries as leaves.
- Assume keys are nonempty strings without dots.
- Preserve original leaf values.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Differentiate an empty mapping from a nonempty mapping: an empty dictionary is a leaf that must survive flattening. Lists are also opaque values, even when they contain dictionaries.

## Tips
- Why should an empty dictionary remain visible in the flattened result?

## Example Behavior
`flatten_json({'a': {'b': 2}, 'c': []})` → `{'a.b': 2, 'c': []}`.

*Source: gauntlex/19-file-automation/321-unflatten-json/README.md*

### 321 — Rebuild Nested JSON

## Description
Reverse a flat mapping of dotted paths into nested dictionaries, creating intermediate containers only where needed.

## Requirements
- Implement `unflatten_json(data)` in `starter/solution.py`.
- Accept flat keys made of nonempty dot-separated components.
- Construct nested dictionaries for intermediate path components.
- Assign each original leaf value at its final component.
- Assume no conflicting paths such as `a` and `a.b`.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Build intermediate dictionaries only for nonfinal path components, then place the supplied leaf at its terminal key. Rely on the stated absence of prefix conflicts rather than inventing a conflict policy.

## Tips
- What intermediate structure is needed for a key with three components?

## Example Behavior
`unflatten_json({'a.b': 2, 'a.c': 3})` → `{'a': {'b': 2, 'c': 3}}`.

*Source: gauntlex/19-file-automation/322-file-checksum/README.md*

### 322 — Fingerprint a File

## Description
Large files should be hashed without loading all bytes into memory. Compute a content fingerprint from the exact raw byte stream.

## Requirements
- Implement `file_checksum(path)` in `starter/solution.py`.
- Read the file at `path` in bounded chunks.
- Compute SHA-256 over its raw bytes, without text decoding or newline changes.
- Return the lowercase hexadecimal digest.
- Do not modify the file.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Process binary data in bounded chunks and update one ongoing hash state. A checksum must depend on the exact file bytes, including newline encodings, rather than decoded text.

## Tips
- Why must binary file bytes be hashed without text conversion?

## Example Behavior
A file containing the bytes `abc` has SHA-256 digest `ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad`.

*Source: gauntlex/19-file-automation/323-count-file-lines/README.md*

### 323 — Count File Records

## Description
A logical line may end with a newline or at end-of-file. Count both forms correctly when reading UTF-8 text.

## Requirements
- Implement `count_file_lines(path)` in `starter/solution.py`.
- Read a UTF-8 text file.
- Return the number of logical lines, including a final nonempty line without a newline.
- Return zero for an empty file.
- Universal newline handling is permitted.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Count logical records rather than raw newline characters: a final nonempty segment is a line even without a trailing newline. Empty input must not become one phantom line.

## Tips
- Why does counting newline characters alone miss some final lines?

## Example Behavior
A file containing `alpha\nbeta` has two logical lines; an empty file has zero.

*Source: gauntlex/19-file-automation/324-append-jsonl/README.md*

### 324 — Append Structured Records

## Description
JSON Lines stores independent JSON values on separate lines. Append a new value without destroying existing records.

## Requirements
- Implement `append_jsonl(path, value)` in `starter/solution.py`.
- Open or create the UTF-8 file at `path` for appending.
- Serialize the JSON-compatible value in compact JSON with sorted object keys.
- Append exactly one serialized record followed by a newline.
- Return `None` and preserve existing content.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Preserve existing file content and append one complete UTF-8 JSON record per call. Canonical key ordering and compact separators make output stable for downstream consumers.

## Tips
- Why must each appended value end with a newline?

## Example Behavior
Appending `{'b': 2, 'a': 1}` writes `{"a":1,"b":2}\n` at the end of the file.

*Source: gauntlex/19-file-automation/325-read-jsonl/README.md*

### 325 — Load a JSON Lines Stream

## Description
JSON Lines files contain one independent JSON document per nonblank line. Read the stream in order while allowing malformed JSON to surface as an error.

## Requirements
- Implement `read_jsonl(path)` in `starter/solution.py`.
- Read the file as UTF-8 text.
- Skip blank or whitespace-only lines.
- Parse every other line as a JSON value and return the values in original order.
- Propagate JSON decoding errors rather than silently ignoring invalid records.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Treat each nonblank line as its own JSON document, preserving stream order and supporting any valid JSON value type. Invalid nonblank lines must raise a decoding error rather than disappear.

## Tips
- Why must each line be decoded independently?

## Example Behavior
A file with lines `{"a":1}`, blank, and `[2,3]` produces `[{'a': 1}, [2, 3]]`.

*Source: gauntlex/19-file-automation/326-write-atomic/README.md*

### 326 — Replace a File Safely

## Description
Writing directly to a destination risks leaving partial content if a write is interrupted. Prepare replacement content in the same directory before switching files.

## Requirements
- Implement `write_text_atomic(path, text)` in `starter/solution.py`.
- Write the supplied string as UTF-8.
- Use a temporary file in the destination's existing parent directory.
- Atomically replace the destination with the completed temporary file.
- Return `None`; leave no temporary file after a successful replacement.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Create the temporary file in the destination's existing parent directory to keep replacement on the same filesystem. Complete and close the temporary write before replacing the destination; clean up temporary files if an operation fails.

## Tips
- Why should the temporary file be created on the same filesystem as the destination?

## Example Behavior
Writing `'ready\n'` to an existing destination replaces its previous contents with exactly `ready` followed by a newline.

*Source: gauntlex/19-file-automation/327-find-duplicates/README.md*

### 327 — Find Duplicate Content

## Description
Files with different names can contain identical bytes. Group duplicate content by SHA-256 fingerprints rather than comparing filenames.

## Requirements
- Implement `duplicate_hashes(paths)` in `starter/solution.py`.
- Accept a list of file paths.
- Hash each file's raw bytes with SHA-256.
- Return a dictionary from lowercase digest strings to sorted path strings.
- Include only digests associated with more than one supplied path.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Group files by digest of raw bytes, then omit groups containing only one supplied path. Sort path strings within every retained group so the result does not depend on traversal order.

## Tips
- Why is file size or filename alone insufficient to identify duplicates?

## Example Behavior
Two distinct paths containing the same bytes appear together under one digest; a unique file is omitted.

*Source: gauntlex/19-file-automation/328-csv-group-sum/README.md*

### 328 — Aggregate CSV Values

## Description
Tabular data often needs totals by category. Use CSV column names rather than fixed positions to group and sum numeric records.

## Requirements
- Implement `csv_group_sum(path, category_column, amount_column)` in `starter/solution.py`.
- Read the CSV file with its header row.
- Locate the category and amount columns by their supplied names.
- Treat amounts as valid integer strings and sum them by category.
- Return a category-to-integer-total dictionary; return `{}` when there are no data rows.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Read the header to locate columns by name, rather than assuming their positions. Aggregate valid integer values under the category text exactly as parsed; an empty data section produces an empty mapping.

## Tips
- What happens when the columns appear in a different order?

## Example Behavior
For rows `kind,amount` followed by `food,4` and `food,6`, the result is `{'food': 10}`.

*Source: gauntlex/19-file-automation/329-csv-dedupe/README.md*

### 329 — Count Unique CSV Rows

## Description
A CSV file may repeat complete data rows. Count distinct parsed records while excluding the header from the data.

## Requirements
- Implement `csv_unique_rows(path)` in `starter/solution.py`.
- Read a valid CSV file with a header.
- Compare data rows by all parsed field values, regardless of row order.
- Return the number of distinct data rows as an integer.
- Do not count the header as a data row.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Compare the entire parsed row, not the original CSV text or one selected field. Identical rows count once regardless of where they occur, while the header is never a data record.

## Tips
- Why is comparing only one field insufficient for full-row deduplication?

## Example Behavior
For data rows `a,1`, `a,1`, and `a,2`, the unique row count is `2`.

*Source: gauntlex/19-file-automation/330-directory-manifest/README.md*

### 330 — Map a Directory

## Description
A directory manifest describes all regular files below a root using portable relative paths. Traverse subdirectories without following directory symlinks.

## Requirements
- Implement `directory_manifest(root)` in `starter/solution.py`.
- Recursively find regular files beneath the supplied root directory.
- Return their paths relative to the root using POSIX forward slashes.
- Sort the resulting path strings alphabetically.
- Exclude directories and do not follow directory symlinks.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Traverse directories recursively but do not descend into symlinked directories. Express every discovered regular file as a POSIX path relative to the supplied root and sort the completed list.

## Tips
- Why is a relative POSIX path more portable than an absolute local path?

## Example Behavior
A root containing `a.txt` and `docs/b.txt` produces `['a.txt', 'docs/b.txt']`.

*Source: gauntlex/19-file-automation/331-filter-by-suffix/README.md*

### 331 — Select File Types

## Description
Filter a sequence of filenames by final extension without changing the filenames or their order.

## Requirements
- Implement `filter_suffix(names, suffix)` in `starter/solution.py`.
- Accept filenames and a suffix that includes its leading dot.
- Match the final suffix case-insensitively.
- Return the original matching filenames in input order.
- Do not match a similar substring that is not the final suffix.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Match the complete final suffix without treating a similar substring in the middle of a filename as a match. Keep original filenames and input ordering while comparing without case sensitivity.

## Tips
- Why should `report.csv.bak` not match a `.csv` filter?

## Example Behavior
`filter_suffix(['A.CSV', 'b.txt', 'c.csv'], '.csv')` → `['A.CSV', 'c.csv']`.

*Source: gauntlex/19-file-automation/332-safe-archive-name/README.md*

### 332 — Inspect Archive Paths

## Description
Archive member names can contain traversal or platform-specific absolute paths. Validate the name before it could be used for extraction.

## Requirements
- Implement `archive_member_safe(name)` in `starter/solution.py`.
- Return `True` only for nonempty relative POSIX member names.
- Reject leading slashes, backslashes, empty segments, `.` segments, and `..` segments.
- Reject Windows drive prefixes such as `C:`.
- Do not read or write any files.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Check every member path component rather than trusting normalization to remove dangerous segments. Reject Windows drive prefixes and backslashes even when the host platform is not Windows.

## Tips
- Why must Windows-style paths be rejected even on a POSIX system?

## Example Behavior
`archive_member_safe('docs/readme.md')` → `True`; `archive_member_safe('../secret')` → `False`.

*Source: gauntlex/19-file-automation/333-rotate-logs/README.md*

### 333 — Plan Log Backups

## Description
Log rotation can be planned as a deterministic sequence of backup names. This exercise generates names without performing filesystem operations.

## Requirements
- Implement `rotation_names(base, backups)` in `starter/solution.py`.
- Accept a base filename and a positive backup count.
- Return filenames formed by appending `.1` through `.N` to the base.
- Keep the names in ascending numeric order.
- Do not create, rename, or delete files.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Generate a predictable ordered plan without touching the filesystem. The numeric suffix sequence starts at one and ends at the requested positive backup count.

## Tips
- Why is separating a rotation plan from actual file operations useful?

## Example Behavior
`rotation_names('app.log', 3)` → `['app.log.1', 'app.log.2', 'app.log.3']`.

*Source: gauntlex/19-file-automation/334-config-fingerprint/README.md*

### 334 — Fingerprint Configuration

## Description
Configuration fingerprints should remain identical when dictionaries contain the same data in different insertion orders. Canonicalize structured content before hashing.

## Requirements
- Implement `config_fingerprint(config)` in `starter/solution.py`.
- Accept a JSON-compatible configuration value.
- Serialize it as compact JSON with dictionary keys sorted.
- Encode the canonical representation as UTF-8 and hash with SHA-256.
- Return the lowercase hexadecimal digest; do not mutate the configuration.
- Use Python's standard library only. Do not print or mutate caller-owned inputs.

## Design Considerations
Canonicalize JSON by sorting object keys and using compact separators before UTF-8 encoding. Hash the resulting bytes so dictionary insertion order cannot change the fingerprint.

## Tips
- Why does sorting dictionary keys matter for reproducible hashes?

## Example Behavior
`config_fingerprint({'a': 1, 'b': 2})` and `config_fingerprint({'b': 2, 'a': 1})` return the same digest.

---

## Wsgi Web

*Source: gauntlex/20-wsgi-web/335-wsgi-health/README.md*

### 335 — Your First WSGI Response

## Description
WSGI applications receive request metadata and a callback for response headers. Create a health response that works regardless of the requested path.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Call `start_response` exactly once with HTTP 200 and `Content-Type: application/json`.
- Return an iterable containing UTF-8 bytes for `{"status":"ok"}`.
- Do not depend on any particular request path.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
A WSGI application reports status and headers through `start_response`, then returns an iterable of byte chunks. Do not make the health response depend on the path or return a plain string.

## Tips
- Why must the response body contain bytes rather than a Python string?

## Example Behavior
For any request, status is `200 OK` and body is `b'{"status":"ok"}'`.

*Source: gauntlex/20-wsgi-web/336-wsgi-routing/README.md*

### 336 — Route by Path

## Description
A web service chooses responses using the request path. Distinguish a known health route from all other locations.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Read `PATH_INFO` from the WSGI environment.
- For `/health`, return HTTP 200 with body `ok`.
- For other paths, return HTTP 404 with body `not found`.
- Use `Content-Type: text/plain; charset=utf-8`.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Choose status and body from `PATH_INFO` before starting the response. Keep the health route distinct from every unknown path so missing resources never receive a success status.

## Tips
- Why should an unknown route not share the health route's success status?

## Example Behavior
`/health` → `200` and `b'ok'`; `/missing` → `404` and `b'not found'`.

*Source: gauntlex/20-wsgi-web/337-wsgi-method/README.md*

### 337 — Method Matters

## Description
The same URL can support one HTTP method while rejecting another. Distinguish a missing route from a disallowed method.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Accept GET `/resource` with HTTP 200 and body `resource`.
- Return HTTP 405 with body `method not allowed` for other methods at `/resource`.
- Return HTTP 404 with body `not found` for other paths.
- Set a text/plain content type.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Check route existence and request method separately: a known resource with an unsupported method is not the same as an unknown URL. Keep each status paired with its specified body.

## Tips
- What information does 405 convey that 404 does not?

## Example Behavior
GET `/resource` → `200`; POST `/resource` → `405`; GET `/else` → `404`.

*Source: gauntlex/20-wsgi-web/338-wsgi-query/README.md*

### 338 — Decode Query Input

## Description
Query parameters are encoded separately from the URL path. Decode the first `message` value on an echo route.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Handle GET `/echo` and read the first `message` value from `QUERY_STRING`.
- Decode percent escapes and plus-as-space form encoding.
- Return the decoded message as UTF-8 bytes and use text/plain with UTF-8 charset.
- Return HTTP 404 for other paths.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Parse `QUERY_STRING` independently of `PATH_INFO`, preserving the first value for repeated `message` keys. Decode percent escapes and plus signs before UTF-8 encoding the response.

## Tips
- Why is splitting a raw query string on every equals sign unreliable?

## Example Behavior
GET `/echo?message=hello+world` → `b'hello world'`.

*Source: gauntlex/20-wsgi-web/339-wsgi-json/README.md*

### 339 — Serialize a Web Response

## Description
A JSON API must serialize Python data into valid compact JSON and label its response correctly.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/data`, return HTTP 200 and `Content-Type: application/json`.
- Serialize `{"name":"Gauntlex","ready":true}` as compact JSON with sorted keys.
- Return the encoded bytes.
- For other paths, return HTTP 404 with an empty body.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Construct a JSON representation rather than Python's string representation of a dictionary. Serialize deterministically with compact separators and sorted keys, then encode it to bytes.

## Tips
- Why is Python's `True` not the same literal as JSON's `true`?

## Example Behavior
GET `/data` → `b'{"name":"Gauntlex","ready":true}'`.

*Source: gauntlex/20-wsgi-web/340-wsgi-post-body/README.md*

### 340 — Read a Request Body

## Description
WSGI exposes request bodies as a byte stream. Read only the declared bytes before transforming their decoded text.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For POST `/uppercase`, read exactly `CONTENT_LENGTH` bytes from `wsgi.input`.
- Decode UTF-8, uppercase the text, and return UTF-8 bytes with HTTP 200.
- Set `Content-Type: text/plain`.
- Return HTTP 404 for other paths.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Respect the declared request-body byte count when reading `wsgi.input`. Decode only the bytes belonging to this request and keep the response body in bytes after transforming text.

## Tips
- What could go wrong if the application reads beyond the advertised length?

## Example Behavior
POST `/uppercase` with body `hello` → `b'HELLO'`.

*Source: gauntlex/20-wsgi-web/341-wsgi-json-post/README.md*

### 341 — Validate JSON Input

## Description
A JSON endpoint must validate structure and field types before computing a result. Invalid input should produce a stable client error.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For POST `/sum`, accept JSON containing integer `a` and integer `b`.
- Return compact JSON `{"sum":total}` with HTTP 200.
- For malformed JSON or missing/noninteger fields, return HTTP 400 and `{"error":"bad request"}`.
- Use `Content-Type: application/json`; return HTTP 404 for other paths.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Validate the JSON document's shape and both field types before calculating a sum. In Python, Boolean values satisfy integer type checks, so distinguish them explicitly for this contract.

## Tips
- Why must Boolean values be considered separately when validating Python integers?

## Example Behavior
POST `/sum` with `{"a":2,"b":3}` → `b'{"sum":5}'`; invalid input → HTTP 400.

*Source: gauntlex/20-wsgi-web/342-wsgi-headers/README.md*

### 342 — Inspect Request Headers

## Description
WSGI represents HTTP request headers through environment keys. Expose a selected header without assuming it exists.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/agent`, read `HTTP_USER_AGENT` from `environ`.
- Return its value as UTF-8 bytes, or empty bytes when absent.
- Respond with HTTP 200 and `Content-Type: text/plain`.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
WSGI request headers appear as environment variables, commonly with an `HTTP_` prefix. Handle an absent user-agent header as an empty response rather than raising an error.

## Tips
- How do HTTP header names become WSGI environment keys?

## Example Behavior
When `HTTP_USER_AGENT` is `ExampleClient`, the response body is `b'ExampleClient'`.

*Source: gauntlex/20-wsgi-web/343-wsgi-head/README.md*

### 343 — Headers Without a Body

## Description
GET retrieves a resource body, while HEAD requests only response metadata. Support both on one route.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/status`, return HTTP 200 and body `ready`.
- For HEAD `/status`, return HTTP 200 and an empty body.
- Use `Content-Type: text/plain` for both.
- Return HTTP 404 for other paths.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Preserve the route's successful status and response metadata for HEAD while omitting its body. GET and HEAD differ in representation delivery, not in whether the resource exists.

## Tips
- Why does HEAD omit a body even when the resource exists?

## Example Behavior
GET `/status` → `b'ready'`; HEAD `/status` → `b''`.

*Source: gauntlex/20-wsgi-web/344-wsgi-redirect/README.md*

### 344 — Move a Resource

## Description
When a resource moves, a redirect tells clients where to request it next. Preserve distinct behavior for old and new paths.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- GET `/old` returns HTTP 302 Found with `Location: /new` and an empty body.
- GET `/new` returns HTTP 200 and body `new`.
- Other paths return HTTP 404.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
A redirect requires both the redirect status and a `Location` header naming the new path. Keep the destination's ordinary success response separate from the old path.

## Tips
- Why is a Location header needed in addition to a 302 status?

## Example Behavior
GET `/old` → `302 Found`, `Location: /new`, empty body.

*Source: gauntlex/20-wsgi-web/345-wsgi-cookie/README.md*

### 345 — Recognize a Session Cookie

## Description
Cookies arrive in a request header containing multiple name-value pairs. Determine whether a meaningful session cookie exists.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/cookie`, inspect `HTTP_COOKIE`.
- Return body `seen` when a cookie named `session` has a nonempty value.
- Otherwise return body `missing`.
- Respond with HTTP 200 and `Content-Type: text/plain`.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Parse cookie name-value pairs without mistaking the mere presence of `session` for a usable session. The contract requires a nonempty value; other cookie names must not affect the result.

## Tips
- Why is the presence of a cookie name insufficient when its value is empty?

## Example Behavior
`HTTP_COOKIE='theme=dark; session=abc'` → `b'seen'`; `session=` → `b'missing'`.

*Source: gauntlex/20-wsgi-web/346-wsgi-auth/README.md*

### 346 — Protect a Private Route

## Description
A private endpoint must verify a bearer credential before releasing its content. Validate the authorization scheme and compare the secret safely.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/private`, require Authorization `Bearer secret-token`.
- Treat the `Bearer` scheme case-insensitively.
- Use a timing-resistant comparison for the token.
- Return HTTP 200 with body `welcome` on success, or HTTP 401 with body `unauthorized` otherwise.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Validate the authorization scheme separately from the credential and accept case variations of `Bearer`. Compare the supplied token with the expected secret using a timing-resistant operation.

## Tips
- Why should token comparison avoid leaking information through timing differences?

## Example Behavior
`Authorization: bearer secret-token` → HTTP 200; an incorrect token → HTTP 401.

*Source: gauntlex/20-wsgi-web/347-wsgi-cors/README.md*

### 347 — Control Cross-Origin Access

## Description
Cross-origin headers must not trust origins merely because they resemble an approved domain. Allow only one exact origin.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/public`, return HTTP 200 and body `ok`.
- Add `Access-Control-Allow-Origin: https://gauntlex.example` only when `HTTP_ORIGIN` exactly matches that value.
- Omit the allow-origin header for missing or different origins.
- Set `Content-Type: text/plain`.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Treat the approved origin as an exact string, not a suffix or substring pattern. Omit the allow-origin header entirely for missing or unapproved origins rather than reflecting untrusted input.

## Tips
- Why is a suffix or substring match unsafe for origin allowlists?

## Example Behavior
Origin `https://gauntlex.example` receives the allow-origin header; `https://gauntlex.example.evil` does not.

*Source: gauntlex/20-wsgi-web/348-wsgi-conditional/README.md*

### 348 — Avoid Unchanged Responses

## Description
Entity tags allow a client to ask whether cached content is still current. Return a body only when the tag does not match.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/version`, set `ETag` to the exact value `"v1"`.
- Without an exact matching `HTTP_IF_NONE_MATCH`, return HTTP 200 with body `version one`.
- With an exact match, return HTTP 304 Not Modified and an empty body.
- Include the same ETag in both responses.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Return the same exact quoted ETag in both cache-hit and cache-miss responses. Only an exact matching conditional header produces 304 and an empty body; otherwise return the resource.

## Tips
- Why should a 304 response omit the representation body?

## Example Behavior
`If-None-Match: "v1"` → HTTP 304 with empty body and ETag `"v1"`.

*Source: gauntlex/20-wsgi-web/349-wsgi-error-handler/README.md*

### 349 — Safe Server Errors

## Description
An internal exception should not expose implementation details to API clients. Provide a predictable failure response while preserving normal behavior.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- GET `/safe` returns HTTP 200 with body `ok`.
- GET `/crash` catches an internal `ValueError` and returns HTTP 500 with body `internal error`.
- Do not expose exception text in the response.
- Use `Content-Type: text/plain`.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Convert the expected internal failure into a stable HTTP 500 response without exposing exception details or a traceback. Keep the ordinary route's successful response unaffected.

## Tips
- Why is a developer-facing exception message unsafe to return directly?

## Example Behavior
GET `/crash` → HTTP 500 with `b'internal error'`, not a traceback.

*Source: gauntlex/20-wsgi-web/350-wsgi-request-id/README.md*

### 350 — Validate Request IDs

## Description
Request identifiers can help correlate logs, but arbitrary client-supplied header values should not be reflected without validation.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/request`, return HTTP 200 with body `ok`.
- Accept `HTTP_X_REQUEST_ID` only when it is nonempty ASCII alphanumeric text of at most 32 characters.
- Set `X-Request-ID` to that accepted value, or to `generated` otherwise.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Validate both ASCII-only alphanumeric characters and the maximum length before reflecting a client-provided identifier. Use the prescribed fallback when any check fails.

## Tips
- Why must length and character restrictions be checked before reflecting a header?

## Example Behavior
`HTTP_X_REQUEST_ID='abc123'` → response header `X-Request-ID: abc123`; `abc-123` → `generated`.

*Source: gauntlex/20-wsgi-web/351-wsgi-content-length/README.md*

### 351 — Count Response Bytes

## Description
HTTP Content-Length measures bytes rather than Unicode characters. Build a response containing a non-ASCII character and report its encoded size.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For GET `/payload`, return UTF-8 bytes for `café` with HTTP 200.
- Set `Content-Type: text/plain; charset=utf-8`.
- Set `Content-Length` to the decimal byte length of the actual response body.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Encode the response body to UTF-8 before measuring its size. `Content-Length` describes transmitted bytes, not Unicode code points or the length of a source string.

## Tips
- Why is the length of a Unicode string not always its UTF-8 byte length?

## Example Behavior
GET `/payload` → body `b'caf\xc3\xa9'` and `Content-Length: 5`.

*Source: gauntlex/20-wsgi-web/352-wsgi-form/README.md*

### 352 — Read Form Fields

## Description
HTML forms commonly submit URL-encoded data in a POST body. Decode it and extract the first matching field.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- For POST `/form`, read the `application/x-www-form-urlencoded` body.
- Decode percent escapes and plus-as-space encoding.
- Return the first `name` field value as UTF-8 bytes, or empty bytes if absent.
- Respond with HTTP 200 and `Content-Type: text/plain`.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Read and decode the URL-encoded POST body using form semantics, including plus-as-space. For repeated `name` fields, return only the first decoded value.

## Tips
- Why should repeated form fields use the first value for this contract?

## Example Behavior
POST body `name=Ada+Lovelace` → `b'Ada Lovelace'`.

*Source: gauntlex/20-wsgi-web/353-wsgi-not-found-json/README.md*

### 353 — Consistent Not Found

## Description
Even an error-only service should provide predictable JSON and HTTP metadata. Include the requested path in a structured not-found response.

## Requirements
- Implement `application(environ, start_response)` in `starter/solution.py`.
- Return HTTP 404 Not Found for every request.
- Set `Content-Type: application/json`.
- Return compact JSON with keys `error` set to `not found` and `path` set to `PATH_INFO` or `''` when missing.
- Return JSON as bytes.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Serialize the error and requested path as a compact JSON object and encode it to bytes. Even a service that always returns 404 must send consistent content type and response status.

## Tips
- Why does a structured error need the same encoding discipline as a successful response?

## Example Behavior
With `PATH_INFO='/missing'`, body is `b'{"error":"not found","path":"/missing"}'`.

*Source: gauntlex/20-wsgi-web/354-wsgi-middleware/README.md*

### 354 — Wrap an Application

## Description
WSGI middleware surrounds an existing application without replacing its business logic. Add response metadata while forwarding the original body untouched.

## Requirements
- Implement `wrap_app(app)` in `starter/solution.py`.
- Implement `wrap_app(app)` to return a WSGI callable.
- Forward incoming environment and the wrapped application's response behavior.
- Append `X-Powered-By: Gauntlex` exactly once to response headers.
- Do not consume or alter the wrapped application's body iterable.
- Use Python's standard library and the WSGI interface only; do not make network requests, print debug output, or mutate `environ`.

## Design Considerations
Wrap `start_response` to append the required header once while preserving the wrapped application's status and other headers. Forward its body iterable without eagerly consuming or changing it.

## Tips
- Why should middleware return the original iterable rather than reading it eagerly?

## Example Behavior
A wrapped app's original response body remains unchanged, while headers include exactly one `X-Powered-By: Gauntlex`.

---

## Data Science

*Source: gauntlex/21-data-science/355-min-max-scale/README.md*

### 355 — Scale to Zero and One

## Description
Different numeric ranges make features difficult to compare. Rescale observations using the dataset minimum and maximum while preserving their order.

## Requirements
- Implement `min_max_scale(values)` in `starter/solution.py`.
- Map each value to `(value - minimum) / (maximum - minimum)`.
- Return `[]` for empty input.
- If all values are equal, return one zero per value.
- Do not modify the original sequence.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Calculate the minimum and maximum across the entire supplied sequence before transforming observations. Handle an empty or constant dataset explicitly so no division by zero occurs.

## Tips
- Why does a constant dataset need special handling?

## Example Behavior
`min_max_scale([2, 4, 6])` → `[0.0, 0.5, 1.0]`.

*Source: gauntlex/21-data-science/356-z-score-scale/README.md*

### 356 — Standardize Observations

## Description
Express each observation relative to the population's center and spread, rather than its original units.

## Requirements
- Implement `z_score_scale(values)` in `starter/solution.py`.
- Calculate the population mean and population standard deviation (variance divided by `n`).
- Return each value's deviation from the mean divided by that standard deviation.
- Return `[]` for empty input and zeros for zero variance.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Use population variance with divisor `n`, not sample variance with `n-1`. If every observation equals the mean, return a zero for each position instead of dividing by zero.

## Tips
- How does population variance differ from sample variance?

## Example Behavior
`z_score_scale([2, 2, 2])` → `[0.0, 0.0, 0.0]`.

*Source: gauntlex/21-data-science/357-moving-average/README.md*

### 357 — Smooth with Windows

## Description
A moving average summarizes adjacent observations and smooths short-term fluctuations without changing their sequence.

## Requirements
- Implement `moving_average(values, k)` in `starter/solution.py`.
- Accept a sequence and positive integer window size `k`.
- Return floating-point averages for each consecutive window of exactly `k` observations.
- Return `[]` when `k` exceeds the sequence length.
- Raise `ValueError` when `k < 1`.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Generate a result only for each complete window of length `k`; preserve observation order. An oversized window produces no results, while a nonpositive size is invalid.

## Tips
- How does the next window differ from the previous window?

## Example Behavior
`moving_average([2, 4, 6, 8], 2)` → `[3.0, 5.0, 7.0]`.

*Source: gauntlex/21-data-science/358-exponential-smoothing/README.md*

### 358 — Weighted Recent History

## Description
Exponential smoothing balances a new observation with the previous smoothed estimate, producing a history-aware series.

## Requirements
- Implement `exponential_smoothing(values, alpha)` in `starter/solution.py`.
- Require smoothing factor `alpha` to satisfy `0 < alpha <= 1`.
- For nonempty input, begin with the first observation unchanged.
- For later observations, combine the current value and previous smoothed output using `alpha` and `1-alpha`.
- Return `[]` for empty input.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Initialize the smoothed sequence from the first observation, then combine each later raw value with the previous smoothed result. The parameter bounds keep the recurrence meaningful.

## Tips
- Why must the recurrence use the previous smoothed value rather than the previous raw observation?

## Example Behavior
`exponential_smoothing([10, 20, 30], 0.5)` → `[10, 15.0, 22.5]`.

*Source: gauntlex/21-data-science/359-weighted-mean/README.md*

### 359 — Weighted Observations

## Description
Some observations contribute more to a summary than others. Compute a mean that respects their supplied nonnegative weights.

## Requirements
- Implement `weighted_mean(values, weights)` in `starter/solution.py`.
- Require equal-length nonempty value and weight sequences.
- Reject negative weights and a zero total weight with `ValueError`.
- Return the sum of value-times-weight products divided by the sum of weights.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Validate that values and weights align and that the total weight is positive. Zero-weight observations are allowed, but negative weights and an all-zero weighting are not.

## Tips
- What happens if every weight is zero?

## Example Behavior
`weighted_mean([10, 20], [1, 3])` → `17.5`.

*Source: gauntlex/21-data-science/360-covariance/README.md*

### 360 — Move Together

## Description
Covariance describes whether two series tend to rise and fall together relative to their own means.

## Requirements
- Implement `population_covariance(xs, ys)` in `starter/solution.py`.
- Require equal-length, nonempty numeric sequences.
- Compute each series' mean and sum paired deviations' products.
- Divide by the full number of observations for population covariance.
- Raise `ValueError` for empty or mismatched inputs.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Pair observations by index, measure both deviations from their respective means, and divide the aggregate by the population count. Reject empty and unequal-length series.

## Tips
- Why is the population divisor `n` instead of `n-1`?

## Example Behavior
`population_covariance([1, 2, 3], [2, 4, 6])` → approximately `1.3333333333`.

*Source: gauntlex/21-data-science/361-quantile-linear/README.md*

### 361 — Interpolate a Quantile

## Description
Quantiles locate positions in sorted observations, including positions that fall between two neighboring values.

## Requirements
- Implement `quantile(values, q)` in `starter/solution.py`.
- Require nonempty values and `q` between 0 and 1 inclusive.
- Sort observations without mutating input.
- Use the position `(n - 1) * q` and linearly interpolate between neighboring values when necessary.
- Raise `ValueError` for invalid `q` or empty input.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Sort a copy of the data before locating the fractional index `(n - 1) * q`. When the position lies between observations, interpolate rather than rounding to a nearby index.

## Tips
- How does an interpolated quantile differ from selecting the nearest observation?

## Example Behavior
`quantile([0, 10, 20, 30], 0.25)` → `7.5`.

*Source: gauntlex/21-data-science/362-confusion-matrix/README.md*

### 362 — Classify the Outcomes

## Description
Binary classifiers can be evaluated by counting correct and incorrect predictions for positive and negative cases.

## Requirements
- Implement `confusion_matrix(actual, predicted)` in `starter/solution.py`.
- Require actual and predicted Boolean sequences of equal length.
- Return integer counts under keys `tp`, `tn`, `fp`, and `fn`.
- Classify each paired observation exactly once.
- Raise `ValueError` for length mismatch.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Assign each actual/predicted Boolean pair to exactly one of the four outcome categories. Distinguish a false positive from a false negative by which side of the pair is positive.

## Tips
- What distinguishes a false positive from a false negative?

## Example Behavior
`confusion_matrix([True, False], [True, True])` → `{'tp': 1, 'tn': 0, 'fp': 1, 'fn': 0}`.

*Source: gauntlex/21-data-science/363-classification-metrics/README.md*

### 363 — Measure a Classifier

## Description
Different evaluation metrics capture different kinds of classification performance. Derive four measures from outcome counts.

## Requirements
- Implement `classification_metrics(tp, tn, fp, fn)` in `starter/solution.py`.
- Accept nonnegative integer `tp`, `tn`, `fp`, and `fn`; reject negative counts with `ValueError`.
- Return a dictionary containing floating-point `precision`, `recall`, `accuracy`, and `f1`.
- Use `0.0` whenever a metric's denominator is zero, including an empty sample.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Derive each measure from the relevant counts rather than assuming all metrics share a denominator. Return `0.0` for undefined zero-denominator cases, including an empty sample.

## Tips
- Why can precision and recall disagree for the same classifier?

## Example Behavior
`classification_metrics(1, 1, 0, 0)` → all four metrics equal `1.0`.

*Source: gauntlex/21-data-science/364-mean-absolute-error/README.md*

### 364 — Average Prediction Error

## Description
Prediction errors above and below the target should not cancel. Measure the average magnitude of deviations.

## Requirements
- Implement `mean_absolute_error(actual, predicted)` in `starter/solution.py`.
- Require equal-length, nonempty actual and predicted sequences.
- Compute absolute differences for corresponding observations.
- Return their arithmetic mean.
- Raise `ValueError` for empty or mismatched sequences.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Take the absolute magnitude of each paired residual before averaging, so overprediction and underprediction cannot cancel. Require at least one matched observation.

## Tips
- Why is taking absolute values necessary before averaging?

## Example Behavior
`mean_absolute_error([1, 3], [2, 1])` → `1.5`.

*Source: gauntlex/21-data-science/365-root-mean-square-error/README.md*

### 365 — Penalize Large Errors

## Description
Squaring prediction errors makes larger deviations contribute more strongly to the overall error score.

## Requirements
- Implement `root_mean_square_error(actual, predicted)` in `starter/solution.py`.
- Require nonempty actual and predicted numeric sequences of equal length.
- Square each paired prediction difference, average those squares, and return the square root.
- Raise `ValueError` for empty or mismatched sequences.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Square each paired prediction residual before averaging and taking the square root. This makes large misses more influential than they would be under absolute-error averaging.

## Tips
- Why does squaring make large errors more influential?

## Example Behavior
`root_mean_square_error([0, 0], [3, 4])` → approximately `3.5355339`.

*Source: gauntlex/21-data-science/366-r-squared/README.md*

### 366 — Explain the Variation

## Description
The coefficient of determination compares prediction residuals against the natural variation in the observed targets.

## Requirements
- Implement `r_squared(actual, predicted)` in `starter/solution.py`.
- Require equal-length, nonempty actual and predicted sequences.
- Compute `1 - SSE/SST` using squared residuals and squared deviations from the actual mean.
- If all actual values are equal, return `1.0` for exact predictions and `0.0` otherwise.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Compare residual error against variation around the actual mean. A constant target has no natural variation, so use the specified exact-prediction rule instead of dividing by zero.

## Tips
- Why does a constant target sequence require a special rule?

## Example Behavior
`r_squared([1, 2, 3], [1, 2, 3])` → `1.0`.

*Source: gauntlex/21-data-science/367-euclidean-distance/README.md*

### 367 — Straight-Line Distance

## Description
Numeric vectors represent points in a coordinate space. Measure their straight-line separation across all dimensions.

## Requirements
- Implement `euclidean_distance(a, b)` in `starter/solution.py`.
- Require vectors of equal length, or raise `ValueError`.
- Return the square root of the sum of squared coordinate differences.
- Return `0` for two empty vectors.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Match coordinates by position and require equal dimensionality. The square root of accumulated squared differences gives straight-line distance; two empty vectors have zero distance.

## Tips
- Why can vectors of different dimensions not be compared directly?

## Example Behavior
`euclidean_distance([0, 0], [3, 4])` → `5.0`.

*Source: gauntlex/21-data-science/368-cosine-similarity/README.md*

### 368 — Compare Directions

## Description
Cosine similarity compares vector orientation rather than raw distance, making direction the focus of the measure.

## Requirements
- Implement `cosine_similarity(a, b)` in `starter/solution.py`.
- Require equal-length vectors, or raise `ValueError`.
- Compute the dot product divided by the product of vector magnitudes.
- Return `0.0` when either magnitude is zero, including empty vectors.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Calculate directional similarity from a dot product and the two vector magnitudes. A zero-magnitude vector has no defined direction, so return the prescribed zero result.

## Tips
- Why is a zero vector a special case for directional similarity?

## Example Behavior
`cosine_similarity([1, 0], [0, 1])` → `0.0`; identical unit vectors → `1.0`.

*Source: gauntlex/21-data-science/369-manhattan-distance/README.md*

### 369 — City-Block Distance

## Description
Some distances are measured by adding coordinate-wise travel rather than following a straight line.

## Requirements
- Implement `manhattan_distance(a, b)` in `starter/solution.py`.
- Require equal-length numeric vectors; raise `ValueError` on mismatch.
- Return the sum of absolute differences between corresponding coordinates.
- Return `0` for two empty vectors.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Add absolute coordinate differences rather than squaring them. The result represents axis-aligned travel and is defined as zero for two empty vectors.

## Tips
- How does this distance differ from Euclidean distance on a two-dimensional grid?

## Example Behavior
`manhattan_distance([0, 0], [3, 4])` → `7`.

*Source: gauntlex/21-data-science/370-k-nearest-neighbors/README.md*

### 370 — Find Nearby Examples

## Description
Nearest-neighbor search ranks examples by their distance from a query, with deterministic tie-breaking.

## Requirements
- Implement `nearest_indices(vectors, query, k)` in `starter/solution.py`.
- Accept a list of numeric vectors, a query vector, and nonnegative integer `k`.
- Compare each vector using squared Euclidean distance to the query.
- Return indices of the nearest `k` vectors, breaking equal-distance ties by lower original index.
- Raise `ValueError` for mismatched dimensions or negative `k`; allow `k` greater than the dataset length.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Rank each candidate by squared Euclidean distance, using its original index as a deterministic tie-breaker. If `k` exceeds the dataset size, return every candidate in ranked order.

## Tips
- Why is the square root unnecessary when ranking distances?

## Example Behavior
`nearest_indices([[0], [2], [4]], [3], 2)` → `[1, 2]`.

*Source: gauntlex/21-data-science/371-train-test-split/README.md*

### 371 — Hold Out Examples

## Description
Model evaluation requires separating training and held-out observations. Preserve the original order instead of shuffling.

## Requirements
- Implement `train_test_split(items, test_fraction)` in `starter/solution.py`.
- Require `test_fraction` between `0` and `1` inclusive; otherwise raise `ValueError`.
- Use `floor(len(items) * test_fraction)` as the test count.
- Take test items from the end and return `[training_items, test_items]`.
- Preserve item order in both groups.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Compute the held-out count using the specified floor rule and select that many items from the end. Keep both partitions ordered and avoid randomization so results are reproducible.

## Tips
- Why does choosing the final observations matter for reproducibility?

## Example Behavior
`train_test_split([1, 2, 3, 4], 0.25)` → `[[1, 2, 3], [4]]`.

*Source: gauntlex/21-data-science/372-minibatches/README.md*

### 372 — Train in Batches

## Description
Large datasets are often processed in smaller consecutive groups. Preserve all observations, including a final incomplete group.

## Requirements
- Implement `mini_batches(items, batch_size)` in `starter/solution.py`.
- Require positive integer `batch_size`; raise `ValueError` otherwise.
- Split input into consecutive lists with at most `batch_size` items.
- Preserve original order and include a shorter final batch.
- Return `[]` for empty input.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Partition consecutive observations without overlap or omission. Keep the last smaller batch when the input length is not divisible by the requested positive batch size.

## Tips
- Why should a partially filled final batch not be discarded?

## Example Behavior
`mini_batches([1, 2, 3, 4, 5], 2)` → `[[1, 2], [3, 4], [5]]`.

*Source: gauntlex/21-data-science/373-one-hot-encode/README.md*

### 373 — Encode Categories

## Description
Categorical labels can be represented as binary vectors with one active position. The supplied class order defines that position.

## Requirements
- Implement `one_hot_encode(labels, classes)` in `starter/solution.py`.
- Accept hashable labels and an ordered sequence of distinct classes.
- Return one row per label, with `1` at its class position and `0` elsewhere.
- Raise `ValueError` for duplicate classes or labels not found among classes.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Use the supplied class sequence as the fixed coordinate order. Reject duplicate class definitions and unknown labels rather than silently producing ambiguous or all-zero rows.

## Tips
- Why must the class order be fixed before encoding?

## Example Behavior
`one_hot_encode(['cat', 'dog'], ['dog', 'cat'])` → `[[0, 1], [1, 0]]`.

*Source: gauntlex/21-data-science/374-standardize-columns/README.md*

### 374 — Normalize Each Feature

## Description
Different features can have different scales. Standardize each matrix column independently using population statistics.

## Requirements
- Implement `standardize_columns(matrix)` in `starter/solution.py`.
- Accept a rectangular matrix of numeric rows.
- Compute each column's population mean and standard deviation.
- Standardize each column independently; replace constant columns with zeros.
- Return `[]` for an empty matrix; raise `ValueError` for ragged rows.
- Use Python's standard library only; do not use NumPy, pandas, or scikit-learn. Do not print or mutate inputs.
- Floating-point results may be compared approximately.

## Design Considerations
Compute population statistics separately for each feature column, not across the whole matrix. Detect ragged rows and turn constant columns into zeros while preserving row order.

## Tips
- Why would computing one mean for the entire matrix distort individual features?

## Example Behavior
`standardize_columns([[1, 10], [3, 10]])` → `[[-1.0, 0.0], [1.0, 0.0]]`.

---

## Advanced Algorithms

*Source: gauntlex/22-advanced-algorithms/375-binary-search-bound/README.md*

### 375 — First Not Smaller

## Description
Search a sorted collection for the first position at which a target could be inserted without placing it after an equal value. The result is an insertion boundary, even when the target is absent.

## Requirements
- Implement `lower_bound(values, target)` in `starter/solution.py`.
- Assume `values` is sorted in ascending order and may contain duplicates.
- Return the index of the first element greater than or equal to `target`; return `len(values)` if there is none.
- Use O(log n) comparisons; do not mutate the input or print output.
- Use Python's standard library only.

## Tips
- What does the boundary mean when all elements are smaller than the target?
- Which half can be discarded when a middle value equals the target?

## Example Behavior
`lower_bound([1, 2, 2, 5], 2)` → `1`; `lower_bound([1, 2], 3)` → `2`.

*Source: gauntlex/22-advanced-algorithms/376-upper-bound/README.md*

### 376 — First Strictly Greater

## Description
Locate the insertion boundary immediately after all values equal to a target in an ascending sequence. Unlike a lower bound, equality must remain on the left of the answer.

## Requirements
- Implement `upper_bound(values, target)` in `starter/solution.py`.
- Assume ascending sorted values, including possible duplicates.
- Return the first index whose value is strictly greater than `target`; return `len(values)` when no such element exists.
- Use O(log n) comparisons; do not mutate inputs or print.
- Use Python's standard library only.

## Tips
- How should an equality comparison affect the search interval?
- What index should an empty sequence return?

## Example Behavior
`upper_bound([1, 2, 2, 5], 2)` → `3`; `upper_bound([], 2)` → `0`.

*Source: gauntlex/22-advanced-algorithms/377-merge-intervals/README.md*

### 377 — Merge Integer Ranges

## Description
Combine a collection of inclusive integer ranges into a canonical, sorted set of nonoverlapping ranges. Adjacent integer ranges must be combined as well as overlapping ones.

## Requirements
- Implement `merge_intervals(intervals)` in `starter/solution.py`.
- Each input interval is `[start, end]` with `start <= end`; inputs need not be sorted.
- Return merged intervals sorted by their starting value.
- Merge when the next start is at most the current end plus one, because endpoints are inclusive integers.
- Do not mutate input intervals or print.
- Use Python's standard library only.

## Tips
- Why is sorting useful before merging?
- Why do `[1, 2]` and `[3, 4]` merge under this contract?

## Example Behavior
`merge_intervals([[5, 7], [1, 2], [3, 4]])` → `[[1, 7]]`.

*Source: gauntlex/22-advanced-algorithms/378-interval-intersection/README.md*

### 378 — Where Ranges Overlap

## Description
Find every region shared by two ordered interval collections. Each collection already contains disjoint inclusive ranges, so compare their boundaries without combining unrelated regions.

## Requirements
- Implement `interval_intersection(a, b)` in `starter/solution.py`.
- Both inputs are sorted lists of pairwise-disjoint inclusive integer intervals.
- Return all nonempty pairwise intersections as `[start, end]` ranges in ascending order.
- An intersection consisting of one shared endpoint counts.
- Do not mutate either input or print.
- Use Python's standard library only.

## Tips
- Which of two current intervals can no longer overlap later intervals?
- When is the overlap a single point rather than an empty interval?

## Example Behavior
`interval_intersection([[1, 3], [6, 8]], [[3, 6]])` → `[[3, 3], [6, 6]]`.

*Source: gauntlex/22-advanced-algorithms/379-longest-unique-substring/README.md*

### 379 — Longest Distinct Window

## Description
Measure the longest contiguous stretch of Unicode text in which no character repeats. A substring must stay contiguous; skipping repeated characters would change the problem.

## Requirements
- Implement `longest_unique_substring(text)` in `starter/solution.py`.
- Return the maximum number of characters in a contiguous substring with no repeated Unicode characters.
- Return `0` for empty text.
- Target O(n) time rather than rechecking every substring.
- Do not print or mutate inputs.
- Use Python's standard library only.

## Tips
- How can the left edge of a valid window move when a repeated character appears?
- What information about earlier occurrences would avoid rescanning?

## Example Behavior
`longest_unique_substring('abba')` → `2`; `longest_unique_substring('')` → `0`.

*Source: gauntlex/22-advanced-algorithms/380-minimum-window/README.md*

### 380 — Smallest Covering Substring

## Description
Find the shortest contiguous part of a string that covers every required character, including repeated requirements. If several shortest windows qualify, choose the earliest.

## Requirements
- Implement `minimum_window(text, pattern)` in `starter/solution.py`.
- The selected substring must contain every character of `pattern` at least as many times as it occurs there.
- Return the shortest qualifying substring; break equal-length ties by leftmost position.
- Return `''` when no qualifying window exists or when the pattern is empty.
- Do not mutate inputs or print.
- Use Python's standard library only.

## Tips
- Why is a set of required characters insufficient for repeated letters?
- When can the left edge of a valid window be advanced safely?

## Example Behavior
`minimum_window('ADOBECODEBANC', 'ABC')` → `'BANC'`; `minimum_window('a', 'aa')` → `''`.

*Source: gauntlex/22-advanced-algorithms/381-top-k-frequent/README.md*

### 381 — Frequency with Stable Ties

## Description
Rank distinct values by how often they occur, retaining first-seen order when frequencies match. This makes results reproducible without relying on sorting the values themselves.

## Requirements
- Implement `top_k_frequent(values, k)` in `starter/solution.py`.
- Input values are hashable; `k` is an integer.
- Return up to `k` distinct values ordered by descending occurrence count.
- For equal counts, rank the value first encountered in the input earlier.
- Raise `ValueError` for negative `k`; `k=0` returns an empty list.
- Do not mutate inputs or print.
- Use Python's standard library only.

## Tips
- What two pieces of information must be retained for each distinct value?
- What happens when `k` exceeds the number of distinct values?

## Example Behavior
`top_k_frequent(['b', 'a', 'b', 'a', 'c'], 2)` → `['b', 'a']`.

*Source: gauntlex/22-advanced-algorithms/382-shortest-path-grid/README.md*

### 382 — Shortest Grid Route

## Description
Navigate a rectangular grid from its upper-left corner to its lower-right corner while avoiding blocked cells. Return the fewest orthogonal moves, not the number of visited cells.

## Requirements
- Implement `shortest_path_grid(grid)` in `starter/solution.py`.
- Cells are `0` for open and `1` for blocked; assume equal row lengths.
- Movement is permitted up, down, left, or right, never diagonally.
- Return the minimum number of moves from top-left to bottom-right.
- Return `-1` for an empty grid, blocked endpoint, or unreachable destination.
- Do not mutate the grid or print.
- Use Python's standard library only.

## Tips
- Why does exploring reachable cells by distance layers find a shortest route?
- How many moves does a single open cell require?

## Example Behavior
`shortest_path_grid([[0, 0], [1, 0]])` → `2`; `shortest_path_grid([[1]])` → `-1`.

*Source: gauntlex/22-advanced-algorithms/383-dijkstra-distances/README.md*

### 383 — Weighted Shortest Paths

## Description
Determine the least total cost from a starting node to every reachable node in a directed weighted graph. A path discovered first is not necessarily the cheapest.

## Requirements
- Implement `dijkstra_distances(graph, start)` in `starter/solution.py`.
- `graph` maps hashable nodes to lists of `[neighbor, weight]` edges; all valid weights are nonnegative.
- Return a mapping from each reachable node to its minimum total distance, including `start: 0`.
- Include reachable nodes that appear only as neighbors, not as graph keys.
- Raise `ValueError` if a negative edge weight is supplied.
- Do not mutate the graph or print.
- Use Python's standard library only.

## Tips
- Why can a later route improve an earlier tentative distance?
- What should happen to a reachable neighbor absent from the graph's keys?

## Example Behavior
`dijkstra_distances({'A': [['B', 5], ['C', 1]], 'C': [['B', 2]]}, 'A')` → `{'A': 0, 'C': 1, 'B': 3}`.

*Source: gauntlex/22-advanced-algorithms/384-longest-increasing-subsequence/README.md*

### 384 — Increasing Subsequence

## Description
Find the maximum length of a strictly increasing subsequence while preserving the original relative order. Elements in a subsequence need not be adjacent.

## Requirements
- Implement `lis_length(values)` in `starter/solution.py`.
- Return the length of the longest strictly increasing subsequence of integer values.
- Equal consecutive chosen values do not count as increasing.
- Return `0` for empty input.
- Target O(n log n) time; do not mutate inputs or print.
- Use Python's standard library only.

## Tips
- How is a subsequence different from a contiguous substring?
- What compact information could represent promising subsequences without storing them all?

## Example Behavior
`lis_length([10, 9, 2, 5, 3, 7, 101, 18])` → `4`; `lis_length([])` → `0`.

---

## Security Crypto

*Source: gauntlex/23-security-crypto/385-caesar-cipher/README.md*

### 385 — Shift the Alphabet

## Description
Implement a classical substitution cipher for ASCII letters while preserving all other text.

## Requirements
- Implement `caesar_cipher(text, shift)` in `starter/solution.py`.
- Shift ASCII letters by integer shift, wrapping within A-Z and a-z; leave other characters unchanged. Negative shifts are allowed.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Transform ASCII letters independently within their uppercase and lowercase alphabets; punctuation, digits, and non-ASCII characters must remain unchanged.

## Tips
A classical cipher is an exercise in text transformation, not a secure way to protect secrets.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`caesar_cipher('Az-9', 1)` → `'Ba-9'`; `caesar_cipher('Ba', -1)` → `'Az'`.

*Source: gauntlex/23-security-crypto/386-rot13/README.md*

### 386 — Half an Alphabet

## Description
Apply a fixed alphabet rotation that reverses itself when applied twice.

## Requirements
- Implement `rot13(text)` in `starter/solution.py`.
- Apply ROT13 to ASCII letters only, preserving case and all other characters. Applying it twice restores the input.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Apply a fixed rotation of 13 positions to ASCII letters while preserving their case. Applying the operation a second time must restore the original string.

## Tips
Check that capitalization and punctuation survive unchanged.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`rot13('Hello, World!')` → `'Uryyb, Jbeyq!'`.

*Source: gauntlex/23-security-crypto/387-hex-encode/README.md*

### 387 — Text to Hexadecimal

## Description
Encode UTF-8 text into a lowercase hexadecimal representation of its bytes.

## Requirements
- Implement `hex_encode(text)` in `starter/solution.py`.
- Return lowercase hexadecimal representation of UTF-8 bytes of the input string, without spaces or prefix.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Encode the input as UTF-8 bytes before converting each byte to hexadecimal. Unicode characters may occupy more than one byte, so do not encode code points directly.

## Tips
Unicode characters can occupy several bytes before hexadecimal encoding.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`hex_encode('Hi')` → `'4869'`; `hex_encode('é')` → `'c3a9'`.

*Source: gauntlex/23-security-crypto/388-hex-decode/README.md*

### 388 — Hexadecimal to Text

## Description
Decode hexadecimal bytes into UTF-8 text with clear failures for invalid input.

## Requirements
- Implement `hex_decode(hex_text)` in `starter/solution.py`.
- Decode a hexadecimal string to UTF-8 text. Raise ValueError for odd-length or invalid hex, and UnicodeDecodeError for invalid UTF-8 bytes.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Validate hexadecimal syntax and decode bytes as UTF-8, distinguishing invalid hex text from invalid Unicode byte sequences. Do not silently replace decoding errors.

## Tips
Invalid hexadecimal syntax and invalid UTF-8 are different error conditions.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`hex_decode('4869')` → `'Hi'`; `hex_decode('f')` raises `ValueError`.

*Source: gauntlex/23-security-crypto/389-base64-encode/README.md*

### 389 — Encode Base64

## Description
Represent UTF-8 text as standard Base64, including required padding.

## Requirements
- Implement `base64_encode(text)` in `starter/solution.py`.
- Return standard Base64 encoding of the UTF-8 bytes of text, including padding.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Encode UTF-8 bytes using standard Base64, retaining any required `=` padding. Base64 is a reversible representation, not encryption.

## Tips
Base64 encodes bytes and does not provide confidentiality.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`base64_encode('Hi')` → `'SGk='`.

*Source: gauntlex/23-security-crypto/390-base64-decode/README.md*

### 390 — Decode Base64

## Description
Decode strictly validated Base64 text back into Unicode.

## Requirements
- Implement `base64_decode(encoded)` in `starter/solution.py`.
- Decode standard Base64 text to UTF-8. Reject invalid Base64 characters or padding with ValueError. Propagate UnicodeDecodeError for invalid UTF-8.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Reject malformed Base64 characters and padding instead of permissively discarding them. After decoding bytes, propagate any UTF-8 decoding error.

## Tips
Malformed padding and invalid decoded UTF-8 must not be silently accepted.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`base64_decode('SGk=')` → `'Hi'`; malformed Base64 raises `ValueError`.

*Source: gauntlex/23-security-crypto/391-hmac-sign/README.md*

### 391 — Sign a Message

## Description
Create a keyed SHA-256 message authentication code using a shared secret.

## Requirements
- Implement `hmac_sign(secret, message)` in `starter/solution.py`.
- Return lowercase HMAC-SHA256 hex digest for UTF-8 message using UTF-8 secret key.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Use the standard library's HMAC-SHA256 implementation over UTF-8 secret and message bytes. Do not substitute a plain hash of concatenated strings for a keyed MAC.

## Tips
A message authentication code depends on both the key and message.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
Signing the same message with the same secret produces the same 64-character lowercase hexadecimal digest.

*Source: gauntlex/23-security-crypto/392-hmac-verify/README.md*

### 392 — Authenticate a Signature

## Description
Verify a message authentication code without leaking the first mismatching position.

## Requirements
- Implement `hmac_verify(secret, message, signature)` in `starter/solution.py`.
- Return True only if lowercase or uppercase hexadecimal signature equals the HMAC-SHA256 signature of UTF-8 message with UTF-8 secret. Reject malformed signatures by returning False. Use constant-time comparison.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Validate the supplied hexadecimal signature before comparison, accept upper- or lowercase hex, and use a timing-resistant equality primitive for the expected MAC.

## Tips
Reject malformed signatures before using a timing-resistant comparison.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
A signature produced by `hmac_sign('key', 'message')` verifies for the same secret and message; a changed message returns `False`.

*Source: gauntlex/23-security-crypto/393-pbkdf2-key/README.md*

### 393 — Derive a Key

## Description
Derive fixed-length key material from a password, salt, and iteration count.

## Requirements
- Implement `derive_key(password, salt, iterations)` in `starter/solution.py`.
- Return lowercase hex of a 32-byte PBKDF2-HMAC-SHA256 derived key for UTF-8 password and salt with positive integer iterations. Raise ValueError for nonpositive iterations.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Use PBKDF2-HMAC-SHA256 from the standard library with the requested positive iteration count and a 32-byte derived key. Encode the final key as lowercase hexadecimal.

## Tips
A key-derivation function deliberately repeats work; iterations must be positive.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
For valid inputs, `derive_key('pass', 'salt', 1000)` returns a deterministic 64-character lowercase hexadecimal string; zero iterations raises `ValueError`.

*Source: gauntlex/23-security-crypto/394-random-token/README.md*

### 394 — Secure Random Token

## Description
Generate a URL-safe token from cryptographically secure random bytes.

## Requirements
- Implement `random_token(n)` in `starter/solution.py`.
- Return a URL-safe Base64 token representing exactly n cryptographically random bytes, without trailing padding. Require n>=1. Tests check format and decoded length, not a fixed random output.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Generate exactly the requested number of cryptographically secure random bytes before URL-safe Base64 encoding. Remove trailing padding, and never use predictable general-purpose randomness.

## Tips
A security token needs a secure randomness source, not a predictable pseudo-random sequence.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`random_token(16)` returns a URL-safe token whose Base64-decoded payload is exactly 16 bytes; `random_token(0)` is invalid.

*Source: gauntlex/23-security-crypto/395-password-strength/README.md*

### 395 — Rule-Based Password Score

## Description
Score a password against four explicit character and length criteria.

## Requirements
- Implement `password_strength(password)` in `starter/solution.py`.
- Return a score 0–4, adding one point each for length>=12, at least one ASCII lowercase, at least one ASCII uppercase, and at least one ASCII digit. No entropy claims.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Score only the four stated rules: minimum length, ASCII lowercase, ASCII uppercase, and ASCII digit. This educational score does not measure password entropy or guarantee security.

## Tips
This simple score is not an estimate of actual password entropy or a security guarantee.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`password_strength('Abcdefghij12')` → `4`; `password_strength('abc')` → `1`.

*Source: gauntlex/23-security-crypto/396-mask-secret/README.md*

### 396 — Reveal Only the End

## Description
Hide a secret's leading characters while allowing a specified number of trailing characters to remain visible.

## Requirements
- Implement `mask_secret(secret, visible_count)` in `starter/solution.py`.
- Return the last visible_count characters of secret prefixed with asterisks for hidden characters. If visible_count is zero, mask all characters. Require visible_count>=0.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Preserve only the requested trailing characters and replace each hidden character with an asterisk. A zero visible count hides everything; a count beyond the length hides nothing.

## Tips
The visible count can be zero or larger than the secret length.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`mask_secret('abcdef', 2)` → `'****ef'`; `mask_secret('abc', 0)` → `'***'`.

*Source: gauntlex/23-security-crypto/397-validate-ipv4/README.md*

### 397 — Canonical IPv4

## Description
Check whether text is a correctly formed dotted-decimal IPv4 address.

## Requirements
- Implement `valid_ipv4(text)` in `starter/solution.py`.
- Return True only for a canonical dotted-decimal IPv4 address with exactly four components, each decimal 0–255 and no leading zeros unless the component is 0. Reject whitespace and signs.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Validate exactly four ASCII decimal components in canonical dotted notation. Reject whitespace, signs, out-of-range octets, and leading zeros on nonzero-length components.

## Tips
Leading zeros, signs, and whitespace can make an address noncanonical.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`valid_ipv4('192.168.1.1')` → `True`; `valid_ipv4('192.168.01.1')` → `False`.

*Source: gauntlex/23-security-crypto/398-cidr-network/README.md*

### 398 — Normalize a Network

## Description
Turn an IPv4 CIDR expression into its canonical network address and prefix.

## Requirements
- Implement `cidr_network(text)` in `starter/solution.py`.
- Given an IPv4 CIDR string, return the canonical network address with prefix as `A.B.C.D/N`. Accept host bits in input. Raise ValueError on invalid addresses or prefix lengths.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Parse the IPv4 address and prefix with standard-library networking utilities, accepting host bits in the input while returning the canonical network address.

## Tips
Host bits may be present in the input, but the result represents the network.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`cidr_network('192.168.1.42/24')` → `'192.168.1.0/24'`.

*Source: gauntlex/23-security-crypto/399-cidr-contains/README.md*

### 399 — Network Membership

## Description
Determine whether an IPv4 address belongs to a specified CIDR network.

## Requirements
- Implement `cidr_contains(network, address)` in `starter/solution.py`.
- Return True if IPv4 address belongs to IPv4 CIDR network, otherwise False. Raise ValueError on malformed inputs.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Determine membership from the full IPv4 network prefix rather than textual address prefixes. Malformed network or address inputs must raise `ValueError`.

## Tips
Network membership depends on the prefix length, not just matching leading text.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`cidr_contains('10.0.0.0/8', '10.2.3.4')` → `True`; `cidr_contains('10.0.0.0/8', '11.0.0.1')` → `False`.

*Source: gauntlex/23-security-crypto/400-safe-url-host/README.md*

### 400 — Inspect a Web Host

## Description
Extract a valid HTTP or HTTPS hostname while rejecting malformed authorities and unsafe URL syntax.

## Requirements
- Implement `safe_url_host(url)` in `starter/solution.py`.
- Return lowercase hostname from an absolute HTTP or HTTPS URL, without port. Raise ValueError for missing hostname, non-HTTP schemes, username/password components, or control characters in the URL. This is syntax validation, not SSRF protection.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Validate URL scheme, authority, credentials, and control characters before returning a normalized hostname. Hostname extraction alone is not sufficient protection against SSRF.

## Tips
Syntax validation alone does not make a URL safe to fetch; SSRF defenses require additional checks.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`safe_url_host('https://Example.COM:443/path')` → `'example.com'`; a URL containing user credentials raises `ValueError`.

*Source: gauntlex/23-security-crypto/401-redact-headers/README.md*

### 401 — Hide Sensitive Headers

## Description
Create a copy of HTTP headers with credential-bearing values redacted.

## Requirements
- Implement `redact_headers(headers)` in `starter/solution.py`.
- Given a mapping of HTTP header names to strings, return a new mapping with values replaced by `[REDACTED]` for Authorization, Cookie, Set-Cookie and X-API-Key, case-insensitively. Preserve original key casing and other values.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Match sensitive header names case-insensitively but preserve the caller's original header spelling in the copied result. Never modify the source mapping.

## Tips
Preserve original header names while comparing them without regard to case.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`redact_headers({'authorization': 'Bearer abc', 'Accept': 'text/plain'})` → `{'authorization': '[REDACTED]', 'Accept': 'text/plain'}`.

*Source: gauntlex/23-security-crypto/402-query-param-filter/README.md*

### 402 — Allowlisted Query Parameters

## Description
Keep only permitted URL query parameters while preserving their original order and repeated keys.

## Requirements
- Implement `filter_query_params(query, allowed)` in `starter/solution.py`.
- Given a URL query string and an iterable of allowed parameter names, return a compact URL query string containing only allowed parameters in original order, preserving repeated keys. Decode and re-encode form URL encoding. Empty result is empty string.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Treat query parameters as an ordered sequence of key-value pairs so repeated names survive. Decode and re-encode form encoding rather than filtering raw substrings.

## Tips
A mapping may discard repeated query keys; the input is an ordered sequence of pairs.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`filter_query_params('a=1&b=2&a=3', ['a'])` → `'a=1&a=3'`.

*Source: gauntlex/23-security-crypto/403-security-event-counts/README.md*

### 403 — Summarize Security Events

## Description
Group security events by severity and type without assuming a fixed list of categories.

## Requirements
- Implement `security_event_counts(events)` in `starter/solution.py`.
- Given a list of event dictionaries containing `type` and `severity` strings, return counts grouped by severity: mapping severity to mapping type to integer count. Preserve all categories, including unknown strings.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Count every severity/type combination without relying on a fixed vocabulary. Unknown category strings are legitimate data and must remain in the nested result.

## Tips
Unknown categories are still valid data and should be counted.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`security_event_counts([{'severity': 'high', 'type': 'login'}, {'severity': 'high', 'type': 'login'}])` → `{'high': {'login': 2}}`.

*Source: gauntlex/23-security-crypto/404-constant-time-match/README.md*

### 404 — Timing-Resistant Equality

## Description
Compare two UTF-8 strings using a standard-library primitive suitable for sensitive comparisons.

## Requirements
- Implement `constant_time_match(a, b)` in `starter/solution.py`.
- Given two UTF-8 strings, return whether they are equal using a constant-time comparison primitive from the standard library. Do not implement a manual early-exit loop.
- Use the Python standard library only.
- Do not print or mutate caller-owned data.

## Design Considerations
Compare UTF-8 encoded strings with a standard-library timing-resistant equality primitive. Avoid manual loops that stop at the first mismatched byte.

## Tips
A manual early-exit comparison can reveal information through timing differences.

Use established standard-library primitives where security is involved; do not invent cryptographic algorithms.

## Example Behavior
`constant_time_match('café', 'café')` → `True`; `constant_time_match('abc', 'abd')` → `False`.

---

## Capstones

*Source: gauntlex/18-capstones/311-task-tracker/README.md*

### 311 — Persistent Task Tracker

## Description
Build a task-management command-line application whose data survives between runs. Users must be able to add, list, complete, and remove tasks.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Commands: `python main.py add TITLE`, `list`, `done ID`, and `delete ID`. Store tasks in a SQLite file specified by `TASK_DB` environment variable; default `tasks.db` in the working directory. The list command prints compact sorted-key JSON of all tasks ordered by ID, with objects `{id:int,title:str,done:bool}`. Add prints the new integer ID, done/delete print `ok` on success and `not found` otherwise. Unknown commands return exit status 2 and print usage to stderr. Titles must not be empty after trimming.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Design the CLI so every command operates on the same persisted SQLite state across separate invocations. Treat malformed titles and missing task IDs as distinct cases.

## Example Behavior
Adding a task and then listing tasks in a fresh process must still show the new task; an unknown command exits with status 2.

## Tips
Separate command parsing from persistence. Think through missing IDs, empty titles, and stable record ordering.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.

*Source: gauntlex/18-capstones/312-log-analyzer/README.md*

### 312 — Streaming Log Inspector

## Description
Create a tool that turns raw application logs into a reliable summary, ignoring invalid records.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Read UTF-8 lines from stdin in `LEVEL|YYYY-MM-DD|MESSAGE` format. LEVEL is INFO, WARN, or ERROR. Validate calendar dates, skip malformed lines, and count each level. Print one compact sorted-key JSON object with keys `total`, `INFO`, `WARN`, `ERROR`, and `dates`, where dates maps YYYY-MM-DD to the number of valid records on that date. Exit successfully even when input is empty. MESSAGE may contain additional pipe symbols.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Parse only the first two separators as structural delimiters; later pipes belong to the message. Validate dates as real calendar dates, not merely strings matching a pattern.

## Example Behavior
A valid `INFO|2026-01-01|start|ready` line counts as one INFO event; an impossible date does not contribute.

## Tips
The log message may contain extra separators. Only validated records should affect counts.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.

*Source: gauntlex/18-capstones/313-expense-ledger/README.md*

### 313 — Expense Ledger

## Description
Build a persistent expense tracker that records amounts as integer cents and summarizes spending by category.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Use `EXPENSE_DB` environment variable or default `expenses.db`. Commands: `add CATEGORY AMOUNT_CENTS`, `summary`, `list`. Amount must be a positive integer; invalid input exits 2 without inserting. `add` prints the new integer ID. `list` prints compact sorted-key JSON array of `{id,category,amount_cents}` in ID order. `summary` prints compact sorted-key JSON mapping category to total integer cents. The database persists across process runs. No floating-point currency arithmetic.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Keep monetary values as integer cents through storage and aggregation. Invalid amounts must not create rows or change summaries.

## Example Behavior
After adding 125 and 75 cents in one category, its summary total is 200 cents, not a floating-point approximation.

## Tips
Money values must not be rounded through floating-point arithmetic.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.

*Source: gauntlex/18-capstones/314-http-api-server/README.md*

### 314 — A Minimal HTTP Service

## Description
Build a small local HTTP API with a health endpoint, an echo endpoint, and predictable JSON errors.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
`main.py` must start an HTTP server on 127.0.0.1 and the port given by `PORT` (positive integer). Implement GET `/health` returning status 200 and JSON `{"status":"ok"}`; GET `/echo?message=TEXT` returning status 200 and JSON `{"message":"TEXT"}` with percent and plus decoding; all other paths return status 404 and JSON `{"error":"not found"}`. Send Content-Type `application/json`. Serialize responses as compact JSON. Shut down cleanly when terminated. Avoid printing request logs to stdout.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use external services or third-party dependencies.
- Keep all state local and ensure deterministic JSON response shapes.
- Do not print debugging information to stdout.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Separate URL path matching from query-string parsing, and encode all responses consistently as compact JSON. Keep request logs off stdout.

## Example Behavior
A GET request to `/health` returns HTTP 200 and `{"status":"ok"}`; an unknown path returns HTTP 404 with the specified JSON error.

## Tips
A request's path and query parameters are different parts of its URL. Keep response encoding consistent.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.

*Source: gauntlex/18-capstones/405-inventory-manager/README.md*

### 405 — Inventory Manager

## Description
Build a persistent stock-management CLI that records quantities and prevents stock from becoming negative.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Build a SQLite-backed inventory CLI. INVENTORY_DB specifies database path. Commands: add SKU QTY, adjust SKU DELTA, get SKU, list. add prints ok or exists; adjust prints ok, insufficient, or not found. get prints compact sorted-key JSON {sku,quantity} or null; list prints JSON array sorted by SKU. Reject invalid integers with exit 2; never permit negative stock.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Guard updates against negative stock before committing changes. Distinguish an unknown SKU from an existing SKU with insufficient quantity.

## Example Behavior
An adjustment that would make stock negative returns `insufficient` and leaves the persisted quantity unchanged.

## Tips
Treat stock updates as guarded state transitions. Invalid quantities and insufficient stock are different failures.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.

*Source: gauntlex/18-capstones/406-contact-book/README.md*

### 406 — Contact Directory

## Description
Build a persistent contact book with case-insensitive email uniqueness and searchable names and addresses.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Build SQLite contact book. CONTACT_DB specifies path. Commands: add NAME EMAIL, find TERM, delete EMAIL, list. Emails are unique case-insensitively; retain original casing. add prints ok or exists; delete prints ok or not found. list and find print compact sorted-key JSON arrays of {name,email}, sorted by lowercase email; find matches case-insensitive substrings in name or email. Empty names/emails exit 2.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Store original email spelling while enforcing uniqueness and lookups case-insensitively. Sort records by normalized email, not by display name.

## Example Behavior
After adding `Ada@Example.com`, adding `ada@example.com` returns `exists` without creating a second contact.

## Tips
Preserve original email spelling while comparing addresses case-insensitively.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.

*Source: gauntlex/18-capstones/407-csv-etl-pipeline/README.md*

### 407 — CSV Data Pipeline

## Description
Transform CSV records into validated, deduplicated JSON Lines using safe file replacement.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Run python main.py INPUT.csv OUTPUT.jsonl. CSV header id,name,amount_cents. Trim fields; require nonempty id/name and nonnegative integer amount. Skip invalid rows; deduplicate by id keeping first valid row. Write compact sorted-key JSONL in original order using temporary file and atomic replacement. Print compact sorted-key JSON {written:N,skipped:M}. Missing args exit 2.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Validate each row before reserving its ID for deduplication. Write output to a temporary file and replace the destination only after the output is complete.

## Example Behavior
If an invalid row uses ID `x` before a valid row with ID `x`, the valid row may still be written as the first valid occurrence.

## Tips
Deduplication keeps the first valid row for each identifier; an invalid earlier row must not claim that identifier.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.

*Source: gauntlex/18-capstones/408-event-sourced-wallet/README.md*

### 408 — Event-Sourced Wallet

## Description
Build a wallet whose balances are derived from an append-only history of credit and debit events.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Use SQLite WALLET_DB path. Commands credit ACCOUNT AMOUNT, debit ACCOUNT AMOUNT, balance ACCOUNT, history ACCOUNT. Amounts are positive integer cents. credit/debit print ok; insufficient debit prints insufficient without recording an event. balance prints integer. history prints compact sorted-key JSON array of {id,account,delta} in event ID order. Events are append-only; balances must be reproducible by replay. Invalid amounts exit 2.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Use append-only events as the source of truth. A rejected debit must leave the event history untouched, and replay must reproduce balances.

## Example Behavior
Credit 500 cents and debit 200 cents for one account: the balance is 300 cents, with two ordered history entries.

## Tips
A rejected debit must not leave an event behind. Every balance must be reproducible from history.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.

*Source: gauntlex/18-capstones/409-markdown-link-checker/README.md*

### 409 — Local Link Inspector

## Description
Inspect Markdown files for broken local links without contacting external websites.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements
Run python main.py ROOT. Recursively inspect Markdown files. Extract inline links [label](target) where target has no spaces or parentheses. Ignore http:, https:, mailto:, and # links. Remove query/fragment from local targets. Resolve relative to containing file; targets beginning / resolve under ROOT. Flag missing files and paths escaping ROOT, including symlinks. Print compact sorted-key JSON array {file,target} sorted by file and target. Exit 1 for broken links, else 0. Never make network requests.

## Constraints
- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables
- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain how persistence, input validation, or the service lifecycle works where applicable.

## Design Considerations
Resolve paths against the correct base and verify their canonical locations remain under ROOT, including when symbolic links are involved. Do not fetch remote links.

## Example Behavior
A Markdown link pointing outside ROOT through `../` or a symlink is reported broken even if the target file exists.

## Tips
A path can appear inside the project yet resolve outside it through traversal or a symbolic link.

## Guide and Auditor
The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.

