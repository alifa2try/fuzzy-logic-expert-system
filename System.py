import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# Antecedent = input, Consequent = output

# __UNIVERSES__
nsp = ctrl.Antecedent(np.arange(0, 1.0, 0.05), 'Number of spare parts (normalized)')
nsp['very small'] = fuzz.trapmf(nsp.universe, [0, 0, 0.10, 0.30])
nsp['small'] = fuzz.trimf(nsp.universe, [0, 0.20, 0.40])
nsp['rather small'] = fuzz.trimf(nsp.universe, [0.25, 0.35, 0.45])
nsp['medium'] = fuzz.trimf(nsp.universe, [0.30, 0.50, 0.70])
nsp['rather large'] = fuzz.trimf(nsp.universe, [0.55, 0.65, 0.75])
nsp['large'] = fuzz.trimf(nsp.universe, [0.60, 0.80, 1])
nsp['very large'] = fuzz.trapmf(nsp.universe, [0.70, 0.85, 1, 1])
# n.view()

nss = ctrl.Antecedent(np.arange(0, 1.0, 0.05), 'Number of spare servers (normalized)')
nss['very small'] = fuzz.trapmf(nss.universe, [0, 0, 0.15, 0.35])
nss['rather small'] = fuzz.trimf(nss.universe, [0.15, 0.30, 0.45])
nss['medium'] = fuzz.trimf(nss.universe, [0.30, 0.50, 0.70])
nss['rather large'] = fuzz.trimf(nss.universe, [0.55, 0.70, 0.85])
nss['very large'] = fuzz.trapmf(nss.universe, [0.60, 0.80, 1, 1])
# ns.view()

md = ctrl.Antecedent(np.arange(0, 1.0, 0.05), 'Mean delay (normalized)')
md['very small'] = fuzz.trapmf(md.universe, [0, 0, 0.15, 0.30])
md['small'] = fuzz.trimf(md.universe, [0, 0.30, 0.50])
md['medium'] = fuzz.trapmf(md.universe, [0.40, 0.55, 0.70, 0.70])
# md.view()

ruf = ctrl.Antecedent(np.arange(0, 1.0, 0.05), 'Repair utilisation factor')
ruf['low'] = fuzz.trapmf(ruf.universe, [0, 0.0, 0.40, 0.60])
ruf['medium'] = fuzz.trimf(ruf.universe, [0.40, 0.60, 0.80])
ruf['high'] = fuzz.trapmf(ruf.universe, [0.60, 0.80, 1, 1])
ruf.view()


# __RULES__

