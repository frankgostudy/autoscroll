# Sublime Auto Scroll Plugin

A Python plugin for **Sublime Text** that enables smooth and customizable auto-scrolling functionality.

## Features

### Core Functions
- Start/Stop auto-scrolling with `Ctrl + Alt + S`
- Adjust scrolling speed with `Ctrl + Alt + Up/Down`
- Smooth scrolling with configurable frequency and distance
- Downward scrolling from current position
- Direct viewport position control using `set_viewport_position`

### Performance Parameters
- Initial Speed: 20ms delay (recommended range: 20-50ms)
- Minimum Speed: 10ms (prevents unreadable rapid scrolling)
- Scrolling Distance: 2 pixels per scroll (adjustable up to 10 pixels)
- Maximum Delay: 2000ms for very slow scrolling

## Installation

1. Save `auto_scroll.py` to Sublime Text's `Packages/User/` directory
2. Restart Sublime Text

### Key Bindings Setup

Add to `Preferences > Key Bindings`:

```json
[
    {
        "keys": ["ctrl+alt+s"],
        "command": "auto_scroll"
    },
    {
        "keys": ["ctrl+alt+up"],
        "command": "auto_scroll_increase_speed"
    },
    {
        "keys": ["ctrl+alt+down"],
        "command": "auto_scroll_decrease_speed"
    }
]
```

### Logitech Mouse Setup
For enhanced control, you can configure Logitech mice (e.g., Anywhere 2) as follows:
- Middle button: Map to `Ctrl + Alt + S` to toggle auto-scroll
- Scroll wheel right: Map to `Ctrl + Alt + Up` to increase speed
- Scroll wheel left: Map to `Ctrl + Alt + Down` to decrease speed

## Usage

### Basic Controls
- Toggle Auto-scroll: `Ctrl + Alt + S`
- Increase Speed: `Ctrl + Alt + Up`
- Decrease Speed: `Ctrl + Alt + Down`

### Speed Control Details
- Speed increases by reducing delay interval
- Speed decreases by increasing delay interval
- Speed adjustments also modify scrolling distance
  - Faster = Larger distance
  - Slower = Smaller distance

## Development Notes

### Plugin Creation
1. Access via Tools > Developer > New Plugin
2. Insert auto_scroll.py code
3. Save in appropriate directory

### Optimization Points
- Smooth animation through high-frequency updates
- Balanced scroll distance for natural movement
- Flexible speed adjustment system
- Direct viewport control for precise scrolling

## Contributing

Pull requests welcome for plugin improvements. Please submit issues for bugs or feature requests.

## License

MIT License - See LICENSE file for details
