import sublime
import sublime_plugin

class AutoScrollHandler:
    is_scrolling = False
    speed = 20  # 初始速度設為 20ms，滾動頻率高
    timeout_id = None
    scroll_distance = 2  # 每次捲動距離設為 2 像素

    @classmethod
    def start(cls, view):
        if not cls.is_scrolling:
            cls.is_scrolling = True
            cls.scroll(view)

    @classmethod
    def stop(cls):
        if cls.is_scrolling:
            cls.is_scrolling = False
            if cls.timeout_id:
                sublime.cancel_timeout(cls.timeout_id)
                cls.timeout_id = None

    @classmethod
    def scroll(cls, view):
        if cls.is_scrolling:
            # 使用 viewport_position 平滑向下滾動
            viewport_position = view.viewport_position()
            new_position = (viewport_position[0], viewport_position[1] + cls.scroll_distance)
            view.set_viewport_position(new_position, False)
            cls.timeout_id = sublime.set_timeout_async(lambda: cls.scroll(view), cls.speed)

    @classmethod
    def increase_speed(cls):
        # 加速時減少間隔時間，但保持平滑
        cls.speed = max(10, cls.speed - 5)  # 最小速度設為 10ms
        cls.scroll_distance = min(10, cls.scroll_distance + 1)  # 增加滾動距離，最大距離為 10

    @classmethod
    def decrease_speed(cls):
        # 減速時增加間隔時間
        cls.speed = min(100, cls.speed + 5)  # 最大速度設為 100ms
        cls.scroll_distance = max(1, cls.scroll_distance - 1)  # 減少滾動距離，最小距離為 1

class AutoScrollCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if AutoScrollHandler.is_scrolling:
            AutoScrollHandler.stop()
        else:
            AutoScrollHandler.start(self.view)

class AutoScrollIncreaseSpeedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        AutoScrollHandler.increase_speed()
        sublime.status_message(f"AutoScroll Speed: {AutoScrollHandler.speed}ms, Distance: {AutoScrollHandler.scroll_distance}")

class AutoScrollDecreaseSpeedCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        AutoScrollHandler.decrease_speed()
        sublime.status_message(f"AutoScroll Speed: {AutoScrollHandler.speed}ms, Distance: {AutoScrollHandler.scroll_distance}")
