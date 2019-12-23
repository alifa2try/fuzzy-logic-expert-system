import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# New Antecedent/Consequent objects hold universe variables and membership
# Antecedent = input, Consequent = output

# __UNIVERSE_INPUTS__
nss = ctrl.Antecedent(np.arange(0, 1.0, 0.05), 'Number of spare servers (normalized)')
nss['small'] = fuzz.trapmf(nss.universe, [0, 0, 0.15, 0.35])
nss['rather small'] = fuzz.trimf(nss.universe, [0.15, 0.30, 0.45])
nss['medium'] = fuzz.trimf(nss.universe, [0.30, 0.50, 0.70])
nss['rather large'] = fuzz.trimf(nss.universe, [0.55, 0.70, 0.85])
nss['large'] = fuzz.trapmf(nss.universe, [0.60, 0.80, 1, 1])
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
# ruf.view()

# __UNIVERSE_OUTPUTS__
nsp = ctrl.Consequent(np.arange(0, 1.0, 0.05), 'Number of spare parts (normalized)')
nsp['very small'] = fuzz.trapmf(nsp.universe, [0, 0, 0.10, 0.30])
nsp['small'] = fuzz.trimf(nsp.universe, [0, 0.20, 0.40])
nsp['rather small'] = fuzz.trimf(nsp.universe, [0.25, 0.35, 0.45])
nsp['medium'] = fuzz.trimf(nsp.universe, [0.30, 0.50, 0.70])
nsp['rather large'] = fuzz.trimf(nsp.universe, [0.55, 0.65, 0.75])
nsp['large'] = fuzz.trimf(nsp.universe, [0.60, 0.80, 1])
nsp['very large'] = fuzz.trapmf(nsp.universe, [0.70, 0.85, 1, 1])
# n.view()

# __RULES__
# Rule Base 1
rules1 = [
    ctrl.Rule(ruf['low'], nsp['small']),
    ctrl.Rule(ruf['medium'], nsp['medium']),
    ctrl.Rule(ruf['high'], nsp['large']),
    ctrl.Rule(md['very small'] & nss['small'], nsp['very large']),
    ctrl.Rule(md['small'] & nss['small'], nsp['large']),
    ctrl.Rule(md['medium'] & nss['small'], nsp['medium']),
    ctrl.Rule(md['very small'] & nss['small'], nsp['rather large']),
    ctrl.Rule(md['small'] & nss['medium'], nsp['rather small']),
    ctrl.Rule(md['medium'] & nss['medium'], nsp['small']),
    ctrl.Rule(md['very small'] & nss['large'], nsp['medium']),
    ctrl.Rule(md['small'] & nss['large'], nsp['small']),
    ctrl.Rule(md['medium'] & nss['large'], nsp['very small']),
]

# Rule Base 2
rules2 = [
    ctrl.Rule(md['very small'] & nss['small'] & ruf['low'], nsp['very small']),
    ctrl.Rule(md['small'] & nss['small'] & ruf['low'], nsp['very small']),
    ctrl.Rule(md['medium'] & nss['small'] & ruf['low'], nsp['very small']),
    ctrl.Rule(md['very small'] & nss['medium'] & ruf['low'], nsp['very small']),
    ctrl.Rule(md['small'] & nss['medium'] & ruf['low'], nsp['very small']),
    ctrl.Rule(md['medium'] & nss['medium'] & ruf['low'], nsp['very small']),
    ctrl.Rule(md['very small'] & nss['large'] & ruf['low'], nsp['small']),
    ctrl.Rule(md['small'] & nss['large'] & ruf['low'], nsp['small']),
    ctrl.Rule(md['medium'] & nss['large'] & ruf['low'], nsp['small']),
    ctrl.Rule(md['very small'] & nss['small'] & ruf['medium'], nsp['small']),
    ctrl.Rule(md['small'] & nss['small'] & ruf['medium'], nsp['very small']),
    ctrl.Rule(md['medium'] & nss['small'] & ruf['medium'], nsp['very small']),
    ctrl.Rule(md['very small'] & nss['medium'] & ruf['medium'], nsp['rather small']),
    ctrl.Rule(md['small'] & nss['medium'] & ruf['medium'], nsp['small']),
    ctrl.Rule(md['medium'] & nss['medium'] & ruf['medium'], nsp['very small']),
    ctrl.Rule(md['very small'] & nss['large'] & ruf['medium'], nsp['medium']),
    ctrl.Rule(md['small'] & nss['large'] & ruf['medium'], nsp['rather small']),
    ctrl.Rule(md['medium'] & nss['large'] & ruf['medium'], nsp['small']),
    ctrl.Rule(md['very small'] & nss['small'] & ruf['high'], nsp['very large']),
    ctrl.Rule(md['small'] & nss['small'] & ruf['high'], nsp['large']),
    ctrl.Rule(md['medium'] & nss['small'] & ruf['high'], nsp['medium']),
    ctrl.Rule(md['very small'] & nss['small'] & ruf['high'], nsp['medium']),
    ctrl.Rule(md['small'] & nss['medium'] & ruf['high'], nsp['medium']),
    ctrl.Rule(md['medium'] & nss['medium'] & ruf['high'], nsp['small']),
    ctrl.Rule(md['very small'] & nss['large'] & ruf['high'], nsp['rather large']),
    ctrl.Rule(md['small'] & nss['large'] & ruf['high'], nsp['medium']),
    ctrl.Rule(md['medium'] & nss['large'] & ruf['high'], nsp['rather small']),
]

tipping_ctrl = ctrl.ControlSystem(rules1 + rules2)
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)
tipping.input['Number of spare servers (normalized)'] = 0.2
tipping.input['Repair utilisation factor'] = 0.5
tipping.input['Mean delay (normalized)'] = 0.8
tipping.compute()
print(tipping.output['Number of spare parts (normalized)'])
nsp.view(sim=tipping)
