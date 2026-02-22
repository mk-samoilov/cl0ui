# Widgets

All widgets are accessed through the `w` singleton imported from `cl0ui.widgets`.

```python
from cl0ui.widgets import w
```

---

## `w.text(text, style=None)`

Renders a single line of text. Supports inline [markup](markup.md).

```python
w.text(text="Hello, world!")
w.text(text="[#BOLD]Bold[#RESET] and [#CYAN]colored[#RESET]")
w.text(text="Status: [#BRIGHT_GREEN]OK[#RESET]", style=MyTextStyle())
```

---

## `w.option(text, style=None) → bool`

An inline selectable item rendered as `[ text ]`. Returns `True` on the tick it is activated.

```python
if w.option(text="Do something"):
    perform_action()
```

Focus moves with `↑` / `↓`. Activated with `Enter` or `Space`.

---

## `w.button(text, style=None) → bool`

A bordered button rendered as a box. Returns `True` on the tick it is activated.

```python
if w.button(text="Exit"):
    cl0ui.quit()
```

Padding around the label is controlled by `BaseButtonStyle.padding` (default `2`).

---

## `w.separation(length, style=None)`

Draws a horizontal line of `length` characters.

```python
w.separation(24)
```

The character used is `─` by default, configurable via `BaseSeparationStyle.char`.

---

## `w.spacing()`

Inserts one blank line.

---

## Scrolling

When content is taller than the terminal window the interface scrolls automatically to keep the focused widget visible with a margin of `win_height // 4` rows.
