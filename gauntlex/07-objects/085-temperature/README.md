# Two Scales, One Value

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

## Example Behavior

`Temperature(0).fahrenheit` is `32`; `Temperature.from_fahrenheit(212).celsius` is `100`.
