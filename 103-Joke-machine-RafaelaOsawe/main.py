from guizero import App, ButtonGroup, Text, PushButton

def jokes():
    if joke_choice.value == "Stick":
      display_joke.value = "What is brown and sticky? A stick!"
    if joke_choice.value == "Fluff":
      display_joke.value = "What's pink and fluffy? Pink Fluff. What's Blue and Fluffy? - Pink Fluff holding it's breath."
    if joke_choice.value == "Chicken":
      display_joke.value = ("What does a mummy chicken say to her smart chick? - You are egg-cellent!")
    if joke_choice.value == "Frog":
      display_joke.value = "What do you call a 100-year-old toad? - An old croak."

app = App()
message = Text(app, text="Choose a joke from the list below:")
joke_choice = ButtonGroup(app, options=["Stick", "Fluff", "Chicken", "Frog"])
joke_button = PushButton(app, command=jokes, text=("Show joke"))
display_joke = Text(app, "Waiting for a joke...")

app.display()