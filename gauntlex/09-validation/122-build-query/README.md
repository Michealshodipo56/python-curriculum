# Write URL Parameters

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
