# Code Structure, Comments & Formatting

## Comments

- Avoid Bad Comments
  - avoid comments that have redundant information
  - avoid comments that make dividers / block markers
  - avoid misleading comments
  -  avoid commented-out code instead deleted it.


- **Use Good Comments** like:
  - Legal Information
  - Explanations which can't be replaced by good naming like explain a regex
  - Warnings
  - Todo Notes
  - For Documenting A public API.


## Code Formatting
1. **Vertical Formatting** -> Space between lines, Grouping of Code.
2. **Horizontal Formatting** -> Indentation, Space between code, line width.

### Vertical Formatting
- code should be readable like an essay - "top to bottom without too many jumps":
  1. Consider splitting files with multiple concepts (e.g classes) into multiple files.
  2. Different concepts ("areas") should be separated by spacing.
  3. Similar concepts ("areas") should not be separated by spacing.
  4. Related concepts should be kept close to each other.


### Horizontal Formatting
- Lines of code should be readable without scrolling avoid very long "sentences":
  - Use indentation even if not required
  - Break long statements into multiple shorter ones.
  - Use clear but not unreadable long names.