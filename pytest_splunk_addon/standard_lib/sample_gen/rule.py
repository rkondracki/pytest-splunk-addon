import abc

@abc.ABC
class Rule(object):
    
    def __init__(self, token, replacement_type, replacement, key=False):
        self.token = token
        self.replacement_type = replacement_type
        self.replacement = replacement 
        self.key = key

    @classmethod
    def parse_rules(cls, rules):
        rule_map = {
            "random": {
                "int": IntRule
            }
        }
        for each_rule in rules:
            replacement_type = each_rule.get("replacement_type")
            replacement_type_map = rule_map.get(replacement_type)
            replacement = replacement_type_map.get(each_rule.get("replacement"), each_rule.get("replacement"))
            token = each_rule.get("token")
            yield cls(token, replacement_type, replacement)

    @abc.abstractmethod
    def apply(self, sample):
        """
        Apply the rule to a string. 
        """
        return sample.replace(self.token, self.replacement)


class IntRule(Rule):
    pass
