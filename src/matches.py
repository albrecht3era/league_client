from match import Match


class Matches:

    def __init__(self):
        self.MATCHES = dict()
        self.ACCOUNT_IDS = list()

    def add_matches(self, riot_request, account_id, requester):
        matches = riot_request.split("},")
        matches[0] = matches[0][matches[0].index("[")+1:]
        matches[len(matches)-1] = matches[len(matches)-1][:matches[len(matches)-1].index("],")]
        if account_id not in self.ACCOUNT_IDS:
            self.ACCOUNT_IDS.append(account_id)
        for match in matches:
            new_match = Match(match, account_id, requester)
            self.MATCHES[new_match.get_game_id()] = new_match

    def get_match(self, match_id):
        return self.MATCHES[match_id]

    def get_matches(self):
        return self.MATCHES.items()

    def get_latest_match(self):
        last_match = None
        last_time_stamp = -1
        for match in self.MATCHES.values():
            if int(match.get_timestamp()) > last_time_stamp:
                last_time_stamp = int(match.get_timestamp())
                last_match = match
        return last_match
