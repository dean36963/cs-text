from Character import Character
from Actions import action_from_alias
import sys


class Player(Character):
    def get_action(self, info):
        try:
            print("You are currently at {}.".format(self.location().location_name().name()))
            for location, enemies in info.enemies_in_sight().items():
                print("At location {} you can see {} enemies.".format(
                    location.location_name().name(),
                    len(enemies)
                ))
            print("There are {} enemies left.".format(
                info.num_enemy()
            ))
            if info.turns_til_explosion > 0 and info.turns_til_explosion < 99:
                print("There are {} turns left until bomb explodes.".format(info.turns_til_explosion))
            else:
                print("There are {} turns left this round.".format(
                   info.turns_left
                ))
            for location, teammates in info.team_mates_by_location().items():
                print("{} teammates are at {}".format(
                    len(teammates),
                    location.location_name().name()
                ))
            if self.health < 100:
                print("You have {} HP".format(self.health))
            if self.has_bomb:
                print("You have the bomb.")

            action = None
            option = None
            while not action:
                action_string = input("> ")
                action = action_from_alias(action_string)
                if not action:
                    continue
                if action.options(self):
                    while not option:
                        print(action.option_prompt())
                        for i, possible_option in enumerate(action.options(self)):
                            print("  [{}]: {}".format(
                                i,
                                possible_option.location_name().name()
                            ))
                        option_string = input("> ")
                        try:
                            option = action.options(self)[int(option_string)]
                        except IndexError:
                            continue
            return action(option,self)
        except KeyboardInterrupt:
            print("RAGE QUIT")
            sys.exit(0)
        except EOFError:
            print("RAGE QUIT")
            sys.exit(0)

