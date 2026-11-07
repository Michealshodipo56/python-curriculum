# Python Curriculum — Verified Learning Order

> This is the canonical easiest-to-hardest arrangement for Gauntlex integration. Read it top to bottom. Every listed task points to its pinned authored source; solutions and answer keys are deliberately excluded.

## Audit basis

- **702 primary task files inspected**; **693 assigned** and **9 explicitly withheld/merged**.
- **2606 local starter, support, and test-contract files read** alongside the primary task files.
- Sources: 30 Days 29, C1 194, learn.python 313, Exercism 158.
- Each primary source path appears once. Source-native order is retained where tasks build cumulatively; cross-source placement follows prerequisites rather than repository folder order.
- Existing semantic review notes are honored. Generated/template-heavy project tracks are ordered by their declared level, required tooling, baseline contract, and dependency chain.
- A phase is an unlock boundary. Within a phase, complete entries from top to bottom.

## Difficulty ladder

- **01. Start here: terminal, REPL and first programs** — 7 tasks. Run Python, read tracebacks, print values, and save a script before introducing abstractions.
- **02. Values, input and expressions** — 8 tasks. Variables, numeric operations, strings, booleans, conversion and user input.
- **03. Decisions and repetition** — 38 tasks. Comparisons, conditionals, loops and small stateful programs.
- **04. Collections and data shaping** — 42 tasks. Lists, tuples, dictionaries, sets, comprehensions and nested data.
- **05. Functions, modules and decomposition** — 61 tasks. Return values, parameters, scope, recursion, imports and reusable program structure.
- **06. Files, errors, dates and text parsing** — 36 tasks. Path handling, CSV/JSON, exceptions, regular expressions, validation and robust I/O.
- **07. Objects, typing and Python protocols** — 35 tasks. Classes, dataclasses, inheritance, iterators, generators and type contracts.
- **08. Algorithms and data structures** — 82 tasks. Complexity, search, sorting, stacks, queues, trees, graphs and dynamic programming.
- **09. Testing, debugging and code quality** — 59 tasks. pytest, fixtures, parametrization, mocking, refactoring and quality gates.
- **10. Command-line tools and automation** — 85 tasks. CLI design, filesystem automation, scheduling, subprocesses and resilient batch work.
- **11. HTTP, scraping and API clients** — 44 tasks. HTTP fundamentals, requests, authentication, pagination, scraping and client design.
- **12. Databases and durable data** — 35 tasks. SQLite, SQL, ORM patterns, migrations, idempotency and data pipelines.
- **13. Web applications and services** — 25 tasks. Flask, FastAPI, Django, forms, sessions, CRUD services and API delivery.
- **14. Data analysis, statistics and machine learning** — 36 tasks. NumPy, pandas, visualization, statistics, model training and evaluation.
- **15. Async and concurrent Python** — 11 tasks. Coroutines, producer-consumer systems, concurrent I/O and process coordination.
- **16. Packaging, delivery and operations** — 28 tasks. Packages, Docker, CI, deployment, configuration and operational readiness.
- **17. Architecture, security and reliability** — 57 tasks. System boundaries, observability, policy, performance, resilience and technical leadership.
- **18. Capstones** — 4 tasks. Integrate multiple domains into portfolio-scale, tested and documented systems.

---

## 01 · Start here: terminal, REPL and first programs

Run Python, read tracebacks, print values, and save a script before introducing abstractions.

### learn.python

1. **Hello World** · beginner exercise · Absolute beginner — [learn.python/projects/level-00-absolute-beginner/02-hello-world/exercise.py](learn.python/projects/level-00-absolute-beginner/02-hello-world/exercise.py)
2. **Your First Script** · beginner exercise · Absolute beginner — [learn.python/projects/level-00-absolute-beginner/03-your-first-script/exercise.py](learn.python/projects/level-00-absolute-beginner/03-your-first-script/exercise.py)

### 30 Days

3. **🐍 30 Days Of Python** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/readme.md](30-Days-Of-Python/readme.md)

### C1

4. **Homework Problem 1 — Verify Your Install** · assignment · Beginner — [C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/homework/problem-01-verify-your-install.md](C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/homework/problem-01-verify-your-install.md)
5. **Homework Problem 2 — Project Skeleton with a venv** · assignment · Beginner — [C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/homework/problem-02-project-skeleton-with-a-venv.md](C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/homework/problem-02-project-skeleton-with-a-venv.md)
6. **Homework Problem 4 — Install and Freeze a Package** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/homework/problem-04-install-and-freeze-a-package.md](C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/homework/problem-04-install-and-freeze-a-package.md)
7. **Homework Problem 5 — Publish Your Repo to GitHub** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/homework/problem-05-publish-your-repo-to-github.md](C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/homework/problem-05-publish-your-repo-to-github.md)

## 02 · Values, input and expressions

Variables, numeric operations, strings, booleans, conversion and user input.

### learn.python

9. **Variables** · beginner exercise · Beginner — [learn.python/projects/level-00-absolute-beginner/04-variables/exercise.py](learn.python/projects/level-00-absolute-beginner/04-variables/exercise.py)
10. **Numbers And Math** · beginner exercise · Beginner — [learn.python/projects/level-00-absolute-beginner/05-numbers-and-math/exercise.py](learn.python/projects/level-00-absolute-beginner/05-numbers-and-math/exercise.py)
11. **Strings And Text** · beginner exercise · Beginner — [learn.python/projects/level-00-absolute-beginner/06-strings-and-text/exercise.py](learn.python/projects/level-00-absolute-beginner/06-strings-and-text/exercise.py)
12. **User Input** · beginner exercise · Beginner — [learn.python/projects/level-00-absolute-beginner/07-user-input/exercise.py](learn.python/projects/level-00-absolute-beginner/07-user-input/exercise.py)

### 30 Days

13. **📘 Day 2** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md](30-Days-Of-Python/02_Day_Variables_builtin_functions/02_variables_builtin_functions.md)
14. **📘 Day 3** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/03_Day_Operators/03_operators.md](30-Days-Of-Python/03_Day_Operators/03_operators.md)
15. **Day 4** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/04_Day_Strings/04_strings.md](30-Days-Of-Python/04_Day_Strings/04_strings.md)

### learn.python

16. **Challenge: Swap Variables** · challenge · practice — [learn.python/practice/challenges/beginner/01-swap-variables.py](learn.python/practice/challenges/beginner/01-swap-variables.py)

## 03 · Decisions and repetition

Comparisons, conditionals, loops and small stateful programs.

### learn.python

17. **Making Decisions** · beginner exercise · Beginner — [learn.python/projects/level-00-absolute-beginner/08-making-decisions/exercise.py](learn.python/projects/level-00-absolute-beginner/08-making-decisions/exercise.py)
18. **For Loops** · beginner exercise · Beginner — [learn.python/projects/level-00-absolute-beginner/10-for-loops/exercise.py](learn.python/projects/level-00-absolute-beginner/10-for-loops/exercise.py)
19. **While Loops** · beginner exercise · Beginner — [learn.python/projects/level-00-absolute-beginner/11-while-loops/exercise.py](learn.python/projects/level-00-absolute-beginner/11-while-loops/exercise.py)

### 30 Days

20. **📘 Day 9** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/09_Day_Conditionals/09_conditionals.md](30-Days-Of-Python/09_Day_Conditionals/09_conditionals.md)
21. **📘 Day 10** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/10_Day_Loops/10_loops.md](30-Days-Of-Python/10_Day_Loops/10_loops.md)

### Exercism

22. **Black Jack** · concept · Beginner — [python-curriculum/exercises/concept/black-jack/.docs/instructions.md](python-curriculum/exercises/concept/black-jack/.docs/instructions.md)
23. **Card Games** · concept · Beginner — [python-curriculum/exercises/concept/card-games/.docs/instructions.md](python-curriculum/exercises/concept/card-games/.docs/instructions.md)
24. **Ghost Gobble Arcade Game** · concept · Beginner — [python-curriculum/exercises/concept/ghost-gobble-arcade-game/.docs/instructions.md](python-curriculum/exercises/concept/ghost-gobble-arcade-game/.docs/instructions.md)
25. **Little Sister's Essay** · concept · Beginner — [python-curriculum/exercises/concept/little-sisters-essay/.docs/instructions.md](python-curriculum/exercises/concept/little-sisters-essay/.docs/instructions.md)
26. **Little Sister's Vocabulary** · concept · Beginner — [python-curriculum/exercises/concept/little-sisters-vocab/.docs/instructions.md](python-curriculum/exercises/concept/little-sisters-vocab/.docs/instructions.md)
27. **Making the Grade** · concept · Beginner — [python-curriculum/exercises/concept/making-the-grade/.docs/instructions.md](python-curriculum/exercises/concept/making-the-grade/.docs/instructions.md)
28. **Meltdown Mitigation** · concept · Beginner — [python-curriculum/exercises/concept/meltdown-mitigation/.docs/instructions.md](python-curriculum/exercises/concept/meltdown-mitigation/.docs/instructions.md)
29. **Armstrong Numbers** · practice · Beginner — [python-curriculum/exercises/practice/armstrong-numbers/.docs/instructions.md](python-curriculum/exercises/practice/armstrong-numbers/.docs/instructions.md)
30. **Bob** · practice · Beginner — [python-curriculum/exercises/practice/bob/.docs/instructions.md](python-curriculum/exercises/practice/bob/.docs/instructions.md)
31. **Darts** · practice · Beginner — [python-curriculum/exercises/practice/darts/.docs/instructions.md](python-curriculum/exercises/practice/darts/.docs/instructions.md)
32. **Difference of Squares** · practice · Beginner — [python-curriculum/exercises/practice/difference-of-squares/.docs/instructions.md](python-curriculum/exercises/practice/difference-of-squares/.docs/instructions.md)
33. **Leap** · practice · Beginner — [python-curriculum/exercises/practice/leap/.docs/instructions.md](python-curriculum/exercises/practice/leap/.docs/instructions.md)
34. **Raindrops** · practice · Beginner — [python-curriculum/exercises/practice/raindrops/.docs/instructions.md](python-curriculum/exercises/practice/raindrops/.docs/instructions.md)
35. **Reverse String** · practice · Beginner — [python-curriculum/exercises/practice/reverse-string/.docs/instructions.md](python-curriculum/exercises/practice/reverse-string/.docs/instructions.md)
36. **Acronym** · practice · Beginner plus — [python-curriculum/exercises/practice/acronym/.docs/instructions.md](python-curriculum/exercises/practice/acronym/.docs/instructions.md)
37. **Anagram** · practice · Beginner plus — [python-curriculum/exercises/practice/anagram/.docs/instructions.md](python-curriculum/exercises/practice/anagram/.docs/instructions.md)
38. **Beer Song** · practice · Beginner plus — [python-curriculum/exercises/practice/beer-song/.docs/instructions.md](python-curriculum/exercises/practice/beer-song/.docs/instructions.md)
39. **Bottle Song** · practice · Beginner plus — [python-curriculum/exercises/practice/bottle-song/.docs/instructions.md](python-curriculum/exercises/practice/bottle-song/.docs/instructions.md)
40. **House** · practice · Beginner plus — [python-curriculum/exercises/practice/house/.docs/instructions.md](python-curriculum/exercises/practice/house/.docs/instructions.md)
41. **Rotational Cipher** · practice · Beginner plus — [python-curriculum/exercises/practice/rotational-cipher/.docs/instructions.md](python-curriculum/exercises/practice/rotational-cipher/.docs/instructions.md)
42. **Atbash Cipher** · practice · Intermediate — [python-curriculum/exercises/practice/atbash-cipher/.docs/instructions.md](python-curriculum/exercises/practice/atbash-cipher/.docs/instructions.md)
43. **Diamond** · practice · Intermediate — [python-curriculum/exercises/practice/diamond/.docs/instructions.md](python-curriculum/exercises/practice/diamond/.docs/instructions.md)
44. **Food Chain** · practice · Intermediate — [python-curriculum/exercises/practice/food-chain/.docs/instructions.md](python-curriculum/exercises/practice/food-chain/.docs/instructions.md)
45. **Pig Latin** · practice · Intermediate — [python-curriculum/exercises/practice/pig-latin/.docs/instructions.md](python-curriculum/exercises/practice/pig-latin/.docs/instructions.md)
46. **Run-Length Encoding** · practice · Intermediate — [python-curriculum/exercises/practice/run-length-encoding/.docs/instructions.md](python-curriculum/exercises/practice/run-length-encoding/.docs/instructions.md)
47. **Twelve Days** · practice · Intermediate — [python-curriculum/exercises/practice/twelve-days/.docs/instructions.md](python-curriculum/exercises/practice/twelve-days/.docs/instructions.md)

### learn.python

48. **Challenge: FizzBuzz** · challenge · practice — [learn.python/practice/challenges/beginner/02-fizzbuzz.py](learn.python/practice/challenges/beginner/02-fizzbuzz.py)
49. **Challenge: Reverse String** · challenge · practice — [learn.python/practice/challenges/beginner/03-reverse-string.py](learn.python/practice/challenges/beginner/03-reverse-string.py)
50. **Challenge: Count Vowels** · challenge · practice — [learn.python/practice/challenges/beginner/04-count-vowels.py](learn.python/practice/challenges/beginner/04-count-vowels.py)
51. **Challenge: Palindrome Check** · challenge · practice — [learn.python/practice/challenges/beginner/05-palindrome-check.py](learn.python/practice/challenges/beginner/05-palindrome-check.py)
52. **Challenge: Sum of Digits** · challenge · practice — [learn.python/practice/challenges/beginner/06-sum-of-digits.py](learn.python/practice/challenges/beginner/06-sum-of-digits.py)
53. **Challenge: Find Maximum** · challenge · practice — [learn.python/practice/challenges/beginner/07-find-max.py](learn.python/practice/challenges/beginner/07-find-max.py)
54. **Challenge: Caesar Cipher** · challenge · practice — [learn.python/practice/challenges/beginner/10-caesar-cipher.py](learn.python/practice/challenges/beginner/10-caesar-cipher.py)

## 04 · Collections and data shaping

Lists, tuples, dictionaries, sets, comprehensions and nested data.

### learn.python

55. **Lists** · beginner exercise · Beginner — [learn.python/projects/level-00-absolute-beginner/09-lists/exercise.py](learn.python/projects/level-00-absolute-beginner/09-lists/exercise.py)
56. **Dictionaries** · beginner exercise · Beginner — [learn.python/projects/level-00-absolute-beginner/12-dictionaries/exercise.py](learn.python/projects/level-00-absolute-beginner/12-dictionaries/exercise.py)

### 30 Days

57. **Day 5** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/05_Day_Lists/05_lists.md](30-Days-Of-Python/05_Day_Lists/05_lists.md)
58. **Day 6** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/06_Day_Tuples/06_tuples.md](30-Days-Of-Python/06_Day_Tuples/06_tuples.md)
59. **📘 Day 7** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/07_Day_Sets/07_sets.md](30-Days-Of-Python/07_Day_Sets/07_sets.md)
60. **📘 Day 8** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/08_Day_Dictionaries/08_dictionaries.md](30-Days-Of-Python/08_Day_Dictionaries/08_dictionaries.md)
61. **📘 Day 13** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/13_Day_List_comprehension/13_list_comprehension.md](30-Days-Of-Python/13_Day_List_comprehension/13_list_comprehension.md)

### Exercism

