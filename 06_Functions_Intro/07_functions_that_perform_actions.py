def banner_text(text):
    screen_width = 60
    if len(text) > screen_width - 4:
        print("EEK!!")
        print("the text is too long to fit in the specified width")
    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output = f"**{centred_text}**"
        print(output)
        

def main():
    banner_text("*")
    banner_text("Welcome")
    banner_text("nog meer testen")
    banner_text("*")


if __name__ == "__main__":
    main()