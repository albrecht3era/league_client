from datetime import datetime
from matches import Matches
from match import Match

class Summoner:

    def __init__(self, request, requester):
        self.REQUESTER = requester
        fields = request.split(",")
        self.ID = self.field_info(fields[0])
        self.ACCOUNT_ID = self.field_info(fields[1])
        self.NAME = self.field_info(fields[2])
        self.PROFILE_ICON_ID = self.field_info(fields[3])
        self.REVISION_DATE = self.field_info(fields[4])
        self.SUMMONER_LEVEL = self.field_info(fields[5])
        self.CURRENT_MATCH = Match
        self.MATCHES = Matches()

    def get_id(self):
        return self.ID

    def get_account_id(self):
        return self.ACCOUNT_ID

    def get_name(self):
        return self.NAME

    def get_profile_icon_id(self):
        return self.PROFILE_ICON_ID

    def get_revision_date(self):
        return self.REVISION_DATE

    def get_summoner_level(self):
        return self.SUMMONER_LEVEL

    def get_matches(self):
        self.MATCHES = self.REQUESTER.get_matches(self.ACCOUNT_ID, self.REQUESTER)
        self.CURRENT_MATCH = self.MATCHES.get_latest_match()

    def get_current_match(self):
        return self.CURRENT_MATCH

    def print_summoner(self):
        self.print_status("ID: " + self.ID)
        self.print_status("Account ID: " + self.ACCOUNT_ID)
        self.print_status("Name: " + self.NAME)
        self.print_status("Profile Icon ID:" + self.PROFILE_ICON_ID)
        self.print_status("Revision Date: " + self.REVISION_DATE)
        self.print_status("Summoner Level: " + self.SUMMONER_LEVEL)

    @staticmethod
    def field_info(field):
        if "}" in field:
            field = field[:field.index("}")]
        return field[field.index(":")+1:].replace("\"", "")

    @staticmethod
    def print_status(message):
        print("[" + str(datetime.now()) + "] " + message)