62. **Resistor Color** · practice · Beginner — [python-curriculum/exercises/practice/resistor-color/.docs/instructions.md](python-curriculum/exercises/practice/resistor-color/.docs/instructions.md)
63. **Resistor Color Duo** · practice · Beginner — [python-curriculum/exercises/practice/resistor-color-duo/.docs/instructions.md](python-curriculum/exercises/practice/resistor-color-duo/.docs/instructions.md)
64. **Chaitana's Colossal Coaster** · concept · Beginner — [python-curriculum/exercises/concept/chaitanas-colossal-coaster/.docs/instructions.md](python-curriculum/exercises/concept/chaitanas-colossal-coaster/.docs/instructions.md)
65. **Inventory Management** · concept · Beginner — [python-curriculum/exercises/concept/inventory-management/.docs/instructions.md](python-curriculum/exercises/concept/inventory-management/.docs/instructions.md)
66. **Tisbury Treasure Hunt** · concept · Beginner — [python-curriculum/exercises/concept/tisbury-treasure-hunt/.docs/instructions.md](python-curriculum/exercises/concept/tisbury-treasure-hunt/.docs/instructions.md)
67. **Isogram** · practice · Beginner — [python-curriculum/exercises/practice/isogram/.docs/instructions.md](python-curriculum/exercises/practice/isogram/.docs/instructions.md)
68. **Line Up** · practice · Beginner — [python-curriculum/exercises/practice/line-up/.docs/instructions.md](python-curriculum/exercises/practice/line-up/.docs/instructions.md)
69. **Pangram** · practice · Beginner — [python-curriculum/exercises/practice/pangram/.docs/instructions.md](python-curriculum/exercises/practice/pangram/.docs/instructions.md)
70. **RNA Transcription** · practice · Beginner — [python-curriculum/exercises/practice/rna-transcription/.docs/instructions.md](python-curriculum/exercises/practice/rna-transcription/.docs/instructions.md)
71. **Triangle** · practice · Beginner — [python-curriculum/exercises/practice/triangle/.docs/instructions.md](python-curriculum/exercises/practice/triangle/.docs/instructions.md)
72. **Resistor Color Trio** · practice · Beginner plus — [python-curriculum/exercises/practice/resistor-color-trio/.docs/instructions.md](python-curriculum/exercises/practice/resistor-color-trio/.docs/instructions.md)
73. **Cater Waiter** · concept · Beginner plus — [python-curriculum/exercises/concept/cater-waiter/.docs/instructions.md](python-curriculum/exercises/concept/cater-waiter/.docs/instructions.md)
74. **Mecha Munch Management** · concept · Beginner plus — [python-curriculum/exercises/concept/mecha-munch-management/.docs/instructions.md](python-curriculum/exercises/concept/mecha-munch-management/.docs/instructions.md)
75. **ETL** · practice · Beginner plus — [python-curriculum/exercises/practice/etl/.docs/instructions.md](python-curriculum/exercises/practice/etl/.docs/instructions.md)
76. **Nucleotide Count** · practice · Beginner plus — [python-curriculum/exercises/practice/nucleotide-count/.docs/instructions.md](python-curriculum/exercises/practice/nucleotide-count/.docs/instructions.md)
77. **Protein Translation** · practice · Beginner plus — [python-curriculum/exercises/practice/protein-translation/.docs/instructions.md](python-curriculum/exercises/practice/protein-translation/.docs/instructions.md)
78. **Scrabble Score** · practice · Beginner plus — [python-curriculum/exercises/practice/scrabble-score/.docs/instructions.md](python-curriculum/exercises/practice/scrabble-score/.docs/instructions.md)
79. **Secret Handshake** · practice · Beginner plus — [python-curriculum/exercises/practice/secret-handshake/.docs/instructions.md](python-curriculum/exercises/practice/secret-handshake/.docs/instructions.md)
80. **Sum of Multiples** · practice · Beginner plus — [python-curriculum/exercises/practice/sum-of-multiples/.docs/instructions.md](python-curriculum/exercises/practice/sum-of-multiples/.docs/instructions.md)
81. **Resistor Color Expert** · practice · Intermediate — [python-curriculum/exercises/practice/resistor-color-expert/.docs/instructions.md](python-curriculum/exercises/practice/resistor-color-expert/.docs/instructions.md)
82. **Crypto Square** · practice · Intermediate — [python-curriculum/exercises/practice/crypto-square/.docs/instructions.md](python-curriculum/exercises/practice/crypto-square/.docs/instructions.md)
83. **Flower Field** · practice · Intermediate — [python-curriculum/exercises/practice/flower-field/.docs/instructions.md](python-curriculum/exercises/practice/flower-field/.docs/instructions.md)
84. **Conway's Game of Life** · practice · Intermediate — [python-curriculum/exercises/practice/game-of-life/.docs/instructions.md](python-curriculum/exercises/practice/game-of-life/.docs/instructions.md)
85. **Saddle Points** · practice · Intermediate — [python-curriculum/exercises/practice/saddle-points/.docs/instructions.md](python-curriculum/exercises/practice/saddle-points/.docs/instructions.md)
86. **Spiral Matrix** · practice · Intermediate — [python-curriculum/exercises/practice/spiral-matrix/.docs/instructions.md](python-curriculum/exercises/practice/spiral-matrix/.docs/instructions.md)
87. **Transpose** · practice · Intermediate — [python-curriculum/exercises/practice/transpose/.docs/instructions.md](python-curriculum/exercises/practice/transpose/.docs/instructions.md)
88. **Yacht** · practice · Intermediate — [python-curriculum/exercises/practice/yacht/.docs/instructions.md](python-curriculum/exercises/practice/yacht/.docs/instructions.md)

### learn.python

89. **Challenge: Remove Duplicates** · challenge · practice — [learn.python/practice/challenges/beginner/08-remove-duplicates.py](learn.python/practice/challenges/beginner/08-remove-duplicates.py)
90. **Challenge: Word Frequency** · challenge · practice — [learn.python/practice/challenges/beginner/09-word-frequency.py](learn.python/practice/challenges/beginner/09-word-frequency.py)
91. **Challenge: Flatten List** · challenge · practice — [learn.python/practice/challenges/beginner/11-flatten-list.py](learn.python/practice/challenges/beginner/11-flatten-list.py)
92. **Challenge: Matrix Transpose** · challenge · practice — [learn.python/practice/challenges/beginner/12-matrix-transpose.py](learn.python/practice/challenges/beginner/12-matrix-transpose.py)
93. **Challenge: Anagram Check** · challenge · practice — [learn.python/practice/challenges/beginner/15-anagram-check.py](learn.python/practice/challenges/beginner/15-anagram-check.py)
94. **Fill-In Challenge 1 — List Filtering** · challenge · practice — [learn.python/practice/challenges/fill-in/01_list_filter.py](learn.python/practice/challenges/fill-in/01_list_filter.py)
95. **Fill-In Challenge 2 — Dictionary Builder** · challenge · practice — [learn.python/practice/challenges/fill-in/02_dict_builder.py](learn.python/practice/challenges/fill-in/02_dict_builder.py)
96. **Fill-In Challenge 4 — String Formatter** · challenge · practice — [learn.python/practice/challenges/fill-in/04_string_formatter.py](learn.python/practice/challenges/fill-in/04_string_formatter.py)

## 05 · Functions, modules and decomposition

Return values, parameters, scope, recursion, imports and reusable program structure.

### learn.python

97. **Functions** · beginner exercise · Beginner — [learn.python/projects/level-00-absolute-beginner/13-functions/exercise.py](learn.python/projects/level-00-absolute-beginner/13-functions/exercise.py)

### 30 Days

98. **📘 Day 11** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/11_Day_Functions/11_functions.md](30-Days-Of-Python/11_Day_Functions/11_functions.md)
99. **📘 Day 12** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/12_Day_Modules/12_modules.md](30-Days-Of-Python/12_Day_Modules/12_modules.md)
100. **📘 Day 14** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/14_Day_Higher_order_functions/14_higher_order_functions.md](30-Days-Of-Python/14_Day_Higher_order_functions/14_higher_order_functions.md)

### C1

101. **Exercise 1 — Hello, World** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/exercises/exercise-01-hello-world.md](C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/exercises/exercise-01-hello-world.md)
102. **Exercise 2 — REPL Explorer** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/exercises/exercise-02-repl-explorer.md](C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/exercises/exercise-02-repl-explorer.md)
103. **Exercise 1 — Variable Swap** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/exercises/exercise-01-variable-swap.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/exercises/exercise-01-variable-swap.md)
104. **Exercise 2 — String Formatter** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/exercises/exercise-02-string-formatter.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/exercises/exercise-02-string-formatter.md)
105. **Exercise 3 — Temperature Converter** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/exercises/exercise-03-temperature-converter.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/exercises/exercise-03-temperature-converter.md)
106. **Exercise 1 — FizzBuzz** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/exercises/exercise-01-fizzbuzz.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/exercises/exercise-01-fizzbuzz.md)
107. **Exercise 2 — Sum of Evens** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/exercises/exercise-02-sum-evens.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/exercises/exercise-02-sum-evens.md)
108. **Exercise 3 — Password Checker** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/exercises/exercise-03-password-checker.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/exercises/exercise-03-password-checker.md)
109. **Exercise 4 — Multiplication Table** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/exercises/exercise-04-multiplication-table.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/exercises/exercise-04-multiplication-table.md)
110. **Exercise 1 — Function Basics** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/exercises/exercise-01-function-basics.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/exercises/exercise-01-function-basics.md)
111. **Exercise 2 — args and kwargs** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/exercises/exercise-02-args-kwargs.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/exercises/exercise-02-args-kwargs.md)
112. **Exercise 4 — Scope Mystery** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/exercises/exercise-04-scope-mystery.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/exercises/exercise-04-scope-mystery.md)
113. **Exercise 5 — Import and Use** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/exercises/exercise-05-import-and-use.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/exercises/exercise-05-import-and-use.md)
114. **Exercise 1 — List Operations** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/exercises/exercise-01-list-operations.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/exercises/exercise-01-list-operations.md)
115. **Exercise 2 — Deduplicate** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/exercises/exercise-02-deduplicate.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/exercises/exercise-02-deduplicate.md)
116. **Exercise 3 — Word Frequency** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/exercises/exercise-03-word-frequency.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/exercises/exercise-03-word-frequency.md)
117. **Exercise 4 — Set Operations** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/exercises/exercise-04-set-operations.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/exercises/exercise-04-set-operations.md)
118. **Exercise 5 — Comprehensions** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/exercises/exercise-05-comprehensions.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/exercises/exercise-05-comprehensions.md)
119. **Homework Problem 3 — A Tiny Script with Comments and a Docstring** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/homework/problem-03-a-tiny-script-with-comments-and-a-docstring.md](C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/homework/problem-03-a-tiny-script-with-comments-and-a-docstring.md)
120. **Homework Problem 1 — Simple Interest Calculator** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/homework/problem-01-simple-interest-calculator.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/homework/problem-01-simple-interest-calculator.md)
121. **Homework Problem 2 — BMI Calculator** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/homework/problem-02-bmi-calculator.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/homework/problem-02-bmi-calculator.md)
122. **Homework Problem 3 — Word and Character Counter** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/homework/problem-03-word-and-character-counter.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/homework/problem-03-word-and-character-counter.md)
123. **Homework Problem 4 — Grade Letter Assigner (No if)** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/homework/problem-04-grade-letter-assigner-no-if.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/homework/problem-04-grade-letter-assigner-no-if.md)
124. **Homework Problem 5 — Compound Interest** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/homework/problem-05-compound-interest.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/homework/problem-05-compound-interest.md)
125. **Homework Problem 6 — Distance and Speed Report** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/homework/problem-06-distance-and-speed-report.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/homework/problem-06-distance-and-speed-report.md)
126. **Homework Problem 1 — Leap Year Checker** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/homework/problem-01-leap-year-checker.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/homework/problem-01-leap-year-checker.md)
127. **Homework Problem 2 — Count Vowels in a String** · assignment · Beginner — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/homework/problem-02-count-vowels-in-a-string.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/homework/problem-02-count-vowels-in-a-string.md)
128. **Homework Problem 3 — Reverse a Number** · assignment · Beginner — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/homework/problem-03-reverse-a-number.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/homework/problem-03-reverse-a-number.md)
129. **Homework Problem 4 — Sum of Digits** · assignment · Beginner — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/homework/problem-04-sum-of-digits.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/homework/problem-04-sum-of-digits.md)
130. **Homework Problem 5 — Fibonacci Numbers up to N** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/homework/problem-05-fibonacci-numbers-up-to-n.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/homework/problem-05-fibonacci-numbers-up-to-n.md)
131. **Homework Problem 1 — Temperature Module** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/homework/problem-01-temperature-module.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/homework/problem-01-temperature-module.md)
132. **Homework Problem 2 — Password Strength** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/homework/problem-02-password-strength.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/homework/problem-02-password-strength.md)
133. **Homework Problem 5 — Dict Builder** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/homework/problem-05-dict-builder.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/homework/problem-05-dict-builder.md)
134. **Homework Problem 6 — Importing From a Custom Module** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/homework/problem-06-importing-from-a-custom-module.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/homework/problem-06-importing-from-a-custom-module.md)
135. **Homework Problem 1 — Matrix transpose (with a comprehension)** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/homework/problem-01-matrix-transpose-with-a-comprehension.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/homework/problem-01-matrix-transpose-with-a-comprehension.md)
136. **Homework Problem 2 — Invert a dictionary** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/homework/problem-02-invert-a-dictionary.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/homework/problem-02-invert-a-dictionary.md)
137. **Homework Problem 4 — Find duplicates** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/homework/problem-04-find-duplicates.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/homework/problem-04-find-duplicates.md)
138. **Homework Problem 5 — Group by first letter** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/homework/problem-05-group-by-first-letter.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/homework/problem-05-group-by-first-letter.md)
139. **Homework Problem 6 — Intersect dictionaries** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/homework/problem-06-intersect-dictionaries.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/homework/problem-06-intersect-dictionaries.md)
140. **Challenge 1 — Tip Calculator** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/challenges/challenge-01-tip-calculator.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/challenges/challenge-01-tip-calculator.md)
141. **Challenge 2 — Mad Libs Generator** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/challenges/challenge-02-mad-libs.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/challenges/challenge-02-mad-libs.md)
142. **Challenge 1 — Caesar Cipher** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/challenges/challenge-01-caesar-cipher.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/challenges/challenge-01-caesar-cipher.md)
143. **Challenge 2 — Rock, Paper, Scissors** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/challenges/challenge-02-rps.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/challenges/challenge-02-rps.md)
144. **Challenge 1 — Mini Calculator Module** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/challenges/challenge-01-mini-calculator-module.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/challenges/challenge-01-mini-calculator-module.md)
145. **Challenge 2 — Text Stats Package** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/challenges/challenge-02-text-stats-package.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/challenges/challenge-02-text-stats-package.md)
146. **Challenge 1 — Anagram Groups** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/challenges/challenge-01-anagram-groups.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/challenges/challenge-01-anagram-groups.md)
147. **Challenge 2 — Inventory Tracker** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/challenges/challenge-02-inventory-tracker.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/challenges/challenge-02-inventory-tracker.md)

### Exercism

148. **Currency Exchange** · concept · Beginner — [python-curriculum/exercises/concept/currency-exchange/.docs/instructions.md](python-curriculum/exercises/concept/currency-exchange/.docs/instructions.md)
149. **Guido's Gorgeous Lasagna** · concept · Beginner — [python-curriculum/exercises/concept/guidos-gorgeous-lasagna/.docs/instructions.md](python-curriculum/exercises/concept/guidos-gorgeous-lasagna/.docs/instructions.md)
150. **Hello World** · practice · Beginner — [python-curriculum/exercises/practice/hello-world/.docs/instructions.md](python-curriculum/exercises/practice/hello-world/.docs/instructions.md)
151. **Two Fer** · practice · Beginner — [python-curriculum/exercises/practice/two-fer/.docs/instructions.md](python-curriculum/exercises/practice/two-fer/.docs/instructions.md)
152. **Proverb** · practice · Intermediate — [python-curriculum/exercises/practice/proverb/.docs/instructions.md](python-curriculum/exercises/practice/proverb/.docs/instructions.md)

### C1

153. **Mini-Project — "Hello, You"** · project · project — [C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/mini-project/README.md)
154. **Mini-Project — Unit Converter CLI** · project · project — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/mini-project/README.md)
155. **Mini-Project — Number Guessing Game** · project · project — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/mini-project/README.md)
156. **Mini-Project — Personal Finance Calculator** · project · project — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/mini-project/README.md)
157. **Mini-Project — Contact Book Manager** · project · project — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/mini-project/README.md)

## 06 · Files, errors, dates and text parsing

Path handling, CSV/JSON, exceptions, regular expressions, validation and robust I/O.

### learn.python

158. **Reading Files** · beginner exercise · Beginner — [learn.python/projects/level-00-absolute-beginner/14-reading-files/exercise.py](learn.python/projects/level-00-absolute-beginner/14-reading-files/exercise.py)
159. **Putting It Together** · beginner exercise · Beginner integration — [learn.python/projects/level-00-absolute-beginner/15-putting-it-together/exercise.py](learn.python/projects/level-00-absolute-beginner/15-putting-it-together/exercise.py)

### 30 Days

160. **📘 Day 15** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/15_Day_Python_type_errors/15_python_type_errors.md](30-Days-Of-Python/15_Day_Python_type_errors/15_python_type_errors.md)
161. **📘 Day 16** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/16_Day_Python_date_time/16_python_datetime.md](30-Days-Of-Python/16_Day_Python_date_time/16_python_datetime.md)
162. **📘 Day 17** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/17_Day_Exception_handling/17_exception_handling.md](30-Days-Of-Python/17_Day_Exception_handling/17_exception_handling.md)
163. **📘 Day 18** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/18_Day_Regular_expressions/18_regular_expressions.md](30-Days-Of-Python/18_Day_Regular_expressions/18_regular_expressions.md)
164. **📘 Day 19** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/19_Day_File_handling/19_file_handling.md](30-Days-Of-Python/19_Day_File_handling/19_file_handling.md)

### C1

165. **Exercise 1 — Read, Clean, Write** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/exercises/exercise-01-read-write.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/exercises/exercise-01-read-write.md)
166. **Exercise 2 — CSV Roundtrip** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/exercises/exercise-02-csv-roundtrip.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/exercises/exercise-02-csv-roundtrip.md)
167. **Exercise 3 — JSON Config** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/exercises/exercise-03-json-config.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/exercises/exercise-03-json-config.md)
168. **Exercise 4 — Safe Divide** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/exercises/exercise-04-safe-divide.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/exercises/exercise-04-safe-divide.md)
169. **Exercise 5 — Custom Exception** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/exercises/exercise-05-custom-exception.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/exercises/exercise-05-custom-exception.md)
170. **Homework Problem 1 — Word-count CLI** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/homework/problem-01-word-count-cli.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/homework/problem-01-word-count-cli.md)
171. **Homework Problem 2 — CSV Merger** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/homework/problem-02-csv-merger.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/homework/problem-02-csv-merger.md)
172. **Homework Problem 3 — JSON Pretty-Printer** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/homework/problem-03-json-pretty-printer.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/homework/problem-03-json-pretty-printer.md)
173. **Homework Problem 4 — Retry-On-Error Decorator (Preview Of Decorators)** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/homework/problem-04-retry-on-error-decorator-preview-of-decorators.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/homework/problem-04-retry-on-error-decorator-preview-of-decorators.md)
174. **Homework Problem 5 — File Watcher (Poll-Based)** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/homework/problem-05-file-watcher-poll-based.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/homework/problem-05-file-watcher-poll-based.md)
175. **Homework Problem 6 — Atomic-Save Helper** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/homework/problem-06-atomic-save-helper.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/homework/problem-06-atomic-save-helper.md)
176. **Challenge 1 — Recursive Line Counter** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/challenges/challenge-01-recursive-line-counter.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/challenges/challenge-01-recursive-line-counter.md)
177. **Challenge 2 — Config Validator** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/challenges/challenge-02-config-validator.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/challenges/challenge-02-config-validator.md)

### Exercism

