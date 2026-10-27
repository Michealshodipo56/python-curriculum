"""Materialize explicitly reviewed question decisions, not inferred task topics.

The chapter keys locate source files only. Each decision below was written
after reading its complete exercise block. Unlisted chapters stay unreviewed.
"""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[1]
# objective | concepts | required skills | stage | disposition | review note
D = {}
D["readme.md"] = [
"Check the installed Python interpreter version.|terminal;interpreter version|terminal basics|setup|Practice|Version check complements installation; do not confuse a shell command with Python syntax.",
"Evaluate seven arithmetic operations on 3 and 4 in the interactive interpreter.|REPL;arithmetic operators|running Python;numeric values|numbers|Practice|All seven operator subparts retained as one source question.",
"Evaluate personal and course-description string literals in the REPL.|strings;REPL|running Python|string-basics|Practice|No print requirement in the interactive shell.",
"Inspect numeric, complex, list and personal-text types with type().|type inspection;numeric types;list literals|running Python;strings;numbers;list literals|type-inspection|Practice|List type example needs prior list-literal preview; source has no tests.",
"Create and run a Python script repeating the earlier REPL arithmetic, text and type checks.|scripts;print;directories;terminal navigation|terminal basics;REPL;arithmetic;strings;type inspection|scripts|Practice|This depends on all four preceding source prompts, not just Hello World.",
"Construct examples of every listed built-in numeric and collection type.|type literals;bool;list;tuple;set;dict|numeric types;strings;booleans;lists;tuples;sets;dictionaries|collections-review|Practice|Move after collections despite source calling it Day1. Includes all source-specified types.",
"Calculate Euclidean distance between the supplied two-dimensional points.|coordinate arithmetic;powers;square root|arithmetic;exponentiation|numbers|Practice|Source points (2,3),(10,8); output need not be integer. No class required.",
]
D["02_variables_builtin_functions.md"] = [
"Create the day_2 folder and variables.py script.|directories;scripts|terminal navigation;creating files|setup|Practice|Source workspace naming retained.",
"Add the specified day-description Python comment.|comments|editing scripts|syntax|Practice|A comment does not print output.",
"Declare and assign a first-name variable.|assignment;strings|strings;variables|variables|Practice|Part of cumulative variables.py sequence.",
"Declare and assign a last-name variable.|assignment;strings|strings;variables|variables|Practice|Optional repetition of first-name assignment.",
"Declare and assign a full-name variable.|assignment;strings|strings;variables|variables|Practice|Source does not require deriving it by concatenation.",
"Declare and assign a country variable.|assignment;strings|strings;variables|variables|Practice|Optional assignment repetition.",
"Declare and assign a city variable.|assignment;strings|strings;variables|variables|Practice|Optional assignment repetition.",
"Declare and assign an age variable.|assignment;integers|integers;variables|variables|Practice|Keep personal-data examples learner-chosen.",
"Declare and assign a year variable.|assignment;integers|integers;variables|variables|Practice|Optional numeric assignment repetition.",
"Declare and assign an is_married flag.|booleans;assignment|booleans;variables|logic|Practice|Learner may choose fictional example values.",
"Declare and assign an is_true flag.|booleans;assignment|booleans;variables|logic|Practice|Optional flag assignment repetition.",
"Declare and assign an is_light_on flag.|booleans;assignment|booleans;variables|logic|Practice|Optional flag assignment repetition.",
"Assign multiple variables in one line.|multiple assignment;unpacking|variables;assignment|unpacking|Practice|This requires multiple assignment before completion.",
"Inspect the types of every variable declared in the preceding source exercise set.|type;variable inspection|variables;booleans;strings;numbers|type-inspection|Practice|Depends on declared source variables, not an isolated prompt.",
"Measure the first-name string length.|len;strings|variables;strings|strings|Practice|Reuses first_name.",
"Compare the first-name and last-name lengths.|len;comparisons|strings;comparison operators|logic|Practice|Move after numeric comparisons.",
"Assign the supplied operands to num_one and num_two.|assignment;integers|variables;integers|variables|Practice|Defines shared inputs for the following seven arithmetic prompts.",
"Add the two named operands and store total.|addition;assignment|numeric variables|numbers|Practice|Uses operands from preceding source item.",
"Subtract num_two from num_one and store diff.|subtraction;assignment|numeric variables|numbers|Practice|Operand order matters.",
"Multiply the two named operands and store product.|multiplication;assignment|numeric variables|numbers|Practice|Same source operands, distinct operator practice.",
"Divide num_one by num_two and store division.|true division;floats|numeric variables;division|numbers|Practice|Python true division yields float.",
"Calculate num_two modulo num_one and store remainder.|modulo;assignment|numeric variables;modulo|numbers|Practice|Source reverses operands compared with surrounding operations.",
"Raise num_one to num_two and store exp.|exponentiation;assignment|numeric variables;exponentiation|numbers|Practice|Uses **, not ^.",
"Calculate floor division of num_one by num_two.|floor division;assignment|numeric variables;floor division|numbers|Practice|Floor division is not generally truncation for negative values.",
"Calculate circle area and circumference for a fixed radius and then an entered radius.|input;numeric conversion;circle formulas|arithmetic;input;float conversion|input|Practice|Keep all three nested requirements. Fixed radius30 then user input; source does not prescribe pi precision here.",
"Collect first name, last name, country and age with input() into named variables.|input;assignment|variables;strings;input|input|Practice|Input returns text; source does not explicitly demand converting age.",
"Use help('keywords') to inspect Python reserved words.|help;keywords;interactive exploration|running Python;function calls|syntax|Practice|No package installation needed.",
]
D["03_operators.md"] = [
"Assign an integer age value.|integers;assignment|variables;integers|variables|Practice|Overlaps earlier age-variable assignment; optional repetition.",
"Assign a floating-point height value.|float;assignment|variables;floats|variables|Practice|Extends assignment practice to float.",
"Assign a complex-number value.|complex literals;assignment|variables;complex number literals|numeric-types|Practice|Python imaginary suffix j, not bare mathematical i.",
"Read triangle base and height and calculate its area.|input;float conversion;area|input;numeric conversion;arithmetic|input|Practice|Source example b20,h10 yields100.",
"Read three triangle sides and calculate perimeter.|input;numeric conversion;sum|input;numeric conversion;arithmetic|input|Practice|No triangle-inequality validation requested by source.",
"Read rectangle dimensions and calculate area and perimeter.|input;formulas;arithmetic|input;numeric conversion;arithmetic|input|Practice|Two outputs from same inputs.",
"Read a circle radius and calculate area and circumference using pi3.14.|input;arithmetic;formula reuse|input;numeric conversion;arithmetic|input|Practice|Near-repeat of Day2 circle work; retain optional variant with explicit pi.",
"Determine slope and both intercepts of y=2x-2.|linear equations;arithmetic|arithmetic;coordinate geometry|numbers|Practice|Mathematical interpretation prerequisite must be explained before task.",
"Calculate slope and Euclidean distance between (2,2) and (6,10).|coordinate differences;division;square root|arithmetic;coordinate geometry;exponentiation|numbers|Practice|Source slope notation omits parentheses: interpret (y2-y1)/(x2-x1), not y2-y1/x2-x1.",
"Compare the slopes calculated in the preceding two questions.|comparisons;numeric values|comparison operators;linear equations|logic|Practice|Retain dependency on source items8 and9.",
"Evaluate the supplied quadratic at several x values and identify its zero.|exponentiation;expressions;mathematical reasoning|arithmetic;variables;exponentiation|numbers|Practice|Source x^2 means mathematical square; Python uses **, whereas ^ is XOR. Manual evaluations allowed before loops.",
"Compare the lengths of python and dragon to produce a false result.|len;comparisons|strings;comparison operators|logic|Practice|Both words have six characters.",
"Combine two substring-membership checks with and.|membership;boolean conjunction|strings;in;and|logic|Practice|Source asks whether on occurs in both words.",
"Test whether jargon occurs in the supplied sentence.|substring membership|strings;in|logic|Practice|Use actual sentence from source.",
"Evaluate the negated claim that on occurs in neither python nor dragon.|negation;membership;boolean reasoning|strings;in;not;and|logic|Practice|Source wording is ambiguous and factually false; treat as evaluating a claim, not forcing True. Clarify before assigning.",
"Convert the length of python to float and then to text.|len;type conversion|strings;len;float;str|conversion|Practice|Do not convert the letters themselves to a number.",
"Determine evenness by checking remainder after division by two.|modulo;comparison|integers;modulo;comparison operators|logic|Practice|No conditional or function required by this prompt.",
"Compare 7//3 with int(2.7).|floor division;numeric conversion;comparison|floor division;int conversion;comparisons|logic|Practice|Positive operands agree; do not generalize truncation to negatives.",
"Compare the types of a numeric string and an integer.|type;type comparison|strings;integers;type inspection;comparisons|type-inspection|Practice|Values look similar but types differ.",
"Investigate int('9.8') and whether it can be compared with10.|conversion errors;ValueError|int conversion;reading exceptions|errors|Practice|Direct int('9.8') raises ValueError, so ordinary comparison never runs. Source phrasing presumes a value; flag and explain rather than claim it equals10.",
"Read hours and hourly rate and calculate weekly earnings.|input;float conversion;multiplication|input;numeric conversion;arithmetic|input|Practice|Straight multiplication only; overtime policy not requested.",
"Read years lived and convert to seconds using the source's365-day-year convention.|input;unit conversion;multiplication|input;numeric conversion;arithmetic|input|Practice|Source hundred-year wording unclear, example computes entered years lived, not remaining life. State convention; no calendar/leap-year inference.",
"Display the supplied five-row number, constant, square and cube table.|formatted output;exponentiation|print;arithmetic;string formatting|formatting|Practice|Can print explicit rows; loop-based refinement optional after loops. Preserve all five columns.",
]

