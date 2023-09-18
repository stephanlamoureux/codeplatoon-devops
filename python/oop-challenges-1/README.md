# OOP Challenges 1

Since you're on your way to becoming Object Oriented Programming whiz, it's time to throw some more involved challenges your way.

## Constructor Challenge I:  Customer Banking Accounts

In this challenge, you are creating functionality for users to open up a bank account from which they can deposit and withdraw funds.

>1. Create a new class for a **CustomerBankAccount**.
>2. Create fields for the Account Number, Balance, Customer Name, Email and Phone Number.
>3. Create methods to read, write and update each field.  Basically, some getters and setters.
>4. Create two additional methods:
>    1. One to allow the customer to **deposit** the funds (this should increment the balance field)
>    2. One to allow the customer to **withdraw** funds (this should deduct from the balance fields but not allow the withdrawal to complete if their founds are insufficient).
>5. Create some validation code using your getters and setters to confirm your code is working at each step of the user flow.  You should be able to show that a new user can be created and that this user can deposit and withdraw funds.

## Constructor Challenge II:  Browser Based Game Server

In this challenge, you are writing out object models for a web3 based gaming start up.  You'll need to be able to provide functionality for players hopping into a central hub, joining a game type and creating the appropriate character and selecting from a list of available character subclass.

>1. Create a base **HubPlayer** class with basic fields such as name, email, username, and player ID.
>2. Create an **ActivePlayer** subclass that will be instantiated when the player actively joins a game.  This player will now have a field for tracking the **points** they've earned in this game, a field for **Character ID list**, and a field to specify the selected **Character ID**.
>3. You'll now need to create a **Character** class, and give it some appropriate parameters, such as a character **name**.  Whatever game style and additional parameters is up to you.
>4. Since we want our players to have the choice to choose between different subclasses for their Character, you should now make a **subclass** for your character that will inherit from the Character class, while introducing new fields.  For example, if you were making a medieval hack and slash game, you might have different sub-classes that have different skills and weapon types.
>5. Build out the appropriate methods for **CRUDing** (Create Read Update Delete) all the necessary class fields to use for validating the user flow.  Users should be able to create a player account, become an ActivePlayer by hopping into a game, where they can walk through the flow of creating a character, and then choosing a subclass for that character.
