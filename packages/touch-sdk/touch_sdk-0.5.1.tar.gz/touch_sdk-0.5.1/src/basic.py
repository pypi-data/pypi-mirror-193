from touch_sdk import Watch

class PPGWatch(Watch):
    custom_data = {
        "4b574af5-72d7-45d2-a1bb-23cd0ec20c57": ">ffqi"
    }

    def on_custom_data(self, uuid, content):
        print(content)

watch = PPGWatch()
watch.start()