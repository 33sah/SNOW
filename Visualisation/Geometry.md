## Constraints
1) Volume must be $100cm^2$.
2) Volume must have a height at least equal to $2cm$ to match CERN's beam spot size.
3) Surface Area must be maximised as much as possible. - In order to facilitate neutron and heat release. 

### Cylinder

Maximising Surface Area:

Consider a cylinder of Volume: V, Surface Area: A, Radius: r and Height: h

$$ V = {\pi r^2h} $$

$$ h = {V \over \pi r^2} $$

$$ A = {2\pi rh + 2\pi r^2} $$

$$ A = {2\pi r {V \over \pi r^2} + 2\pi r^2} $$

$$ A = {2V \over r} + {2\pi r^2} $$

$$ V = 100 $$ 

$$ h \geq 2 $$

$$ r \leq {\sqrt {100 \over \pi h}} $$

$$ r \leq {\sqrt {100 \over 2\pi}} $$



### Sphere

Not much to do here, simply solve for radius: 

$$ V = {4 \over 3}{\pi r^3} $$

$$ {3V \over 4\pi} = r^3 $$

$$ r = {\sqrt[3] {3V \over 4\pi}} $$

$$ V = 100 $$

$$ r = {\sqrt[3] {300 \over 4\pi}} $$

$$ r = 2.879411911 $$

### Torus

Consider a Torus of Volume: V, Surface Area: A, Inner Radius: r and Swept Radius: R

$$ V = 2\pi^2 r^2 R $$

$$ R = {V \over {2\pi^2 r^2}} $$

$$ A = 4\pi^2 r R $$

$$ A = {{4\pi^2 rV} \over {2\pi^2 r^2}} $$

$$ A = {2V \over r} $$

$$ V = 100 $$

$$ r \geq 1 $$

$$ A \leq 200 $$

As this is the maximum value, we find that $r=1$, $A=200$ and $R = {100 \over {2\pi^2}} = 5.066059182$