# Shared defaults only express previously reviewed skill groups; objectives and
# exceptions remain explicit per source question.
def group(filename, stage, requires, rows):
    decisions = []
    for row in rows:
        parts = row.split("|")
        objective, concepts = parts[:2]
        note = parts[2] if len(parts) > 2 else "Full numbered source prompt reviewed; optional focused reinforcement."
        decisions.append("|".join([objective, concepts, requires, stage, "Practice", note]))
    D[filename] = decisions

group("04_strings.md", "strings", "strings;variables;string methods;indexing;slicing;lists;format specifications", [
"Concatenate four words into Thirty Days Of Python.|concatenation;spacing",
"Concatenate three words into Coding For All.|concatenation;spacing|Near-identical concatenation repetition; preserve optional.",
"Assign Coding For All to company.|assignment;strings|Defines shared company variable for following prompts.",
"Print the company string.|print;variables",
"Print the length of company.|len;print",
"Convert company text to uppercase.|upper;case conversion",
"Convert company text to lowercase.|lower;case conversion",
"Compare capitalize, title and swapcase on the given text.|capitalize;title;swapcase",
"Slice the first word out of Coding For All.|slicing|Cut out is ambiguous between extract and remove; source has no test. State intended slice output when assigning.",
"Check for Coding with index, find or another string-search method.|substring search;find;index|Explain index raises on absence while find returns -1; supplied target is present.",
"Replace Coding with Python in the supplied phrase.|replace;case sensitivity|Prompt spells coding lowercase but source phrase uses Coding. Use exact source-case substring; flag mismatch.",
"Replace Everyone with All in Python for Everyone.|replace",
"Split Coding For All into space-separated words.|split;lists",
"Split the supplied company-name text at commas.|split;delimiters|Source does not explicitly require trimming the following spaces.",
"Retrieve the first character by index0.|indexing",
"Determine the final valid index of the phrase.|len;index bounds|Question asks index, not final character; avoid returning character by mistake.",
"Retrieve the character at index10.|indexing",
"Build the acronym for Python For Everyone.|initials;split;join|Fixed phrase may use explicit indices; general algorithm optional after loops.",
"Build the acronym for Coding For All.|initials;split;join|Overlaps previous fixed-phrase acronym; optional practice before general Exercism Acronym.",
"Find the first C position with index().|index;substring search",
"Find the first F position with index().|index;substring search",
"Find the final l position with rfind().|rfind;reverse search",
"Find the first because occurrence in the supplied sentence.|find;index;substring search",
"Find the final because occurrence using rindex().|rindex;reverse search",
"Extract the repeated because because because substring by slicing.|slicing;substring bounds",
"Find the first because occurrence in the repeated-conjunction sentence.|find;index|Exact repetition of earlier same-chapter item23; mark as duplicate alternate on that item instead of an additional numbered task.",
"Extract the repeated because because because phrase.|slicing|Exact repetition of same-chapter item25; mark as duplicate alternate rather than another numbered task.",
"Test whether Coding For All begins with Coding.|startswith;boolean result",
"Test whether Coding For All ends with lowercase coding.|endswith;case sensitivity|Result false; source asks case-sensitive substring.",
"Strip leading and trailing spaces from the supplied padded phrase.|strip;whitespace|Source displays HTML nonbreaking-space entities. Clarify use actual spaces, not literal ampersand-n-b-s-p text.",
"Check which of the two supplied names is a valid identifier.|isidentifier;names|30DaysOfPython is tested as a string, not parsed as an invalid variable assignment.",
"Join the given library names with hash-and-space separators.|join;lists",
"Print the supplied two sentences separated by a newline escape.|escape sequences;print",
"Print the supplied name, age, country and city table using tabs.|tab escape;formatted text",
"Format the circle-radius and calculated-area sentence.|string formatting;arithmetic",
"Format all seven arithmetic results with the displayed numeric precision.|format specifications;operators|Division8/6 displays1.33; plain float interpolation does not match source example.",
])

