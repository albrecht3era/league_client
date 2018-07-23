from datetime import datetime


class Match:
    def __init__(self, riot_request, summoner_name, requester):
        self.REQUESTER = requester
        fields = riot_request.split(",")
        self.PLATFORM_ID = Match.field_info(fields[0])
        self.GAME_ID = Match.field_info(fields[1])
        self.CHAMPION = Match.field_info(fields[2])
        self.QUEUE = Match.field_info(fields[3])
        self.SEASON = Match.field_info(fields[4])
        self.TIMESTAMP = Match.field_info(fields[5])
        self.ROLE = Match.field_info(fields[6])
        self.LANE = Match.field_info(fields[7])
        self.SUMMONER_NAME = summoner_name

    def get_lane(self):
        return self.LANE

    def get_game_id(self):
        return self.GAME_ID

    def get_champion(self):
        return self.CHAMPION

    def get_platform_id(self):
        return self.GAME_ID

    def get_timestamp(self):
        return self.TIMESTAMP

    def get_queue(self):
        return self.QUEUE

    def get_role(self):
        return self.ROLE

    def get_season(self):
        return self.SEASON

    def print_match(self):
        self.print_status("Lane: " + self.LANE)
        self.print_status("Game ID: " + self.GAME_ID)
        self.print_status("Champion: " + self.CHAMPION)
        self.print_status("Platform ID: " + self.PLATFORM_ID)
        self.print_status("Timestamp: " + self.TIMESTAMP)
        self.print_status("Queue: " + self.QUEUE)
        self.print_status("Role: " + self.ROLE)
        self.print_status("Season: " + self.SEASON)

    def get_match_info(self):
        match_info = self.REQUESTER.get_match_info(self.GAME_ID)
        print("stop")

    @staticmethod
    def field_info(field):
        if "}" in field:
            field = field[:field.index("}")]
        return field[field.index(":") + 1:].replace("\"", "")

    def print_status(self, message):
        print("[" + str(datetime.now()) + "] " + message)