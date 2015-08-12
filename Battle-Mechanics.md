WrestleVania - A wrestling RPG
==============================

WrestleVania is a new wrestling RPG created by /u/shashwat986 and /u/rick2047. It is (very) loosely based on the Mini Six system by Anti-Paladin games.

This game mechanic can be used in various settings, with minor modifications, however it has been made with wrestling in mind. The mechanic can, broadly, be used to have all kinds of fights:

* Regular wrestling matches
* Tag-team matches
* Ladder matches
* Multiple fighters at the same time (ex. Royal Rumble, Fatal Fourway)
* Dragonball Z fights
* ...

In fact, if the players using WrestleVania only want to fight, there is no real requirement of a Game Master, and it can effectively become GM-less.

Dice Basics:
------------

This game uses regular six-sided dice. One d6 die per player is specifically designated the WhatNext die, and is rolled by each player when required.

Character Creation:
-------------------

Each character is expected to be a wrestler in the organization(s) of their/the GM's choice. The characters may be loosely put into two categories: Face and Heel (although this is entirely dependent on the way the story is being created). In general, you can consider Face/Heel to be equivalent to Good/Evil alignments in D&D and the like. Similarly, characters can have Chaotic/Neutral/Lawful alignments too.

###Nurtured Attributes:

Each character has four attributes, which can be loosely translated to the following:

* Toughness - Health/Hit-Points
* Stamina - Recovery Power
* Strength - Attack Potential
* Counter - Defense Potential

Each player is given 10d6 to distribute among the attributes.
No attribute can go above 4d6. No stat can be less than 0.5 pips.

Users can also choose to "Split the Dice". Each die is equal to 3.5 pips, which carry a constant bonus.

Example progression: 1d6, 1d6 + 0.5, 1d6 + 1, ..., 1d6 + 2.5, 1d6 + 3, 2d6

A character's toughness is not related to die-rolls, but depends on the number of dice you allocate to it.

A player's  `Toughness = 6 * (the number of dice allocated to toughness)`

###Natural Attributes:

Each player also has 2 attributes not directly under their control:

* Degree (initially equal to 1. Degree cannot drop below 0)
* Momentum (initially equal to 0. Momentum cannot drop below 0, and cannot exceed 3)

Degree is initially set to 1. It increases and decreases based on the Charisma die. It cannot drop below 0.
Momentum is initially set to 0. It increases and decreases based on the progression of the fight. It cannot go above 3, and cannot drop below 0.


The Game Mechanics:
-------------------

###Non-Combat Interactions:
For non-combat challenges, {{SOMETHING HAPPENS}}.

###Combat:

There are certain options available to a player in every round of combat:

* Making an Attack
* Performing an Action
* Full-Dodging

####Making an attack:

Each time a player wants to make an attack, he/she needs to provide the following values: Attack Category, Move Speed, and Move Damage.

Attack moves fall in 4 categories:
* Punch
* Kick
* Leap
* Grapple

(check out the _Battle_ section to see how attack moves modify damage dealt)

Speed and Damage are restricted by the following constraints:

* For each move, `Speed + Damage = 5 + 10 * Degree`
* Speed and Damage, both, have to be whole numbers (0, 1, 2, 3, ...)

####Performing an Action:

If a user wishes to perform any action, he/she make the following check by rolling the WhatNext die:

| Status       | Success if               |
|--------------|--------------------------|
| If Fresh     | WhatNext > 1 (2,3,4,5,6) |
| If Tired     | WhatNext > 2 (3,4,5,6)   |
| If Exhausted | WhatNext > 3 (4,5,6)     |
| If Zombie    | WhatNext > 4 (5,6)       |

Note that the GM may modify the success values in this table based on the difficulty of the action. In addition, each action may be broken into a certain number of stages, which have to be completed before the action is over. There may also be some events associated with success/failure/attempt at clearing a stage/action.

#####<u>Examples of Actions:</u>

#####Tag Team Matches:

In a tag-team match, tagging-in the active fighter's team-mate can be considered a one-stage action. If the GM wishes to implement Hot-Tags, the event on-success can be: the incoming player gets a speed-boost of 3 * degree on his/her first attack.

#####Ladder Matches:

In a ladder match, climbing up the ladder to get the title-belt can be considered a 5-stage action. Every time a player attempts to clear a stage in this action, and is attacked, he/she fails (on-attempt event).

