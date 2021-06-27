import iptc


def rule_init():
    rule = iptc.Rule()
    rule.protocol = "tcp"
    rule.target = iptc.Target(rule, "ACCEPT")
    match = rule.create_match("tcp")
    match.dport = "5000"
    rule.add_match(match)
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    chain.insert_rule(rule)


def counter():
    chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
    for rule in chain.rules:
        (packets, bytes) = rule.get_counters()
        print(packets, bytes)


if __name__ == '__main__':
    counter()
