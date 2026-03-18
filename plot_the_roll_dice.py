import plotly.express as px
from dices_class import Die

die=Die()
die_2=Die()
results=[die.roll()*die_2.roll() for roll_num in range(1000)]

max_result=die.num_sides*die_2.num_sides
poss_results=range(1,max_result+1)
frequencies=[results.count(value) for value in poss_results]

title="Results of rolling two D6 dices 1000 Times"
labels={"x":'result','y':'Frequency of result'}
fig=px.bar(x=poss_results,y=frequencies,title=title,labels=labels)

fig.update_layout(xaxis_dtick=1)
fig.show()
