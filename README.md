# py-hunter
An Anti-PEP8 style enforcement tool, to catch implicit booleans, list comprehensions, and other patterns that look cool, but make code harder to maintain and read in the long term

## Usage

No install required. Run directly from GitHub using [uv](https://docs.astral.sh/uv/):

```bash
uvx --from "git+https://github.com/Andrew-Jayne/Py-Hunter" py-hunter <path>
```

Or pin to a specific branch:

```bash
uvx --from "git+https://github.com/Andrew-Jayne/Py-Hunter@main" py-hunter <path>
```

If you have the repo cloned locally:

```bash
uv run py-hunter <path>
```
