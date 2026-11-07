# Gauntlex Python — Learning Path

**409 challenges · 23 sections · IDs 001–409**

Complete challenges in numeric ID order. Each link uses the title in its challenge README. The existing directory numbers and public APIs are unchanged.

Core projects 311–314 are followed by extension tracks 315–404, then final projects 405–409. This respects every existing prerequisite, including 314 → 315. Section 18 therefore appears at two project checkpoints.

Difficulty increases within each topic track. A new topic may begin with a small introductory exercise; a later review exercise may intentionally be easier than the preceding project. Similar topics are retained when they practice another API, validation rule, tie-breaker, or project context.

Before starting, install Python 3.11 or later and learn to run a script from a terminal. Each challenge is independent: work in its `starter/` directory, retain the supplied entrypoint and public signature, and use its existing tests as contract evidence. Function challenges return values; program challenges use the specified input/output interface. Do not copy a solution from another package merely because its function name matches.

Navigation: [Full-text curriculum](GAUNTLEX_PYTHON_CURRICULUM.md) · [Curriculum order and source inventory](CURRICULUM_ORDER.md) · [Audit report](CURRICULUM_AUDIT_REPORT.md) · [Release criteria](gauntlex/QUALITY_AND_RELEASE.md)

## Foundations (13 challenges)

Start with running scripts, exact terminal output, variables, numeric conversion, input, arithmetic, string operations, and simple comparisons. Valid-input assumptions keep the first exercises small.

- **001** [First Signal](gauntlex/01-foundations/001-hello/README.md)
- **002** [The Answer](gauntlex/01-foundations/002-displaynumber/README.md)
- **003** [Two Signals](gauntlex/01-foundations/003-two-lines/README.md)
- **004** [Combine Values](gauntlex/01-foundations/004-addition/README.md)
- **005** [A Personal Greeting](gauntlex/01-foundations/005-greeting/README.md)
- **006** [Identity Card](gauntlex/01-foundations/006-name-card/README.md)
- **007** [Measure a Rectangle](gauntlex/01-foundations/007-rectangle/README.md)
- **008** [Share Into Groups](gauntlex/01-foundations/008-remainder/README.md)
- **009** [Name Initials](gauntlex/01-foundations/009-initials/README.md)
- **010** [Clean Announcement](gauntlex/01-foundations/010-shout/README.md)
- **011** [One Year Later](gauntlex/01-foundations/011-next-year/README.md)
- **012** [Even or Odd](gauntlex/01-foundations/012-even-or-odd/README.md)
- **013** [Choose the Larger](gauntlex/01-foundations/013-larger/README.md)

## Control Flow (9 challenges)

Combine comparisons with branches and loops. Work through inclusive boundaries, zero iterations, running totals, and termination before managing collections.

- **014** [Score Boundaries](gauntlex/02-control-flow/014-grade/README.md)
- **015** [Permission Gate](gauntlex/02-control-flow/015-access/README.md)
- **016** [Count Forward](gauntlex/02-control-flow/016-count/README.md)
- **017** [Running Total](gauntlex/02-control-flow/017-sum-range/README.md)
- **018** [Launch Countdown](gauntlex/02-control-flow/018-countdown/README.md)
- **019** [Even Accumulator](gauntlex/02-control-flow/019-even-sum/README.md)
- **020** [Times Table](gauntlex/02-control-flow/020-multiplication-table/README.md)
- **021** [Decimal Length](gauntlex/02-control-flow/021-digit-count/README.md)
- **022** [Find the Secret](gauntlex/02-control-flow/022-number-guess/README.md)

## Collections (12 challenges)

Parse small sequences, preserve order, and use lists, dictionaries, and sets. Understand indexing, slicing, membership, and duplicate counts before moving calculations into functions.

- **023** [Count the Collection](gauntlex/03-collections/023-list-length/README.md)
- **024** [At Both Ends](gauntlex/03-collections/024-list-ends/README.md)
- **025** [Sum the Collection](gauntlex/03-collections/025-list-total/README.md)
- **026** [Find the Peak](gauntlex/03-collections/026-list-maximum/README.md)
- **027** [Reverse the Sequence](gauntlex/03-collections/027-reverse-words/README.md)
- **028** [Keep the Evens](gauntlex/03-collections/028-filter-even/README.md)
- **029** [First Appearance](gauntlex/03-collections/029-unique-order/README.md)
- **030** [Word Tally](gauntlex/03-collections/030-word-frequency/README.md)
- **031** [Numeric Order](gauntlex/03-collections/031-sort-numbers/README.md)
- **032** [Inside the Boundaries](gauntlex/03-collections/032-middle-slice/README.md)
- **033** [Shared Vocabulary](gauntlex/03-collections/033-set-overlap/README.md)
- **034** [Matching Pairs](gauntlex/03-collections/034-pair-count/README.md)

## Functions (12 challenges)

Switch from terminal programs to reusable functions. Learn parameters, return values, import behavior, and preserving caller-owned data. Earlier input/output skills remain available for later CLI projects.

- **035** [Return a Sum](gauntlex/04-functions/035-sum-function/README.md)
- **036** [Distance from Zero](gauntlex/04-functions/036-absolute-function/README.md)
- **037** [Factorial Product](gauntlex/04-functions/037-factorial/README.md)
- **038** [Mirror Text](gauntlex/04-functions/038-palindrome/README.md)
- **039** [Vowel Census](gauntlex/04-functions/039-vowel-count/README.md)
- **040** [Prime or Composite](gauntlex/04-functions/040-prime-check/README.md)
- **041** [Sequence Memory](gauntlex/04-functions/041-fibonacci/README.md)
- **042** [Same Letters, Different Order](gauntlex/04-functions/042-anagram/README.md)
- **043** [One Level Down](gauntlex/04-functions/043-flatten-once/README.md)
- **044** [First Unrepeated Character](gauntlex/04-functions/044-first-unique/README.md)
- **045** [Divide Into Chunks](gauntlex/04-functions/045-chunk-list/README.md)
- **046** [Greatest Shared Divisor](gauntlex/04-functions/046-gcd/README.md)

