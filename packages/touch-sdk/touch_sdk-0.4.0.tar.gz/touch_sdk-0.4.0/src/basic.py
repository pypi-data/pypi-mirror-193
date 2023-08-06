from touch_sdk import Watch

class MyWatch(Watch):

    # def on_sensors(self, sensors):
    #     print(sensors)

    def on_custom_data(self, uuid, content):
        print(content)


    def on_tap(self):
        print('tap')

    def on_touch_down(self, x, y):
        print('touch down', x, y)

    def on_touch_up(self, x, y):
        print('touch up', x, y)

    def on_touch_move(self, x, y):
        print('touch move', x, y)

    def on_rotary(self, direction):
        print('rotary', direction)

    def on_back_button(self):
        self.trigger_haptics(1.0, 20)
        print('back button')

# watch = MyWatch()
# watch = MyWatch(custom_data={"4b574af1-72d7-45d2-a1bb-23cd0ec20c57": ((">3f", slice(None)),)})  # gyro
watch = MyWatch(custom_data={"4b574af5-72d7-45d2-a1bb-23cd0ec20c57": ((">ffqi", slice(None)),)})
watch.start()