group("05_lists.md", "lists", "lists;indexing;slicing;list methods;strings;sorting;arithmetic", [
"Declare an empty list.|list construction",
"Declare a list with more than five entries.|list literals",
"Find the length of the created list.|len|Depends on list defined in prior source question.",
"Retrieve the first, middle and last list entries.|indexing;len|For even-length learner-created lists, middle convention unspecified; explain choice rather than invent a failing contract.",
"Create a heterogeneous personal-data list.|mixed types;list literals",
"Create the specified seven-company list.|list literals|Defines it_companies for subsequent cumulative operations.",
"Print the company list.|print;list representation",
"Print the company count.|len",
"Print first, middle and last companies.|indexing;len",
"Modify one company and print the list.|item assignment;mutation",
"Append another company.|append;mutation",
"Insert a company in the middle.|insert;indexing",
"Uppercase one company name other than IBM.|string methods;item assignment",
"Join company names using the specified separator.|join;strings|Source separator includes an HTML nbsp entity; use rendered semicolon/space intent and document it.",
"Check company membership.|in;boolean result",
"Sort companies in place.|sort;mutation",
"Reverse the sorted list to descending order.|reverse;sort|Depends on prior ascending sort; reverse alone is not a general descending sort.",
"Slice the first three companies.|slicing",
"Slice the final three companies.|negative slicing",
"Slice the middle company or pair of middle companies.|slicing;len;parity|Length changes from earlier append/insert affect middle indices.",
"Remove the first company.|pop;del",
"Remove the middle company or pair.|slicing;del;len",
"Remove the last company.|pop;negative indexing",
"Clear the company list.|clear;mutation",
"Delete the company-list variable.|del;names|After deletion the name cannot be reused without reinitialization; keep cumulative sequence consistent.",
"Concatenate the supplied frontend and backend technology lists.|list concatenation",
"Copy the joined technology list and insert Python and SQL after Redux.|copy;slice insertion;index|Uses preceding source item26. A copy avoids aliasing the original joined list.",
"Analyze sorted ages with extremes, added duplicates, median, mean, range and absolute differences.|sorting;median;mean;range;abs|Composite source question has six subparts; preserve all. Move after statistics formulas and conditionals for odd/even median. Use current list after adding min/max, not original length by accident.",
"Find the middle country or countries in the supplied dataset.|slicing;len;dataset import|Requires locating/importing local countries data, not merely basic lists; dataset file must be verified.",
"Split countries into two halves, giving the first half one extra country when odd.|slicing;parity;integer division|Requires conditional/parity reasoning and local countries dataset.",
"Unpack the first three named countries and collect the remaining names.|starred unpacking;lists|Move after starred assignment rather than the first lists lesson. Keep source's variable name despite its imprecise regional label.",
])

group("06_tuples.md", "tuples", "tuples;lists;indexing;slicing;len;membership;unpacking", [
"Create an empty tuple.|tuple construction",
"Create tuples of sibling names, using imaginary names if preferred.|tuple literals|Following prompt refers to brothers and sisters tuples; create those separate tuples despite singular wording here.",
"Join sibling tuples into siblings.|tuple concatenation",
"Count entries in the siblings tuple.|len",
"Create a family_members tuple by adding parent names to siblings.|tuple concatenation;immutability|Source says modify tuple; construct a new tuple rather than mutate immutable entries.",
"Unpack siblings and parents from family_members.|unpacking;starred assignment|Requires previous cumulative family tuple and arbitrary sibling count handling.",
"Concatenate fruit, vegetable and animal-product tuples.|tuple concatenation",
"Convert food_stuff_tp into a list.|list conversion|Source about is a typo for above.",
"Slice the middle item or pair from the food collection.|slicing;len;parity",
"Slice the first and final three food items.|slicing;negative indexing",
"Delete food_stuff_tp.|del;names",
"Test Estonia and Iceland membership in the supplied Nordic-country tuple.|in;tuples|Keep both bullet subparts in this parent question; geographical labels not separate assignments.",
])