178. **Collatz Conjecture** · practice · Beginner plus — [python-curriculum/exercises/practice/collatz-conjecture/.docs/instructions.md](python-curriculum/exercises/practice/collatz-conjecture/.docs/instructions.md)
179. **Gigasecond** · practice · Beginner plus — [python-curriculum/exercises/practice/gigasecond/.docs/instructions.md](python-curriculum/exercises/practice/gigasecond/.docs/instructions.md)
180. **Grains** · practice · Beginner plus — [python-curriculum/exercises/practice/grains/.docs/instructions.md](python-curriculum/exercises/practice/grains/.docs/instructions.md)
181. **Hamming** · practice · Beginner plus — [python-curriculum/exercises/practice/hamming/.docs/instructions.md](python-curriculum/exercises/practice/hamming/.docs/instructions.md)
182. **ISBN Verifier** · practice · Beginner plus — [python-curriculum/exercises/practice/isbn-verifier/.docs/instructions.md](python-curriculum/exercises/practice/isbn-verifier/.docs/instructions.md)
183. **Series** · practice · Beginner plus — [python-curriculum/exercises/practice/series/.docs/instructions.md](python-curriculum/exercises/practice/series/.docs/instructions.md)
184. **Pretty Leaflet** · concept · Intermediate — [python-curriculum/exercises/concept/pretty-leaflet/.docs/instructions.md](python-curriculum/exercises/concept/pretty-leaflet/.docs/instructions.md)
185. **Meetup** · practice · Intermediate — [python-curriculum/exercises/practice/meetup/.docs/instructions.md](python-curriculum/exercises/practice/meetup/.docs/instructions.md)
186. **OCR Numbers** · practice · Intermediate — [python-curriculum/exercises/practice/ocr-numbers/.docs/instructions.md](python-curriculum/exercises/practice/ocr-numbers/.docs/instructions.md)
187. **Swift Scheduling** · practice · Intermediate — [python-curriculum/exercises/practice/swift-scheduling/.docs/instructions.md](python-curriculum/exercises/practice/swift-scheduling/.docs/instructions.md)
188. **Tournament** · practice · Intermediate — [python-curriculum/exercises/practice/tournament/.docs/instructions.md](python-curriculum/exercises/practice/tournament/.docs/instructions.md)
189. **Word Count** · practice · Intermediate — [python-curriculum/exercises/practice/word-count/.docs/instructions.md](python-curriculum/exercises/practice/word-count/.docs/instructions.md)
190. **Wordy** · practice · Intermediate — [python-curriculum/exercises/practice/wordy/.docs/instructions.md](python-curriculum/exercises/practice/wordy/.docs/instructions.md)

### learn.python

191. **Fill-In Challenge 3 — File Reader** · challenge · practice — [learn.python/practice/challenges/fill-in/03_file_reader.py](learn.python/practice/challenges/fill-in/03_file_reader.py)
192. **Fill-In Challenge 6 — Error Handler** · challenge · practice — [learn.python/practice/challenges/fill-in/06_error_handler.py](learn.python/practice/challenges/fill-in/06_error_handler.py)

### C1

193. **Mini-Project — Log File Analyzer** · project · project — [C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-06-file-io-exceptions/mini-project/README.md)

## 07 · Objects, typing and Python protocols

Classes, dataclasses, inheritance, iterators, generators and type contracts.

### 30 Days

194. **📘 Day 21** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/21_Day_Classes_and_objects/21_classes_and_objects.md](30-Days-Of-Python/21_Day_Classes_and_objects/21_classes_and_objects.md)

### C1

195. **Exercise 1 — The Dog Class** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/exercises/exercise-01-dog-class.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/exercises/exercise-01-dog-class.md)
196. **Exercise 2 — Rectangle** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/exercises/exercise-02-rectangle.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/exercises/exercise-02-rectangle.md)
197. **Exercise 3 — Inheritance and Shapes** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/exercises/exercise-03-inheritance-shapes.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/exercises/exercise-03-inheritance-shapes.md)
198. **Exercise 4 — Dataclass User** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/exercises/exercise-04-dataclass-user.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/exercises/exercise-04-dataclass-user.md)
199. **Exercise 5 — Bank Account** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/exercises/exercise-05-bank-account.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/exercises/exercise-05-bank-account.md)
200. **Problem 1 — BankAccount with interest** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/homework/problem-01-bankaccount-with-interest.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/homework/problem-01-bankaccount-with-interest.md)
201. **Problem 2 — Polygon hierarchy** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/homework/problem-02-polygon-hierarchy.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/homework/problem-02-polygon-hierarchy.md)
202. **Problem 3 — Stack built on a list** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/homework/problem-03-stack-built-on-a-list.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/homework/problem-03-stack-built-on-a-list.md)
203. **Problem 4 — Simple ORM-like model** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/homework/problem-04-simple-orm-like-model.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/homework/problem-04-simple-orm-like-model.md)
204. **Problem 5 — Observer pattern (light)** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/homework/problem-05-observer-pattern-light.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/homework/problem-05-observer-pattern-light.md)
205. **Problem 6 — Unit-conversion class** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/homework/problem-06-unit-conversion-class.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/homework/problem-06-unit-conversion-class.md)
206. **Challenge 01 — A Deck of Cards** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/challenges/challenge-01-deck-of-cards.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/challenges/challenge-01-deck-of-cards.md)
207. **Challenge 02 — Employee Hierarchy and Payroll** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/challenges/challenge-02-employee-hierarchy.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/challenges/challenge-02-employee-hierarchy.md)

### Exercism

208. **High Scores** · practice · Beginner plus — [python-curriculum/exercises/practice/high-scores/.docs/instructions.md](python-curriculum/exercises/practice/high-scores/.docs/instructions.md)
209. **Matrix** · practice · Beginner plus — [python-curriculum/exercises/practice/matrix/.docs/instructions.md](python-curriculum/exercises/practice/matrix/.docs/instructions.md)
210. **Space Age** · practice · Beginner plus — [python-curriculum/exercises/practice/space-age/.docs/instructions.md](python-curriculum/exercises/practice/space-age/.docs/instructions.md)
211. **Ellen's Alien Game** · concept · Intermediate — [python-curriculum/exercises/concept/ellens-alien-game/.docs/instructions.md](python-curriculum/exercises/concept/ellens-alien-game/.docs/instructions.md)
212. **Locomotive Engineer** · concept · Intermediate — [python-curriculum/exercises/concept/locomotive-engineer/.docs/instructions.md](python-curriculum/exercises/concept/locomotive-engineer/.docs/instructions.md)
213. **Log Levels** · concept · Intermediate — [python-curriculum/exercises/concept/log-levels/.docs/instructions.md](python-curriculum/exercises/concept/log-levels/.docs/instructions.md)
214. **Plane Tickets** · concept · Intermediate — [python-curriculum/exercises/concept/plane-tickets/.docs/instructions.md](python-curriculum/exercises/concept/plane-tickets/.docs/instructions.md)
215. **Accumulate** · practice · Intermediate — [python-curriculum/exercises/practice/accumulate/.docs/instructions.md](python-curriculum/exercises/practice/accumulate/.docs/instructions.md)
216. **Clock** · practice · Intermediate — [python-curriculum/exercises/practice/clock/.docs/instructions.md](python-curriculum/exercises/practice/clock/.docs/instructions.md)
217. **Custom Set** · practice · Intermediate — [python-curriculum/exercises/practice/custom-set/.docs/instructions.md](python-curriculum/exercises/practice/custom-set/.docs/instructions.md)
218. **Error Handling** · practice · Intermediate — [python-curriculum/exercises/practice/error-handling/.docs/instructions.md](python-curriculum/exercises/practice/error-handling/.docs/instructions.md)
219. **Kindergarten Garden** · practice · Intermediate — [python-curriculum/exercises/practice/kindergarten-garden/.docs/instructions.md](python-curriculum/exercises/practice/kindergarten-garden/.docs/instructions.md)
220. **List Ops** · practice · Intermediate — [python-curriculum/exercises/practice/list-ops/.docs/instructions.md](python-curriculum/exercises/practice/list-ops/.docs/instructions.md)
221. **Luhn** · practice · Intermediate — [python-curriculum/exercises/practice/luhn/.docs/instructions.md](python-curriculum/exercises/practice/luhn/.docs/instructions.md)
222. **Phone Number** · practice · Intermediate — [python-curriculum/exercises/practice/phone-number/.docs/instructions.md](python-curriculum/exercises/practice/phone-number/.docs/instructions.md)
223. **Queen Attack** · practice · Intermediate — [python-curriculum/exercises/practice/queen-attack/.docs/instructions.md](python-curriculum/exercises/practice/queen-attack/.docs/instructions.md)
224. **Strain** · practice · Intermediate — [python-curriculum/exercises/practice/strain/.docs/instructions.md](python-curriculum/exercises/practice/strain/.docs/instructions.md)
225. **Complex Numbers** · practice · Intermediate plus — [python-curriculum/exercises/practice/complex-numbers/.docs/instructions.md](python-curriculum/exercises/practice/complex-numbers/.docs/instructions.md)
226. **Rational Numbers** · practice · Intermediate plus — [python-curriculum/exercises/practice/rational-numbers/.docs/instructions.md](python-curriculum/exercises/practice/rational-numbers/.docs/instructions.md)

### learn.python

227. **Fill-In Challenge 5 — Basic Class** · challenge · practice — [learn.python/practice/challenges/fill-in/05_basic_class.py](learn.python/practice/challenges/fill-in/05_basic_class.py)

### C1

228. **Mini-Project — Library Management System** · project · project — [C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-07-object-oriented-programming/mini-project/README.md)

## 08 · Algorithms and data structures

Complexity, search, sorting, stacks, queues, trees, graphs and dynamic programming.

### C1

229. **Exercise 3 — Script vs REPL** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/exercises/exercise-03-script-vs-repl.md](C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/exercises/exercise-03-script-vs-repl.md)
230. **Exercise 5 — Find the Prime** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/exercises/exercise-05-find-prime.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/exercises/exercise-05-find-prime.md)
231. **Exercise 3 — Recursion Intro** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/exercises/exercise-03-recursion-intro.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/exercises/exercise-03-recursion-intro.md)
232. **Homework Problem 4 — Recursive Sum** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/homework/problem-04-recursive-sum.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/homework/problem-04-recursive-sum.md)
233. **Homework Problem 3 — Two-Sum (classic)** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-05-data-structures/homework/problem-03-two-sum-classic.md](C1-Code-Crunch-Convos/curriculum/week-05-data-structures/homework/problem-03-two-sum-classic.md)
234. **Challenge 2 — Environment Audit** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/challenges/challenge-02-environment-audit.md](C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/challenges/challenge-02-environment-audit.md)

### Exercism

235. **Binary** · practice · Beginner plus — [python-curriculum/exercises/practice/binary/.docs/instructions.md](python-curriculum/exercises/practice/binary/.docs/instructions.md)
236. **Eliud's Eggs** · practice · Beginner plus — [python-curriculum/exercises/practice/eliuds-eggs/.docs/instructions.md](python-curriculum/exercises/practice/eliuds-eggs/.docs/instructions.md)
237. **Hexadecimal** · practice · Beginner plus — [python-curriculum/exercises/practice/hexadecimal/.docs/instructions.md](python-curriculum/exercises/practice/hexadecimal/.docs/instructions.md)
238. **Trinary** · practice · Beginner plus — [python-curriculum/exercises/practice/trinary/.docs/instructions.md](python-curriculum/exercises/practice/trinary/.docs/instructions.md)
239. **All Your Base** · practice · Intermediate — [python-curriculum/exercises/practice/all-your-base/.docs/instructions.md](python-curriculum/exercises/practice/all-your-base/.docs/instructions.md)
240. **Allergies** · practice · Intermediate — [python-curriculum/exercises/practice/allergies/.docs/instructions.md](python-curriculum/exercises/practice/allergies/.docs/instructions.md)
241. **Bank Account** · practice · Intermediate — [python-curriculum/exercises/practice/bank-account/.docs/instructions.md](python-curriculum/exercises/practice/bank-account/.docs/instructions.md)
242. **Binary Search** · practice · Intermediate — [python-curriculum/exercises/practice/binary-search/.docs/instructions.md](python-curriculum/exercises/practice/binary-search/.docs/instructions.md)
243. **Circular Buffer** · practice · Intermediate — [python-curriculum/exercises/practice/circular-buffer/.docs/instructions.md](python-curriculum/exercises/practice/circular-buffer/.docs/instructions.md)
244. **D&D Character** · practice · Intermediate — [python-curriculum/exercises/practice/dnd-character/.docs/instructions.md](python-curriculum/exercises/practice/dnd-character/.docs/instructions.md)
245. **DOT DSL** · practice · Intermediate — [python-curriculum/exercises/practice/dot-dsl/.docs/instructions.md](python-curriculum/exercises/practice/dot-dsl/.docs/instructions.md)
246. **Flatten Array** · practice · Intermediate — [python-curriculum/exercises/practice/flatten-array/.docs/instructions.md](python-curriculum/exercises/practice/flatten-array/.docs/instructions.md)
247. **Grade School** · practice · Intermediate — [python-curriculum/exercises/practice/grade-school/.docs/instructions.md](python-curriculum/exercises/practice/grade-school/.docs/instructions.md)
248. **Hangman** · practice · Intermediate — [python-curriculum/exercises/practice/hangman/.docs/instructions.md](python-curriculum/exercises/practice/hangman/.docs/instructions.md)
249. **Killer Sudoku Helper** · practice · Intermediate — [python-curriculum/exercises/practice/killer-sudoku-helper/.docs/instructions.md](python-curriculum/exercises/practice/killer-sudoku-helper/.docs/instructions.md)
250. **Largest Series Product** · practice · Intermediate — [python-curriculum/exercises/practice/largest-series-product/.docs/instructions.md](python-curriculum/exercises/practice/largest-series-product/.docs/instructions.md)
251. **Matching Brackets** · practice · Intermediate — [python-curriculum/exercises/practice/matching-brackets/.docs/instructions.md](python-curriculum/exercises/practice/matching-brackets/.docs/instructions.md)
252. **Nth Prime** · practice · Intermediate — [python-curriculum/exercises/practice/nth-prime/.docs/instructions.md](python-curriculum/exercises/practice/nth-prime/.docs/instructions.md)
253. **Pascal's Triangle** · practice · Intermediate — [python-curriculum/exercises/practice/pascals-triangle/.docs/instructions.md](python-curriculum/exercises/practice/pascals-triangle/.docs/instructions.md)
254. **Perfect Numbers** · practice · Intermediate — [python-curriculum/exercises/practice/perfect-numbers/.docs/instructions.md](python-curriculum/exercises/practice/perfect-numbers/.docs/instructions.md)
255. **Prime Factors** · practice · Intermediate — [python-curriculum/exercises/practice/prime-factors/.docs/instructions.md](python-curriculum/exercises/practice/prime-factors/.docs/instructions.md)
256. **Pythagorean Triplet** · practice · Intermediate — [python-curriculum/exercises/practice/pythagorean-triplet/.docs/instructions.md](python-curriculum/exercises/practice/pythagorean-triplet/.docs/instructions.md)
257. **Rail Fence Cipher** · practice · Intermediate — [python-curriculum/exercises/practice/rail-fence-cipher/.docs/instructions.md](python-curriculum/exercises/practice/rail-fence-cipher/.docs/instructions.md)
258. **Robot Name** · practice · Intermediate — [python-curriculum/exercises/practice/robot-name/.docs/instructions.md](python-curriculum/exercises/practice/robot-name/.docs/instructions.md)
259. **Robot Simulator** · practice · Intermediate — [python-curriculum/exercises/practice/robot-simulator/.docs/instructions.md](python-curriculum/exercises/practice/robot-simulator/.docs/instructions.md)
260. **Roman Numerals** · practice · Intermediate — [python-curriculum/exercises/practice/roman-numerals/.docs/instructions.md](python-curriculum/exercises/practice/roman-numerals/.docs/instructions.md)
261. **Say** · practice · Intermediate — [python-curriculum/exercises/practice/say/.docs/instructions.md](python-curriculum/exercises/practice/say/.docs/instructions.md)
262. **Scale Generator** · practice · Intermediate — [python-curriculum/exercises/practice/scale-generator/.docs/instructions.md](python-curriculum/exercises/practice/scale-generator/.docs/instructions.md)
263. **Sieve** · practice · Intermediate — [python-curriculum/exercises/practice/sieve/.docs/instructions.md](python-curriculum/exercises/practice/sieve/.docs/instructions.md)
264. **Simple Cipher** · practice · Intermediate — [python-curriculum/exercises/practice/simple-cipher/.docs/instructions.md](python-curriculum/exercises/practice/simple-cipher/.docs/instructions.md)
265. **Simple Linked List** · practice · Intermediate — [python-curriculum/exercises/practice/simple-linked-list/.docs/instructions.md](python-curriculum/exercises/practice/simple-linked-list/.docs/instructions.md)
266. **Square Root** · practice · Intermediate — [python-curriculum/exercises/practice/square-root/.docs/instructions.md](python-curriculum/exercises/practice/square-root/.docs/instructions.md)
267. **State of Tic-Tac-Toe** · practice · Intermediate — [python-curriculum/exercises/practice/state-of-tic-tac-toe/.docs/instructions.md](python-curriculum/exercises/practice/state-of-tic-tac-toe/.docs/instructions.md)
268. **Sublist** · practice · Intermediate — [python-curriculum/exercises/practice/sublist/.docs/instructions.md](python-curriculum/exercises/practice/sublist/.docs/instructions.md)
269. **Alphametics** · practice · Advanced — [python-curriculum/exercises/practice/alphametics/.docs/instructions.md](python-curriculum/exercises/practice/alphametics/.docs/instructions.md)
270. **Book Store** · practice · Advanced — [python-curriculum/exercises/practice/book-store/.docs/instructions.md](python-curriculum/exercises/practice/book-store/.docs/instructions.md)
271. **Camicia** · practice · Advanced — [python-curriculum/exercises/practice/camicia/.docs/instructions.md](python-curriculum/exercises/practice/camicia/.docs/instructions.md)
272. **Dominoes** · practice · Advanced — [python-curriculum/exercises/practice/dominoes/.docs/instructions.md](python-curriculum/exercises/practice/dominoes/.docs/instructions.md)
273. **Forth** · practice · Advanced — [python-curriculum/exercises/practice/forth/.docs/instructions.md](python-curriculum/exercises/practice/forth/.docs/instructions.md)
274. **POV** · practice · Advanced — [python-curriculum/exercises/practice/pov/.docs/instructions.md](python-curriculum/exercises/practice/pov/.docs/instructions.md)
275. **SGF Parsing** · practice · Advanced — [python-curriculum/exercises/practice/sgf-parsing/.docs/instructions.md](python-curriculum/exercises/practice/sgf-parsing/.docs/instructions.md)
276. **Two Bucket** · practice · Advanced — [python-curriculum/exercises/practice/two-bucket/.docs/instructions.md](python-curriculum/exercises/practice/two-bucket/.docs/instructions.md)
277. **Zebra Puzzle** · practice · Advanced — [python-curriculum/exercises/practice/zebra-puzzle/.docs/instructions.md](python-curriculum/exercises/practice/zebra-puzzle/.docs/instructions.md)
278. **Zipper** · practice · Advanced — [python-curriculum/exercises/practice/zipper/.docs/instructions.md](python-curriculum/exercises/practice/zipper/.docs/instructions.md)
279. **Affine Cipher** · practice · Intermediate plus — [python-curriculum/exercises/practice/affine-cipher/.docs/instructions.md](python-curriculum/exercises/practice/affine-cipher/.docs/instructions.md)
280. **Binary Search Tree** · practice · Intermediate plus — [python-curriculum/exercises/practice/binary-search-tree/.docs/instructions.md](python-curriculum/exercises/practice/binary-search-tree/.docs/instructions.md)
281. **Bowling** · practice · Intermediate plus — [python-curriculum/exercises/practice/bowling/.docs/instructions.md](python-curriculum/exercises/practice/bowling/.docs/instructions.md)
282. **Change** · practice · Intermediate plus — [python-curriculum/exercises/practice/change/.docs/instructions.md](python-curriculum/exercises/practice/change/.docs/instructions.md)
283. **Connect** · practice · Intermediate plus — [python-curriculum/exercises/practice/connect/.docs/instructions.md](python-curriculum/exercises/practice/connect/.docs/instructions.md)
284. **Go Counting** · practice · Intermediate plus — [python-curriculum/exercises/practice/go-counting/.docs/instructions.md](python-curriculum/exercises/practice/go-counting/.docs/instructions.md)
285. **Knapsack** · practice · Intermediate plus — [python-curriculum/exercises/practice/knapsack/.docs/instructions.md](python-curriculum/exercises/practice/knapsack/.docs/instructions.md)
286. **Linked List** · practice · Intermediate plus — [python-curriculum/exercises/practice/linked-list/.docs/instructions.md](python-curriculum/exercises/practice/linked-list/.docs/instructions.md)
287. **Palindrome Products** · practice · Intermediate plus — [python-curriculum/exercises/practice/palindrome-products/.docs/instructions.md](python-curriculum/exercises/practice/palindrome-products/.docs/instructions.md)
288. **Poker** · practice · Intermediate plus — [python-curriculum/exercises/practice/poker/.docs/instructions.md](python-curriculum/exercises/practice/poker/.docs/instructions.md)
289. **Rectangles** · practice · Intermediate plus — [python-curriculum/exercises/practice/rectangles/.docs/instructions.md](python-curriculum/exercises/practice/rectangles/.docs/instructions.md)
290. **Relative Distance** · practice · Intermediate plus — [python-curriculum/exercises/practice/relative-distance/.docs/instructions.md](python-curriculum/exercises/practice/relative-distance/.docs/instructions.md)
291. **Satellite** · practice · Intermediate plus — [python-curriculum/exercises/practice/satellite/.docs/instructions.md](python-curriculum/exercises/practice/satellite/.docs/instructions.md)
292. **Tree Building** · practice · Intermediate plus — [python-curriculum/exercises/practice/tree-building/.docs/instructions.md](python-curriculum/exercises/practice/tree-building/.docs/instructions.md)
293. **Variable Length Quantity** · practice · Intermediate plus — [python-curriculum/exercises/practice/variable-length-quantity/.docs/instructions.md](python-curriculum/exercises/practice/variable-length-quantity/.docs/instructions.md)
294. **Word Search** · practice · Intermediate plus — [python-curriculum/exercises/practice/word-search/.docs/instructions.md](python-curriculum/exercises/practice/word-search/.docs/instructions.md)

