from enum import Enum
from collections import namedtuple


Condition = Enum("Condition", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent type, containing a 'name' field and a 'category' field, with 'category' being of the type Condition.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result of the meeting.
    """
    
    length = len(agent_listing)

    if length == 0:
        return []
    
    new_list = []

    if length == 1:
        new_list.extend(agent_listing)
        return new_list
    
    iterable_list, non_iterable_list = filtering_out(agent_listing)

    new_list = []

    for i in range(0, len(iterable_list) - 1, 2):
        a1, a2 = disease_spread(iterable_list[i], iterable_list[i+1])
        new_list.extend([a1, a2])

    if len(iterable_list) % 2 == 1:
        new_list.append(iterable_list[-1])
    
    new_list.extend(non_iterable_list)

    # print("\n".join(str(item) for item in new_list))

    return(new_list)

# Defining an axuliary function for better printing

def filtering_out(agent_listing: tuple) -> list:

    eligible_list = []
    non_eligible_list = []

    for agent in agent_listing:
        if is_eligible(agent):
            eligible_list.append(agent)
        else:
            non_eligible_list.append(agent)
    
    return eligible_list, non_eligible_list

def is_eligible(agent1: Agent):
    if agent1.category not in (Condition.HEALTHY, Condition.DEAD):
        return True
    else:
        return False

# Defining an auxiliary function with disease spreading logic

def disease_spread(agent1: Agent, agent2: Agent) -> tuple:

# Adding this because you can't modify the original enum
    cat1 = agent1.category
    cat2 = agent2.category

    # CURE scenarios: if either one of them is of CURE status, bump Condition.SICK up to "Healthy", and Condition.DYING up to Condition.SICK by decreasing value by 1
    if cat1 == Condition.CURE and cat2 in (Condition.SICK, Condition.DYING):
        cat2 = Condition(cat2.value - 1)
    if cat2 == Condition.CURE and cat1 in (Condition.SICK, Condition.DYING):
        cat1 = Condition(cat1.value - 1)

    # SICK/DYING meeting logic
    if cat1 in (Condition.SICK, Condition.DYING) and cat2 in (Condition.SICK, Condition.DYING):
        cat1 = Condition(cat1.value + 1)
        cat2 = Condition(cat2.value + 1)

    # SICK scenarios: SICK → DYING, DYING → DEAD; adding +1 because the original ENUM goes from healthy to dead
    # accounting only for SICK & DYING conditions because all others are unaffected by meetings

    return Agent(agent1.name, cat1), Agent(agent2.name, cat2)