group("07_sets.md", "sets", "sets;set methods;lists;strings;tuples;membership", [
"Measure the supplied company set.|len;sets",
"Add Twitter to the company set.|add;mutation",
"Add several companies at once.|update;iterables",
"Remove one company from the set.|remove;mutation",
"Explain remove versus discard for an absent element.|remove;discard;KeyError|Requires recognizing exceptions before investigating absent-element behavior; no need to write a custom exception.",
"Compute the union of the supplied numeric sets.|union;set algebra",
"Compute their intersection.|intersection;set algebra",
"Check whether A is a subset of B.|issubset",
"Check whether A and B are disjoint.|isdisjoint",
"Compare union in both operand orders.|union;commutativity",
"Compute the symmetric difference.|symmetric_difference",
"Delete the supplied sets.|del;names|Run subsequent independent questions with fresh source fixtures as needed.",
"Compare list length with distinct-age set length.|set conversion;deduplication;len",
"Explain differences among strings, lists, tuples and sets.|mutability;order;uniqueness|Conceptual comparison is a worthwhile retrieval task, not an invented coding challenge.",
"Count distinct words in the supplied sentence using split and set.|split;set;deduplication|Simple whitespace split, not the more demanding punctuation-aware Exercism Word Count.",
])

group("08_dictionaries.md", "dictionaries", "dictionaries;lists;tuples;dictionary methods;type inspection", [
"Create an empty dog dictionary.|dict construction",
"Add the five specified dog attributes.|key assignment;mutation",
"Create a student record with all nine specified keys.|dict literals;mixed values|skills should be a list as clarified by subsequent source prompt.",
"Measure the number of student key-value pairs.|len",
"Retrieve skills and verify its list type.|key lookup;type",
"Add one or two skills to the nested list.|nested mutation;append;extend",
"Convert dictionary keys to a list.|keys;list conversion|keys() returns a view, not a list despite lesson wording; explicit list() needed.",
"Convert dictionary values to a list.|values;list conversion|values() returns a view; do not repeat source's inaccurate list claim.",
"Create a list of key-value tuples.|items;list conversion;tuples|items() returns a view; explicit list conversion meets actual question.",
"Delete one dictionary entry.|del;pop",
"Delete one dictionary variable.|del;names",
])

group("09_conditionals.md", "conditionals", "input;numeric conversion;conditionals;booleans;strings;lists;dictionaries", [
"Read an age and report whether the exercise's18-year driving threshold is met or how many years remain.|input;comparison;if and else|Use source threshold as a programming rule, not a current local licensing statement.",
"Compare entered and reference ages with equal-age and singular/plural difference messages.|nested conditionals;subtraction;string formatting|Source reference my_age must be defined explicitly. Three-way branch plus grammar boundary.",
"Compare two entered numbers and report greater, smaller or equal.|if elif else;numeric comparison",
"Map student scores to the five supplied grade bands.|range conditions;branch order|Boundary values0,59,60,69,70,79,80,89,90,100 deserve checks. Invalid-score behavior unspecified.",
"Map an entered month to the four specified seasons.|membership;branching|Use exercise's stated Northern Hemisphere convention rather than universalizing seasons.",
"Append a fruit only when it is absent and otherwise report an existing entry.|membership;conditional mutation|Reuses supplied fruit list; no loop required.",
"Inspect the supplied nested person record for skills, developer labels and married-in-Finland output.|nested dictionaries;membership;boolean logic;list indexing|Keep all four bullet requirements. Skills-label conditions overlap; document precedence. Requires dictionaries/lists beyond early branching; source's career labels are exercise strings.",
])

group("10_loops.md", "iteration", "for loops;while loops;range;lists;strings;conditionals;arithmetic", [
"Print0 through10 with both for and while loops.|for;while;range|Both implementations required by same question.",
"Count down10 through0 with both loop forms.|range step;while;termination",
"Print a seven-row growing hash triangle.|loops;string repetition",
"Print an eight-by-eight hash grid using nested loops.|nested loops;output layout|Nested loops explicitly required, not a single multiplied full-grid string.",
"Print the supplied0-through10 square multiplication table.|loops;formatting;multiplication",
"Iterate over and print the five supplied technology names.|list iteration;print",
"Print even values from0 through100.|range;modulo;filtering",
"Print odd values from0 through100.|range;modulo;filtering",
"Accumulate and print the sum of0 through100.|accumulators;for loops|Use for loop per source, not only sum(range()).",
"Accumulate separate even and odd sums from0 through100.|partition;accumulators;modulo|Expected sums2550 and2500; include0 correctly.",
"Load the supplied country names and select those containing land.|modules;dataset loading;substring filtering|Requires verified local countries.py and imports; move beyond syntax-only loops.",
"Reverse the given fruit list with a loop.|list construction;indexing;iteration|Loop explicitly required; optional variant reinforcing reversal before algorithmic challenges.",
"Analyze country records for distinct language count, ten most common languages and ten largest populations.|nested iteration;sets;frequencies;sorting|All three numbered subquestions belong to one source dataset assignment. Needs dictionaries, sets, imports and sorting. Spoken means listed-country language frequency, not speaker population unless dataset supports it.",
])

