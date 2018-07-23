class Participant:

    def __init__(self, participant):
        self.PARTICIPANT_ID = self.get_value(participant)
        participant = self.advance_match_info(participant)
        self.TEAM_ID = self.get_value(participant)
        participant = self.advance_match_info(participant)
        self.CHAMPION_ID = self.get_value(participant)
        participant = self.advance_match_info(participant)
        self.SPELL_ONE_ID = self.get_value(participant)
        participant = self.advance_match_info(participant)
        self.SPELL_TWO_ID = self.get_value(participant)
        participant = self.advance_match_info(participant)
        self.PARTICIPANT_ID = self.get_value(participant)
        participant = self.advance_match_info(participant)

    def get_value(self, match_info):
        return match_info[match_info.index(":") + 1:match_info.index(",")].replace("\"", "")

    def advance_match_info(self, match_info):
        return match_info[match_info.index(",") + 1:]

    def get_bool(self, boolean):
        if "false" in boolean or "Fail" in boolean:
            return False
        else:
            return True

