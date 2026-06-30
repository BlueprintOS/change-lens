# Locate Subcommands

## `find <pattern>`

Use to locate definitions by name or glob-like pattern.

Steps:
1. Read project config and build the file list.
2. If `ctags` exists, generate an in-memory symbol index and match symbol names.
3. If `ctags` is missing, fall back to `rg -n` and mark results as text-level.
4. Return at most 20 rows unless the user asks for more.

Output:

```markdown
## Found N matches for "<pattern>"
| Location | Kind | Name | Summary |
|---|---|---|---|
| src/orders/service.py:42 | function | process | short summary |
```

## `where <file:line>`

Use to explain what code contains a line.

Steps:
1. Validate that the file exists and line is numeric or a line range.
2. Find nearest containing symbol using ctags when possible.
3. Print the requested line plus default 3 lines of context.

Output:

```markdown
## path/to/file.py:142

**Position**: `ClassName` -> `method_name`
**Context**:
```text
140  ...
142: target line
144  ...
```
```

## `refs <symbol>`

Use to locate references to a symbol.

Steps:
1. Run `rg -n --no-heading --fixed-strings '<symbol>'` in allowed sources.
2. If tree-sitter is available, filter to identifier/call positions.
3. If not, warn that comments and strings may be included.
4. Group by file with hit counts and sample line numbers.

## `impact <file::func>`

Use to estimate direct call impact.

Steps:
1. Resolve the target definition.
2. Upstream: call internal `refs` and identify containing symbols for each reference.
3. Downstream: inspect target body and list called symbols.
4. Default to `--depth 1`; allow `--depth 2` only with timeout/truncation warnings.

Warn that static analysis cannot reliably follow reflection, generated code, macros, cross-process runtime calls, or third-party internals.

## `draft-concept <name>`

Use to draft a concept card from discovered code.

Steps:
1. Search for the name and nearby variants.
2. Collect likely entry points and references.
3. Output a Markdown draft in chat only.
4. Include unchecked fields for the user to confirm.
