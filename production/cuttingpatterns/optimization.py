from coopr.pyomo import *
import optimization_get
import numpy
from production.models import Coating
from datetime import datetime
from production.utils.get import shortage

model = ConcreteModel()

rs, c, pd, cs, g, rcp, oi = optimization_get.indices()
pastelbord = int(Coating.objects.get(description = 'Pastelbord').id)
today = datetime.now().date()

# Indices *************
model.crad = Set(initialize = [0,1])
model.rs = Set(initialize = rs)
model.c = Set(initialize = c)
model.pd = Set(initialize = pd)
model.cs = Set(initialize = cs)
model.g = Set(initialize = g)
model.rcp = Set(initialize = rcp)
model.oi = Set(initialize = oi)

# partitioning rcp
rcp = {}
for g in model.g:
    rcp[g] = {}
    for cs in model.cs:
        rcp[g][cs] = {}
        for crad in model.crad:
            rcp[g][cs][crad] = optimization_get.rcp_subset(g,cs,crad)

# partitioning oi
oi = {}
for rs in model.rs:
    oi[rs] = {}
    for c in model.c:
        oi[rs][c] = {}
        for pd in model.pd:
            oi[rs][c][pd] = {}
            for crad in model.crad:
                oi[rs][c][pd][crad] = optimization_get.oi_subset(rs,c,pd,crad)


# Data *******************
O = {}
for rs in model.rs:
    O[rs] = {}
    for rcp in model.rcp:
        output = optimization_get.cut_outputs(rs,rcp)
        if output > 0:
            O[rs][rcp] = optimization_get.cut_outputs(rs,rcp)

T = {}
for cs in model.cs:
    T[cs] = {}
    for c in model.c:
        T[cs][c] = {}
        for pd in model.pd:
            T[cs][c][pd] = {}
            for g in model.g:
                T[cs][c][pd][g] = optimization_get.terceros(cs,c,pd,g)

alpha = optimization_get.alpha()
beta = optimization_get.beta()
gamma = optimization_get.gamma()
n1 = optimization_get.n1()
n2 = optimization_get.n2()
n3 = optimization_get.n3()


# Variables ****************
model.z = Var(model.rcp, model.c, model.pd)
model.x = Var(model.rs, model.c, model.pd)


# Objective *****************
def objective_rule(model, n1, n2, n3, pastelbord):
    expr = 0
    for rs in model.rs:
        for pd in model.pd:
            remainder = model.x[rs,pastelbord,pd] + shortage.retail_cuts(today,\
                    0,pastelbord,rs,pd)
            oi_x = oi_subset(rs,pastelbord,pd,0)[:-remainder]
            for oi in oi_x:
                expr += alpha*numpy.exp(-oi*n1)
    for rs in model.rs:
        for pd in model.pd:
            for c in model.pd not in pastelbord:
                if c == pastelbord:
                    continue
                remainder = model.x[rs,c,pd] + shortage.retail_cuts(today,\
                        0,c,rs,pd)
                oi_x = oi_subset(rs,c,pd,0)[:-remainder]
                for oi in oi_x:
                    expr += beta*numpy.exp(-oi*n2)
    for rs in model.rs:
        for pd in model.pd:
            for c in model.pd:
                if c == pastelbord:
                    continue
                remainder = model.x[rs,c,pd] + shortage.retail_cuts(today,1,c,rs.pd)
                oi_x = oi_subset(rs,c,pd,1)[:-remainder]
                for oi in oi_x:
                    expr += gamma*numpy.exp(-oi*n3)
    return expr
model.objective = model.Objective(n1,n2,n3,rule = objective_rule)


# Constraints *****************
def tercero_on_shelf_rule(model, cs, c, pd, g, T):
    return sum(model.z[rcp_element,c,pd] for rcp_element in rcp[g][cs][crad])\
            <= T[cs][c][pd][g]
model.tercer_on_shelf_constraint = Constraint(model.cs, model.c, model.pd, \
        model.g, T, rule = tercero_on_shelf_rule)

def retail_size_count_rule(model, rs, c, p, crad):
    return sum(O[rs][rcp_element]*model.z[rcp_element,c,pd] for rcp_element in\
            rcp[g][cs][crad] if rcp_element in O[rs]) == model.x[rs,c,pd]
model.retail_size_count_constraint = Constraint(model.rs, model.c, model.p,\
        model.crad, rule = retail_size_count_rule)
