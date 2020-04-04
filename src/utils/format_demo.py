import format

if __name__ == "__main__":
    json = format.AlfredJson()
    json.push_back(format.Item("next_input", "demo_title", "demo_subtitle", "./demo_icon_path"))
    print(json.dump())