group("11_functions.md", "functions-practice", "functions;parameters;return;lists;loops;conditionals;strings;arithmetic", [
"Return the sum of two function arguments.|parameters;return;addition",
"Implement a radius-to-circle-area function.|parameters;return;arithmetic|Overlapping circle tasks progress from scripts to reusable function.",
"Sum arbitrary numeric arguments and provide feedback for nonnumeric entries.|variadic arguments;type checks;validation|Requires *args and numeric-type decisions beyond introductory two-parameter functions. Source leaves feedback format unspecified; document it.",
"Convert Celsius to Fahrenheit through a function.|arithmetic;return|Source proposed name contains a hyphen; valid Python identifier convert_celsius_to_fahrenheit must be used and noted.",
"Return the exercise's season for a month argument.|membership;branching;return|Source check-season has illegal identifier hyphen; use check_season explicitly.",
"Return the slope of a linear equation from a documented input representation.|parameters;linear equations|No exact signature or vertical-line behavior supplied. Teach slope and define input contract before assigning; do not invent source tests.",
"Compute the solution set of a quadratic equation.|discriminant;square root;branching|Move after mathematical prerequisites, numeric domains and documented no-real-root/degenerate behavior. Source gives no test or precise input-domain contract; optional challenge.",
"Print each entry of a function-supplied list.|parameters;iteration;print",
"Return a list reversed using loops.|return;iteration;list construction|Source explicitly requires loops; inputs include numeric and string lists.",
"Return capitalized versions of list entries.|string methods;iteration;return",
"Return a list with the supplied new item appended.|list mutation;return|In-place versus copy not specified by tests; state chosen contract instead of requiring one silently.",
"Return a list with the supplied item removed.|list mutation;return|Missing-item policy unspecified; provided examples contain item.",
"Return the inclusive sum of integers through the given bound.|range;accumulation|Source examples5=>15 and100=>5050 establish inclusive endpoint.",
"Return the sum of odd integers through a bound.|modulo;filtering;accumulation",
"Return the sum of even integers through a bound.|modulo;filtering;accumulation",
"Report counts of even and odd integers from zero through the positive bound.|range;counting;modulo|Example100 includes51 evens and50 odds, so zero is included. Wording in the number does not mean decimal digits.",
"Return the factorial of a whole-number argument.|accumulation;factorial;base case|Recursion not mandated. Explain0! before task; negative-input contract unspecified.",
"Check whether a supplied value is empty.|truthiness;len;type contracts|Define supported collection/string types; source does not specify treatment of numeric0 or None.",
"Implement separate mean, median, mode, range, variance and standard-deviation functions for lists.|statistics;sorting;frequency;decomposition|Composite six-function assignment belongs after statistics. Specify sample/population variance convention because source lacks it; verify against statistics library with matching convention.",
"Print a named greeting with Guest as the default argument.|default parameters;string formatting|Print-based default greeting, distinct from return-based Exercism Two Fer.",
"Print names and values of arbitrary keyword arguments.|kwargs;dictionary iteration|Requires **kwargs; preserve both supplied usage examples.",
"Write a primality predicate.|trial division;boolean return|Requires prime definition, loop bounds and efficient divisor checking; optional preparation for larger prime algorithms.",
"Check that all list items are unique.|sets;membership;duplicates|Requires set/membership knowledge beyond function syntax; hashability domain needs documentation if set-based.",
"Check that list entries all have the same data type.|type;iteration;all|Empty-list convention unspecified; document it.",
"Check whether a candidate name is a valid Python variable identifier.|isidentifier;keywords;validation|Identifiers that are reserved keywords cannot be variable names. Requires keyword knowledge in addition to str.isidentifier.",
"Create reusable ranked-language and ranked-population functions over the supplied country records.|dataset import;aggregation;sorting;parameters|Keep both bullet subfunctions and top10/top20 requirement. Reuses prior loop analysis but adds reusable ranking/count parameter. Validate hyphenated local source path before import.",
])

group("12_modules.md", "randomness", "functions;modules;random;string module;loops;lists;input;numeric conversion", [
"Generate a six-character random user ID.|random selection;string construction|Source example alphanumeric; exact alphabet underspecified, later mixed-case examples clarify useful choice. Not an authentication-token task.",
"Read desired ID length and count, then generate that many random IDs.|input;numeric conversion;nested iteration|No parameters allowed by source; two input calls required. Output print/return format not fully specified.",
"Generate a formatted RGB color with three integer components from0 through255.|randint;formatting|Return valid rgb(r,g,b) text matching first source example.",
"Return a requested collection of six-digit hexadecimal color strings.|hex digits;random choice;lists|Requires hexadecimal representation. Source omits exact count signature; define documented argument consistent with generate_colors below.",
"Return a requested collection of RGB color strings.|function reuse;lists|Build on rgb_color_gen instead of duplicating generation.",
"Dispatch color generation by hexa/rgb selector and requested count.|dispatch;function composition;lists|Some supplied RGB example strings omit closing parenthesis; flag typo and retain valid RGB notation. Includes count1 and count3.",
"Return a shuffled version of a supplied list.|random shuffle;copy;mutation|Source does not specify whether original may mutate; document behavior. random.shuffle returns None, so return the list explicitly when using it.",
"Return seven unique random integers drawn from0 through9.|sampling without replacement;sets;lists|Uniqueness explicitly required; random.sample is suitable after module lesson. No duplicate-retry guarantee inferred.",
])

