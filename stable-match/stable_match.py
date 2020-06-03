import random

class Party():

    def __init__(self, name):
        self.name = name
        self.preferences = []
        self.is_free = True
        self.contracted_with = None
        self.proposed_to = []

    def get_contracted(self, party):
        self.contracted_with = party
        self.is_free = False
        party.contracted_with = self
        party.is_free = False

    def break_contract(self):
        party = self.contracted_with
        if self.contracted_with != None:

            self.contracted_with = None
            self.is_free = True

            party.contracted_with = None
            party.is_free = True

            print(f'{self.name} breaks contract with {party.name}')

    def compare_preferences(self, coordinator):
        for preference in self.preferences:
            if preference == coordinator:
                return preference
            if preference == self.contracted_with:
                return preference

    def __repr__(self):
        return self.name

def create_parties(parties_ids):
    parties = []
    for id in parties_ids:
        p = Party(id)
        parties.append(p)
    else:
        return parties

def assing_preferences(instances_list, preferences):
    for instance in instances_list:
        list = preferences[:]
        random.shuffle(list)
        instance.preferences = list

def print_parties(parties):
    for party in parties:
        print(party.name, '\t' ,party.preferences)

def get_name_from_preference_ranking(parties, instance, index):
    for party in parties:
        if party == instance :
            return party.preferences[index]

def match(coordinator_ids, supplier_ids):

    c = create_parties(coordinator_ids)
    s = create_parties(supplier_ids)

    coordinator_preferences = [s[0], s[1], s[2], s[3], s[4], s[5]]
    supplier_preferences = [c[0], c[1], c[2], c[4], c[3], c[5]]

    assing_preferences(c, coordinator_preferences)
    assing_preferences(s, supplier_preferences)

    print('\n')
    print('Coord.', '\t', 'Preferences (desc.)')
    # print('Id', '\t', [1,2,3,4,5,6])
    print_parties(c)
    print('\n')
    print('Suppl.', '\t', 'Preferences (desc.)')
    # print('Id', '\t', [1,2,3,4,5,6])
    print_parties(s)
    print('\n')
    print('Matching')
    while (True):
        pairs_number = len(c)
        stable = 1
        for coordinator in c:
            if (coordinator.is_free == False) and (len(coordinator.proposed_to) != pairs_number):
                stable += 1
                if stable == pairs_number:
                    print("\nSuccess!")
                    return c, s

            for x in range(0, pairs_number):
                if coordinator.contracted_with == None:
                    if x not in coordinator.proposed_to:
                        coordinator.proposed_to.append(x)

                        supplier = get_name_from_preference_ranking(c, coordinator, x)

                        if supplier.contracted_with != None: # if supplier already contracted we need to check if it's contracted with its the best coordinator
                            current_contracted_coordinator = supplier.contracted_with
                            better_coordinator = supplier.compare_preferences(coordinator)

                            if better_coordinator.name != current_contracted_coordinator.name:
                                current_contracted_coordinator.break_contract()
                                supplier.get_contracted(better_coordinator)
                        else:
                            supplier.get_contracted(coordinator) # if supplier not contracted then it gets contracted with current coordinator


def main():

    coordinator_ids = ['C' + str(i) for i in range(1,7)]
    supplier_ids = ['S' + str(i) for i in range(1,7)]

    c, s = match(coordinator_ids, supplier_ids)

    for coordinator in c:
        c_party = coordinator.name
        s_party = coordinator.contracted_with
        print(f'{c_party} ---> {s_party}')

main()
