## Curve Fitting

For both graphs, a logarithmic model $f(x) = a +\hspace 1cm$ $b$ $log(x)$ was used as a starting point to fit the data. 

A logarithmic relationship seemed fitting from the shape of our raw data. This relationship was also suggested by previous research regarding Spallation. [^1]

As for the process of curve fitting itself, `Scipy.optimise.curveFit` was used to determine parameters $a,b$. 

## Proportional Optimisation 

This uses the concept of elasticity to maximise neutron production. 

$N$ = Neutrons Produced 

$PE$ = Proton Energy ($GeV$)

Consider an earlier point on the neutron production graph. It has a very steep gradient so:

$$ \\% \Delta N > \\% \Delta PE $$

A change in Proton Energy leads to a greater proportional change in Neutron Production, thus Proton Energy should be increased. 

Whereas a later point has a much shallower gradient so:

$$ \\% \Delta N < \\% \Delta PE $$

A change in Proton Energy leads to a lesser proportional change in Neutron Production, thus Proton Energy should be decreased. 

Thus we know that the point where the Proton Energy should not be changed should be between these 2 points. This is where: 

$$ \\% \Delta N = \\% \Delta PE $$

As a change in Proton Energy leads to the exact proportional change in Neutron Production so Proton Energy should not be increased or decreased, this is the most optimal point and can be written as:

$$ {{\\% \Delta N} \over { \\% \Delta PE}} = 1 $$

This can also be written as:

$$ {\Delta N \over N} \div {\Delta PE \over PE} $$

As we are dealing with point elasticities, or where there is an infinitesimal change in Proton Energy and Neutron Production:

$$ {dN \over N} \div {dPE \over PE} $$

Simplifying:

$$ {dN \over dPE} {PE \over N} $$

As we can express N in terms of $a +\hspace 1cm$ $b$ $log(x)$:

$$ {dN \over dPE} {PE \over a + b*log(PE)} = 1 $$

Which we can easily solve for. 

For example, if $N = ln(PE)$:

$$ {1 \over PE} {PE \over ln(Pe)} = 1 $$

$$ {1 \over ln(PE)} = 1 $$

$$ ln(PE) = 1 $$

$$ PE = e $$

So the optimum Neutron Yield in this case would be where Proton Energy is $e$.

[^1]: [Neutron Production from Spallation Reactions: Jaegwon Yoo, October 1998](https://www.kns.org/files/pre_paper/30/98A-026.PDF) 
