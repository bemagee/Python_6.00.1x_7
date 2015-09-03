#!/usr/bin/env python
varA = 22
varB = 35

if type(varA)== str or type(varB) == str:
    print "string involved"
elif varA > varB:
    print "bigger"
elif varA == varB:
    print "equal"
else:
    print "smaller"
