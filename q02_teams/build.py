# %load q02_teams/build.py
# default imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# solution
def teams(data=data):
    info=data['info']
    # write your code here
    teams = info['teams']
    print(teams)
    return teams

teams()

