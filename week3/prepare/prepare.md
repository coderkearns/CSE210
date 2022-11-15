> What is encapsulation and why is it important?

Encapsulation is a technique of "hiding" data behind an abstraction, likely inside of a class. The user does not need to worry about a separate store of data controlled by an abstraction, the abstraction can own its own data. (e.g. `BankAccount::deposit(10)` rather than `bank_account.transactions.push({ "type": deposit, "amount": 10})`)

It also helps to "protect" data. While Python only supports an underscore (e.g. `self._transactions`) as a means of signaling that some attribute is private, most languages allow `private` and `public` modifiers to protect attributes. (e.g, `private int[] transactions`)

Encapsulation also make development far easier. Perhaps I know there is an issue with my transaction system. If I did not use encapsulation, I may need to search through dozens of files to find the issue. If I did use encapsulation, I know it must be in the `Transaction` class code, or *maybe* the `BankAccount` code. Understanding a new codebase that uses this principle is also far easier.