group("13_list_comprehension.md", "comprehensions", "functions;lists;tuples;dictionaries;loops;comprehensions;strings;lambdas;arithmetic", [
"Filter the supplied list to negative numbers and zero using a comprehension.|conditional comprehensions;comparison|Comprehension explicitly required.",
"Flatten the supplied nested numeric list with a comprehension.|nested comprehensions|Wording says lists of lists of lists, but actual fixture is two levels. Assign supplied fixture; do not require arbitrary recursive depth.",
"Generate the displayed tuples of n, constant1 and powers through n**5.|comprehensions;tuples;exponentiation|Keep n0 through10. Seven tuple fields include n plus powers0..5; source's zero row uses constant1 for0**0.",
"Transform nested country/city pairs into uppercase names and three-letter country prefixes.|nested iteration;slicing;upper|Output three-element lists; flatten exactly the supplied nesting.",
"Transform nested country/city pairs into a list of dictionaries.|nested comprehension;dictionary literals|Uppercase names and exact country/city keys from supplied output.",
"Flatten nested name pairs into full-name strings.|unpacking;string concatenation|Expected first surname Yetaeyeh differs from input Yetayeh; preserve input spelling and record source typo.",
"Express slope or y-intercept calculation as a lambda with documented arguments.|lambda;linear equations|Mathematical/input contract left open by source; optional challenge following slope instruction, not a hidden fixed signature.",
])

group("14_higher_order_functions.md", "higher-order-functions", "functions;first-class functions;closures;decorators;map;filter;reduce;lists;loops;strings", [
"Explain how map, filter and reduce differ.|mapping;filtering;folding|Retrieval task: distinguish lazy map/filter iterators from single reduced result.",
"Explain higher-order functions, closures and decorators.|first-class functions;scope;wrappers|These overlap rather than being mutually exclusive categories.",
"Define named callback functions before using them with map, filter or reduce.|named functions;callbacks|Source calls it call function; interpret through immediately preceding complete examples. Specify callback input/output contract.",
"Print each supplied country using a for loop.|iteration;print|Simple optional reinforcement despite placement in advanced source chapter.",
"Print each supplied name with a for loop.|iteration;print|Near-identical list iteration practice; optional.",
"Print each supplied number with a for loop.|iteration;print|Optional repetition of earlier loop tasks; no higher-order prerequisite actually needed.",
"Map country names to uppercase and materialize the result list.|map;upper;list",
"Map numbers to their squares and materialize a list.|map;lambda;exponentiation",
"Map names to uppercase.|map;upper|Overlaps country uppercase mapping; optional transfer practice.",
"Use filter to select country names containing land.|filter;substring predicate|Source filter out wording ambiguous; here select matching predicate as lesson examples do. Document predicate explicitly.",
"Use filter to select country names of exactly six characters.|filter;len;comparison",
"Use filter to select country names at least six characters long.|filter;len;comparison",
"Use filter to select country names starting with E.|filter;startswith",
"Compose at least two mapping, filtering or reducing operations.|iterator composition;higher-order functions|Source arr.map(...).filter(...).reduce(...) is JavaScript-style and invalid Python list API; express existing task via nested Python functions or named intermediate iterators.",
"Return only string entries from a supplied heterogeneous list.|type checks;filter;list|Named get_string_lists function; requires explicit supported input iterable.",
"Sum supplied numbers with functools.reduce.|reduce;accumulator|Must import reduce; no need to forbid built-in sum in other tasks.",
"Reduce country names into the exact punctuated North-European-country sentence.|reduce;string joining;separator logic|Final comma/and boundary required by source sentence; not just plain concatenation.",
"Categorize country names by a supplied or documented substring pattern.|functions;filter;dataset import|Source countries.js is a wrong-language filename; verify local Python data. land/ia/island/stan examples retained, exact signature not given.",
"Count country names by initial letter into a dictionary.|dictionary frequency;strings;iteration|Needs full country dataset and dictionary aggregation, not only higher-order syntax.",
"Return the first ten countries from the full dataset.|slicing;dataset import|Source countries.js typo; actual local Python resource needs verification.",
"Return the final ten countries from the full dataset.|negative slicing;dataset import",
"Sort country records by name, capital and population and report ranked language frequencies and population.|sort keys;aggregation;datasets|All three bullet requirements preserved. Reuses earlier country analyses as optional integrated extension; language ranking by locations is not speaker counts.",
])
group("15_python_type_errors.md", "errors", "REPL;variables;strings;lists;dictionaries;modules;numeric conversion", [
"Reproduce every demonstrated error in the REPL, identify its category and inspect the shown fixes.|SyntaxError;NameError;IndexError;ModuleNotFoundError;AttributeError;KeyError;TypeError;ImportError;ValueError;ZeroDivisionError|Entire chapter read. Includes ten error categories despite title Type Errors. Transcript prompts/banners are not executable Python. Error wording may vary across Python versions; match category and cause rather than old transcript caret layout.",
])
group("16_python_datetime.md", "dates", "modules;datetime objects;date objects;timedelta;strings;formatting", [
"Inspect the current day, month, year, hour, minute and timestamp.|datetime.now;attributes;timestamp|Use current runtime values, not static2021 output comments. Naive timestamp conversion uses local timezone.",
"Format current datetime with the specified month/day/year and time format.|strftime;format codes",
"Parse the fixed string5 December,2019 into a datetime object.|strptime;date parsing|Historical string is test input, not a claim about today's date. Source says time but example returns datetime.",
"Calculate the duration from now to the next New Year.|datetime;timedelta;year boundary|Use upcoming January1, not static2020 date from lesson.",
"Calculate elapsed time since1 January1970.|datetime subtraction;epoch;timezone|Explain timezone consistency before subtraction; avoid mixing aware and naive objects. Seconds convention should match UTC epoch if comparing timestamps.",
"Describe practical uses of datetime such as activity timestamps and time-series work.|application reasoning;timestamps|Conceptual reflection, not an invented application build. Listed examples do not require pandas or a blog framework yet.",
])
group("17_exception_handling.md", "unpacking", "lists;starred assignment;unpacking", [
"Unpack the first five country names into a grouped list and the last two into es and ru.|starred assignment;sequence unpacking|Entire chapter read. Actual sole exercise tests unpacking, not exception handling despite chapter title; place by content. Source uses nordic_countries for first five values and separate final names.",
])

