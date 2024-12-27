# Sublime Auto Scroll Plugin

A Python plugin for **Sublime Text** to enable smooth and customizable auto-scrolling functionality.

## Features

- **Start/Stop Auto-Scrolling:** Toggle auto-scroll with a single shortcut.
- **Adjustable Speed:** Increase or decrease scrolling speed using shortcuts.
- **Smooth Scrolling:** Configurable scrolling frequency and distance for a seamless experience.

## Installation

1. Save the `auto_scroll.py` file to your Sublime Text `Packages/User/` directory.
2. Restart Sublime Text to load the plugin.

### Setting Up Key Bindings

To use the plugin, add the following key bindings in `Preferences > Key Bindings`:

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


Usage
Start/Stop Auto-Scrolling: Press Ctrl + Alt + S to toggle auto-scrolling.
Increase Speed: Press Ctrl + Alt + Up to reduce the delay and make scrolling faster.
Decrease Speed: Press Ctrl + Alt + Down to increase the delay and make scrolling slower.
Configuration
The following parameters can be adjusted in the plugin code (auto_scroll.py):

Initial Speed: Default is 20ms. Adjust this in AutoScrollHandler.speed.
Minimum Speed: Set to 10ms for ultra-fast scrolling.
Scrolling Distance: Default is 2 pixels. Modify AutoScrollHandler.scroll_distance to suit your needs.
Contributing
Feel free to fork this repository and submit pull requests to improve the plugin. Suggestions and feedback are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for details.

功能
啟動/停止（Toggle）：

按下 Ctrl + Alt + S 開始或停止自動滾動。
滾動方向：

從現在位置向尾行滾動。

加速/減速：

按下 Ctrl + Alt + Up：減少間隔時間，加速滾動。
按下 Ctrl + Alt + Down：增加間隔時間，減慢滾動。

用 set_viewport_position 直接控制視窗位置
每次增加 Y 座標來實現向下捲動


啟動滾動：

按下 Ctrl + Alt + S 開始滾動，速度為每 500 毫秒滾動 5 像素。
調整速度：

按下 Ctrl + Alt + Up 減少延遲，加速滾動（最小間隔為 5 毫秒）。
按下 Ctrl + Alt + Down 增加延遲，減慢滾動（最大間隔為 2000 毫秒）。
停止滾動：

再次按下 Ctrl + Alt + S 停止滾動。


改進參數
捲動速度（speed）：

建議設置為 20ms 至 50ms，確保滾動頻率足夠高，使動畫更流暢。
每次捲動距離（distance）：

每次捲動距離設置為 2 或 3 像素，這樣滾動幅度不會過大，避免跳動感。

改進點
速度設置：

初始速度為 20ms，更高頻率保證平滑。
最小速度設置為 10ms，避免過快滾動導致難以閱讀。
距離設置：

每次捲動距離設置為 2 像素，確保滾動自然。
可通過加速快捷鍵增加至 10 像素，適應不同需求。
加速/減速調整：

加速同時減少速度間隔（更快滾動）並增加距離（更遠滾動）。
減速時反向操作，讓滾動更加靈活。
快捷鍵配置
json

[
    {
        "keys": ["ctrl+alt+s"],  // 啟動 / 停止自動滾動
        "command": "auto_scroll"
    },
    {
        "keys": ["ctrl+alt+up"],  // 加速滾動
        "command": "auto_scroll_increase_speed"
    },
    {
        "keys": ["ctrl+alt+down"],  // 減速滾動
        "command": "auto_scroll_decrease_speed"
    }
]