### learn.python

295. **Challenge: Binary Search** · challenge · practice — [learn.python/practice/challenges/beginner/13-binary-search.py](learn.python/practice/challenges/beginner/13-binary-search.py)
296. **Challenge: Merge Sorted Lists** · challenge · practice — [learn.python/practice/challenges/beginner/14-merge-sorted.py](learn.python/practice/challenges/beginner/14-merge-sorted.py)
297. **Challenge: Decorator Timer** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/01-decorator-timer.py](learn.python/practice/challenges/intermediate/01-decorator-timer.py)
298. **Challenge: Context Manager for File Backup** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/02-context-manager.py](learn.python/practice/challenges/intermediate/02-context-manager.py)
299. **Challenge: Generator Pipeline** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/03-generator-pipeline.py](learn.python/practice/challenges/intermediate/03-generator-pipeline.py)
300. **Challenge: Class Registry** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/04-class-registry.py](learn.python/practice/challenges/intermediate/04-class-registry.py)
301. **Challenge: Retry Decorator with Exponential Backoff** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/05-retry-decorator.py](learn.python/practice/challenges/intermediate/05-retry-decorator.py)
302. **Challenge: LRU Cache** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/06-lru-cache.py](learn.python/practice/challenges/intermediate/06-lru-cache.py)
303. **Challenge: Event Emitter** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/07-event-emitter.py](learn.python/practice/challenges/intermediate/07-event-emitter.py)
304. **Challenge: Validate Schema** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/08-validate-schema.py](learn.python/practice/challenges/intermediate/08-validate-schema.py)
305. **Challenge: Parse Log File** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/09-parse-log-file.py](learn.python/practice/challenges/intermediate/09-parse-log-file.py)
306. **Challenge: Batch Processor** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/10-batch-processor.py](learn.python/practice/challenges/intermediate/10-batch-processor.py)
307. **Challenge: Rate Limiter (Token Bucket)** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/11-rate-limiter.py](learn.python/practice/challenges/intermediate/11-rate-limiter.py)
308. **Challenge: Tree Traversal** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/12-tree-traversal.py](learn.python/practice/challenges/intermediate/12-tree-traversal.py)
309. **Challenge: CLI Argument Parser** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/14-cli-parser.py](learn.python/practice/challenges/intermediate/14-cli-parser.py)
310. **Challenge: Plugin Loader** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/15-plugin-loader.py](learn.python/practice/challenges/intermediate/15-plugin-loader.py)

## 09 · Testing, debugging and code quality

pytest, fixtures, parametrization, mocking, refactoring and quality gates.

### C1

311. **Exercise 1 — Your First Pytest Tests** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/exercises/exercise-01-first-test.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/exercises/exercise-01-first-test.md)
312. **Exercise 2 — Sharing Setup With Fixtures** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/exercises/exercise-02-fixtures.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/exercises/exercise-02-fixtures.md)
313. **Exercise 3 — Table-Driven Tests With Parametrize** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/exercises/exercise-03-parametrize.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/exercises/exercise-03-parametrize.md)
314. **Exercise 4 — Mocking a Network Call** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/exercises/exercise-04-mocking.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/exercises/exercise-04-mocking.md)
315. **Exercise 5 — Finding the Missing Branch** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/exercises/exercise-05-coverage-gap.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/exercises/exercise-05-coverage-gap.md)
316. **Homework Problem 3 — Leap Year Function With Tests** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/homework/problem-03-leap-year-function-with-tests.md](C1-Code-Crunch-Convos/curriculum/week-04-functions-modules/homework/problem-03-leap-year-function-with-tests.md)
317. **Homework Problem 1 — Renewal rules** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/homework/problem-01-renewal-rules.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/homework/problem-01-renewal-rules.md)
318. **Homework Problem 2 — Dues ledger** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/homework/problem-02-dues-ledger.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/homework/problem-02-dues-ledger.md)
319. **Homework Problem 3 — Hours and minutes** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/homework/problem-03-hours-minutes.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/homework/problem-03-hours-minutes.md)
320. **Homework Problem 4 — Overdue notice** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/homework/problem-04-overdue-notice.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/homework/problem-04-overdue-notice.md)
321. **Homework Problem 5 — Fine schedule** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/homework/problem-05-fine-schedule.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/homework/problem-05-fine-schedule.md)
322. **Homework Problem 6 — Shelf order regression** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/homework/problem-06-shelf-order-regression.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/homework/problem-06-shelf-order-regression.md)
323. **Challenge 1 — TDD FizzBuzz** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/challenges/challenge-01-tdd-fizzbuzz.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/challenges/challenge-01-tdd-fizzbuzz.md)
324. **Challenge 2 — Integration tests for the Week 9 Flask blog** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/challenges/challenge-02-flask-api-tests.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/challenges/challenge-02-flask-api-tests.md)
325. **Challenge 3 — Review the parser** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/challenges/challenge-03-review-the-parser.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/challenges/challenge-03-review-the-parser.md)

### Exercism

326. **Ledger** · practice · Intermediate plus — [python-curriculum/exercises/practice/ledger/.docs/instructions.md](python-curriculum/exercises/practice/ledger/.docs/instructions.md)
327. **Markdown** · practice · Intermediate plus — [python-curriculum/exercises/practice/markdown/.docs/instructions.md](python-curriculum/exercises/practice/markdown/.docs/instructions.md)

### learn.python

328. **BUG HUNT 1 — Off By One** · challenge · debugging practice — [learn.python/practice/challenges/bug-hunt/01_off_by_one.py](learn.python/practice/challenges/bug-hunt/01_off_by_one.py)
329. **BUG HUNT 2 — Scope Confusion** · challenge · debugging practice — [learn.python/practice/challenges/bug-hunt/02_scope_confusion.py](learn.python/practice/challenges/bug-hunt/02_scope_confusion.py)
330. **BUG HUNT 3 — Mutable Defaults** · challenge · debugging practice — [learn.python/practice/challenges/bug-hunt/03_mutable_defaults.py](learn.python/practice/challenges/bug-hunt/03_mutable_defaults.py)
331. **BUG HUNT 4 — Key and Attribute Errors** · challenge · debugging practice — [learn.python/practice/challenges/bug-hunt/04_key_and_attribute_errors.py](learn.python/practice/challenges/bug-hunt/04_key_and_attribute_errors.py)
332. **BUG HUNT 5 — File Handling Bugs** · challenge · debugging practice — [learn.python/practice/challenges/bug-hunt/05_file_handling_bugs.py](learn.python/practice/challenges/bug-hunt/05_file_handling_bugs.py)
333. **BUG HUNT 6 — Comparison Traps** · challenge · debugging practice — [learn.python/practice/challenges/bug-hunt/06_comparison_traps.py](learn.python/practice/challenges/bug-hunt/06_comparison_traps.py)

### C1

334. **Mini-Project — stringutils** · project · project — [C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-11-testing-debugging/mini-project/README.md)

### learn.python

335. **Level 0 / Project 01 - Terminal Hello Lab** · project · project — [learn.python/projects/level-0/01-terminal-hello-lab/README.md](learn.python/projects/level-0/01-terminal-hello-lab/README.md)
336. **Level 0 / Project 02 - Calculator Basics** · project · project — [learn.python/projects/level-0/02-calculator-basics/README.md](learn.python/projects/level-0/02-calculator-basics/README.md)
337. **Level 0 / Project 03 - Temperature Converter** · project · project — [learn.python/projects/level-0/03-temperature-converter/README.md](learn.python/projects/level-0/03-temperature-converter/README.md)
338. **Level 0 / Project 04 - Yes No Questionnaire** · project · project — [learn.python/projects/level-0/04-yes-no-questionnaire/README.md](learn.python/projects/level-0/04-yes-no-questionnaire/README.md)
339. **Level 0 / Project 05 - Number Classifier** · project · project — [learn.python/projects/level-0/05-number-classifier/README.md](learn.python/projects/level-0/05-number-classifier/README.md)
340. **Level 0 / Project 06 - Word Counter Basic** · project · project — [learn.python/projects/level-0/06-word-counter-basic/README.md](learn.python/projects/level-0/06-word-counter-basic/README.md)
341. **Level 0 / Project 07 - First File Reader** · project · project — [learn.python/projects/level-0/07-first-file-reader/README.md](learn.python/projects/level-0/07-first-file-reader/README.md)
342. **Level 0 / Project 08 - string Cleaner Starter** · project · project — [learn.python/projects/level-0/08-string-cleaner-starter/README.md](learn.python/projects/level-0/08-string-cleaner-starter/README.md)
343. **Level 0 / Project 09 - Daily Checklist Writer** · project · project — [learn.python/projects/level-0/09-daily-checklist-writer/README.md](learn.python/projects/level-0/09-daily-checklist-writer/README.md)
344. **Level 0 / Project 10 - Duplicate Line Finder** · project · project — [learn.python/projects/level-0/10-duplicate-line-finder/README.md](learn.python/projects/level-0/10-duplicate-line-finder/README.md)
345. **Level 0 / Project 11 - Simple Menu Loop** · project · project — [learn.python/projects/level-0/11-simple-menu-loop/README.md](learn.python/projects/level-0/11-simple-menu-loop/README.md)
346. **Level 0 / Project 12 - Contact Card Builder** · project · project — [learn.python/projects/level-0/12-contact-card-builder/README.md](learn.python/projects/level-0/12-contact-card-builder/README.md)
347. **Level 0 / Project 13 - Alarm Message Generator** · project · project — [learn.python/projects/level-0/13-alarm-message-generator/README.md](learn.python/projects/level-0/13-alarm-message-generator/README.md)
348. **Level 0 / Project 14 - Line Length Summarizer** · project · project — [learn.python/projects/level-0/14-line-length-summarizer/README.md](learn.python/projects/level-0/14-line-length-summarizer/README.md)
349. **Level 0 / Project 15 - Level 0 Mini Toolkit** · project · project — [learn.python/projects/level-0/15-level0-mini-toolkit/README.md](learn.python/projects/level-0/15-level0-mini-toolkit/README.md)
350. **Level 3 / Project 01 - Package Layout Starter** · project · project — [learn.python/projects/level-3/01-package-layout-starter/README.md](learn.python/projects/level-3/01-package-layout-starter/README.md)
351. **Level 3 / Project 02 - CLI Arguments Workbench** · project · project — [learn.python/projects/level-3/02-cli-arguments-workbench/README.md](learn.python/projects/level-3/02-cli-arguments-workbench/README.md)
352. **Level 3 / Project 03 - Logging Baseline Tool** · project · project — [learn.python/projects/level-3/03-logging-baseline-tool/README.md](learn.python/projects/level-3/03-logging-baseline-tool/README.md)
353. **Level 3 / Project 04 - Test Driven Normalizer** · project · project — [learn.python/projects/level-3/04-test-driven-normalizer/README.md](learn.python/projects/level-3/04-test-driven-normalizer/README.md)
354. **Level 3 / Project 05 - Refactor Monolith Drill** · project · project — [learn.python/projects/level-3/05-refactor-monolith-drill/README.md](learn.python/projects/level-3/05-refactor-monolith-drill/README.md)
355. **Level 3 / Project 06 - Structured Error Handler** · project · project — [learn.python/projects/level-3/06-structured-error-handler/README.md](learn.python/projects/level-3/06-structured-error-handler/README.md)
356. **Level 3 / Project 07 - Batch File Auditor** · project · project — [learn.python/projects/level-3/07-batch-file-auditor/README.md](learn.python/projects/level-3/07-batch-file-auditor/README.md)
357. **Level 3 / Project 08 - Template Driven Reporter** · project · project — [learn.python/projects/level-3/08-template-driven-reporter/README.md](learn.python/projects/level-3/08-template-driven-reporter/README.md)
358. **Level 3 / Project 09 - Reusable Utils Library** · project · project — [learn.python/projects/level-3/09-reusable-utils-library/README.md](learn.python/projects/level-3/09-reusable-utils-library/README.md)
359. **Level 3 / Project 10 - Dependency Boundary Lab** · project · project — [learn.python/projects/level-3/10-dependency-boundary-lab/README.md](learn.python/projects/level-3/10-dependency-boundary-lab/README.md)
360. **Level 3 / Project 11 - Project Config Bootstrap** · project · project — [learn.python/projects/level-3/11-project-config-bootstrap/README.md](learn.python/projects/level-3/11-project-config-bootstrap/README.md)
361. **Level 3 / Project 12 - Parser With Fixtures** · project · project — [learn.python/projects/level-3/12-parser-with-fixtures/README.md](learn.python/projects/level-3/12-parser-with-fixtures/README.md)
362. **Level 3 / Project 13 - Quality Gate Runner** · project · project — [learn.python/projects/level-3/13-quality-gate-runner/README.md](learn.python/projects/level-3/13-quality-gate-runner/README.md)
363. **Level 3 / Project 14 - Service Simulator** · project · project — [learn.python/projects/level-3/14-service-simulator/README.md](learn.python/projects/level-3/14-service-simulator/README.md)
364. **Level 3 / Project 15 - Level 3 Mini Capstone** · project · project — [learn.python/projects/level-3/15-level3-mini-capstone/README.md](learn.python/projects/level-3/15-level3-mini-capstone/README.md)
365. **Module 08 / Project 01: Parametrize** · project · project — [learn.python/projects/modules/08-testing-advanced/01-parametrize/README.md](learn.python/projects/modules/08-testing-advanced/01-parametrize/README.md)
366. **Module 08 / Project 02: Mocking** · project · project — [learn.python/projects/modules/08-testing-advanced/02-mocking/README.md](learn.python/projects/modules/08-testing-advanced/02-mocking/README.md)
367. **Module 08 / Project 03: Fixtures Advanced** · project · project — [learn.python/projects/modules/08-testing-advanced/03-fixtures-advanced/README.md](learn.python/projects/modules/08-testing-advanced/03-fixtures-advanced/README.md)
368. **Module 08 / Project 04: Property-Based Testing** · project · project — [learn.python/projects/modules/08-testing-advanced/04-property-based/README.md](learn.python/projects/modules/08-testing-advanced/04-property-based/README.md)
369. **Module 08 / Project 05: Integration Testing** · project · project — [learn.python/projects/modules/08-testing-advanced/05-integration-testing/README.md](learn.python/projects/modules/08-testing-advanced/05-integration-testing/README.md)

