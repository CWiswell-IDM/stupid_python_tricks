
def base_intervention(start_day=0, coverage=1.0, parent_args=None):
    if parent_args:
        if 'start_day' in parent_args.keys():
            start_day=parent_args['start_day']
        if 'coverage' in parent_args.keys():
            coverage=parent_args['coverage']
    base_dict = {
        'start_day': start_day,
        'coverage': coverage
    }
    return base_dict


def killing_intervention(insecticide=None, killing_eff=1.0,
                         **kwargs):
    iv_dict = base_intervention(parent_args=kwargs)
    if insecticide:
        iv_dict['insecticide'] = insecticide
    iv_dict['killing_effectiveness'] = killing_eff
    return iv_dict


def blocking_killing_iv(insecticide=None, blocking_eff=1.0,
                        killing_eff=0.5, **kwargs):
    iv_dict = base_intervention(parent_args=kwargs)
    if insecticide:
        iv_dict['insecticide'] = insecticide
    iv_dict['blocking_effectiveness'] = blocking_eff
    iv_dict['killing_effectiveness'] = killing_eff
    return iv_dict


if __name__ == "__main__":
    abstract1 = base_intervention()
    print("Abstract all defaults.")
    print(abstract1)
    print()

    abstract2 = base_intervention(start_day=5, coverage=0.2)

    print("Abstract, start day 5 coverage 0.2")
    print(abstract2)
    print()

    killer1 = killing_intervention()
    print("Killer all defaults.")
    print(killer1)
    print()

    killer2 = killing_intervention(start_day=13, coverage=0.87)
    print(f"Killer setting parent properties. Start_Day: 13, Coverage: 0.87")
    print(killer2)
    print()

    killer3 = killing_intervention(insecticide="bleach", coverage=0.34)
    print("Killer setting one parent (coverage 0.34), one local param (Insecticide \"bleach\")")
    print(killer3)
    print()

    blocker1 = blocking_killing_iv()
    print("Blocker all defaults")
    print(blocker1)
    print()

    blocker2 = blocking_killing_iv(Start_Day=31, blocking_eff=0.73, coverage=0.996)
    print("Blocker with two parents surrounding a local param (blocking eff 0.73)")
    print(blocker2)
    print()

    blocker3 = blocking_killing_iv(blocking_eff=0.12, starship_captain="Picard")
    print("Blocker with a local param (blocking eff 0.12) and a wrong one (starship_captain Picard)")
    print(blocker3)
    print()
