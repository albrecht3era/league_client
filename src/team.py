from ban import Ban


class Team:
    def __init__(self, team_info):
        # team_info = team_info[team_info.index("{")+1:]
        self.TEAM_ID = int(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.WIN = self.get_bool(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.FIRST_BLOOD = self.get_bool(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.FIRST_TOWER = self.get_bool(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.FIRST_INHIBITOR = self.get_bool(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.FIRST_BARON = self.get_bool(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.FIRST_DRAGON = self.get_bool(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.FIRST_RIFT_HERALD = self.get_bool(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.TOWER_KILLS = int(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.INHIBITOR_KILLS = int(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.BARON_KILLS = int(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.DRAGON_KILLS = int(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.VILEMAW_KILLS = int(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.RIFT_HERALD_KILLS = int(self.get_value(team_info))
        team_info = self.advance_match_info(team_info)
        self.DOMINION_VICTORY_SCORE = int(self.get_value(team_info))
        self.BANS = list()
        team_info = self.advance_match_info(team_info)
        team_info = team_info[team_info.index("{") + 1:]
        bans = team_info.split("},")
        bans = bans[:5]
        for ban in bans:
            self.BANS.append(Ban(ban))


    def get_bool(self, boolean):
        if "false" in boolean or "Fail" in boolean:
            return False
        else:
            return True

    def get_value(self, match_info):
        return match_info[match_info.index(":")+1:match_info.index(",")].replace("\"", "")

    def advance_match_info(self, match_info):
        return match_info[match_info.index(",")+1:]