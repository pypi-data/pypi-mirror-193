class PeopleDemocracy:
    def __init__(self, governing_body, election_process):
        self.governing_body = governing_body
        self.election_process = election_process

    def make_decisions(self, policy):
        if self.governing_body == "representatives":
            return "The people's representatives vote on the policy."
        elif self.governing_body == "direct democracy":
            return "The people vote directly on the policy."
        else:
            return "The governing body is not specified."

    def hold_elections(self):
        if self.election_process == "free and fair elections":
            return "The people are able to choose their own leaders."
        elif self.election_process == "rigged elections":
            return "The people's choice is not respected."
        else:
            return "The election process is not specified."
