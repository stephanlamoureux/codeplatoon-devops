# OOP Challenges II
Since you're on your way to becoming Object Oriented Programming whiz, it's time to throw some more involved challenges your way.
Let's expand on the previous set of challenges from [OOP Challenges I](https://github.com/codeplatoon-devops/oop-challenges-1) by adding a second set of requirements to each challenge.

## Inheritance Challenge:  Vehicle Catalog
>1. Create a base class of a Vehicle, then create a Car subclass that inherits from this base class.
>2. Create sub-subclass, a specific type of car, like a Model, that inherits from the Car class.
>    1. You will want to add attributes specific to that car, such as model name, steering, catalog description, top speed, average mileage, available colors, brand or make.
>    2. Write the necessary functions to output a data object containing all the chosen attributes as if a customer were selecting options when placing an order. 
>3. Create another sub-class for Vehicle, this time for something like a Motorcycle, Boat, Aircraft, whatever.
>4. You'll make one more sub-subclass, this time for your new Vehicle type.  Let's give it some additional attributes that a Car or car subclass wouldn't have.

## Constructor Challenge I Part II:  Customer Banking Account Categories
You should already have the following from the previous challenge:
>1. CustomerBankAccount class. 
>2. Fields for the Account Number, Balance, Customer Name, Email and Phone Number.
>3. Getters and setters for each field.
>4. Methods for depositing and withdrawing funds.
>5. Code validation.

Let's now add the following:

>6. Now that you've learned about Class Inheritance, let's create some subclasses of the standard BankAccount.  First, let's create a StandardCustomerBankAccount with additional fields for tracking Silver Reward Points and tracking Reward Order Transactions.  Let's mock the Reward Order Transactions as a list of string objects for now.
>7. Create a new class VipCustomer that can earn both Silver and Gold reward points in additiona to also having Reward Order Transactions. 
>8. Create getters and setters for each new field, and implement some validation to confirm your code is working.
>9. Let's now create a new Rewards class to represent prizes that customers can exchange reward points for.  Fields should include the object name and object price in terms of both Silver and Gold points.
>10. We now need to create subclasses of the Rewards Class.  We want to be able to distinguish between tangible, physical objects that can be purchased, and digital purchases such as credits towards one's balance.
>        1. DigitalRewards should have a conversion rate.  Because Silver points and Gold points have different perceived values, they should reduce a customer's monetary balance at different rates.
>        2.  PhysicalRewards will need an inventory count, because they are not infinitely available like digital rewards are.
>        3.  Create getter, setter functions for all these new fields, and implement validation to confirm your code is working as intended.

## Constructor Challenge II Part II:  Browser Based Game Containers
You should have the following:
>1. HubPlayer class, ActivePlayer subclass
>2. Character class, some kind of sub character class
>3. Methods to create, read, update and delete all of these fields.

You probably mocked out the part of the flow where a player hops into a game, triggering the ActivePlayer instantiation, and the flow for selecting a character class and subclass.  Let's start by picking up where we left off there.
>1. Create a proper GameContainer class with fields for a game name and/or game type.  You don't need to get too wild with these, we just need to be able to distinguish between at least two different games.
>2. Create an appropriate GameContainer subclass descriptively suited for the parameters you gave your Character and character subclass.  Update all related methods to allow for the creation, reading, updating (deleting optional but unnecessary for the challenge), of this GameContainer subclass.  You'll need to implement some functionality for a HubPlayer to instantiate a different ActivePlayer instance based on the GameContainer they select.
>3. Create a second GameContainer subclass of a different genre, with different fields to share with the ActivePlayer.  For example, if the player earned points in the first game, maybe they earn credits in this second game.
>4. Either create a new Character class, or simply create new character subclasses if you want to allow players to use this same Character across different games.  Just be sure to set the proper implementations such that the character can only load the subclasses relevant to the GameContainer selected.  A Character can have the same name in a racing game universe as they would in a multiplayer party game universe.  But a subclass in one, such as a driver type using a specific vehicle, wouldn't make sense for a board game where the subclasses may be distinguished by the game piece used to traverse the board.  
>5. Just as before, implement all the necessary CRUD functionality to demonstrate a user's ability to switch GameContainers and character subclasses.