group("18_regular_expressions.md", "regular-expressions", "functions;strings;regular expressions;dictionaries;frequency counts;sorting;numeric conversion", [
"Find the most frequent paragraph word and produce ranked word counts.|tokenization;frequency;sorting|Full exercise block read. Source paragraph literal lacks closing quote; copy actual text with valid string syntax. Display counts keep case (I, If, if separate). First item indentation inconsistent with second; extraction corrected to retain both.",
"Extract signed particle positions from prose and calculate farthest separation.|regex groups;signed integers;min;max|Expected sorted_points includes a duplicate-1 and extraneous2 absent prose. Use actual extracted positions; farthest distance20 unchanged.",
"Write a pattern checking Python variable-name syntax.|regex anchors;identifier validation|Examples cover ASCII names; full valid-variable semantics also exclude keywords and may allow Unicode. State ASCII exercise scope versus Python-wide identifier validity and check keywords if claiming full validity.",
"Clean embedded noise characters from text and report its three most frequent words.|re.sub;tokenization;frequency;sorting|Preserve clean_text and most_frequent_words subparts. Expected counts preserve case and specify a tie ordering. Remove noise within words rather than split tea@cher into fragments.",
])
group("19_file_handling.md", "file-processing", "functions;files;context managers;strings;JSON;CSV;regular expressions;dictionaries;sorting", [
"Write a line-and-word counting function and apply it to all four supplied speech files.|file reading;splitlines;word counting|Preserve all four nested datasets. Definition of word/blank lines should be documented. Source melina filename needs existence check.",
"Load country JSON and return a requested number of most widespread listed languages.|JSON;aggregation;ranked output|Examples place positional10 after keyword filename, invalid Python call syntax. Example top10 shows11 entries. Specify valid call and requested count; historic dataset counts, not current world-language facts.",
"Load country JSON and return ranked country/population records for top10 or top3.|JSON;sorting;record transformation|Same invalid keyword-before-positional call example. Treat historical population values as fixture data; do not relabel as current statistics.",
"Extract incoming email addresses from the supplied mail-exchange dataset.|file parsing;regular expressions;headers|Prompt email_exchange_big.txt differs from actual candidate email_exchanges_big.txt; verify local spelling. Extract incoming-header semantics rather than every email-looking token. Do not publish raw addresses in audit evidence.",
"Return descending word-frequency tuples from a text string or file with a requested top count.|tokenization;file IO;frequency;sorting|Source sample.txt may be illustrative or missing; verify. Distinguish text from path through documented interface; no exact tokenizer/tie policy specified.",
"Apply the word-frequency function to all four speech transcripts.|function reuse;batch analysis|Source alternates find_most_common_words and find_most_frequent_words; explicitly reuse documented actual function. All four files retained in same parent assignment.",
"Build text similarity analysis with cleaning, supplied stop-word removal and a documented similarity metric.|text preprocessing;sets;similarity;decomposition|Actual source mini-project; metric unspecified, so learner chooses and documents rather than pretend exact expected score. Compare provided Michelle/Melina transcripts. Requires stop_words.py verification.",
"Find ten most repeated words in the supplied Romeo and Juliet text.|file processing;tokenization;frequency|Overlaps earlier word counting but literary dataset transfer retained optional.",
"Analyze Hacker News CSV for Python, JavaScript variants and Java excluding JavaScript.|CSV;case handling;boolean filtering|Preserve all three subcounts. Clarify whether lines means CSV records or raw lines containing multiline fields; source lacks tests. Do not mix Java substring into JavaScript count.",
])
group("20_python_package_manager.md", "external-data", "virtual environments;packages;HTTP requests;JSON;files;statistics;HTML;BeautifulSoup;sorting", [
"Fetch the specified Gutenberg text and report its ten most frequent words.|HTTP;text tokenization;frequency|Actual task content is remote text analysis, not package installation alone. Duplicates local Romeo analysis with added HTTP dependency. Verify original URL; do not silently replace inaccessible source.",
"Analyze cat-breed API weight ranges, lifespan ranges and country/breed frequencies.|HTTP;JSON;range parsing;statistics|All three nested outputs retained. Metric weight/lifespan often strings containing ranges; aggregation convention unspecified, must document choice. API availability/key needs verification; do not claim current external run without it.",
"Analyze country API for ten largest countries, language frequency and distinct language count.|HTTP;JSON;aggregation;sorting|Original restcountries.eu endpoint must be verified. Largest could mean area or population; source ambiguous, choose area with explicit documented interpretation. Language listed-country frequency differs from speaker counts.",
"Fetch and inspect the UCI dataset listing, using BeautifulSoup if needed.|HTTP;HTML parsing;selectors|Source says UCL but URL is UCI. Broad read-content task; overlaps later structured UCI JSON export, retain preparatory/alternate resource rather than duplicate the entire project.",
])
group("21_classes_and_objects.md", "classes-statistics", "classes;methods;lists;dictionaries;sets;tuples;statistics;sorting;formatting", [
"Build a Statistics class implementing central tendency, variability, extremes, count, percentiles, frequencies and a summary report.|classes;statistical methods;aggregation;formatting|Full actual assignment and sample outputs read. data instance creation omitted. Mean29.76 rounds30; shown variance17.5 follows population convention despite sample wording. Percentile required in prose without expected example; document method. mode standalone dict and describe tuple disagree, so explain display/API choice.",
"Build PersonAccount with described income/expense entries, addition methods, totals, balance and account information.|classes;state;record collections;aggregation|Actual source project. Incomes/expenses described as sets of amount/description entries; tuples can satisfy hashability but identical entries deduplicate. State chosen representation and duplicate policy. No invented storage/API requirements.",
])
group("22_web_scraping.md", "web-scraping", "HTTP;requests;HTML;CSS selectors;BeautifulSoup;JSON;file writing;exceptions", [
"Scrape Boston University facts/statistics and save structured JSON.|HTML extraction;JSON export|Full chapter read. Original URL live availability and actual page structure require verification; retain source attribution and report any block. Scope extraction to source task.",
"Extract the UCI dataset table and serialize it as JSON.|table parsing;headers;JSON|Source example selector targets legacy cellpadding3 table and assumes index0; modern page may differ. Builds on package-manager UCI inspection rather than treating them as unrelated courses.",
"Extract the US-presidents table into JSON despite its irregular row structure.|HTML tables;rowspan;data normalization;JSON|Full brief read. Actual task external page, no local table fixture verified yet. Needs robust multirow handling; not a Python syntax beginner exercise.",
])
group("23_virtual_environment.md", "environments", "terminal navigation;Python installation;packages;virtual environments", [
"Create a project-local environment, activate it, install Flask, inspect packages and deactivate.|venv;activation;pip;dependency isolation;gitignore|Full chapter read. Move before first third-party install. Old freeze output is illustrative, not required pins. Git Bash activation example malformed; supply shell-appropriate instruction. Built-in venv avoids prerequisite virtualenv install on Windows. Empty __init__ package claims elsewhere do not expose every function automatically.",
])

