label start:
    "Hi, if you added an extension in the game/extensions subdirectory, it should have loaded."
    "Exiting soon..."
    $ renpy.quit()

screen yesno_prompt(message = "Are you sure?", yes_action = [], no_action = []):
    style_prefix 'yesno'
    image 'black'
    vbox:
        text message
        textbutton "Yes":
            action yes_action
        textbutton "No":
            action no_action

style yesno:
    align (0.5, 0.5)
style yesno_button is yesno
style yesno_text is yesno
style yesno_vbox is yesno
