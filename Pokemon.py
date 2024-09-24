#Import Things we need
import random
import time
import sys

#The code that creates a small delay between letters
def delay_print(s):
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.025)

def SUPER_delay_print(s):
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.12)

class Pokemon:
  
  def __init__(self, name, type, moves, attack, defense, health):
    self.name = name
    self.type = type
    self.moves = moves
    self.attack = attack
    self.defense = defense
    self.health = health

  def fight(self, Pokemon2):
    print("------Pokemon Battle------")
    
    #Print user pokemon information
    print(f"\n{self.name}")
    print("TYPE", self.type)
    print("ATTACK", self.attack)
    print("DEFENSE", self.defense)
    print("HEALTH", self.health)

    #Print computer pokemon information
    print(f"\n{Pokemon2.name}")
    print("TYPE", Pokemon2.type)
    print("ATTACK", Pokemon2.attack)
    print("DEFENSE", Pokemon2.defense)
    print("HEALTH", Pokemon2.health)

    #Type advantages and disadvantages
    version = ['Fire', 'Water', 'Grass']
    if self.type == Pokemon2.type:
      attack1="It's not very effective..."
      attack2="It's not very effective..."
    elif (self.type=='Fire' and Pokemon2.type=='Water') or (self.type=='Water' and Pokemon2.type=='Grass') or (self.type=='Grass' and Pokemon2.type=='Fire'):
      Pokemon2.attack*=2
      self.attack/=2
      attack1="It's not very effective..."
      attack2="It's super effective!!!
    elif (self.type=='Fire' and Pokemon2.type=='Grass') or (self.type=='Water' and Pokemon2.type=='Fire') or (self.type=='Grass' and Pokemon2.type=='Water'):
      Pokemon2.attack/=2
      self.attack*=2
      attack1="It's super effective!!!"
      attack2="It's not very effective..."

    #Application should run while pokemon still have health (AKA it finishes when you die)
    while (self.health > 0) and (Pokemon2.health > 0):
      print(f"\nGo {self.name}")
      for i, x in enumerate(self.moves):
        print(f"{i+1}.", x)
      index = int(input('Pick a move: '))
      delay_print(f"\n{self.name} used {self.moves[index-1]}!\n")

      time.sleep(1)
      SUPER_delay_print(attack1)

      #Determine attack damage
      Pokemon2.health -= self.attack
      
      if Pokemon2.health<=0:
        Pokemon2.health=0
        delay_print(f"{Pokemon2.name} has fainted. \n")
        delay_print('You won. Opponent paid you $1000 Pokedollars')
        break
      
      time.sleep(1)

      #Pokemon2's turn
      print(f"\nGo {Pokemon2.name}")
      index = random.randint(1, 4)
      delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!\n")
      time.sleep(1)
      SUPER_delay_print(attack2)

      #Determine attack damage
      self.health -= Pokemon2.attack
      time.sleep(1)
      print(f"\n{self.name}\t\tHLTH\t{self.health}")
      print(f"\n{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
      time.sleep(0.5)

      #Check to see if user has fainted
      if self.health <= 0:
        self.health=0
        delay_print(f"{self.name} has fainted. \n")
        delay_print('You lost. You paid $1000. Skill issue.')
        break

if __name__ == '__main__':
  #Create Pokemon
  Pokemonlist = [
    Pokemon('Charizard', 'Fire',
       ['Flamethrower', 'Fire Punch', 'Blast Burn', 'Ember'], 13, 10, 65),
    Pokemon('Greninja', 'Water',
       ['Water Shuriken', 'Hydro Pump', 'Hydro Cannon', 'Bubble Beam'], 18, 8, 55),
    Pokemon('Torterra', 'Grass',
       ['Solar Beam', 'Energy Ball', 'Freny Plant', 'Bullet Seed'], 9, 14, 100)
   ]
  #TO DO: Give pokemon moves with separate types
  userChoice = str(
     input(
          'Choose a Pokemon from this very short list. Charizard, Greninja, or Torterra: '
      ))
  while userChoice not in "CharizardcharizardGreninjagreninjaTorterratorterra":
    userChoice = str(
    input(
        'Choose a Pokemon from this very short list. Charizard, Greninja, or Torterra: '
      ))
  userChoice=userChoice[0].upper()+userChoice[1:]
  if userChoice == 'Charizard':
    userChoice = Pokemonlist[0]
  elif userChoice == 'Greninja':
    userChoice = Pokemonlist[1]
  elif userChoice == 'Torterra':
    userChoice = Pokemonlist[2]
  else:
    print('Invalid choice. Please choose a pokemon from the list')
  #Shows the three (soon to be 4-6) pokemon on a list
  computerChoice = random.choice(Pokemonlist)
  print(userChoice)
  userChoice.fight(computerChoice)
