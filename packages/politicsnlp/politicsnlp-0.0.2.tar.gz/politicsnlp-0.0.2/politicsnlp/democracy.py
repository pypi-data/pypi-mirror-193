class Democracy:
    def __init__(self, election_rights, free_speech, rule_of_law, political_competition):
        self.election_rights = election_rights
        self.free_speech = free_speech
        self.rule_of_law = rule_of_law
        self.political_competition = political_competition

    def participate(self):
        print("Everyone has the opportunity to participate in political decision-making.")

    def safeguard(self):
        print("The rule of law guarantees the equal protection of everyone's rights.")

    def compete(self):
        print("Political parties and factions have equal opportunities to compete for political power.")

    def promote(self):
        print("We promote free speech and the right to express diverse opinions.")

# 示例
democracy = Democracy(True, True, True, True)
democracy.participate()
democracy.safeguard()
democracy.compete()
democracy.promote()