## 10 · Command-line tools and automation

CLI design, filesystem automation, scheduling, subprocesses and resilient batch work.

### C1

370. **Exercise 4 — Input Parsing** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/exercises/exercise-04-input-parsing.md](C1-Code-Crunch-Convos/curriculum/week-02-data-types-operators/exercises/exercise-04-input-parsing.md)
371. **Exercise 1 — Greet CLI** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/exercises/exercise-01-greet-cli.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/exercises/exercise-01-greet-cli.md)
372. **Exercise 2 — Bulk Rename** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/exercises/exercise-02-bulk-rename.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/exercises/exercise-02-bulk-rename.md)
373. **Exercise 3 — Run Shell** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/exercises/exercise-03-run-shell.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/exercises/exercise-03-run-shell.md)
374. **Exercise 4 — Scrape Quotes** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/exercises/exercise-04-scrape-quotes.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/exercises/exercise-04-scrape-quotes.md)
375. **Exercise 5 — Schedule** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/exercises/exercise-05-schedule.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/exercises/exercise-05-schedule.md)
376. **Homework Problem 6 — Combine Everything with a Small CLI** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/homework/problem-06-combine-everything-with-a-small-cli.md](C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/homework/problem-06-combine-everything-with-a-small-cli.md)
377. **Homework Problem 6 — Simple ATM Menu** · assignment · Intermediate — [C1-Code-Crunch-Convos/curriculum/week-03-control-flow/homework/problem-06-simple-atm-menu.md](C1-Code-Crunch-Convos/curriculum/week-03-control-flow/homework/problem-06-simple-atm-menu.md)
378. **Homework 1 — Dotfile backup script** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/homework/problem-01-dotfile-backup.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/homework/problem-01-dotfile-backup.md)
379. **Homework 2 — Photo-by-EXIF-date organizer** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/homework/problem-02-photo-exif-organizer.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/homework/problem-02-photo-exif-organizer.md)
380. **Homework 3 — CSV to Markdown converter** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/homework/problem-03-csv-to-markdown.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/homework/problem-03-csv-to-markdown.md)
381. **Homework 4 — Batch image resizer** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/homework/problem-04-image-resizer.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/homework/problem-04-image-resizer.md)
382. **Homework 5 — GitHub releases fetcher** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/homework/problem-05-github-releases.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/homework/problem-05-github-releases.md)
383. **Homework 6 — Educational port scanner (localhost only)** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/homework/problem-06-port-scanner.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/homework/problem-06-port-scanner.md)
384. **Challenge 1 — Personalized ASCII Banner** · assignment · Beginner plus — [C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/challenges/challenge-01-personalized-banner.md](C1-Code-Crunch-Convos/curriculum/week-01-python-foundations/challenges/challenge-01-personalized-banner.md)
385. **Challenge 01 — Website watcher** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/challenges/challenge-01-website-watcher.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/challenges/challenge-01-website-watcher.md)
386. **Challenge 02 — PDF renamer** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/challenges/challenge-02-pdf-renamer.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/challenges/challenge-02-pdf-renamer.md)

### Exercism

387. **Grep** · practice · Intermediate — [python-curriculum/exercises/practice/grep/.docs/instructions.md](python-curriculum/exercises/practice/grep/.docs/instructions.md)

### C1

388. **Mini-Project — File Organizer Bot** · project · project — [C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-12-automation-scripting/mini-project/README.md)

### learn.python

389. **Level 1 / Project 01 - Input Validator Lab** · project · project — [learn.python/projects/level-1/01-input-validator-lab/README.md](learn.python/projects/level-1/01-input-validator-lab/README.md)
390. **Level 1 / Project 02 - Password Strength Checker** · project · project — [learn.python/projects/level-1/02-password-strength-checker/README.md](learn.python/projects/level-1/02-password-strength-checker/README.md)
391. **Level 1 / Project 03 - Unit Price Calculator** · project · project — [learn.python/projects/level-1/03-unit-price-calculator/README.md](learn.python/projects/level-1/03-unit-price-calculator/README.md)
392. **Level 1 / Project 04 - Log Line Parser** · project · project — [learn.python/projects/level-1/04-log-line-parser/README.md](learn.python/projects/level-1/04-log-line-parser/README.md)
393. **Level 1 / Project 05 - CSV First Reader** · project · project — [learn.python/projects/level-1/05-csv-first-reader/README.md](learn.python/projects/level-1/05-csv-first-reader/README.md)
394. **Level 1 / Project 06 - Simple Gradebook Engine** · project · project — [learn.python/projects/level-1/06-simple-gradebook-engine/README.md](learn.python/projects/level-1/06-simple-gradebook-engine/README.md)
395. **Level 1 / Project 07 - Date Difference Helper** · project · project — [learn.python/projects/level-1/07-date-difference-helper/README.md](learn.python/projects/level-1/07-date-difference-helper/README.md)
396. **Level 1 / Project 08 - Path Exists Checker** · project · project — [learn.python/projects/level-1/08-path-exists-checker/README.md](learn.python/projects/level-1/08-path-exists-checker/README.md)
397. **Level 1 / Project 09 - JSON Settings Loader** · project · project — [learn.python/projects/level-1/09-json-settings-loader/README.md](learn.python/projects/level-1/09-json-settings-loader/README.md)
398. **Level 1 / Project 10 - Ticket Priority Router** · project · project — [learn.python/projects/level-1/10-ticket-priority-router/README.md](learn.python/projects/level-1/10-ticket-priority-router/README.md)
399. **Level 1 / Project 11 - Command Dispatcher** · project · project — [learn.python/projects/level-1/11-command-dispatcher/README.md](learn.python/projects/level-1/11-command-dispatcher/README.md)
400. **Level 1 / Project 12 - File Extension Counter** · project · project — [learn.python/projects/level-1/12-file-extension-counter/README.md](learn.python/projects/level-1/12-file-extension-counter/README.md)
401. **Level 1 / Project 13 - Batch Rename Simulator** · project · project — [learn.python/projects/level-1/13-batch-rename-simulator/README.md](learn.python/projects/level-1/13-batch-rename-simulator/README.md)
402. **Level 1 / Project 14 - Basic Expense Tracker** · project · project — [learn.python/projects/level-1/14-basic-expense-tracker/README.md](learn.python/projects/level-1/14-basic-expense-tracker/README.md)
403. **Level 1 / Project 15 - Level 1 Mini Automation** · project · project — [learn.python/projects/level-1/15-level1-mini-automation/README.md](learn.python/projects/level-1/15-level1-mini-automation/README.md)
404. **Level 2 / Project 01 - Dictionary Lookup Service** · project · project — [learn.python/projects/level-2/01-dictionary-lookup-service/README.md](learn.python/projects/level-2/01-dictionary-lookup-service/README.md)
405. **Level 2 / Project 02 - Nested Data Flattener** · project · project — [learn.python/projects/level-2/02-nested-data-flattener/README.md](learn.python/projects/level-2/02-nested-data-flattener/README.md)
406. **Level 2 / Project 03 - Data Cleaning Pipeline** · project · project — [learn.python/projects/level-2/03-data-cleaning-pipeline/README.md](learn.python/projects/level-2/03-data-cleaning-pipeline/README.md)
407. **Level 2 / Project 04 - Error Safe Divider** · project · project — [learn.python/projects/level-2/04-error-safe-divider/README.md](learn.python/projects/level-2/04-error-safe-divider/README.md)
408. **Level 2 / Project 05 - Text Report Generator** · project · project — [learn.python/projects/level-2/05-text-report-generator/README.md](learn.python/projects/level-2/05-text-report-generator/README.md)
409. **Level 2 / Project 06 - Records Deduplicator** · project · project — [learn.python/projects/level-2/06-records-deduplicator/README.md](learn.python/projects/level-2/06-records-deduplicator/README.md)
410. **Level 2 / Project 07 - List Search Benchmark** · project · project — [learn.python/projects/level-2/07-list-search-benchmark/README.md](learn.python/projects/level-2/07-list-search-benchmark/README.md)
411. **Level 2 / Project 08 - Mini Inventory Engine** · project · project — [learn.python/projects/level-2/08-mini-inventory-engine/README.md](learn.python/projects/level-2/08-mini-inventory-engine/README.md)
412. **Level 2 / Project 09 - Config Driven Calculator** · project · project — [learn.python/projects/level-2/09-config-driven-calculator/README.md](learn.python/projects/level-2/09-config-driven-calculator/README.md)
413. **Level 2 / Project 10 - Mock API Response Parser** · project · project — [learn.python/projects/level-2/10-mock-api-response-parser/README.md](learn.python/projects/level-2/10-mock-api-response-parser/README.md)
414. **Level 2 / Project 11 - Retry Loop Practice** · project · project — [learn.python/projects/level-2/11-retry-loop-practice/README.md](learn.python/projects/level-2/11-retry-loop-practice/README.md)
415. **Level 2 / Project 12 - CSV to JSON Converter** · project · project — [learn.python/projects/level-2/12-csv-to-json-converter/README.md](learn.python/projects/level-2/12-csv-to-json-converter/README.md)
416. **Level 2 / Project 13 - Validation Rule Engine** · project · project — [learn.python/projects/level-2/13-validation-rule-engine/README.md](learn.python/projects/level-2/13-validation-rule-engine/README.md)
417. **Level 2 / Project 14 - Anomaly Flagger** · project · project — [learn.python/projects/level-2/14-anomaly-flagger/README.md](learn.python/projects/level-2/14-anomaly-flagger/README.md)
418. **Level 2 / Project 15 - Level 2 Mini Capstone** · project · project — [learn.python/projects/level-2/15-level2-mini-capstone/README.md](learn.python/projects/level-2/15-level2-mini-capstone/README.md)
419. **Level 2 / Project 16 - Markdown to HTML Converter** · project · project — [learn.python/projects/level-2/16-markdown-to-html-converter/README.md](learn.python/projects/level-2/16-markdown-to-html-converter/README.md)
420. **Level 4 / Project 01 - Schema Validator Engine** · project · project — [learn.python/projects/level-4/01-schema-validator-engine/README.md](learn.python/projects/level-4/01-schema-validator-engine/README.md)
421. **Level 4 / Project 02 - Excel Input Health Check** · project · project — [learn.python/projects/level-4/02-excel-input-health-check/README.md](learn.python/projects/level-4/02-excel-input-health-check/README.md)
422. **Level 4 / Project 03 - Robust CSV Ingestor** · project · project — [learn.python/projects/level-4/03-robust-csv-ingestor/README.md](learn.python/projects/level-4/03-robust-csv-ingestor/README.md)
423. **Level 4 / Project 04 - Data Contract Enforcer** · project · project — [learn.python/projects/level-4/04-data-contract-enforcer/README.md](learn.python/projects/level-4/04-data-contract-enforcer/README.md)
424. **Level 4 / Project 05 - Path Safe File Mover** · project · project — [learn.python/projects/level-4/05-path-safe-file-mover/README.md](learn.python/projects/level-4/05-path-safe-file-mover/README.md)
425. **Level 4 / Project 06 - Backup Rotation Tool** · project · project — [learn.python/projects/level-4/06-backup-rotation-tool/README.md](learn.python/projects/level-4/06-backup-rotation-tool/README.md)
426. **Level 4 / Project 07 - Duplicate Record Investigator** · project · project — [learn.python/projects/level-4/07-duplicate-record-investigator/README.md](learn.python/projects/level-4/07-duplicate-record-investigator/README.md)
427. **Level 4 / Project 08 - Malformed Row Quarantine** · project · project — [learn.python/projects/level-4/08-malformed-row-quarantine/README.md](learn.python/projects/level-4/08-malformed-row-quarantine/README.md)
428. **Level 4 / Project 09 - Transformation Pipeline V1** · project · project — [learn.python/projects/level-4/09-transformation-pipeline-v1/README.md](learn.python/projects/level-4/09-transformation-pipeline-v1/README.md)
429. **Level 4 / Project 10 - Run Manifest Generator** · project · project — [learn.python/projects/level-4/10-run-manifest-generator/README.md](learn.python/projects/level-4/10-run-manifest-generator/README.md)
430. **Level 4 / Project 11 - Audit Log Enhancer** · project · project — [learn.python/projects/level-4/11-audit-log-enhancer/README.md](learn.python/projects/level-4/11-audit-log-enhancer/README.md)
431. **Level 4 / Project 12 - Checkpoint Recovery Tool** · project · project — [learn.python/projects/level-4/12-checkpoint-recovery-tool/README.md](learn.python/projects/level-4/12-checkpoint-recovery-tool/README.md)
432. **Level 4 / Project 13 - Reconciliation Reporter** · project · project — [learn.python/projects/level-4/13-reconciliation-reporter/README.md](learn.python/projects/level-4/13-reconciliation-reporter/README.md)
433. **Level 4 / Project 14 - Configurable Batch Runner** · project · project — [learn.python/projects/level-4/14-configurable-batch-runner/README.md](learn.python/projects/level-4/14-configurable-batch-runner/README.md)
434. **Level 4 / Project 15 - Level 4 Mini Capstone** · project · project — [learn.python/projects/level-4/15-level4-mini-capstone/README.md](learn.python/projects/level-4/15-level4-mini-capstone/README.md)
435. **Level 5 / Project 01 - Schedule Ready Script** · project · intermediate/advanced — [learn.python/projects/level-5/01-schedule-ready-script/README.md](learn.python/projects/level-5/01-schedule-ready-script/README.md)
436. **Level 5 / Project 02 - Alert Threshold Monitor** · project · intermediate/advanced — [learn.python/projects/level-5/02-alert-threshold-monitor/README.md](learn.python/projects/level-5/02-alert-threshold-monitor/README.md)
437. **Level 5 / Project 03 - Multi File ETL Runner** · project · intermediate/advanced — [learn.python/projects/level-5/03-multi-file-etl-runner/README.md](learn.python/projects/level-5/03-multi-file-etl-runner/README.md)
438. **Level 5 / Project 04 - Config Layer Priority** · project · intermediate/advanced — [learn.python/projects/level-5/04-config-layer-priority/README.md](learn.python/projects/level-5/04-config-layer-priority/README.md)
439. **Level 5 / Project 05 - Plugin Style Transformer** · project · intermediate/advanced — [learn.python/projects/level-5/05-plugin-style-transformer/README.md](learn.python/projects/level-5/05-plugin-style-transformer/README.md)
440. **Level 5 / Project 06 - Metrics Summary Engine** · project · intermediate/advanced — [learn.python/projects/level-5/06-metrics-summary-engine/README.md](learn.python/projects/level-5/06-metrics-summary-engine/README.md)
441. **Level 5 / Project 07 - Resilient JSON Loader** · project · intermediate/advanced — [learn.python/projects/level-5/07-resilient-json-loader/README.md](learn.python/projects/level-5/07-resilient-json-loader/README.md)
442. **Level 5 / Project 08 - Cross File Joiner** · project · intermediate/advanced — [learn.python/projects/level-5/08-cross-file-joiner/README.md](learn.python/projects/level-5/08-cross-file-joiner/README.md)
443. **Level 5 / Project 09 - Template Report Renderer** · project · intermediate/advanced — [learn.python/projects/level-5/09-template-report-renderer/README.md](learn.python/projects/level-5/09-template-report-renderer/README.md)
444. **Level 5 / Project 10 - API Polling Simulator** · project · intermediate/advanced — [learn.python/projects/level-5/10-api-polling-simulator/README.md](learn.python/projects/level-5/10-api-polling-simulator/README.md)
445. **Level 5 / Project 11 - Retry Backoff Runner** · project · intermediate/advanced — [learn.python/projects/level-5/11-retry-backoff-runner/README.md](learn.python/projects/level-5/11-retry-backoff-runner/README.md)
446. **Level 5 / Project 12 - Fail Safe Exporter** · project · intermediate/advanced — [learn.python/projects/level-5/12-fail-safe-exporter/README.md](learn.python/projects/level-5/12-fail-safe-exporter/README.md)
447. **Level 5 / Project 13 - Operational Run Logger** · project · intermediate/advanced — [learn.python/projects/level-5/13-operational-run-logger/README.md](learn.python/projects/level-5/13-operational-run-logger/README.md)
448. **Level 5 / Project 14 - Change Detection Tool** · project · intermediate/advanced — [learn.python/projects/level-5/14-change-detection-tool/README.md](learn.python/projects/level-5/14-change-detection-tool/README.md)
449. **Level 5 / Project 15 - Level 5 Mini Capstone** · project · intermediate/advanced — [learn.python/projects/level-5/15-level5-mini-capstone/README.md](learn.python/projects/level-5/15-level5-mini-capstone/README.md)
450. **Module 02 / Project 01 -- Click Basics** · project · project — [learn.python/projects/modules/02-cli-tools/01-click-basics/README.md](learn.python/projects/modules/02-cli-tools/01-click-basics/README.md)
451. **Module 02 / Project 02 -- Multi-Command CLI** · project · project — [learn.python/projects/modules/02-cli-tools/02-multi-command-cli/README.md](learn.python/projects/modules/02-cli-tools/02-multi-command-cli/README.md)
452. **Module 02 / Project 03 -- Interactive Prompts** · project · project — [learn.python/projects/modules/02-cli-tools/03-interactive-prompts/README.md](learn.python/projects/modules/02-cli-tools/03-interactive-prompts/README.md)
453. **Module 02 / Project 04 -- File Processor CLI** · project · project — [learn.python/projects/modules/02-cli-tools/04-file-processor-cli/README.md](learn.python/projects/modules/02-cli-tools/04-file-processor-cli/README.md)
454. **Module 02 / Project 05 -- Typer Migration** · project · project — [learn.python/projects/modules/02-cli-tools/05-typer-migration/README.md](learn.python/projects/modules/02-cli-tools/05-typer-migration/README.md)

