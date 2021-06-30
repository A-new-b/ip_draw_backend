import iptc


def rule_init():
    rule = iptc.Rule()
    rule.protocol = "tcp"
    rule.target = iptc.Target(rule, "ACCEPT")
    match = rule.create_match("tcp")
    match.dport = "5000"
    rule.add_match(match)
    chain = iptc.Chain(iptc.Table(iptc.Table.MANGLE), "INPUT")
    chain.insert_rule(rule)


def counter():
    table = iptc.Table(iptc.Table.MANGLE)
    chain = iptc.Chain(table, "INPUT")
    table.refresh()
    packets_list = []
    for rule in chain.rules:
        (packets, bytes) = rule.get_counters()
        packets_list.append((packets, bytes))
        print(packets, bytes)
    return packets_list


def stop():
    table = iptc.Table(iptc.Table.MANGLE)
    table.autocommit = False
    chain = iptc.Chain(table, "INPUT")
    for rule in chain.rules:
        chain.delete_rule(rule)
    table.commit()
    table.autocommit = True


if __name__ == '__main__':
    print(counter())
