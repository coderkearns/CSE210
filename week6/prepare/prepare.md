> What is maintainability and why is it important?

Maintainability is important to allow your code to grow and change over time. If you write code that is not designed for maintainability, it might be faster in the short term, but as you add features and fix bugs it begins take *exponentially longer* to make changes. You may have to dig through dozens of files of sequential code, or modify code in a dozen places to allow for the new feature.

An example of unmaintainable code might be hardcoding all the `Action()` classes into one large `Script()`-like function. Sure, it would be easy to write at first, you just write each step one at a time. However, once you have an obscure bug you have no idea where to look. You have to debug almost the entire function in order to fix simple problems.

Our code is the opposite, a good example of maintainability. It separates the various things the program should be doing into services and actions that are self-contained and store similar functionality, allowing us to know where to look. Do we have a rendering bug? We know to check the `VideoService()` and rendering Actions.
