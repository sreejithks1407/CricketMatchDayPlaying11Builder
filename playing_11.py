import batters as bt
import pacers as ps
import spinners as sp
import allrounders as al
import wicketkeepers as wk


def playing_11(available_batters, no_of_batters, available_wicketkeepers, available_allrounders, no_of_allrounders, available_pacers, no_of_pacers, available_spinners, no_of_spinners):

    batters = bt.pick_batters(available_batters, no_of_batters)
    wicketkeeper = wk.pick_wicketkeeper(available_wicketkeepers)
    alrounders = al.pick_allrounders(available_allrounders, no_of_allrounders)
    spinners = sp.pick_spinners(available_spinners, no_of_spinners)
    pacers = ps.pick_pacers(available_pacers, no_of_pacers)

    playing_11 = batters+wicketkeeper+alrounders+spinners+pacers

    return playing_11


available_batters = ['Mathew Hayden', 'Ricky Ponting',
                     'Mike Hussey', 'Michael Clarke', 'Travis Head']
available_wicketkeepers = ['Adam Gilchrist', 'Tim Paine',
                           'Brad Haddin', 'Alex Carey', 'Mathew Wade']
available_pacers = ['Glen Mcgrath', 'Brett Lee',
                    'Nathan Bracken', 'Shaun Tait', 'Jason Gillespy', 'Mitchel Starc', 'Josh Hazelwood']
available_allrounders = ['Mitchel Johnson',
                         'Pat Cummins', 'Andrew Symmons', 'Shane Watson', 'Glen Maxwell', 'Mitchel Marsh', 'Cameron White']
available_spinners = ['Shane Warne', 'Brad Hodge', 'Nathan Lyon']


match_day_playing_11 = playing_11(available_batters, 3, available_wicketkeepers,
                                  available_allrounders, 3, available_pacers, 3, available_spinners, 1)
print(match_day_playing_11)
