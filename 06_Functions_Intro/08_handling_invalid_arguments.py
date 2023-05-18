def banner_text(text):
    """
    Prints a banner containing the text.
    """
    screen_width = 50
    if len(text) > screen_width:
        raise ValueError(f"String {text} is larger than {screen_width} characters.")
    if text == "*":
        print(f"{'#' * screen_width}")
    center_text = text.center(screen_width)
    print(center_text)
    

def mai_banner():
    """
    Prints a banner containing the text
    """
    banner_text("*")
    banner_text("TESTING")
    banner_text("fwohedfiugwaeuifytbweinocruoweycfgnweyimryoicnuwfigwuoaeuvcoigrulieuwfnlvgcriluwnfgrkwhsef")
    banner_text("*")
    
if __name__ == "__main__":
    mai_banner()