## 11 · HTTP, scraping and API clients

HTTP fundamentals, requests, authentication, pagination, scraping and client design.

### 30 Days

455. **📘 Day 22** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/22_Day_Web_scraping/22_web_scraping.md](30-Days-Of-Python/22_Day_Web_scraping/22_web_scraping.md)
456. **📘 Day 28** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/28_Day_API/28_API.md](30-Days-Of-Python/28_Day_API/28_API.md)

### C1

457. **Exercise 1 — Your First GET Request** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/exercises/exercise-01-first-get-request.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/exercises/exercise-01-first-get-request.md)
458. **Exercise 2 — PokeAPI and Nested JSON** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/exercises/exercise-02-pokemon-api.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/exercises/exercise-02-pokemon-api.md)
459. **Exercise 3 — Sending Data with POST** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/exercises/exercise-03-post-data.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/exercises/exercise-03-post-data.md)
460. **Exercise 4 — Walking Every Page** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/exercises/exercise-04-pagination.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/exercises/exercise-04-pagination.md)
461. **Exercise 5 — When the Network Misbehaves** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/exercises/exercise-05-handle-errors.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/exercises/exercise-05-handle-errors.md)
462. **Homework Problem 1 — HTTP Method Matcher** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/homework/problem-01-http-method-matcher.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/homework/problem-01-http-method-matcher.md)
463. **Homework Problem 2 — JSON Path Walker** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/homework/problem-02-json-path-walker.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/homework/problem-02-json-path-walker.md)
464. **Homework Problem 3 — Rate-Limit Decorator** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/homework/problem-03-rate-limit-decorator.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/homework/problem-03-rate-limit-decorator.md)
465. **Homework Problem 4 — Mock API Client** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/homework/problem-04-mock-api-client.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/homework/problem-04-mock-api-client.md)
466. **Homework Problem 5 — Link Header Parser** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/homework/problem-05-link-header-parser.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/homework/problem-05-link-header-parser.md)
467. **Homework Problem 6 — Tiny URL-Shortener Client** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/homework/problem-06-tiny-url-shortener-client.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/homework/problem-06-tiny-url-shortener-client.md)
468. **Challenge 01 — Currency Converter CLI** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/challenges/challenge-01-currency-converter.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/challenges/challenge-01-currency-converter.md)
469. **Challenge 02 — GitHub User Stats** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/challenges/challenge-02-github-user-stats.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/challenges/challenge-02-github-user-stats.md)

### Exercism

470. **PaaS I/O** · practice · Advanced — [python-curriculum/exercises/practice/paasio/.docs/instructions.md](python-curriculum/exercises/practice/paasio/.docs/instructions.md)
471. **REST API** · practice · Intermediate plus — [python-curriculum/exercises/practice/rest-api/.docs/instructions.md](python-curriculum/exercises/practice/rest-api/.docs/instructions.md)

### C1

472. **Mini-Project — Weather Dashboard CLI** · project · project — [C1-Code-Crunch-Convos/curriculum/week-08-apis-json/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-08-apis-json/mini-project/README.md)

### learn.python

473. **Level 7 / Project 01 - API Query Adapter** · project · intermediate/advanced — [learn.python/projects/level-7/01-api-query-adapter/README.md](learn.python/projects/level-7/01-api-query-adapter/README.md)
474. **Level 7 / Project 02 - Monitoring API Adapter** · project · intermediate/advanced — [learn.python/projects/level-7/02-monitoring-api-adapter/README.md](learn.python/projects/level-7/02-monitoring-api-adapter/README.md)
475. **Level 7 / Project 03 - Unified Cache Writer** · project · intermediate/advanced — [learn.python/projects/level-7/03-unified-cache-writer/README.md](learn.python/projects/level-7/03-unified-cache-writer/README.md)
476. **Level 7 / Project 04 - Source Field Mapper** · project · intermediate/advanced — [learn.python/projects/level-7/04-source-field-mapper/README.md](learn.python/projects/level-7/04-source-field-mapper/README.md)
477. **Level 7 / Project 05 - Polling Cadence Manager** · project · intermediate/advanced — [learn.python/projects/level-7/05-polling-cadence-manager/README.md](learn.python/projects/level-7/05-polling-cadence-manager/README.md)
478. **Level 7 / Project 06 - Token Rotation Simulator** · project · intermediate/advanced — [learn.python/projects/level-7/06-token-rotation-simulator/README.md](learn.python/projects/level-7/06-token-rotation-simulator/README.md)
479. **Level 7 / Project 07 - Stale Data Detector** · project · intermediate/advanced — [learn.python/projects/level-7/07-stale-data-detector/README.md](learn.python/projects/level-7/07-stale-data-detector/README.md)
480. **Level 7 / Project 08 - Ingestion Observability Kit** · project · intermediate/advanced — [learn.python/projects/level-7/08-ingestion-observability-kit/README.md](learn.python/projects/level-7/08-ingestion-observability-kit/README.md)
481. **Level 7 / Project 09 - Contract Version Checker** · project · intermediate/advanced — [learn.python/projects/level-7/09-contract-version-checker/README.md](learn.python/projects/level-7/09-contract-version-checker/README.md)
482. **Level 7 / Project 10 - Multi Source Reconciler** · project · intermediate/advanced — [learn.python/projects/level-7/10-multi-source-reconciler/README.md](learn.python/projects/level-7/10-multi-source-reconciler/README.md)
483. **Level 7 / Project 11 - Pipeline Feature Flags** · project · intermediate/advanced — [learn.python/projects/level-7/11-pipeline-feature-flags/README.md](learn.python/projects/level-7/11-pipeline-feature-flags/README.md)
484. **Level 7 / Project 12 - Incident Mode Switch** · project · intermediate/advanced — [learn.python/projects/level-7/12-incident-mode-switch/README.md](learn.python/projects/level-7/12-incident-mode-switch/README.md)
485. **Level 7 / Project 13 - Service Account Policy Check** · project · intermediate/advanced — [learn.python/projects/level-7/13-service-account-policy-check/README.md](learn.python/projects/level-7/13-service-account-policy-check/README.md)
486. **Level 7 / Project 14 - Cache Backfill Runner** · project · intermediate/advanced — [learn.python/projects/level-7/14-cache-backfill-runner/README.md](learn.python/projects/level-7/14-cache-backfill-runner/README.md)
487. **Level 7 / Project 15 - Level 7 Mini Capstone** · project · intermediate/advanced — [learn.python/projects/level-7/15-level7-mini-capstone/README.md](learn.python/projects/level-7/15-level7-mini-capstone/README.md)
488. **Module 01 / Project 01: Fetch a Webpage** · project · project — [learn.python/projects/modules/01-web-scraping/01-fetch-a-webpage/README.md](learn.python/projects/modules/01-web-scraping/01-fetch-a-webpage/README.md)
489. **Module 01 / Project 02: Parse HTML** · project · project — [learn.python/projects/modules/01-web-scraping/02-parse-html/README.md](learn.python/projects/modules/01-web-scraping/02-parse-html/README.md)
490. **Module 01 / Project 03: Extract Structured Data** · project · project — [learn.python/projects/modules/01-web-scraping/03-extract-structured-data/README.md](learn.python/projects/modules/01-web-scraping/03-extract-structured-data/README.md)
491. **Module 01 / Project 04: Multi-Page Scraper** · project · project — [learn.python/projects/modules/01-web-scraping/04-multi-page-scraper/README.md](learn.python/projects/modules/01-web-scraping/04-multi-page-scraper/README.md)
492. **Module 01 / Project 05: Save to CSV** · project · project — [learn.python/projects/modules/01-web-scraping/05-save-to-csv/README.md](learn.python/projects/modules/01-web-scraping/05-save-to-csv/README.md)
493. **Module 03 / Project 01: First API Call** · project · project — [learn.python/projects/modules/03-rest-apis/01-first-api-call/README.md](learn.python/projects/modules/03-rest-apis/01-first-api-call/README.md)
494. **Module 03 / Project 02: Query Parameters** · project · project — [learn.python/projects/modules/03-rest-apis/02-query-parameters/README.md](learn.python/projects/modules/03-rest-apis/02-query-parameters/README.md)
495. **Module 03 / Project 03: POST and Auth** · project · project — [learn.python/projects/modules/03-rest-apis/03-post-and-auth/README.md](learn.python/projects/modules/03-rest-apis/03-post-and-auth/README.md)
496. **Module 03 / Project 04: Error Handling** · project · project — [learn.python/projects/modules/03-rest-apis/04-error-handling/README.md](learn.python/projects/modules/03-rest-apis/04-error-handling/README.md)
497. **Module 03 / Project 05: API Client Class** · project · project — [learn.python/projects/modules/03-rest-apis/05-api-client-class/README.md](learn.python/projects/modules/03-rest-apis/05-api-client-class/README.md)
498. **Module 03 / Project 06: Weather API Dashboard** · project · project — [learn.python/projects/modules/03-rest-apis/06-weather-api-dashboard/README.md](learn.python/projects/modules/03-rest-apis/06-weather-api-dashboard/README.md)

## 12 · Databases and durable data

SQLite, SQL, ORM patterns, migrations, idempotency and data pipelines.

### 30 Days

499. **📘 Day 27** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/27_Day_Python_with_mongodb/27_python_with_mongodb.md](30-Days-Of-Python/27_Day_Python_with_mongodb/27_python_with_mongodb.md)

### C1

500. **Exercise 1 — Your First Table** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/exercises/exercise-01-first-table.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/exercises/exercise-01-first-table.md)
501. **Exercise 2 — Parameterized Queries** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/exercises/exercise-02-parameterized.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/exercises/exercise-02-parameterized.md)
502. **Exercise 3 — Joining Users and Posts** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/exercises/exercise-03-joins.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/exercises/exercise-03-joins.md)
503. **Exercise 4 — Aggregating Sales** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/exercises/exercise-04-aggregate.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/exercises/exercise-04-aggregate.md)
504. **Exercise 5 — The Same Table with SQLAlchemy** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/exercises/exercise-05-sqlalchemy-basic.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/exercises/exercise-05-sqlalchemy-basic.md)
505. **Homework Problem 1 — Design an E-Commerce Schema** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/homework/problem-01-ecommerce-schema.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/homework/problem-01-ecommerce-schema.md)
506. **Homework Problem 2 — A Migration Script** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/homework/problem-02-migration-script.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/homework/problem-02-migration-script.md)
507. **Homework Problem 3 — CSV → SQLite Importer** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/homework/problem-03-csv-importer.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/homework/problem-03-csv-importer.md)
508. **Homework Problem 4 — Query Optimizer Puzzle** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/homework/problem-04-query-optimizer.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/homework/problem-04-query-optimizer.md)
509. **Homework Problem 5 — ORM Relationships (One-to-Many)** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/homework/problem-05-orm-relationships.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/homework/problem-05-orm-relationships.md)
510. **Homework Problem 6 — Backup and Restore Script** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/homework/problem-06-backup-restore.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/homework/problem-06-backup-restore.md)
511. **Challenge 01 — Library Management with SQLite** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/challenges/challenge-01-library-with-sqlite.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/challenges/challenge-01-library-with-sqlite.md)
512. **Challenge 02 — Flask Blog backed by SQLite** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/challenges/challenge-02-blog-with-db.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/challenges/challenge-02-blog-with-db.md)
513. **Mini-Project — SQLite Task Tracker CLI** · project · project — [C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-10-databases-sql/mini-project/README.md)

### learn.python

514. **Level 6 / Project 01 - SQL Connection Simulator** · project · intermediate/advanced — [learn.python/projects/level-6/01-sql-connection-simulator/README.md](learn.python/projects/level-6/01-sql-connection-simulator/README.md)
515. **Level 6 / Project 02 - Staging Table Loader** · project · intermediate/advanced — [learn.python/projects/level-6/02-staging-table-loader/README.md](learn.python/projects/level-6/02-staging-table-loader/README.md)
516. **Level 6 / Project 03 - Idempotency Key Builder** · project · intermediate/advanced — [learn.python/projects/level-6/03-idempotency-key-builder/README.md](learn.python/projects/level-6/03-idempotency-key-builder/README.md)
517. **Level 6 / Project 04 - Upsert Strategy Lab** · project · intermediate/advanced — [learn.python/projects/level-6/04-upsert-strategy-lab/README.md](learn.python/projects/level-6/04-upsert-strategy-lab/README.md)
518. **Level 6 / Project 05 - Transaction Rollback Drill** · project · intermediate/advanced — [learn.python/projects/level-6/05-transaction-rollback-drill/README.md](learn.python/projects/level-6/05-transaction-rollback-drill/README.md)
519. **Level 6 / Project 06 - Query Performance Checker** · project · intermediate/advanced — [learn.python/projects/level-6/06-query-performance-checker/README.md](learn.python/projects/level-6/06-query-performance-checker/README.md)
520. **Level 6 / Project 07 - SQL Summary Publisher** · project · intermediate/advanced — [learn.python/projects/level-6/07-sql-summary-publisher/README.md](learn.python/projects/level-6/07-sql-summary-publisher/README.md)
521. **Level 6 / Project 08 - Data Lineage Capture** · project · intermediate/advanced — [learn.python/projects/level-6/08-data-lineage-capture/README.md](learn.python/projects/level-6/08-data-lineage-capture/README.md)
522. **Level 6 / Project 09 - Incremental Load Simulator** · project · intermediate/advanced — [learn.python/projects/level-6/09-incremental-load-simulator/README.md](learn.python/projects/level-6/09-incremental-load-simulator/README.md)
523. **Level 6 / Project 10 - Table Drift Detector** · project · intermediate/advanced — [learn.python/projects/level-6/10-table-drift-detector/README.md](learn.python/projects/level-6/10-table-drift-detector/README.md)
524. **Level 6 / Project 11 - Dead Letter Row Handler** · project · intermediate/advanced — [learn.python/projects/level-6/11-dead-letter-row-handler/README.md](learn.python/projects/level-6/11-dead-letter-row-handler/README.md)
525. **Level 6 / Project 12 - ETL Health Dashboard Feed** · project · intermediate/advanced — [learn.python/projects/level-6/12-etl-health-dashboard-feed/README.md](learn.python/projects/level-6/12-etl-health-dashboard-feed/README.md)
526. **Level 6 / Project 13 - Batch Window Controller** · project · intermediate/advanced — [learn.python/projects/level-6/13-batch-window-controller/README.md](learn.python/projects/level-6/13-batch-window-controller/README.md)
527. **Level 6 / Project 14 - SQL Runbook Generator** · project · intermediate/advanced — [learn.python/projects/level-6/14-sql-runbook-generator/README.md](learn.python/projects/level-6/14-sql-runbook-generator/README.md)
528. **Level 6 / Project 15 - Level 6 Mini Capstone** · project · intermediate/advanced — [learn.python/projects/level-6/15-level6-mini-capstone/README.md](learn.python/projects/level-6/15-level6-mini-capstone/README.md)
529. **Module 06 / Project 01: SQLite Basics** · project · project — [learn.python/projects/modules/06-databases-orm/01-sqlite-basics/README.md](learn.python/projects/modules/06-databases-orm/01-sqlite-basics/README.md)
530. **Module 06 / Project 02: SQLAlchemy Models** · project · project — [learn.python/projects/modules/06-databases-orm/02-sqlalchemy-models/README.md](learn.python/projects/modules/06-databases-orm/02-sqlalchemy-models/README.md)
531. **Module 06 / Project 03: CRUD Operations** · project · project — [learn.python/projects/modules/06-databases-orm/03-crud-operations/README.md](learn.python/projects/modules/06-databases-orm/03-crud-operations/README.md)
532. **Module 06 / Project 04: Migrations with Alembic** · project · project — [learn.python/projects/modules/06-databases-orm/04-migrations-alembic/README.md](learn.python/projects/modules/06-databases-orm/04-migrations-alembic/README.md)
533. **Module 06 / Project 05: Query Optimization** · project · project — [learn.python/projects/modules/06-databases-orm/05-query-optimization/README.md](learn.python/projects/modules/06-databases-orm/05-query-optimization/README.md)

## 13 · Web applications and services

Flask, FastAPI, Django, forms, sessions, CRUD services and API delivery.

### 30 Days

534. **📘 Day 26** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/26_Day_Python_web/26_python_web.md](30-Days-Of-Python/26_Day_Python_web/26_python_web.md)
535. **let's import the flask** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/29_Day_Building_API/29_building_API.md](30-Days-Of-Python/29_Day_Building_API/29_building_API.md)

### C1

