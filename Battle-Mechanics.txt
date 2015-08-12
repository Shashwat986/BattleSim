WrestleVania - A wrestling RPG
==============================

WrestleVania is a new wrestling RPG created by /u/shashwat986 and /u/rick2047. It is (very) loosely based on the Mini Six system by Anti-Paladin games.

This game mechanic can be used in various settings, with minor modifications (mentioned in boxes along this document), however it has been made with wrestling in mind. The mechanic can, broadly, be used to have all kinds of fights:

* Regular wrestling matches
* Tag-team matches
* Ladder matches
* Multiple fighters at the same time (ex. Royal Rumble, Fatal Fourway)
* Dragonball Z fights
* ...

In fact, if the players using WrestleVania only want to fight, there is no real requirement of a Game Master, and it can effectively become GM-less.

Dice Basics:
------------

This game uses regular six-sided dice. One d6 die is controlled by the GM (or the other players). This die represents the charisma effect of the players on the audience.

Character Creation:
-------------------

Each character is expected to be a wrestler in the organization(s) of their/the GM's choice. The characters may be loosely put into two categories: Face and Heel (although this is entirely dependent on the way the story is being created). In general, you can consider Face/Heel to be equivalent to Good/Evil alignments in D&D and the like. Similarly, characters can have Chaotic/Neutral/Lawful alignments too.

###Controllable Attributes:

Each character has four attributes, which can be loosely translated to the following:

* Toughness - Health/Hit-Points
* Stamina - Recovery Power
* Strength - Attack Potential
* Counter - Defense Potential

Each player is given 10d6 to distribute among the attributes.
No attribute can go above 4d6. No stat can be less than 0.5 pips.

Users can also choose to "Split the Dice". Each die is equal to 3.5 pips, which carry a constant bonus.
Example progression: 1d6, 1d6 + 0.5, 1d6 + 1, ..., 1d6 + 3, 1d6 + 3.5, 2d6

A character's toughness is not related to die-rolls, but depends on the number of dice you allocate to it.
Your Toughness = 6 * (the number of dice allocated to toughness)

###Uncontrollable Attributes:

Each player also has 2 attributes not under their control:

* Degree (initially equal to 1)
* Momentum (initially equal to 0)

Degree increases and decreases based on the Charisma die.
Momentum increases and decreases based on the fight.


The Game Mechanics:
-------------------

For non-combat challenges, {{SOMETHING HAPPENS}}.

###Combat:

####Making an attack:

Each time a player wants to make an attack, he/she needs to provide the following values: Move Category, Move Speed, and Move Damage.

Moves fall in 4 categories:
* Punch
* Kick
* Leap
* Grapple

Speed and Damage are restricted by the following constraint:
* For each move, Speed + Damage should be equal to 5 + 10 * Player Degree

####HP and Status changes:

This system uses an HP (Hit-Points) mechanic. The initial hitpoints are calculated as follows:

Initial HP = 4 * Toughness

Based on the current HP of the fighter, he/she may have one of the following condition statuses.

* Fresh
* Tired
* Exhausted
* Zombie

+--------------------------------+----------------------------+
| Condition                      | Status                     |
+--------------------------------+----------------------------+
| If current HP > 3 * Toughness  | Fresh                      |
| If current HP > 2 * Toughness  | Tired                      |
| If current HP > 1 * Toughness  | Exhausted                  |
| If current HP > 0              | Zombie                     |
| If current HP = 0              | The player is Knocked Out! |
+--------------------------------+----------------------------+

###Audience, Charisma, and Momentum:

The charisma die (1d6 + momentum) will roll at the end of every combat turn for each player. On a roll = 5-6, the audience gets pumped, and wants to see more action from that player. The degree of the player increases as per the following chart:

+--------------+-------------------+
| If Fresh     | 1d6 > 0 (always)  |
| If Tired     | 1d6 > 2 (3,4,5,6) |
| If Exhausted | 1d6 > 4 (5,6)     |
| If Zombie    | 1d6 > 6 (never)   |
+--------------+-------------------+

On a roll = 1, the audience gets bored, and wants to see more drama from that player. The degree of the player reduces by 1 or 2 (by die roll).

If the HP difference between any two players is greater than 6 * (#toughness dice + #stamina dice), the weaker player becomes the 'underdog'. His/her degree increases to 4.

###Battle:

0. Players choose their moves. Inform GM without showing the other player(s). Players tell GM by providing the move type, move speed, and move damage. GM releases move order.

1. Move with higher Speed goes first (a higher value on a 1d6 die is used to break ties).

2. Move has (Strength + Speed + Matching) power. If this power > (Counter + Enemy's Speed), the move hits, else the move fails. (If equal, higher speed wins)

3. Matching is based on category of moves:
   ... > Leap > Punch > Kick > Grapple > Leap > Punch > ...

   +----------------+---------+-------+------+---------+------+
   |                          |        Defending Move         |
   +                          +-------+------+---------+------+
   |                          | Punch | Kick | Grapple | Leap |
   +----------------+---------+-------+------+---------+------+
   |                | Punch   |   0   |  +3  |   0     |  -3  |
   +                +---------+-------+------+---------+------+
   | Attacking Move | Kick    |   -3  |  0   |    +3   |   0  |
   +                +---------+-------+------+---------+------+
   |                | Grapple |   0   |  -3  |    0    |  +3  |
   +                +---------+-------+------+---------+------+
   |                | Leap    |   +3  |   0  |   -3    |   0  |
   +----------------+---------+-------+------+---------+------+


   +3 if Punch vs. Kick
   +3 if Kick vs. Grapple
   +3 if Grapple vs. Leap
   +3 if Leap vs. Punch
   -3 if Kick vs. Punch
   -3 if Punch vs. Leap
   -3 if Leap vs. Grapple
   -3 if Grapple vs. Kick
   0 otherwise

4. If the move hits, it does (Damage + Strength) damage, and HP of the opponent reduces.

5. Each player rolls the stamina dice and adds the total to their HP.

6. The Audience makes a decision (i.e. the charisma die rolls, and the degrees of the players may change)

####Tag Team Matches:

If you wish to tag your teammate in, you roll a die:

If Fresh,       1d6 > 0 (always)
If Tired,       1d6 > 2 (3,4,5,6)
If Exhausted,   1d6 > 4 (5,6)
If Zombie,      1d6 > 6 (never)

The new incoming player will get a speed cut of 3*degree in his/her first attack.













