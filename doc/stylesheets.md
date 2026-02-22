# Stylesheets

Every widget accepts an optional `style=` parameter. Styles are plain Python classes that inherit from a `Base*Style` class and override class attributes.

```python
from cl0ui.stylesheets import BaseButtonStyle

class DangerButton(BaseButtonStyle):
    focused_fg = curses.COLOR_RED

if w.button(text="Delete", style=DangerButton()):
    ...
```

No decorator or registration is needed. Unset fields fall back to the parent's defaults.

---

## BaseTextStyle

| Field  | Type  | Default    | Description                                |
|--------|-------|------------|--------------------------------------------|
| `attr` | `int` | `A_NORMAL` | curses attribute (bold, dim, …)            |
| `fg`   | `int` | `-1`       | foreground color (`-1` = terminal default) |
| `bg`   | `int` | `-1`       | background color                           |

---

## BaseOptionStyle

| Field          | Type  | Default     | Description                 |
|----------------|-------|-------------|-----------------------------|
| `attr`         | `int` | `A_NORMAL`  | attribute when not focused  |
| `focused_attr` | `int` | `A_REVERSE` | attribute when focused      |
| `fg`           | `int` | `-1`        | foreground when not focused |
| `bg`           | `int` | `-1`        | background when not focused |
| `focused_fg`   | `int` | `-1`        | foreground when focused     |
| `focused_bg`   | `int` | `-1`        | background when focused     |

---

## BaseButtonStyle

| Field          | Type  | Default     | Description                             |
|----------------|-------|-------------|-----------------------------------------|
| `attr`         | `int` | `A_NORMAL`  | attribute when not focused              |
| `focused_attr` | `int` | `A_REVERSE` | attribute applied to label when focused |
| `padding`      | `int` | `2`         | spaces between border and label         |
| `fg`           | `int` | `-1`        | foreground when not focused             |
| `bg`           | `int` | `-1`        | background when not focused             |
| `focused_fg`   | `int` | `-1`        | foreground when focused                 |
| `focused_bg`   | `int` | `-1`        | background when focused                 |

Only the inner label row is highlighted on focus; the border lines are always rendered without attributes.

---

## BaseSeparationStyle

| Field  | Type  | Default    | Description                         |
|--------|-------|------------|-------------------------------------|
| `attr` | `int` | `A_NORMAL` | curses attribute                    |
| `char` | `str` | `─`        | character repeated to form the line |
| `fg`   | `int` | `-1`       | foreground color                    |
| `bg`   | `int` | `-1`       | background color                    |

---

## Color values

`fg` / `bg` / `focused_fg` / `focused_bg` accept any integer valid as a curses color index:

- `curses.COLOR_*` constants (0–7)
- 256-color palette indices (0–255)
- `-1` for the terminal's default color

See [markup.md](markup.md) for the full list of named colors available via inline tags.