536. **Exercise 1 — Hello, Flask** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/exercises/exercise-01-hello-flask.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/exercises/exercise-01-hello-flask.md)
537. **Exercise 2 — Multiple Routes and URL Converters** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/exercises/exercise-02-multiple-routes.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/exercises/exercise-02-multiple-routes.md)
538. **Exercise 3 — Template Loop** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/exercises/exercise-03-template-loop.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/exercises/exercise-03-template-loop.md)
539. **Exercise 4 — Form Echo** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/exercises/exercise-04-form-echo.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/exercises/exercise-04-form-echo.md)
540. **Homework Problem 1 — Custom 404 page** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/homework/problem-01-custom-404-page.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/homework/problem-01-custom-404-page.md)
541. **Homework Problem 2 — Base template** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/homework/problem-02-base-template.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/homework/problem-02-base-template.md)
542. **Homework Problem 3 — Weather route** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/homework/problem-03-weather-route.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/homework/problem-03-weather-route.md)
543. **Homework Problem 4 — Post tags** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/homework/problem-04-post-tags.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/homework/problem-04-post-tags.md)
544. **Homework Problem 5 — Search filter** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/homework/problem-05-search-filter.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/homework/problem-05-search-filter.md)
545. **Homework Problem 6 — Session auth (demo only)** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/homework/problem-06-session-auth-demo.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/homework/problem-06-session-auth-demo.md)
546. **Challenge 01 — Todo App** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/challenges/challenge-01-todo-app.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/challenges/challenge-01-todo-app.md)
547. **Challenge 02 — Tiny URL Shortener** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/challenges/challenge-02-url-shortener.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/challenges/challenge-02-url-shortener.md)
548. **Mini-Project — Personal Blog** · project · project — [C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-09-web-development-flask/mini-project/README.md)

### learn.python

549. **Module 04 / Project 01: Hello FastAPI** · project · project — [learn.python/projects/modules/04-fastapi-web/01-hello-fastapi/README.md](learn.python/projects/modules/04-fastapi-web/01-hello-fastapi/README.md)
550. **Module 04 / Project 02: CRUD API** · project · project — [learn.python/projects/modules/04-fastapi-web/02-crud-api/README.md](learn.python/projects/modules/04-fastapi-web/02-crud-api/README.md)
551. **Module 04 / Project 03: Database-Backed API** · project · project — [learn.python/projects/modules/04-fastapi-web/03-database-backed/README.md](learn.python/projects/modules/04-fastapi-web/03-database-backed/README.md)
552. **Module 04 / Project 04: Authentication** · project · project — [learn.python/projects/modules/04-fastapi-web/04-authentication/README.md](learn.python/projects/modules/04-fastapi-web/04-authentication/README.md)
553. **Module 04 / Project 05: Full App** · project · project — [learn.python/projects/modules/04-fastapi-web/05-full-app/README.md](learn.python/projects/modules/04-fastapi-web/05-full-app/README.md)
554. **Module 10 / Project 01: Django Setup** · project · project — [learn.python/projects/modules/10-django-fullstack/01-django-setup/README.md](learn.python/projects/modules/10-django-fullstack/01-django-setup/README.md)
555. **Module 10 / Project 02: Views & Templates** · project · project — [learn.python/projects/modules/10-django-fullstack/02-views-templates/README.md](learn.python/projects/modules/10-django-fullstack/02-views-templates/README.md)
556. **Module 10 / Project 03: Forms & Auth** · project · project — [learn.python/projects/modules/10-django-fullstack/03-forms-auth/README.md](learn.python/projects/modules/10-django-fullstack/03-forms-auth/README.md)
557. **Module 10 / Project 04: REST Framework** · project · project — [learn.python/projects/modules/10-django-fullstack/04-rest-framework/README.md](learn.python/projects/modules/10-django-fullstack/04-rest-framework/README.md)
558. **Module 10 / Project 05: Complete App** · project · project — [learn.python/projects/modules/10-django-fullstack/05-complete-app/README.md](learn.python/projects/modules/10-django-fullstack/05-complete-app/README.md)

## 14 · Data analysis, statistics and machine learning

NumPy, pandas, visualization, statistics, model training and evaluation.

### 30 Days

559. **📘 Day 24** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/24_Day_Statistics/24_statistics.md](30-Days-Of-Python/24_Day_Statistics/24_statistics.md)
560. **📘 Day 25** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/25_Day_Pandas/25_pandas.md](30-Days-Of-Python/25_Day_Pandas/25_pandas.md)

### C1

561. **Exercise 1 — NumPy Arrays** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/exercises/exercise-01-numpy-arrays.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/exercises/exercise-01-numpy-arrays.md)
562. **Exercise 2 — Load and Inspect** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/exercises/exercise-02-load-and-inspect.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/exercises/exercise-02-load-and-inspect.md)
563. **Exercise 3 — Filter and Sort** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/exercises/exercise-03-filter-and-sort.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/exercises/exercise-03-filter-and-sort.md)
564. **Exercise 4 — Groupby** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/exercises/exercise-04-groupby.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/exercises/exercise-04-groupby.md)
565. **Exercise 5 — Plot** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/exercises/exercise-05-plot.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/exercises/exercise-05-plot.md)
566. **Exercise 1 — Your First Model: Price From Floor Area** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/exercises/exercise-01-linear-regression.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/exercises/exercise-01-linear-regression.md)
567. **Exercise 2 — Iris Classifier** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/exercises/exercise-02-iris-classifier.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/exercises/exercise-02-iris-classifier.md)
568. **Exercise 3 — Why randomstate Matters** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/exercises/exercise-03-train-test-split.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/exercises/exercise-03-train-test-split.md)
569. **Exercise 4 — Scaler and Model in One Pipeline** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/exercises/exercise-04-pipeline.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/exercises/exercise-04-pipeline.md)
570. **Exercise 5 — Reading the Confusion Matrix** · assignment · guided — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/exercises/exercise-05-confusion-matrix.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/exercises/exercise-05-confusion-matrix.md)
571. **Homework 1 — CSV to JSON converter** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/homework/problem-01-csv-to-json.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/homework/problem-01-csv-to-json.md)
572. **Homework 2 — Missing-data report** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/homework/problem-02-missing-data-report.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/homework/problem-02-missing-data-report.md)
573. **Homework 3 — Merge two DataFrames** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/homework/problem-03-merge-dataframes.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/homework/problem-03-merge-dataframes.md)
574. **Homework 4 — Pivot table from raw** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/homework/problem-04-pivot-table.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/homework/problem-04-pivot-table.md)
575. **Homework 5 — Multi-line chart** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/homework/problem-05-multi-line-chart.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/homework/problem-05-multi-line-chart.md)
576. **Homework 6 — Find correlations** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/homework/problem-06-correlations.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/homework/problem-06-correlations.md)
577. **Problem 1 — Housing Regression: Linear vs Boosted** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/homework/problem-01-housing-regression.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/homework/problem-01-housing-regression.md)
578. **Problem 2 — Churn Classification: When Accuracy Lies** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/homework/problem-02-churn-classification.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/homework/problem-02-churn-classification.md)
579. **Problem 3 — Feature Importance: What the Forest Leaned On** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/homework/problem-03-feature-importance.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/homework/problem-03-feature-importance.md)
580. **Problem 4 — Hyperparameter Tuning With GridSearchCV** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/homework/problem-04-grid-search.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/homework/problem-04-grid-search.md)
581. **Problem 5 — Learning Curve: More Data, or a Bigger Brain?** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/homework/problem-05-learning-curve.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/homework/problem-05-learning-curve.md)
582. **Problem 6 — Fairness Audit: One Model, Three Scorecards** · assignment · practice — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/homework/problem-06-fairness-audit.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/homework/problem-06-fairness-audit.md)
583. **Challenge 1 — Titanic Exploratory Data Analysis** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/challenges/challenge-01-titanic-eda.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/challenges/challenge-01-titanic-eda.md)
584. **Challenge 2 — Time Series: Resample & Rolling Mean** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/challenges/challenge-02-time-series.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/challenges/challenge-02-time-series.md)
585. **Challenge 1 — Predict Titanic Survival, Then Audit It** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/challenges/challenge-01-titanic-survival.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/challenges/challenge-01-titanic-survival.md)
586. **Challenge 2 — Customer Segmentation With k-means** · assignment · challenge — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/challenges/challenge-02-kmeans-clustering.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/challenges/challenge-02-kmeans-clustering.md)
587. **Mini-Project — Real-World Dataset Analysis** · project · project — [C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-13-data-analysis/mini-project/README.md)
588. **Mini-Project — SMS Spam Classifier** · project · project — [C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/mini-project/README.md](C1-Code-Crunch-Convos/curriculum/week-14-intro-ai-ml/mini-project/README.md)

### learn.python

589. **Module 07 / Project 01: Pandas Basics** · project · project — [learn.python/projects/modules/07-data-analysis/01-pandas-basics/README.md](learn.python/projects/modules/07-data-analysis/01-pandas-basics/README.md)
590. **Module 07 / Project 02: Filtering & Grouping** · project · project — [learn.python/projects/modules/07-data-analysis/02-filtering-grouping/README.md](learn.python/projects/modules/07-data-analysis/02-filtering-grouping/README.md)
591. **Module 07 / Project 03: Data Cleaning** · project · project — [learn.python/projects/modules/07-data-analysis/03-data-cleaning/README.md](learn.python/projects/modules/07-data-analysis/03-data-cleaning/README.md)
592. **Module 07 / Project 04: Visualization** · project · project — [learn.python/projects/modules/07-data-analysis/04-visualization/README.md](learn.python/projects/modules/07-data-analysis/04-visualization/README.md)
593. **Module 07 / Project 05: Analysis Report** · project · project — [learn.python/projects/modules/07-data-analysis/05-analysis-report/README.md](learn.python/projects/modules/07-data-analysis/05-analysis-report/README.md)
594. **Module 07 / Project 06: NumPy Foundations** · project · project — [learn.python/projects/modules/07-data-analysis/06-numpy-foundations/README.md](learn.python/projects/modules/07-data-analysis/06-numpy-foundations/README.md)

## 15 · Async and concurrent Python

Coroutines, producer-consumer systems, concurrent I/O and process coordination.

### Exercism

595. **Parallel Letter Frequency** · practice · Advanced — [python-curriculum/exercises/practice/parallel-letter-frequency/.docs/instructions.md](python-curriculum/exercises/practice/parallel-letter-frequency/.docs/instructions.md)

### learn.python

596. **Challenge 03: Async Web Scraper** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/03_async_web_scraper.py](learn.python/practice/challenges/advanced/03_async_web_scraper.py)
597. **Challenge 09: Async Producer-Consumer** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/09_async_producer_consumer.py](learn.python/practice/challenges/advanced/09_async_producer_consumer.py)
598. **Challenge 11: Coroutine Scheduler** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/11_coroutine_scheduler.py](learn.python/practice/challenges/advanced/11_coroutine_scheduler.py)
599. **Challenge: Async Fetcher with Concurrency Limit** · challenge · intermediate challenge — [learn.python/practice/challenges/intermediate/13-async-fetcher.py](learn.python/practice/challenges/intermediate/13-async-fetcher.py)
600. **Module 05 / Project 01: Async Basics** · project · project — [learn.python/projects/modules/05-async-python/01-async-basics/README.md](learn.python/projects/modules/05-async-python/01-async-basics/README.md)
601. **Module 05 / Project 02: Concurrent Requests** · project · project — [learn.python/projects/modules/05-async-python/02-concurrent-requests/README.md](learn.python/projects/modules/05-async-python/02-concurrent-requests/README.md)
602. **Module 05 / Project 03: Async File Processing** · project · project — [learn.python/projects/modules/05-async-python/03-async-file-processing/README.md](learn.python/projects/modules/05-async-python/03-async-file-processing/README.md)
603. **Module 05 / Project 04: Producer-Consumer** · project · project — [learn.python/projects/modules/05-async-python/04-producer-consumer/README.md](learn.python/projects/modules/05-async-python/04-producer-consumer/README.md)
604. **Module 05 / Project 05: Async Web Server** · project · project — [learn.python/projects/modules/05-async-python/05-async-web-server/README.md](learn.python/projects/modules/05-async-python/05-async-web-server/README.md)
605. **Module 05 / Project 06: WebSocket Chat Server** · project · project — [learn.python/projects/modules/05-async-python/06-websocket-chat/README.md](learn.python/projects/modules/05-async-python/06-websocket-chat/README.md)

## 16 · Packaging, delivery and operations

Packages, Docker, CI, deployment, configuration and operational readiness.

### 30 Days

606. **📘 Day 20** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/20_Day_Python_package_manager/20_python_package_manager.md](30-Days-Of-Python/20_Day_Python_package_manager/20_python_package_manager.md)
607. **📘 Day 23** · day lesson and exercises · lesson + exercises — [30-Days-Of-Python/23_Day_Virtual_environment/23_virtual_environment.md](30-Days-Of-Python/23_Day_Virtual_environment/23_virtual_environment.md)

### learn.python

608. **Level 8 / Project 01 - Dashboard KPI Assembler** · project · intermediate/advanced — [learn.python/projects/level-8/01-dashboard-kpi-assembler/README.md](learn.python/projects/level-8/01-dashboard-kpi-assembler/README.md)
609. **Level 8 / Project 02 - Query Cache Layer** · project · intermediate/advanced — [learn.python/projects/level-8/02-query-cache-layer/README.md](learn.python/projects/level-8/02-query-cache-layer/README.md)
610. **Level 8 / Project 03 - Pagination Stress Lab** · project · intermediate/advanced — [learn.python/projects/level-8/03-pagination-stress-lab/README.md](learn.python/projects/level-8/03-pagination-stress-lab/README.md)
611. **Level 8 / Project 04 - Filter State Manager** · project · intermediate/advanced — [learn.python/projects/level-8/04-filter-state-manager/README.md](learn.python/projects/level-8/04-filter-state-manager/README.md)
612. **Level 8 / Project 05 - Export Governance Check** · project · intermediate/advanced — [learn.python/projects/level-8/05-export-governance-check/README.md](learn.python/projects/level-8/05-export-governance-check/README.md)
613. **Level 8 / Project 06 - Response Time Profiler** · project · intermediate/advanced — [learn.python/projects/level-8/06-response-time-profiler/README.md](learn.python/projects/level-8/06-response-time-profiler/README.md)
614. **Level 8 / Project 07 - Concurrency Queue Simulator** · project · intermediate/advanced — [learn.python/projects/level-8/07-concurrency-queue-simulator/README.md](learn.python/projects/level-8/07-concurrency-queue-simulator/README.md)
615. **Level 8 / Project 08 - Fault Injection Harness** · project · intermediate/advanced — [learn.python/projects/level-8/08-fault-injection-harness/README.md](learn.python/projects/level-8/08-fault-injection-harness/README.md)
616. **Level 8 / Project 09 - Graceful Degradation Engine** · project · intermediate/advanced — [learn.python/projects/level-8/09-graceful-degradation-engine/README.md](learn.python/projects/level-8/09-graceful-degradation-engine/README.md)
617. **Level 8 / Project 10 - Dependency Timeout Matrix** · project · intermediate/advanced — [learn.python/projects/level-8/10-dependency-timeout-matrix/README.md](learn.python/projects/level-8/10-dependency-timeout-matrix/README.md)
618. **Level 8 / Project 11 - Synthetic Monitor Runner** · project · intermediate/advanced — [learn.python/projects/level-8/11-synthetic-monitor-runner/README.md](learn.python/projects/level-8/11-synthetic-monitor-runner/README.md)
619. **Level 8 / Project 12 - Release Readiness Evaluator** · project · intermediate/advanced — [learn.python/projects/level-8/12-release-readiness-evaluator/README.md](learn.python/projects/level-8/12-release-readiness-evaluator/README.md)
620. **Level 8 / Project 13 - SLA Breach Detector** · project · intermediate/advanced — [learn.python/projects/level-8/13-sla-breach-detector/README.md](learn.python/projects/level-8/13-sla-breach-detector/README.md)
621. **Level 8 / Project 14 - User Journey Tracer** · project · intermediate/advanced — [learn.python/projects/level-8/14-user-journey-tracer/README.md](learn.python/projects/level-8/14-user-journey-tracer/README.md)
622. **Level 8 / Project 15 - Level 8 Mini Capstone** · project · intermediate/advanced — [learn.python/projects/level-8/15-level8-mini-capstone/README.md](learn.python/projects/level-8/15-level8-mini-capstone/README.md)
623. **Module 09 / Project 01: First Dockerfile** · project · project — [learn.python/projects/modules/09-docker-deployment/01-first-dockerfile/README.md](learn.python/projects/modules/09-docker-deployment/01-first-dockerfile/README.md)
624. **Module 09 / Project 02: Multi-Stage Build** · project · project — [learn.python/projects/modules/09-docker-deployment/02-multi-stage-build/README.md](learn.python/projects/modules/09-docker-deployment/02-multi-stage-build/README.md)
625. **Module 09 / Project 03: Docker Compose** · project · project — [learn.python/projects/modules/09-docker-deployment/03-docker-compose/README.md](learn.python/projects/modules/09-docker-deployment/03-docker-compose/README.md)
626. **Module 09 / Project 04: CI with GitHub Actions** · project · project — [learn.python/projects/modules/09-docker-deployment/04-ci-github-actions/README.md](learn.python/projects/modules/09-docker-deployment/04-ci-github-actions/README.md)
627. **Module 09 / Project 05: Production Config** · project · project — [learn.python/projects/modules/09-docker-deployment/05-production-config/README.md](learn.python/projects/modules/09-docker-deployment/05-production-config/README.md)
628. **Module 11 / Project 01: Package Structure** · project · project — [learn.python/projects/modules/11-package-publishing/01-package-structure/README.md](learn.python/projects/modules/11-package-publishing/01-package-structure/README.md)
629. **Module 11 / Project 02: Build and Test** · project · project — [learn.python/projects/modules/11-package-publishing/02-build-and-test/README.md](learn.python/projects/modules/11-package-publishing/02-build-and-test/README.md)
630. **Module 11 / Project 03: Publish to PyPI** · project · project — [learn.python/projects/modules/11-package-publishing/03-publish-to-pypi/README.md](learn.python/projects/modules/11-package-publishing/03-publish-to-pypi/README.md)
631. **Module 12 / Project 01: Deploy to Railway** · project · project — [learn.python/projects/modules/12-cloud-deploy/01-deploy-to-railway/README.md](learn.python/projects/modules/12-cloud-deploy/01-deploy-to-railway/README.md)
632. **Module 12 / Project 02: Deploy with Database** · project · project — [learn.python/projects/modules/12-cloud-deploy/02-deploy-with-database/README.md](learn.python/projects/modules/12-cloud-deploy/02-deploy-with-database/README.md)
633. **Module 12 / Project 03: Production Checklist** · project · project — [learn.python/projects/modules/12-cloud-deploy/03-production-checklist/README.md](learn.python/projects/modules/12-cloud-deploy/03-production-checklist/README.md)

