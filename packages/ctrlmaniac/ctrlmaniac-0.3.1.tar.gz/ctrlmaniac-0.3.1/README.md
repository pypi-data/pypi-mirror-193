# Davide Di Criscito

```python
class CtrlManiac:
    """CtrlManiac because i overuse the ctrl key."""

    def __init__(self):
        """My specifications."""
        self.name = "Davide"
        self.surname = "Di Criscito"
        self.nickname = "Dave"
        self.pronouns = (
            "He",
            "Him",
        )

        self.languages_spoken = ["it_IT", "en_US", "en_GB"]

        self.description = "I'm a full-stack web developer! Eager to learn new things, always with one new project in mind, passionate about programming with computers."

        self.websites = [
            "https://ctrlmaniac.me",
            "https://www.linkedin.com/in/dcdavide/",
        ]

        self.hobbies = [
            "coding",
            "hiking",
            "photography",
            "watching movies & TV series",
            "listening to music",
            "reading books and comics",
            "going out with my friends and have fun",
        ]

        self.coding_languages = [
            "Python",  # I simply love it
            "JavaScript",
            "Typescript",
            "Java",
            "Golang",
        ]

        self.favourite_tools = [
            "poetry",  # makes it simpler to manage a python project
            "black",  # chooses a coding style for me and makes my code pretty
            "isort",  # sorts python imports so that everything is really clear
            "flake8",  # tells me whether I've made a mistake
            "pydocstyle",  # helps me write better documentation
            "yarn",  # I love it for the workspace feature
            "lerna",  # I use it to manage my monorepos
            "prettier",  # chooses a coding style for me and makes my code pretty
        ]

        self.IDEs = [
            "VScode",  # because it's awesome!
        ]

    def greet(self) -> None:
        """Say hi."""
        print(
            f"Hi! I'm {self.name} {self.surname}, but you can call me {self.nickname}."
        )
        print(self.description)
        print(f"You can know more about me by visiting my website: {self.websites[0]}")
```

## Fun Fact

You can install this package via pip by running `pip install ctrlmaniac` and then excecute the program by typing into your terminal `python -m ctrlmaniac` and see the output!

Or import the package:

```
>>> from ctrlmaniac import ctrlmaniac
>>> me = ctrlmaniac.CtrlManiac()

>>> me.greet()
Hi! I'm Davide Di Criscito, but you can call me Dave.
I'm currently an Artisan, soon-to-be a full-stack web developer!
You can know more about me by visiting my website: https://ctrlmaniac.me
```

## Stats

[![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=ctrlmaniac)](https://github.com/anuraghazra/github-readme-stats)
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=ctrlmaniac)](https://github.com/anuraghazra/github-readme-stats)
