# Inline Markup

`w.text()` supports inline style tags directly inside the string. Tags are written as `[#TAG]` and apply from that point forward until `[#RESET]` or another tag overrides them.

```python
w.text(text="Normal [#BOLD]bold[#RESET] normal")
w.text(text="[#CYAN]Time:[#RESET] [#MAGENTA]12:34:56[#RESET]")
w.text(text="[#BOLD][#RED]Error:[#RESET] something went wrong")
```

Tags stack with the widget's base `style=`: `[#RESET]` restores to the base style, not to terminal defaults.

---

## Color tags

### Standard (always available)

| Tag          | Color   |
|--------------|---------|
| `[#BLACK]`   | Black   |
| `[#RED]`     | Red     |
| `[#GREEN]`   | Green   |
| `[#YELLOW]`  | Yellow  |
| `[#BLUE]`    | Blue    |
| `[#MAGENTA]` | Magenta |
| `[#CYAN]`    | Cyan    |
| `[#WHITE]`   | White   |

### Bright / 256-color (8–15)

| Tag                           | Color         |
|-------------------------------|---------------|
| `[#GRAY]` / `[#GREY]`         | Dark gray     |
| `[#BRIGHT_RED]`               | Bright red    |
| `[#BRIGHT_GREEN]` / `[#LIME]` | Bright green  |
| `[#BRIGHT_YELLOW]`            | Bright yellow |
| `[#BRIGHT_BLUE]`              | Bright blue   |
| `[#PINK]`                     | Pink          |
| `[#BRIGHT_CYAN]`              | Bright cyan   |
| `[#BRIGHT_WHITE]`             | Bright white  |

### Extended 256-color

| Tag                         | Tag               | Tag             |
|-----------------------------|-------------------|-----------------|
| `[#ORANGE]`                 | `[#LIGHT_ORANGE]` | `[#GOLD]`       |
| `[#PURPLE]`                 | `[#VIOLET]`       | `[#INDIGO]`     |
| `[#NAVY]`                   | `[#TEAL]`         | `[#DARK_GREEN]` |
| `[#MAROON]` / `[#DARK_RED]` | `[#BROWN]`        | `[#OLIVE]`      |
| `[#SALMON]`                 | `[#CORAL]`        | `[#ROSE]`       |
| `[#SKY_BLUE]`               | `[#LIGHT_BLUE]`   | `[#MINT]`       |
| `[#LAVENDER]`               | `[#DARK_GRAY]`    | `[#LIGHT_GRAY]` |

---

## Attribute tags

| Tag            | Effect                      |
|----------------|-----------------------------|
| `[#BOLD]`      | Bold                        |
| `[#DIM]`       | Dim                         |
| `[#ITALIC]`    | Italic (terminal-dependent) |
| `[#UNDERLINE]` | Underline                   |
| `[#REVERSE]`   | Reverse fg/bg               |
| `[#BLINK]`     | Blink (terminal-dependent)  |

---

## Reset

| Tag        | Effect                             |
|------------|------------------------------------|
| `[#RESET]` | Restore to the widget's base style |

---

## Notes

- Tags are case-insensitive: `[#bold]` and `[#BOLD]` are equivalent.
- Unknown tags are silently ignored.
- Extended colors require a 256-color terminal (`TERM=xterm-256color` or similar).
- `[#ITALIC]` and `[#BLINK]` depend on terminal support.