## 17 · Architecture, security and reliability

System boundaries, observability, policy, performance, resilience and technical leadership.

### Exercism

634. **React** · practice · Advanced — [python-curriculum/exercises/practice/react/.docs/instructions.md](python-curriculum/exercises/practice/react/.docs/instructions.md)
635. **Diffie-Hellman** · practice · Intermediate plus — [python-curriculum/exercises/practice/diffie-hellman/.docs/instructions.md](python-curriculum/exercises/practice/diffie-hellman/.docs/instructions.md)

### learn.python

636. **Challenge 01: Generator Pipeline** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/01_generator_pipeline.py](learn.python/practice/challenges/advanced/01_generator_pipeline.py)
637. **Challenge 02: Custom Context Manager** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/02_custom_context_manager.py](learn.python/practice/challenges/advanced/02_custom_context_manager.py)
638. **Challenge 04: Metaclass Registry** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/04_metaclass_registry.py](learn.python/practice/challenges/advanced/04_metaclass_registry.py)
639. **Challenge 05: Type Narrowing** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/05_type_narrowing.py](learn.python/practice/challenges/advanced/05_type_narrowing.py)
640. **Challenge 06: Decorator Stack** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/06_decorator_stack.py](learn.python/practice/challenges/advanced/06_decorator_stack.py)
641. **Challenge 07: Dataclass Validation** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/07_dataclass_validation.py](learn.python/practice/challenges/advanced/07_dataclass_validation.py)
642. **Challenge 08: Protocol Interfaces** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/08_protocol_interfaces.py](learn.python/practice/challenges/advanced/08_protocol_interfaces.py)
643. **Challenge 10: Descriptor Protocol** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/10_descriptor_protocol.py](learn.python/practice/challenges/advanced/10_descriptor_protocol.py)
644. **Challenge 12: Generic Repository** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/12_generic_repository.py](learn.python/practice/challenges/advanced/12_generic_repository.py)
645. **Challenge 13: Event System** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/13_event_system.py](learn.python/practice/challenges/advanced/13_event_system.py)
646. **Challenge 14: AST Code Analyzer** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/14_ast_code_analyzer.py](learn.python/practice/challenges/advanced/14_ast_code_analyzer.py)
647. **Challenge 15: Functional Pipeline** · challenge · advanced challenge — [learn.python/practice/challenges/advanced/15_functional_pipeline.py](learn.python/practice/challenges/advanced/15_functional_pipeline.py)
648. **A calculator that evaluates simple arithmetic expressions.** · challenge · project — [learn.python/practice/challenges/refactoring/01_spaghetti_calculator/messy.py](learn.python/practice/challenges/refactoring/01_spaghetti_calculator/messy.py)
649. **Monthly sales report generator.** · challenge · project — [learn.python/practice/challenges/refactoring/02_monolithic_report/messy.py](learn.python/practice/challenges/refactoring/02_monolithic_report/messy.py)
650. **API client for a public data service.** · challenge · project — [learn.python/practice/challenges/refactoring/03_copy_paste_api/messy.py](learn.python/practice/challenges/refactoring/03_copy_paste_api/messy.py)
651. **Elite Track / Algorithms and Complexity Lab** · project · advanced — [learn.python/projects/elite-track/01-algorithms-complexity-lab/README.md](learn.python/projects/elite-track/01-algorithms-complexity-lab/README.md)
652. **Elite Track / Concurrent Job System** · project · advanced — [learn.python/projects/elite-track/02-concurrent-job-system/README.md](learn.python/projects/elite-track/02-concurrent-job-system/README.md)
653. **Elite Track / Distributed Cache Simulator** · project · advanced — [learn.python/projects/elite-track/03-distributed-cache-simulator/README.md](learn.python/projects/elite-track/03-distributed-cache-simulator/README.md)
654. **Elite Track / Secure Auth Gateway** · project · advanced — [learn.python/projects/elite-track/04-secure-auth-gateway/README.md](learn.python/projects/elite-track/04-secure-auth-gateway/README.md)
655. **Elite Track / Performance Profiler Workbench** · project · advanced — [learn.python/projects/elite-track/05-performance-profiler-workbench/README.md](learn.python/projects/elite-track/05-performance-profiler-workbench/README.md)
656. **Elite Track / Event Driven Architecture Lab** · project · advanced — [learn.python/projects/elite-track/06-event-driven-architecture-lab/README.md](learn.python/projects/elite-track/06-event-driven-architecture-lab/README.md)
657. **Elite Track / Observability SLO Platform** · project · advanced — [learn.python/projects/elite-track/07-observability-slo-platform/README.md](learn.python/projects/elite-track/07-observability-slo-platform/README.md)
658. **Elite Track / Policy and Compliance Engine** · project · advanced — [learn.python/projects/elite-track/08-policy-compliance-engine/README.md](learn.python/projects/elite-track/08-policy-compliance-engine/README.md)
659. **Elite Track / Open Source Maintainer Simulator** · project · advanced — [learn.python/projects/elite-track/09-open-source-maintainer-simulator/README.md](learn.python/projects/elite-track/09-open-source-maintainer-simulator/README.md)
660. **Elite Track / Staff Engineer Capstone** · project · advanced — [learn.python/projects/elite-track/10-staff-engineer-capstone/README.md](learn.python/projects/elite-track/10-staff-engineer-capstone/README.md)
661. **Level 10 / Project 01 - Enterprise Python Blueprint** · project · intermediate/advanced — [learn.python/projects/level-10/01-enterprise-python-blueprint/README.md](learn.python/projects/level-10/01-enterprise-python-blueprint/README.md)
662. **Level 10 / Project 02 - Autonomous Run Orchestrator** · project · intermediate/advanced — [learn.python/projects/level-10/02-autonomous-run-orchestrator/README.md](learn.python/projects/level-10/02-autonomous-run-orchestrator/README.md)
663. **Level 10 / Project 03 - Policy As Code Validator** · project · intermediate/advanced — [learn.python/projects/level-10/03-policy-as-code-validator/README.md](learn.python/projects/level-10/03-policy-as-code-validator/README.md)
664. **Level 10 / Project 04 - Multi Tenant Data Guard** · project · intermediate/advanced — [learn.python/projects/level-10/04-multi-tenant-data-guard/README.md](learn.python/projects/level-10/04-multi-tenant-data-guard/README.md)
665. **Level 10 / Project 05 - Compliance Evidence Builder** · project · intermediate/advanced — [learn.python/projects/level-10/05-compliance-evidence-builder/README.md](learn.python/projects/level-10/05-compliance-evidence-builder/README.md)
666. **Level 10 / Project 06 - Resilience Chaos Workbench** · project · intermediate/advanced — [learn.python/projects/level-10/06-resilience-chaos-workbench/README.md](learn.python/projects/level-10/06-resilience-chaos-workbench/README.md)
667. **Level 10 / Project 07 - High Risk Change Gate** · project · intermediate/advanced — [learn.python/projects/level-10/07-high-risk-change-gate/README.md](learn.python/projects/level-10/07-high-risk-change-gate/README.md)
668. **Level 10 / Project 08 - Zero Downtime Migration Lab** · project · intermediate/advanced — [learn.python/projects/level-10/08-zero-downtime-migration-lab/README.md](learn.python/projects/level-10/08-zero-downtime-migration-lab/README.md)
669. **Level 10 / Project 09 - Strategic Architecture Review** · project · intermediate/advanced — [learn.python/projects/level-10/09-strategic-architecture-review/README.md](learn.python/projects/level-10/09-strategic-architecture-review/README.md)
670. **Level 10 / Project 10 - Executive Metrics Publisher** · project · intermediate/advanced — [learn.python/projects/level-10/10-executive-metrics-publisher/README.md](learn.python/projects/level-10/10-executive-metrics-publisher/README.md)
671. **Level 10 / Project 11 - Production Readiness Director** · project · intermediate/advanced — [learn.python/projects/level-10/11-production-readiness-director/README.md](learn.python/projects/level-10/11-production-readiness-director/README.md)
672. **Level 10 / Project 12 - Onboarding Accelerator System** · project · intermediate/advanced — [learn.python/projects/level-10/12-onboarding-accelerator-system/README.md](learn.python/projects/level-10/12-onboarding-accelerator-system/README.md)
673. **Level 10 / Project 13 - Legacy Modernization Planner** · project · intermediate/advanced — [learn.python/projects/level-10/13-legacy-modernization-planner/README.md](learn.python/projects/level-10/13-legacy-modernization-planner/README.md)
674. **Level 10 / Project 14 - SME Mentorship Toolkit** · project · intermediate/advanced — [learn.python/projects/level-10/14-sme-mentorship-toolkit/README.md](learn.python/projects/level-10/14-sme-mentorship-toolkit/README.md)
675. **Level 10 / Project 15 - Level 10 Grand Capstone** · project · intermediate/advanced — [learn.python/projects/level-10/15-level10-grand-capstone/README.md](learn.python/projects/level-10/15-level10-grand-capstone/README.md)
676. **Level 9 / Project 01 - Architecture Decision Log** · project · intermediate/advanced — [learn.python/projects/level-9/01-architecture-decision-log/README.md](learn.python/projects/level-9/01-architecture-decision-log/README.md)
677. **Level 9 / Project 02 - Domain Boundary Enforcer** · project · intermediate/advanced — [learn.python/projects/level-9/02-domain-boundary-enforcer/README.md](learn.python/projects/level-9/02-domain-boundary-enforcer/README.md)
678. **Level 9 / Project 03 - Event Driven Pipeline Lab** · project · intermediate/advanced — [learn.python/projects/level-9/03-event-driven-pipeline-lab/README.md](learn.python/projects/level-9/03-event-driven-pipeline-lab/README.md)
679. **Level 9 / Project 04 - Observability SLO Pack** · project · intermediate/advanced — [learn.python/projects/level-9/04-observability-slo-pack/README.md](learn.python/projects/level-9/04-observability-slo-pack/README.md)
680. **Level 9 / Project 05 - Capacity Planning Model** · project · intermediate/advanced — [learn.python/projects/level-9/05-capacity-planning-model/README.md](learn.python/projects/level-9/05-capacity-planning-model/README.md)
681. **Level 9 / Project 06 - Reliability Scorecard** · project · intermediate/advanced — [learn.python/projects/level-9/06-reliability-scorecard/README.md](learn.python/projects/level-9/06-reliability-scorecard/README.md)
682. **Level 9 / Project 07 - Canary Rollout Simulator** · project · intermediate/advanced — [learn.python/projects/level-9/07-canary-rollout-simulator/README.md](learn.python/projects/level-9/07-canary-rollout-simulator/README.md)
683. **Level 9 / Project 08 - Change Impact Analyzer** · project · intermediate/advanced — [learn.python/projects/level-9/08-change-impact-analyzer/README.md](learn.python/projects/level-9/08-change-impact-analyzer/README.md)
684. **Level 9 / Project 09 - Security Baseline Auditor** · project · intermediate/advanced — [learn.python/projects/level-9/09-security-baseline-auditor/README.md](learn.python/projects/level-9/09-security-baseline-auditor/README.md)
685. **Level 9 / Project 10 - Data Governance Enforcer** · project · intermediate/advanced — [learn.python/projects/level-9/10-data-governance-enforcer/README.md](learn.python/projects/level-9/10-data-governance-enforcer/README.md)
686. **Level 9 / Project 11 - Recovery Time Estimator** · project · intermediate/advanced — [learn.python/projects/level-9/11-recovery-time-estimator/README.md](learn.python/projects/level-9/11-recovery-time-estimator/README.md)
687. **Level 9 / Project 12 - Incident Postmortem Generator** · project · intermediate/advanced — [learn.python/projects/level-9/12-incident-postmortem-generator/README.md](learn.python/projects/level-9/12-incident-postmortem-generator/README.md)
688. **Level 9 / Project 13 - Platform Cost Estimator** · project · intermediate/advanced — [learn.python/projects/level-9/13-platform-cost-estimator/README.md](learn.python/projects/level-9/13-platform-cost-estimator/README.md)
689. **Level 9 / Project 14 - Cross Team Handoff Kit** · project · intermediate/advanced — [learn.python/projects/level-9/14-cross-team-handoff-kit/README.md](learn.python/projects/level-9/14-cross-team-handoff-kit/README.md)
690. **Level 9 / Project 15 - Level 9 Mini Capstone** · project · intermediate/advanced — [learn.python/projects/level-9/15-level9-mini-capstone/README.md](learn.python/projects/level-9/15-level9-mini-capstone/README.md)

## 18 · Capstones

Integrate multiple domains into portfolio-scale, tested and documented systems.

### C1

691. **Capstone Project Master Guide** · project · project — [C1-Code-Crunch-Convos/projects/capstone/README.md](C1-Code-Crunch-Convos/projects/capstone/README.md)

### learn.python

692. **Capstone 01 — Personal Finance Tracker** · project · project — [learn.python/projects/capstones/01_personal_finance_tracker/README.md](learn.python/projects/capstones/01_personal_finance_tracker/README.md)
693. **Capstone 02 — API Aggregator** · project · project — [learn.python/projects/capstones/02_api_aggregator/README.md](learn.python/projects/capstones/02_api_aggregator/README.md)
694. **Capstone 03 — Task Automation System** · project · project — [learn.python/projects/capstones/03_task_automation_system/README.md](learn.python/projects/capstones/03_task_automation_system/README.md)

---

## Not assigned as separate unlocks

These files were inspected, but assigning them separately would duplicate a task, expose a known-broken contract, or create a non-task unlock.

- **Day 30** — [30-Days-Of-Python/30_Day_Conclusions/30_conclusions.md](30-Days-Of-Python/30_Day_Conclusions/30_conclusions.md) — Conclusion/outro contains no independent programming assignment.
- **📘 Day 24** — [30-Days-Of-Python/numpy.md](30-Days-Of-Python/numpy.md) — Alternate duplicate of the Day 24 NumPy lab; keep as a source reference, not a second unlock.
- **Mini-Projects Index** — [C1-Code-Crunch-Convos/projects/mini-projects/README.md](C1-Code-Crunch-Convos/projects/mini-projects/README.md) — Container/index page; its concrete child projects are already sequenced.
- **Electric Bill** — [python-curriculum/exercises/concept/electric-bill/.docs/instructions.md](python-curriculum/exercises/concept/electric-bill/.docs/instructions.md) — Instructions demand get_kW_value/get_kWh_value, while starter and tests demand get_kW_amount/get_kwh_amount. Watts divided by 1000 then 3600 is not an energy calculation without duration. Reference tests pass their own legacy contract but do not resolve these instruction defects; Currency Exchange is the stronger arithmetic assignment.
- **Restaurant Rozalynn** — [python-curriculum/exercises/concept/restaurant-rozalynn/.docs/instructions.md](python-curriculum/exercises/concept/restaurant-rozalynn/.docs/instructions.md) — Full six-part instructions and test bodies reviewed. arrange_reservations must seat Walter first under the prose, but test_arrange_reservations_1 expects Walter omitted and Frank first. Tests also call an undocumented no-argument form. Reference passes its tests, but that cannot reconcile the contradictory contract; quarantine pending source repair.
- **Minesweeper** — [python-curriculum/exercises/practice/minesweeper/.docs/instructions.md](python-curriculum/exercises/practice/minesweeper/.docs/instructions.md) — Full docs, starter and every test read. Deprecated near-exact duplicate of Flower Field, with identical shape/character error and same algorithm/API. Flower Field adds an adjacent-double-flower test. Preserve this source as alternate practice link on Flower Field rather than duplicate a numbered assignment; not broken.
- **Octal** — [python-curriculum/exercises/practice/octal/.docs/instructions.md](python-curriculum/exercises/practice/octal/.docs/instructions.md) — Full task, starter and tests reviewed. Quarantine: instructions explicitly require treating invalid input as octal0, while tests require ValueError for 8, carrot and6789. Deprecated and redundant with stronger All Your Base; reference passes tests but cannot satisfy contradictory invalid-input prose.
- **Point Mutations** — [python-curriculum/exercises/practice/point-mutations/.docs/instructions.md](python-curriculum/exercises/practice/point-mutations/.docs/instructions.md) — Full brief, starter and all tests reviewed. Explicitly replaced by Hamming. Prose promises equal-length inputs and defines Hamming distance only there, but tests require ignoring unequal trailing lengths. Exclude contradictory legacy duplicate; retain verified Hamming with explicit equal-length validation.

## Integration rules for Gauntlex

1. Treat the sequence number as curriculum order, not the source repository's alphabetical order.
2. Preserve authored instructions and starter files. Strip worked solutions, exemplar files, answer sections and hidden-test expectations from learner payloads.
3. Make each phase sequential by default. A task unlocks only after the preceding assigned task passes its server-owned evaluation and audit.
4. Keep project and challenge tasks in the same Python course progress ledger; do not mix them with Go or TypeScript progress.
5. Use the pinned source path as the stable import identity. Titles are display labels and may repeat across sources.
6. Keep the withheld list out of the learner path unless its recorded issue is resolved and reviewed again.

## Verification footer

- Assigned sequence range: **1–694**.
- Unique primary paths: **702/702**.
- Total inspected primary bytes: **6,762,570**.
- SHA-256 fingerprints captured during generation: **702 distinct contents**.
