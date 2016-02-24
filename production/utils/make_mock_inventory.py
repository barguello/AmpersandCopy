from production.models import RetailCutWip, Coating, RetailSize, PanelDepth, CoatingSize, GradedWip, RetailCuttingPattern
from datetime import datetime


g_list = RetailCuttingPattern.objects.values('grade').distinct()
g_list = [int(element['grade']) for element in g_list]
cs_list = CoatingSize.objects.all()
rs_list = RetailSize.objects.all()
c_list = Coating.objects.all()
pd_list = PanelDepth.objects.all()
is_cradled = [0,1]

wip_type = 'Beginning of Period Inventory'

date = datetime(2014, 01, 01, 0, 0, 0, 0)

for rs in rs_list:
    for c in c_list:
        for pd in pd_list:
            for crad in is_cradled:
                wip = RetailCutWip(date = date, quantity = 10, is_cradled = crad,\
                        coating = c, retail_size = rs, panel_depth = pd,\
                        type = wip_type)
                #RetailCutWip.save(wip)

for g in g_list:
    for c in c_list:
        for pd in pd_list:
            for cs in cs_list:
                wip = GradedWip(date = date, quantity = 10, coating = c,\
                        grade = g, panel_depth = pd, coating_size = cs,\
                        type = wip_type)
                GradedWip.save(wip)
