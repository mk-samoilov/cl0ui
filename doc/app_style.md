# App Style

The application window style is passed to `cl0ui.run()` via the `style=` parameter.

```python
import cl0ui
from cl0ui.stylesheets import BaseAppStyle

class MyAppStyle(BaseAppStyle):
    smoothed_frame = True
    frame_fg = curses.COLOR_CYAN
    title_fg = curses.COLOR_CYAN

cl0ui.run(draw_frame_callback=frame, title="My App", style=MyAppStyle())
```

Without `style=`, all defaults apply.

---

## BaseAppStyle

| Field | Type | Default | Description |
|---|---|---|---|
| `smoothed_frame` | `bool` | `False` | Rounded corners (`╭╮╰╯`) vs sharp (`┌┐└┘`) |
| `frame_attr` | `int` | `A_NORMAL` | curses attribute for the border lines |
| `frame_fg` | `int` | `-1` | Border foreground color |
| `frame_bg` | `int` | `-1` | Border background color |
| `title_attr` | `int` | `A_BOLD` | curses attribute for the title text |
| `title_fg` | `int` | `-1` | Title foreground color |
| `title_bg` | `int` | `-1` | Title background color |

---

## Frame styles

**Sharp** (`smoothed_frame = False`, default):
```
┌─ My App ───────────────────┐
│                            │
└────────────────────────────┘
```

**Rounded** (`smoothed_frame = True`):
```
╭─ My App ───────────────────╮
│                            │
╰────────────────────────────╯
```
