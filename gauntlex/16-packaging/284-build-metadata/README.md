# Package Metadata

## Description
Assemble package metadata without exposing mutable input lists to later changes.

### Behavior contract
Return a dictionary with keys name, version, requires_python, dependencies from name, version, minimum_python, and dependency list. Copy the dependencies list so caller changes do not affect the result.

## Requirements
- Implement `build_metadata(name, version, minimum_python, dependencies)` in `starter/solution.py`.
- Return the specified result; do not print or prompt.
- Use Python's standard library only.
- Do not mutate caller-owned collections.

## Tips
Copying a list avoids surprising changes after the result is returned.

The learner must develop the implementation from the stated contract.