group("24_statistics.md", "numpy", "NumPy;array shapes;broadcasting;statistics;linear algebra;Matplotlib;Seaborn;SciPy;notebooks", [
"Reproduce the chapter's array construction, vectorized arithmetic, slicing, random sampling, statistics, linear algebra and plotting examples.|NumPy;reshaping;stacking;random distributions;axes;matrix multiplication;plots|Full chapter read in three ranges. Near-duplicate numpy.md fixes the missing array-closing parenthesis, so select that variant as main optional lab and attach this as alternate. Both contain undefined numpy_float_list, output mislabeled as Python and legacy plotting calls; not a clean core introduction.",
])
group("25_pandas.md", "pandas", "packages;pandas;CSV;Series;DataFrames;boolean indexing;strings", [
"Load the supplied Hacker News CSV into a DataFrame.|read_csv;DataFrames|Full lesson teaching text/code read; rendered HTML example tables summarized separately. Verify local fixture and case-sensitive title-column name.",
"Inspect the first five DataFrame rows.|head|Depends on loaded Hacker News DataFrame.",
"Inspect the last five DataFrame rows.|tail|Same dataset, contrasting head/tail exploration.",
"Extract the title column as a pandas Series.|column selection;Series|Use actual CSV header spelling from fixture, not guessed Title/title casing.",
"Report table shape, filter Python and JavaScript titles and explore the results.|shape;str.contains;boolean indexing;exploratory analysis|Keep all three trailing bullets as part of source parent question. Document case sensitivity and missing-title handling; compare with earlier CSV-reader analysis rather than count as unrelated data.",
])
group("26_python_web.md", "flask-projects", "functions;decorators;HTTP;Flask;Jinja;HTML;CSS;forms;text processing;virtual environments;Git", [
"Complete the Flask Text Analyzer application using the supplied routing, templates, navigation, static assets and form workflow.|Flask;template inheritance;forms;redirects;text analysis|Entire chapter read. Form action hardcodes author's remote deployment rather than local route; result template and text analysis implementation left to learner. Debug-server public deployment instructions and claimed free hosting are legacy, not a production model. Demo URL availability must be reported. Preserve as optional project after stronger verified backend work.",
])
group("28_API.md", "HTTP", "terminal;web basics;JSON", [
"Read the supplied explanation of APIs, HTTP requests/responses, headers, bodies and CRUD methods.|HTTP;status codes;headers;REST;CRUD|Entire chapter read. Move before HTTP clients and Flask. Statement that server always closes after each response ignores persistent connections; response format examples describe HTTP/1.x. API is not necessarily an SLA. No account signup required for reading.",
])
group("29_building_API.md", "backend-projects", "Flask;HTTP;JSON;MongoDB;PyMongo;ObjectId;validation;exceptions;API testing;environment configuration", [
"Implement the supplied student-record CRUD API with Flask and MongoDB.|routes;GET;POST;PUT;DELETE;document persistence|Entire source chapter and all inline code read. Severely incomplete baseline: undefined student in GET, missing request import, bodyless duplicate update_student definitions, duplicate PUT endpoint names, None responses, update_one lacking $set, hardcoded URI. Retain only annotated optional repair challenge after stronger API project; do not claim snippets work. Live demo unverified pending URL check.",
])
group("numpy.md", "numpy", "NumPy;array shapes;broadcasting;statistics;linear algebra;Matplotlib;Seaborn;SciPy;notebooks", [
"Reproduce the supplied NumPy, statistics, linear-algebra and visualization examples while identifying documented source defects.|NumPy;vectorization;reshaping;sampling;statistics;matrix products;plots|Shared tutorial body read through Day24 plus every full-file difference reviewed. This variant fixes malformed three_by_four_array code; no unique task beyond Repeat all examples. Both need defect guidance and compatible plotting APIs; keep optional lab rather than clean core lesson. Do not assign both variants separately.",
])

def main():
    questions = json.loads((ROOT / "review/.cache/30days_questions.json").read_text(encoding="utf-8"))
    records = []
    for filename, decisions in D.items():
        selected = [q for q in questions if Path(q["path"]).name == filename]
        if len(selected) != len(decisions):
            raise ValueError((filename, len(selected), len(decisions)))
        for question, decision in zip(selected, decisions):
            objective, concepts, requires, stage, disposition, note = decision.split("|")
            records.append({**question, "objective": objective, "concepts": concepts.split(";"),
                "requires": requires.split(";"), "stage_hint": stage, "type": disposition,
                "review_note": note, "review": "full numbered parent brief read; chapter lesson review separate"})
    out = ROOT / "review/30days_decisions.json"
    out.write_text(json.dumps(records, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(f"Recorded {len(records)} reviewed questions in {len(D)} chapters")

if __name__ == "__main__": main()