## Algorithms (16 challenges)

Combine functions and collections in search, transformation, matrix, delimiter, and recursive problems. Challenge 051 needs last-in-first-out reasoning, not a previously implemented Stack class. Challenge 059 revisits the same idea with only one delimiter type.

- **047** [Count the Words](gauntlex/05-algorithms/047-word-count/README.md)
- **048** [Longest in the Line](gauntlex/05-algorithms/048-longest-word/README.md)
- **049** [Circular Shift](gauntlex/05-algorithms/049-rotate-list/README.md)
- **050** [Two Ordered Streams](gauntlex/05-algorithms/050-merge-sorted/README.md)
- **051** [Nested Delimiters](gauntlex/05-algorithms/051-balanced-brackets/README.md)
- **052** [Compress Repeated Runs](gauntlex/05-algorithms/052-run-length/README.md)
- **053** [Alphabet Rotation](gauntlex/05-algorithms/053-caesar/README.md)
- **054** [Shared Beginning](gauntlex/05-algorithms/054-common-prefix/README.md)
- **055** [Rows Become Columns](gauntlex/05-algorithms/055-matrix-transpose/README.md)
- **056** [Halve the Search](gauntlex/05-algorithms/056-binary-search/README.md)
- **057** [Runner-Up Value](gauntlex/05-algorithms/057-second-largest/README.md)
- **058** [Group by Size](gauntlex/05-algorithms/058-group-by-length/README.md)
- **059** [Balance the Parentheses](gauntlex/05-algorithms/059-valid-parentheses/README.md)
- **060** [Zeros to the Back](gauntlex/05-algorithms/060-move-zeros/README.md)
- **061** [Build Pascal's Row](gauntlex/05-algorithms/061-pascal-row/README.md)
- **062** [Unfold Nested Lists](gauntlex/05-algorithms/062-flatten-recursive/README.md)

## Text Files (18 challenges)

Build on string and dictionary work to introduce standard-library parsing, imports, exception handling, dates, context managers, UTF-8, and file paths. Challenges 063–077 transform in-memory data; 078–080 apply those ideas to caller-supplied files. Read a module’s documentation as needed; no third-party parser is required.

- **063** [One Space Apart](gauntlex/06-text-files/063-normalize-spaces/README.md)
- **064** [Count the Lines](gauntlex/06-text-files/064-line-count/README.md)
- **065** [Parse With Care](gauntlex/06-text-files/065-safe-integer/README.md)
- **066** [Numbers Hidden in Text](gauntlex/06-text-files/066-extract-numbers/README.md)
- **067** [Protect the Address](gauntlex/06-text-files/067-mask-email/README.md)
- **068** [URL-Friendly Words](gauntlex/06-text-files/068-slugify/README.md)
- **069** [Fields and Quotes](gauntlex/06-text-files/069-csv-row/README.md)
- **070** [Find a JSON Field](gauntlex/06-text-files/070-json-value/README.md)
- **071** [Compact JSON Text](gauntlex/06-text-files/071-json-compact/README.md)
- **072** [Final File Suffix](gauntlex/06-text-files/072-path-extension/README.md)
- **073** [Division Without Failure](gauntlex/06-text-files/073-safe-divide/README.md)
- **074** [Real Calendar Dates](gauntlex/06-text-files/074-parse-date/README.md)
- **075** [Calendar Distance](gauntlex/06-text-files/075-days-between/README.md)
- **076** [Day of the Week](gauntlex/06-text-files/076-iso-weekday/README.md)
- **077** [Keep Valid Records](gauntlex/06-text-files/077-clean-records/README.md)
- **078** [Read the Line Count](gauntlex/06-text-files/078-count-file-lines/README.md)
- **079** [Load Structured Data](gauntlex/06-text-files/079-read-json-file/README.md)
- **080** [Sum a CSV Column](gauntlex/06-text-files/080-csv-column-total/README.md)

## Objects (15 challenges)

Introduce classes, constructors, methods, properties, class methods, invariants, callbacks, and persistent object state. Start with stack/queue behavior before validation-heavy objects and cache policies.

- **081** [Last In, First Out](gauntlex/07-objects/081-stack/README.md)
- **082** [First In, First Out](gauntlex/07-objects/082-queue/README.md)
- **083** [Count by Key](gauntlex/07-objects/083-counter/README.md)
- **084** [Guard the Balance](gauntlex/07-objects/084-bank-account/README.md)
- **085** [Two Scales, One Value](gauntlex/07-objects/085-temperature/README.md)
- **086** [Shape Invariants](gauntlex/07-objects/086-rectangle-class/README.md)
- **087** [Track the Work](gauntlex/07-objects/087-todo-list/README.md)
- **088** [Immutable Coordinates](gauntlex/07-objects/088-point/README.md)
- **089** [Stock Ledger](gauntlex/07-objects/089-inventory/README.md)
- **090** [Student Averages](gauntlex/07-objects/090-gradebook/README.md)
- **091** [Publish and Listen](gauntlex/07-objects/091-event-emitter/README.md)
- **092** [Remember the Recent](gauntlex/07-objects/092-lru-cache/README.md)
- **093** [Step Back in Time](gauntlex/07-objects/093-undo-history/README.md)
- **094** [Cart Rules](gauntlex/07-objects/094-shopping-cart/README.md)
- **095** [Serve by Priority](gauntlex/07-objects/095-task-priority/README.md)

## Problem Solving (20 challenges)

Extend earlier algorithm work to prefix products, windows, matrices, graph traversal, and directed cycles. A graph is represented with the dictionaries and lists already introduced; no external graph library is needed.

- **096** [Find the Pair](gauntlex/08-problem-solving/096-two-sum/README.md)
- **097** [Totals Along the Way](gauntlex/08-problem-solving/097-prefix-sums/README.md)
- **098** [Best Continuous Segment](gauntlex/08-problem-solving/098-max-subarray/README.md)
- **099** [Everyone Else's Product](gauntlex/08-problem-solving/099-product-except-self/README.md)
- **100** [Quarter Turn](gauntlex/08-problem-solving/100-rotate-matrix/README.md)
- **101** [Walk the Spiral](gauntlex/08-problem-solving/101-spiral-order/README.md)
- **102** [Write in Base Two](gauntlex/08-problem-solving/102-binary-conversion/README.md)
- **103** [Number to Numeral](gauntlex/08-problem-solving/103-roman-numerals/README.md)
- **104** [Numeral to Number](gauntlex/08-problem-solving/104-roman-to-int/README.md)
- **105** [Longest Without Repeats](gauntlex/08-problem-solving/105-longest-unique-substring/README.md)
- **106** [Smallest Sufficient Window](gauntlex/08-problem-solving/106-min-window-sum/README.md)
- **107** [Families of Letters](gauntlex/08-problem-solving/107-group-anagrams/README.md)
- **108** [Most Common Values](gauntlex/08-problem-solving/108-top-k-frequent/README.md)
- **109** [Unify Time Ranges](gauntlex/08-problem-solving/109-interval-merge/README.md)
- **110** [Add a New Range](gauntlex/08-problem-solving/110-interval-insert/README.md)
- **111** [Sudoku Constraints](gauntlex/08-problem-solving/111-valid-sudoku/README.md)
- **112** [Recolor a Region](gauntlex/08-problem-solving/112-flood-fill/README.md)
- **113** [Count the Islands](gauntlex/08-problem-solving/113-islands/README.md)
- **114** [Shortest Route](gauntlex/08-problem-solving/114-bfs-shortest-path/README.md)
- **115** [Detect a Loop](gauntlex/08-problem-solving/115-cycle-detection/README.md)

## Validation (25 challenges)

Revisit parsing with explicit rejection policies, normalization, exact types, and deterministic tie-breaking. Similar earlier exercises provide practice; these contracts must be read independently.

- **116** [Distinct After Normalization](gauntlex/09-validation/116-dedupe-normalized/README.md)
- **117** [Interpret a Boolean](gauntlex/09-validation/117-parse-boolean/README.md)
- **118** [Stay Within Bounds](gauntlex/09-validation/118-clamp/README.md)
- **119** [Telephone Canonical Form](gauntlex/09-validation/119-normalize-phone/README.md)
- **120** [Password Rules](gauntlex/09-validation/120-validate-password/README.md)
- **121** [Read URL Parameters](gauntlex/09-validation/121-parse-query/README.md)
- **122** [Write URL Parameters](gauntlex/09-validation/122-build-query/README.md)
- **123** [Four Network Octets](gauntlex/09-validation/123-validate-ipv4/README.md)
- **124** [Structured Log Entry](gauntlex/09-validation/124-parse-log-line/README.md)
- **125** [Log Severity Summary](gauntlex/09-validation/125-count-log-levels/README.md)
- **126** [Text Segments](gauntlex/09-validation/126-chunk-text/README.md)
- **127** [Configuration Assignments](gauntlex/09-validation/127-parse-env/README.md)
- **128** [Hide Sensitive Tokens](gauntlex/09-validation/128-redact-secrets/README.md)
- **129** [Canonical URL Paths](gauntlex/09-validation/129-normalize-url-path/README.md)
- **130** [Safe File Labels](gauntlex/09-validation/130-safe-filename/README.md)
- **131** [Clock Text to Seconds](gauntlex/09-validation/131-parse-duration/README.md)
- **132** [Seconds to Clock Text](gauntlex/09-validation/132-format-duration/README.md)
- **133** [Decode an RGB Color](gauntlex/09-validation/133-parse-hex-color/README.md)
- **134** [Encode an RGB Color](gauntlex/09-validation/134-format-hex-color/README.md)
- **135** [Clean the Tags](gauntlex/09-validation/135-normalize-tags/README.md)
- **136** [Domain Extraction](gauntlex/09-validation/136-email-domain/README.md)
- **137** [Shared Dictionary Keys](gauntlex/09-validation/137-common-keys/README.md)
- **138** [Reverse a Relationship](gauntlex/09-validation/138-invert-mapping/README.md)
- **139** [What Changed?](gauntlex/09-validation/139-diff-sets/README.md)
- **140** [Word Leaderboard](gauntlex/09-validation/140-top-words/README.md)

## Cli Tools (20 challenges)

Return to complete terminal programs and process streams, CSV, and JSON. Programs receive standard input rather than interactive prompts. Examples show escaped newline and tab characters to make exact stream behavior visible.

- **141** [Reverse the Stream](gauntlex/10-cli-tools/141-echo-lines/README.md)
- **142** [Line Numbers](gauntlex/10-cli-tools/142-number-lines/README.md)
- **143** [Find Matching Lines](gauntlex/10-cli-tools/143-grep-literal/README.md)
- **144** [First Lines Only](gauntlex/10-cli-tools/144-head-lines/README.md)
- **145** [Last Lines Only](gauntlex/10-cli-tools/145-tail-lines/README.md)
- **146** [Order the Lines](gauntlex/10-cli-tools/146-sort-lines/README.md)
- **147** [Collapse Repeated Lines](gauntlex/10-cli-tools/147-unique-adjacent/README.md)
- **148** [Count Matching Lines](gauntlex/10-cli-tools/148-count-occurrences/README.md)
- **149** [Sum the Stream](gauntlex/10-cli-tools/149-sum-columns/README.md)
- **150** [CSV to Tabs](gauntlex/10-cli-tools/150-csv-to-tsv/README.md)
- **151** [Readable JSON](gauntlex/10-cli-tools/151-json-pretty/README.md)
- **152** [Compact JSON Stream](gauntlex/10-cli-tools/152-json-lines/README.md)
- **153** [Count Active Records](gauntlex/10-cli-tools/153-jsonl-count/README.md)
- **154** [Extract JSON Fields](gauntlex/10-cli-tools/154-jsonl-select/README.md)
- **155** [Count CSV Records](gauntlex/10-cli-tools/155-csv-row-count/README.md)
- **156** [Extract a CSV Column](gauntlex/10-cli-tools/156-csv-select-column/README.md)
- **157** [Filter CSV Records](gauntlex/10-cli-tools/157-csv-filter-equal/README.md)
- **158** [Three Text Measures](gauntlex/10-cli-tools/158-word-count-cli/README.md)
- **159** [Value Histogram](gauntlex/10-cli-tools/159-histogram/README.md)
- **160** [Numeric Stream Summary](gauntlex/10-cli-tools/160-stats-cli/README.md)

## Data Analysis (20 challenges)

Apply collections and arithmetic to statistics and vectors using the standard library. Definitions state population versus sample conventions, tie rules, and empty-input behavior. These are calculation exercises, not a full third-party data-analysis course.

- **161** [The Middle Value](gauntlex/11-data-analysis/161-median/README.md)
- **162** [Most Frequent Observation](gauntlex/11-data-analysis/162-mode/README.md)
- **163** [Spread Around the Mean](gauntlex/11-data-analysis/163-variance/README.md)
- **164** [Standard Spread](gauntlex/11-data-analysis/164-standard-deviation/README.md)
- **165** [Nearest-Rank Percentile](gauntlex/11-data-analysis/165-percentile-nearest/README.md)
- **166** [Sliding Average](gauntlex/11-data-analysis/166-moving-average/README.md)
- **167** [Scale to Unit Range](gauntlex/11-data-analysis/167-normalize-minmax/README.md)
- **168** [Multiply and Accumulate](gauntlex/11-data-analysis/168-dot-product/README.md)
- **169** [Distance in Many Dimensions](gauntlex/11-data-analysis/169-euclidean-distance/README.md)
- **170** [Add Two Grids](gauntlex/11-data-analysis/170-matrix-add/README.md)
- **171** [Matrix Composition](gauntlex/11-data-analysis/171-matrix-multiply/README.md)
- **172** [Build a Histogram](gauntlex/11-data-analysis/172-bucket-count/README.md)
- **173** [Linear Relationship](gauntlex/11-data-analysis/173-pearson-correlation/README.md)
- **174** [Running Products](gauntlex/11-data-analysis/174-cumulative-product/README.md)
- **175** [Observation Counts](gauntlex/11-data-analysis/175-frequency-table/README.md)
- **176** [Unequal Importance](gauntlex/11-data-analysis/176-weighted-mean/README.md)
- **177** [Dense Rankings](gauntlex/11-data-analysis/177-rank-values/README.md)
- **178** [Round to Steps](gauntlex/11-data-analysis/178-quantize/README.md)
- **179** [Outside the Fences](gauntlex/11-data-analysis/179-outlier-iqr/README.md)
- **180** [Fit a Straight Line](gauntlex/11-data-analysis/180-linear-regression/README.md)

## Http Security (25 challenges)

Introduce URL parts, HTTP metadata, representations, authentication helpers, and hashes as local operations. Most challenges make no network requests; the later HTTP projects assemble these pieces into services.

- **181** [Identify the Host](gauntlex/12-http-security/181-url-host/README.md)
- **182** [Resolve a Link](gauntlex/12-http-security/182-url-join/README.md)
- **183** [Read the Response Status](gauntlex/12-http-security/183-parse-http-status/README.md)
- **184** [Canonical Header Names](gauntlex/12-http-security/184-normalize-headers/README.md)
- **185** [Read Cookie Pairs](gauntlex/12-http-security/185-parse-cookie/README.md)
- **186** [Assemble a Cookie Header](gauntlex/12-http-security/186-build-cookie/README.md)
- **187** [Backoff with a Ceiling](gauntlex/12-http-security/187-http-retry-delay/README.md)
- **188** [Page to Offset](gauntlex/12-http-security/188-pagination-offset/README.md)
- **189** [One Page of Results](gauntlex/12-http-security/189-pagination-slice/README.md)
- **190** [Match Every Field](gauntlex/12-http-security/190-query-filter/README.md)
- **191** [Build a JSON Response](gauntlex/12-http-security/191-json-response/README.md)
- **192** [Read a Bearer Token](gauntlex/12-http-security/192-parse-bearer/README.md)
- **193** [Compare Secrets Safely](gauntlex/12-http-security/193-constant-time-compare/README.md)
- **194** [Fingerprint a Message](gauntlex/12-http-security/194-sha256-hex/README.md)
- **195** [Authenticate a Message](gauntlex/12-http-security/195-hmac-signature/README.md)
- **196** [Verify a Signature](gauntlex/12-http-security/196-verify-hmac/README.md)
- **197** [Exact Origin Allowlist](gauntlex/12-http-security/197-cors-origin/README.md)
- **198** [Recognize HTTP Methods](gauntlex/12-http-security/198-http-method/README.md)
- **199** [Extract the Media Type](gauntlex/12-http-security/199-parse-content-type/README.md)
- **200** [Stable Request Identity](gauntlex/12-http-security/200-http-cache-key/README.md)
- **201** [Unique Request Identifier](gauntlex/12-http-security/201-request-id/README.md)
- **202** [Escape One URL Component](gauntlex/12-http-security/202-url-encode-component/README.md)
- **203** [Restore One URL Component](gauntlex/12-http-security/203-url-decode-component/README.md)
- **204** [Decode Basic Credentials](gauntlex/12-http-security/204-parse-basic-auth/README.md)
- **205** [Find the Last Header](gauntlex/12-http-security/205-header-get/README.md)

## Sqlite (25 challenges)

Introduce SQL and caller-owned SQLite connections, then CRUD, filtering, aggregation, joins, schema checks, and transactions. Read about SQL value parameters, explicit ordering, constraints, and savepoints before the relevant exercises.

- **206** [Define the Users Table](gauntlex/13-sqlite/206-create-users/README.md)
- **207** [Register a User](gauntlex/13-sqlite/207-insert-user/README.md)
- **208** [Find One Record](gauntlex/13-sqlite/208-find-user/README.md)
- **209** [Read the User Directory](gauntlex/13-sqlite/209-list-users/README.md)
- **210** [Change a User Email](gauntlex/13-sqlite/210-update-email/README.md)
- **211** [Remove a User](gauntlex/13-sqlite/211-delete-user/README.md)
- **212** [Search Names Literally](gauntlex/13-sqlite/212-search-users/README.md)
- **213** [Count the Directory](gauntlex/13-sqlite/213-count-users/README.md)
- **214** [Paginate User Records](gauntlex/13-sqlite/214-users-page/README.md)
- **215** [Define the Orders Table](gauntlex/13-sqlite/215-create-orders/README.md)
- **216** [Sum Customer Orders](gauntlex/13-sqlite/216-order-total/README.md)
- **217** [Rank Customers by Spending](gauntlex/13-sqlite/217-top-customers/README.md)
- **218** [Orders and Their Owners](gauntlex/13-sqlite/218-join-orders/README.md)
- **219** [Insert Only Once](gauntlex/13-sqlite/219-insert-ignore/README.md)
- **220** [Create or Replace a Score](gauntlex/13-sqlite/220-upsert-score/README.md)
- **221** [Atomic Account Transfer](gauntlex/13-sqlite/221-transaction-transfer/README.md)
- **222** [All or Nothing](gauntlex/13-sqlite/222-transaction-batch/README.md)
- **223** [Allowlisted Sorting](gauntlex/13-sqlite/223-safe-sort/README.md)
- **224** [Count Event Categories](gauntlex/13-sqlite/224-group-counts/README.md)
- **225** [Events After a Date](gauntlex/13-sqlite/225-date-filter/README.md)
- **226** [Inspect the Schema](gauntlex/13-sqlite/226-db-schema-check/README.md)
- **227** [Ensure an Index](gauntlex/13-sqlite/227-db-index/README.md)
- **228** [Store a JSON Document](gauntlex/13-sqlite/228-db-json/README.md)
- **229** [Load a JSON Document](gauntlex/13-sqlite/229-db-json-read/README.md)
- **230** [Revenue by Category](gauntlex/13-sqlite/230-db-report/README.md)

## Async (15 challenges)

Introduce coroutine calls and awaiting before concurrent results, deadlines, retries, bounded work, queues, events, and locks. Concurrency overlaps waiting; it does not require threads or network access here.

- **231** [An Awaitable Greeting](gauntlex/14-async/231-async-greeting/README.md)
- **232** [A Coroutine Result](gauntlex/14-async/232-async-double/README.md)
- **233** [Gather in Order](gauntlex/14-async/233-async-gather/README.md)
- **234** [Concurrent Transformation](gauntlex/14-async/234-async-map/README.md)
- **235** [Set a Deadline](gauntlex/14-async/235-async-timeout/README.md)
- **236** [Try Again](gauntlex/14-async/236-async-retry/README.md)
- **237** [Limit Concurrency](gauntlex/14-async/237-async-semaphore/README.md)
- **238** [First to Finish](gauntlex/14-async/238-async-first/README.md)
- **239** [Drain the Queue](gauntlex/14-async/239-async-queue/README.md)
- **240** [Produce in Sequence](gauntlex/14-async/240-async-producer/README.md)
- **241** [Consume Exactly N](gauntlex/14-async/241-async-consumer/README.md)
- **242** [Wait for a Signal](gauntlex/14-async/242-async-event/README.md)
- **243** [Protected Increment](gauntlex/14-async/243-async-lock/README.md)
- **244** [Concurrent Selection](gauntlex/14-async/244-async-filter/README.md)
- **245** [Process in Waves](gauntlex/14-async/245-async-batch/README.md)

## Testing (25 challenges)

Build assertion and reporting helpers around callable behavior. This section practices observable contracts, exception handling, output capture, comparison, and test-result data; it does not require adding tests to the curriculum repository.

- **246** [Explain a Mismatch](gauntlex/15-testing/246-assert-equal/README.md)
- **247** [Expect a Failure](gauntlex/15-testing/247-assert-raises/README.md)
- **248** [Close Enough](gauntlex/15-testing/248-approx-equal/README.md)
- **249** [Find the Divergence](gauntlex/15-testing/249-first-difference/README.md)
- **250** [Compare Records](gauntlex/15-testing/250-diff-dicts/README.md)
- **251** [Evaluate Examples](gauntlex/15-testing/251-run-cases/README.md)
- **252** [Observe Printed Output](gauntlex/15-testing/252-capture-output/README.md)
- **253** [Check the Order](gauntlex/15-testing/253-is-sorted/README.md)
- **254** [Reject Disorder](gauntlex/15-testing/254-validate-sorted/README.md)
- **255** [Same Elements, New Order](gauntlex/15-testing/255-check-permutation/README.md)
- **256** [Guard the Nonnegative Invariant](gauntlex/15-testing/256-invariant-check/README.md)
- **257** [Count Test Report Lines](gauntlex/15-testing/257-parse-test-report/README.md)
- **258** [Measure the Failure Rate](gauntlex/15-testing/258-flaky-detector/README.md)
- **259** [Select by Name](gauntlex/15-testing/259-test-selection/README.md)
- **260** [Three Outcomes](gauntlex/15-testing/260-test-summary/README.md)
- **261** [Identify a Test](gauntlex/15-testing/261-pytest-nodeid/README.md)
- **262** [Name a Test Function](gauntlex/15-testing/262-test-name-normalize/README.md)
- **263** [Coverage Ratio](gauntlex/15-testing/263-coverage-percent/README.md)
- **264** [Spot Regressions](gauntlex/15-testing/264-regression-check/README.md)
- **265** [Cross-Platform Failures](gauntlex/15-testing/265-test-matrix/README.md)
- **266** [Undetected Mutations](gauntlex/15-testing/266-mutation-survivors/README.md)
- **267** [Unique Case Labels](gauntlex/15-testing/267-test-case-ids/README.md)
- **268** [Compare Stable Snapshots](gauntlex/15-testing/268-snapshot-compare/README.md)
- **269** [Find Slow Cases](gauntlex/15-testing/269-test-duration/README.md)
- **270** [Require Every Item](gauntlex/15-testing/270-assert-subset/README.md)

## Packaging (15 challenges)

Introduce simplified version strings, requirements, environment configuration, manifests, and packaging metadata. The stated grammars are exercise contracts; they do not implement all Python packaging standards.

- **271** [Three-Part Version](gauntlex/16-packaging/271-semver-parse/README.md)
- **272** [Version Ordering](gauntlex/16-packaging/272-semver-compare/README.md)
- **273** [Pinned Dependency](gauntlex/16-packaging/273-dependency-parse/README.md)
- **274** [Dependency Order](gauntlex/16-packaging/274-requirements-sort/README.md)
- **275** [One Requirement per Package](gauntlex/16-packaging/275-requirements-dedupe/README.md)
- **276** [Read Environment Settings](gauntlex/16-packaging/276-env-config/README.md)
- **277** [Apply Overrides](gauntlex/16-packaging/277-config-merge/README.md)
- **278** [Describe Build Files](gauntlex/16-packaging/278-file-manifest/README.md)
- **279** [Write a Release Note](gauntlex/16-packaging/279-release-notes/README.md)
- **280** [Organize Changes](gauntlex/16-packaging/280-changelog-groups/README.md)
- **281** [Name the Entry Point](gauntlex/16-packaging/281-python-entrypoint/README.md)
- **282** [Module to File](gauntlex/16-packaging/282-module-path/README.md)
- **283** [Wheel Filename](gauntlex/16-packaging/283-artifact-name/README.md)
- **284** [Package Metadata](gauntlex/16-packaging/284-build-metadata/README.md)
- **285** [Release Readiness](gauntlex/16-packaging/285-release-checklist/README.md)

## Architecture (25 challenges)

Use earlier graph, validation, HTTP, and hashing work to model dependencies, permissions, request identity, event replay, caching, and reliability policies. These small helpers illustrate selected rules rather than complete distributed systems.

- **286** [Build in Dependency Order](gauntlex/17-architecture/286-dependency-order/README.md)
- **287** [Find Dependency Loops](gauntlex/17-architecture/287-dependency-cycles/README.md)
- **288** [Downstream Reachability](gauntlex/17-architecture/288-reachable-services/README.md)
- **289** [Who Depends on This?](gauntlex/17-architecture/289-reverse-dependencies/README.md)
- **290** [Build in Parallel Layers](gauntlex/17-architecture/290-service-layers/README.md)
- **291** [Transitive Feature Gates](gauntlex/17-architecture/291-feature-flags/README.md)
- **292** [Capture Route Parameters](gauntlex/17-architecture/292-route-match/README.md)
- **293** [Route Specificity](gauntlex/17-architecture/293-route-priority/README.md)
- **294** [Requests in a Time Window](gauntlex/17-architecture/294-rate-limit-window/README.md)
- **295** [Circuit Breaker States](gauntlex/17-architecture/295-circuit-state/README.md)
- **296** [Time to Live](gauntlex/17-architecture/296-cache-expiry/README.md)
- **297** [Evict the Oldest](gauntlex/17-architecture/297-cache-eviction/README.md)
- **298** [Worst Service Health](gauntlex/17-architecture/298-health-rollup/README.md)
- **299** [Protect the Retry Budget](gauntlex/17-architecture/299-retry-budget/README.md)
- **300** [Identify Duplicate Requests](gauntlex/17-architecture/300-idempotency-key/README.md)
- **301** [Choose a Stable Partition](gauntlex/17-architecture/301-partition-key/README.md)
- **302** [Keep First Events](gauntlex/17-architecture/302-event-dedup/README.md)
- **303** [Rebuild Account Balances](gauntlex/17-architecture/303-event-projection/README.md)
- **304** [Replay Exactly Once](gauntlex/17-architecture/304-replay-dedup/README.md)
- **305** [Configuration Changes](gauntlex/17-architecture/305-config-diff/README.md)
- **306** [Permission by Role](gauntlex/17-architecture/306-permission-check/README.md)
- **307** [Inherited Permissions](gauntlex/17-architecture/307-permission-inherit/README.md)
- **308** [Record an Action](gauntlex/17-architecture/308-audit-record/README.md)
- **309** [Structured Errors](gauntlex/17-architecture/309-error-envelope/README.md)
- **310** [Opaque Page Cursor](gauntlex/17-architecture/310-pagination-token/README.md)

## Capstones — Core Projects (311–314)

Integrate prior skills into persistent CLIs and a local HTTP service at 311–314. After the extension tracks, complete larger inventory, contact, ETL, event-history, and path-inspection projects at 405–409.

- **311** [Persistent Task Tracker](gauntlex/18-capstones/311-task-tracker/README.md)
- **312** [Streaming Log Inspector](gauntlex/18-capstones/312-log-analyzer/README.md)
- **313** [Expense Ledger](gauntlex/18-capstones/313-expense-ledger/README.md)
- **314** [A Minimal HTTP Service](gauntlex/18-capstones/314-http-api-server/README.md)

## File Automation (20 challenges)

After the core projects, extend file work with JSON trees, binary fingerprints, atomic replacement, directory manifests, and archive-path validation. Repeated basic operations serve as preparation for the final automation projects.

- **315** [Safe Relative Paths](gauntlex/19-file-automation/315-safe-relative-path/README.md)
- **316** [Recognize File Extensions](gauntlex/19-file-automation/316-file-extension/README.md)
- **317** [One Line Ending](gauntlex/19-file-automation/317-line-ending-normalize/README.md)
- **318** [Read an INI Section](gauntlex/19-file-automation/318-parse-ini-section/README.md)
- **319** [Follow Nested Keys](gauntlex/19-file-automation/319-json-path-get/README.md)
- **320** [Flatten a JSON Tree](gauntlex/19-file-automation/320-flatten-json/README.md)
- **321** [Rebuild Nested JSON](gauntlex/19-file-automation/321-unflatten-json/README.md)
- **322** [Fingerprint a File](gauntlex/19-file-automation/322-file-checksum/README.md)
- **323** [Count File Records](gauntlex/19-file-automation/323-count-file-lines/README.md)
- **324** [Append Structured Records](gauntlex/19-file-automation/324-append-jsonl/README.md)
- **325** [Load a JSON Lines Stream](gauntlex/19-file-automation/325-read-jsonl/README.md)
- **326** [Replace a File Safely](gauntlex/19-file-automation/326-write-atomic/README.md)
- **327** [Find Duplicate Content](gauntlex/19-file-automation/327-find-duplicates/README.md)
- **328** [Aggregate CSV Values](gauntlex/19-file-automation/328-csv-group-sum/README.md)
- **329** [Count Unique CSV Rows](gauntlex/19-file-automation/329-csv-dedupe/README.md)
- **330** [Map a Directory](gauntlex/19-file-automation/330-directory-manifest/README.md)
- **331** [Select File Types](gauntlex/19-file-automation/331-filter-by-suffix/README.md)
- **332** [Inspect Archive Paths](gauntlex/19-file-automation/332-safe-archive-name/README.md)
- **333** [Plan Log Backups](gauntlex/19-file-automation/333-rotate-logs/README.md)
- **334** [Fingerprint Configuration](gauntlex/19-file-automation/334-config-fingerprint/README.md)

## Wsgi Web (20 challenges)

Introduce the WSGI callable, environment mapping, start_response callback, and byte iterable before routing, bodies, headers, auth, caching, errors, and middleware. Invoke these callables locally; these exercises do not require deploying a website.

- **335** [Your First WSGI Response](gauntlex/20-wsgi-web/335-wsgi-health/README.md)
- **336** [Route by Path](gauntlex/20-wsgi-web/336-wsgi-routing/README.md)
- **337** [Method Matters](gauntlex/20-wsgi-web/337-wsgi-method/README.md)
- **338** [Decode Query Input](gauntlex/20-wsgi-web/338-wsgi-query/README.md)
- **339** [Serialize a Web Response](gauntlex/20-wsgi-web/339-wsgi-json/README.md)
- **340** [Read a Request Body](gauntlex/20-wsgi-web/340-wsgi-post-body/README.md)
- **341** [Validate JSON Input](gauntlex/20-wsgi-web/341-wsgi-json-post/README.md)
- **342** [Inspect Request Headers](gauntlex/20-wsgi-web/342-wsgi-headers/README.md)
- **343** [Headers Without a Body](gauntlex/20-wsgi-web/343-wsgi-head/README.md)
- **344** [Move a Resource](gauntlex/20-wsgi-web/344-wsgi-redirect/README.md)
- **345** [Recognize a Session Cookie](gauntlex/20-wsgi-web/345-wsgi-cookie/README.md)
- **346** [Protect a Private Route](gauntlex/20-wsgi-web/346-wsgi-auth/README.md)
- **347** [Control Cross-Origin Access](gauntlex/20-wsgi-web/347-wsgi-cors/README.md)
- **348** [Avoid Unchanged Responses](gauntlex/20-wsgi-web/348-wsgi-conditional/README.md)
- **349** [Safe Server Errors](gauntlex/20-wsgi-web/349-wsgi-error-handler/README.md)
- **350** [Validate Request IDs](gauntlex/20-wsgi-web/350-wsgi-request-id/README.md)
- **351** [Count Response Bytes](gauntlex/20-wsgi-web/351-wsgi-content-length/README.md)
- **352** [Read Form Fields](gauntlex/20-wsgi-web/352-wsgi-form/README.md)
- **353** [Consistent Not Found](gauntlex/20-wsgi-web/353-wsgi-not-found-json/README.md)
- **354** [Wrap an Application](gauntlex/20-wsgi-web/354-wsgi-middleware/README.md)

## Data Science (20 challenges)

Revisit numeric helpers with explicit input validation, then extend to scaling, smoothing, evaluation metrics, nearest-neighbor ranking, ordered holdouts, and categorical encoding. Earlier statistics supply the mathematical prerequisites; no NumPy, pandas, or scikit-learn is required.

- **355** [Scale to Zero and One](gauntlex/21-data-science/355-min-max-scale/README.md)
- **356** [Standardize Observations](gauntlex/21-data-science/356-z-score-scale/README.md)
- **357** [Smooth with Windows](gauntlex/21-data-science/357-moving-average/README.md)
- **358** [Weighted Recent History](gauntlex/21-data-science/358-exponential-smoothing/README.md)
- **359** [Weighted Observations](gauntlex/21-data-science/359-weighted-mean/README.md)
- **360** [Move Together](gauntlex/21-data-science/360-covariance/README.md)
- **361** [Interpolate a Quantile](gauntlex/21-data-science/361-quantile-linear/README.md)
- **362** [Classify the Outcomes](gauntlex/21-data-science/362-confusion-matrix/README.md)
- **363** [Measure a Classifier](gauntlex/21-data-science/363-classification-metrics/README.md)
- **364** [Average Prediction Error](gauntlex/21-data-science/364-mean-absolute-error/README.md)
- **365** [Penalize Large Errors](gauntlex/21-data-science/365-root-mean-square-error/README.md)
- **366** [Explain the Variation](gauntlex/21-data-science/366-r-squared/README.md)
- **367** [Straight-Line Distance](gauntlex/21-data-science/367-euclidean-distance/README.md)
- **368** [Compare Directions](gauntlex/21-data-science/368-cosine-similarity/README.md)
- **369** [City-Block Distance](gauntlex/21-data-science/369-manhattan-distance/README.md)
- **370** [Find Nearby Examples](gauntlex/21-data-science/370-k-nearest-neighbors/README.md)
- **371** [Hold Out Examples](gauntlex/21-data-science/371-train-test-split/README.md)
- **372** [Train in Batches](gauntlex/21-data-science/372-minibatches/README.md)
- **373** [Encode Categories](gauntlex/21-data-science/373-one-hot-encode/README.md)
- **374** [Normalize Each Feature](gauntlex/21-data-science/374-standardize-columns/README.md)

## Advanced Algorithms (10 challenges)

Extend binary search, intervals, windows, and graph search with boundary searches, new tie rules, weighted paths, and explicit performance targets. Follow each contract: adjacent integer intervals here merge differently from challenge 109.

- **375** [First Not Smaller](gauntlex/22-advanced-algorithms/375-binary-search-bound/README.md)
- **376** [First Strictly Greater](gauntlex/22-advanced-algorithms/376-upper-bound/README.md)
- **377** [Merge Integer Ranges](gauntlex/22-advanced-algorithms/377-merge-intervals/README.md)
- **378** [Where Ranges Overlap](gauntlex/22-advanced-algorithms/378-interval-intersection/README.md)
- **379** [Longest Distinct Window](gauntlex/22-advanced-algorithms/379-longest-unique-substring/README.md)
- **380** [Smallest Covering Substring](gauntlex/22-advanced-algorithms/380-minimum-window/README.md)
- **381** [Frequency with Stable Ties](gauntlex/22-advanced-algorithms/381-top-k-frequent/README.md)
- **382** [Shortest Grid Route](gauntlex/22-advanced-algorithms/382-shortest-path-grid/README.md)
- **383** [Weighted Shortest Paths](gauntlex/22-advanced-algorithms/383-dijkstra-distances/README.md)
- **384** [Increasing Subsequence](gauntlex/22-advanced-algorithms/384-longest-increasing-subsequence/README.md)

## Security Crypto (20 challenges)

Consolidate encoding, hashing, validation, and sensitive-data handling before the final projects. Several operations deliberately revisit Section 12 in a security-focused track. Encoding and classical ciphers are not encryption for protecting secrets.

- **385** [Shift the Alphabet](gauntlex/23-security-crypto/385-caesar-cipher/README.md)
- **386** [Half an Alphabet](gauntlex/23-security-crypto/386-rot13/README.md)
- **387** [Text to Hexadecimal](gauntlex/23-security-crypto/387-hex-encode/README.md)
- **388** [Hexadecimal to Text](gauntlex/23-security-crypto/388-hex-decode/README.md)
- **389** [Encode Base64](gauntlex/23-security-crypto/389-base64-encode/README.md)
- **390** [Decode Base64](gauntlex/23-security-crypto/390-base64-decode/README.md)
- **391** [Sign a Message](gauntlex/23-security-crypto/391-hmac-sign/README.md)
- **392** [Authenticate a Signature](gauntlex/23-security-crypto/392-hmac-verify/README.md)
- **393** [Derive a Key](gauntlex/23-security-crypto/393-pbkdf2-key/README.md)
- **394** [Secure Random Token](gauntlex/23-security-crypto/394-random-token/README.md)
- **395** [Rule-Based Password Score](gauntlex/23-security-crypto/395-password-strength/README.md)
- **396** [Reveal Only the End](gauntlex/23-security-crypto/396-mask-secret/README.md)
- **397** [Canonical IPv4](gauntlex/23-security-crypto/397-validate-ipv4/README.md)
- **398** [Normalize a Network](gauntlex/23-security-crypto/398-cidr-network/README.md)
- **399** [Network Membership](gauntlex/23-security-crypto/399-cidr-contains/README.md)
- **400** [Inspect a Web Host](gauntlex/23-security-crypto/400-safe-url-host/README.md)
- **401** [Hide Sensitive Headers](gauntlex/23-security-crypto/401-redact-headers/README.md)
- **402** [Allowlisted Query Parameters](gauntlex/23-security-crypto/402-query-param-filter/README.md)
- **403** [Summarize Security Events](gauntlex/23-security-crypto/403-security-event-counts/README.md)
- **404** [Timing-Resistant Equality](gauntlex/23-security-crypto/404-constant-time-match/README.md)

## Capstones — Final Projects (405–409)

Integrate prior skills into persistent CLIs and a local HTTP service at 311–314. After the extension tracks, complete larger inventory, contact, ETL, event-history, and path-inspection projects at 405–409.

- **405** [Inventory Manager](gauntlex/18-capstones/405-inventory-manager/README.md)
- **406** [Contact Directory](gauntlex/18-capstones/406-contact-book/README.md)
- **407** [CSV Data Pipeline](gauntlex/18-capstones/407-csv-etl-pipeline/README.md)
- **408** [Event-Sourced Wallet](gauntlex/18-capstones/408-event-sourced-wallet/README.md)
- **409** [Local Link Inspector](gauntlex/18-capstones/409-markdown-link-checker/README.md)
