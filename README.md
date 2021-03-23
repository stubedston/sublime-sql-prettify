# SQL-Prettify

Makes your SQL code pretty by using an up-to-date [python-sqlparse](https://github.com/andialbrecht/sqlparse) as a plugin for [Sublime Text](https://www.sublimetext.com/).

## Install

Install via package control. Search for "SQL Prettify".

## Shortcuts

The default key bind for formatting either the entire file (no selected text) or a block of selected text is:

- For Linux / Windows: Ctrl+k, Ctrl+f
- For Mac: Super+k, Super+f

## Settings

Default settings are:

```
{
    // Changes how keywords are formatted. Allowed values are:
    // "upper", "lower" and "capitalize"
    "keyword_case": "upper",
    // Changes how identifiers are formatted. Allowed values are:
    // "upper", "lower", and "capitalize"
    "identifier_case": "lower",
    // Remove comments from the statement
    "strip_comments": true,
    // Use single spaces around all operators
    "use_space_around_operators": true,
    // If truncate_strings is a positive integer, string literals longer than
    // the given value will be truncated
    "truncate_strings": null,
    // If long string literals are truncated (see above) this value will be
    // append to the truncated string
    "truncate_char": "[...]",
    // Insert a newline between the start of the statement and the first
    // column name
    "indent_columns": true,
    // Change how the statement is indented
    "reindent": true,
    // Change how the statement is indented and align keywords
    "reindent_algined": true,
    // Indent all lines after the first
    "indent_after_first": false,
    // If True tabs instead of spaces are used for indentation
    "indent_tabs": false,
    // The width of the indentation, defaults to 2
    "indent_width": 2,
    // The column limit (in characters) for wrapping comma-separated lists. If
    // zero, it puts every column name in the list on its own line
    "wrap_after": 0,
    // Use comma-first notation for column names
    "comma_first": false,
    // Undocumented
    "right_margin": null,
    "stip_whitespace": false
}
```

Plugin supports all options available in python-sqlparse, for a description see [here](https://sqlparse.readthedocs.io/en/latest/api/#formatting).

## Examples
