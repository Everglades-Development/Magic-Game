# Contributing

This is for code contributions and PR guidelines.

## Basic Guidelines

### Use an IDE.
Ideally use [PyCharm](https://www.jetbrains.com/pycharm/download/), or [Visual Studio](https://visualstudio.microsoft.com/vs/). Some text editors, like VS Code will also be good enough.

### Always test your changes.
Do not submit a PR without checking that it works.  
And when creating a PR, make sure it has a detailed name and description, and that it works correctly in-game. 


## Formatting Guidelines

### Follow the style guidelines.
This means:
- 4 space indents.
- `camelCase` or `PascalCase`.
- Limited application of underscores.
- Update .gitattributes and .gitignore if necessary.
- Use a venv to install frameworks (For instructions, [here](https://docs.python.org/3/library/venv.html).


### Do not use a different python game engine.
If you include pyglet, arcade, etc. your PR will be deleeted. Pygame is a good enough engine to create our planned game. 

## Final Notes
If you would like your name to appear in the game's credits, add it to the [list of contributors](https://github.com/Anuken/Mindustry/blob/master/core/assets/contributors) as part of your PR.
