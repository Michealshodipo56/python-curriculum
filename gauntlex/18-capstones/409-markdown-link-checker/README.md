# Local Link Inspector

## Description

Inspect Markdown files for broken local links without contacting external websites.

This is a project challenge. Plan the components, define their responsibilities, and implement the application without a provided solution.

## Requirements

- Run `python main.py ROOT` from `starter/` and recursively inspect Markdown files under the supplied root directory.
- Recognize inline links of the form `[label](target)` where the target contains no spaces or parentheses. Other Markdown link syntax is outside this challenge.
- Ignore targets beginning with `http:`, `https:`, `mailto:`, or `#`. Never make network requests.
- Remove any query string and fragment for filesystem resolution, while keeping the original target in reports.
- Resolve a relative target from the Markdown file's containing directory. Resolve a target beginning with `/` beneath `ROOT`.
- Report missing targets and paths whose canonical destination escapes `ROOT`, including paths escaping through symbolic links.
- Print a compact JSON array of objects with string `file` and `target`, with sorted object keys and records ordered by `file`, then `target`. Express `file` relative to `ROOT` with POSIX slashes.
- Print `[]` if all recognized local links are valid. End output with a newline; exit with status `1` when broken links exist or `0` otherwise.

## Constraints

- Use Python 3.11+ and the standard library only.
- Do not use network services or print debug messages to standard output.

## Deliverables

- Implement the application in `starter/main.py`, with additional modules only when useful.
- Document the program's usage, key design choices, and failure behavior.
- Explain link resolution and containment checks for traversal and symlinks.

## Design Considerations

Resolve paths against the correct base and verify their canonical locations remain under ROOT, including when symbolic links are involved. Do not fetch remote links.

## Example Behavior

A Markdown link pointing outside ROOT through `../` or a symlink is reported broken even if the target file exists.

## Tips

A path can appear inside the project yet resolve outside it through traversal or a symbolic link.

## Guide and Auditor

The Gauntlex Guide should help you reason through decisions and debug issues without supplying finished code. The Auditor may ask you to demonstrate the required behavior and defend your design choices.
