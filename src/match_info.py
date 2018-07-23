from team import Team

class MatchInfo:

    def __init__(self, match_info):
        self.GAME_ID = self.get_value(match_info)
        match_info = self.advance_match_info(match_info)
        self.PLATFORM_ID = self.get_value(match_info)
        match_info = self.advance_match_info(match_info)
        self.GAME_CREATION = self.get_value(match_info)
        match_info = self.advance_match_info(match_info)
        self.GAME_DURATION = self.get_value(match_info)
        match_info = self.advance_match_info(match_info)
        self.QUEUE_ID = self.get_value(match_info)
        match_info = self.advance_match_info(match_info)
        self.MAP_ID = self.get_value(match_info)
        match_info = self.advance_match_info(match_info)
        self.SEASON_ID = self.get_value(match_info)
        match_info = self.advance_match_info(match_info)
        self.GAME_VERSION = self.get_value(match_info)
        match_info = self.advance_match_info(match_info)
        self.GAME_MODE = self.get_value(match_info)
        match_info = self.advance_match_info(match_info)
        self.GAME_TYPE = self.get_value(match_info)
        match_info = self.advance_match_info(match_info)
        team_info = match_info[match_info.index("teamId")+6:]
        team_info = team_info[:team_info.index("teamId")]
        self.TEAMS = list()
        self.TEAMS.append(Team(team_info))
        match_info = match_info[match_info.index("teamId")+6:]
        match_info = match_info[match_info.index("teamId"):]
        team_info = match_info[:match_info.index("participants")]
        match_info = match_info[match_info.index("participants")+16:]
        self.TEAMS.append(Team(team_info))





    def get_value(self, match_info):
        return match_info[match_info.index(":")+1:match_info.index(",")].replace("\"", "")

    def advance_match_info(self, match_info):
        return match_info[match_info.index(",")+1:]
