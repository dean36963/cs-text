
class Route:
    @staticmethod
    def locations():
        return NotImplementedError("Implement")

    def get_next_location(self, location):
        pick_next = False
        for l in self.locations():
            if location == l:
                pick_next = True
                continue
            if pick_next:
                return l
        return None