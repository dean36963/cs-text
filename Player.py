from Character import Character
from Actions import action_from_alias


class Player(Character):
    def get_action(self, info=None):
        try:
            print("You are currently at {}.".format(self.location().location_name().name()))
            # Info processing
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
            exit(0)