#####Fight on a Tight-Rope:

Every combat move has to be preceded by a one-stage action testing balance on the tight-rope. If a player fails, he/she loses 10 Hit-Points. If the player succeeds, he/she is allowed to make a combat move.

####Full-Dodging

If a player chooses, he/she may make a full-dodge on one turn. If he/she is attacked by the opponent on that turn, the opponent's damage on the player is doubled. In return, at the end of the combat round, the player's momentum increases by 1.

###HP and Status changes:

This system uses an HP (Hit-Points) mechanic. The initial hitpoints are calculated as follows:

```
Initial HP = 4 * Toughness
```

Based on the current HP of the fighter, he/she may have one of the following condition statuses.

* Fresh
* Tired
* Exhausted
* Zombie

| Condition                      | Status                     |
|--------------------------------|----------------------------|
| If current HP > 3 * Toughness  | Fresh                      |
| If current HP > 2 * Toughness  | Tired                      |
| If current HP > 1 * Toughness  | Exhausted                  |
| If current HP > 0              | Zombie                     |
| If current HP = 0              | The player is Knocked Out! |

###Audience, Charisma, and Momentum:

The charisma roll `(1d6 + the player's momentum)` will be made at the end of every combat round for all active players. On a value `>= 5`, the audience gets pumped, and wants to see more action from that player. That player then rolls his/her WhatNext die. The degree of the player increases as per the following chart:

| Status       | Success if               |
|--------------|--------------------------|
| If Fresh     | WhatNext > 1 (2,3,4,5,6) |
| If Tired     | WhatNext > 2 (3,4,5,6)   |
| If Exhausted | WhatNext > 3 (4,5,6)     |
| If Zombie    | WhatNext > 4 (5,6)       |

If the WhatNext roll succeeds, the momentum of the player reduces by 1.

On a value `<= 2` on the charisma roll, the audience gets bored, and wants to see more drama from that player. The degree of the player reduces by 1 (irrespective of the status).

If the HP difference between any two players is greater than `6 * (#toughness dice + #stamina dice)`, the weaker player becomes the "underdog". If the player's degree is less than 4, his/her degree increases to 4.

###Battle - Sequence of Moves:

0. Players choose their moves. Inform GM without showing the other player(s). Players tell GM by providing the move-type, move speed, and move damage. Players may also inform the GM that they will be performing an action. On the basis of both players' information, the GM releases the move order.

   One easy way of showing the moves to the GM is by using tokens to represent Speed (since Degree is known, and the GM can calculate the Damage given the Speed), and a 6d die to represent what the player wishes to do (1 = Punch, 2 = Kick, 3 = Grapple, 4 = Leap, 5 = Action, 6 = Full-Dodge).

1. Move with higher Speed goes first (a higher value on a 1d6 die is used to break ties).

2. Move has (Strength + Speed + Matching) power. If this power > (Counter + Enemy's Speed), the move hits, else the move fails. (If equal, higher speed wins)

3. Matching is based on category of moves:

   ... > Leap > Punch > Kick > Grapple > Leap > Punch > ...

   ```
   +------------------------------------------------------------------+
   |                          |            Defending Move             |
   |                          |---------------------------------------|
   |                          |  Punch  |  Kick   | Grapple |  Leap   |
   |--------------------------+---------+---------+---------+---------|
   |                | Punch   |     0   |   +3    |    0    |    -3   |
   |                |---------+---------+---------+---------+---------|
   |                | Kick    |    -3   |    0    |   +3    |     0   |
   | Attacking Move |---------+---------+---------+---------+---------|
   |                | Grapple |     0   |   -3    |    0    |    +3   |
   |                |---------+---------+---------+---------+---------|
   |                | Leap    |    +3   |    0    |   -3    |     0   |
   +------------------------------------------------------------------+
   ```

   * +3 if Punch vs. Kick
   * +3 if Kick vs. Grapple
   * +3 if Grapple vs. Leap
   * +3 if Leap vs. Punch
   * -3 if Kick vs. Punch
   * -3 if Punch vs. Leap
   * -3 if Leap vs. Grapple
   * -3 if Grapple vs. Kick
   * 0 otherwise

4. If the move hits, it does `(Damage + Strength)` damage, and HP of the opponent reduces.

5. Each player rolls the stamina dice and adds the total to their HP.

6. The Audience makes a decision (i.e. the charisma roll is made, and the degrees of the players may change)







