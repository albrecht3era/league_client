class Ban:
    def __init__(self, ban):
        self.CHAMPION_ID = self.get_value(ban)
        ban = self.advance_match_info(ban)
        self.PICK_TURN = self.get_value(ban)


    def get_value(self, match_info):
        if "," in match_info:
            return match_info[match_info.index(":")+1:match_info.index(",")]
        else:
            return match_info[match_info.index(":")+1]

    def advance_match_info(self, match_info):
        return match_info[match_info.index(",")+1:]