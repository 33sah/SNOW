## Constraints
1) Volume must be $100$ $cm^2$.
2) Volume must have a height at least equal to $2cm$ to match CERN's beam spot size.
3) Surface Area must be maximised as much as possible. - In order to facilitate neutron and heat release.
4) If possible, the length of the proton's trajectory through the volume should be maximised. 

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

Plugging into Desmos yields:

![Desmos](https://github.com/33sah/SNOW/assets/107648256/60841de8-7857-4b93-b8c7-51b192c960cd)

So to maximise surface area we can either increase r until $r = {\sqrt {100 \over 2\pi}}$ or decrease r indefinitely.

However as we wish for the proton's trajectory through the volume to be maximised, and we will be firing through the $x$ $or$ $z$ $axis$, we wish to maximise r, so $r = {\sqrt {100 \over 2\pi}} = 3.989$ $cm$, $h = 2$ $cm$ and $A = 150.133$ $cm^2$


### Sphere

Not much to do here, simply solve for radius: 

$$ V = {4 \over 3}{\pi r^3} $$

$$ {3V \over 4\pi} = r^3 $$

$$ r = {\sqrt[3] {3V \over 4\pi}} $$

$$ V = 100 $$

$$ r = {\sqrt[3] {300 \over 4\pi}} $$

$$ r = 2.879411911 $$

$$ A = {4 \pi r^2} $$

Therefore: $A = 104.187941538$ $cm^2$ 

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

As this is the maximum value, we find that $r=1$ $cm$, $A=200$ $cm$ and $R = {100 \over {2\pi^2}} = 5.066059182$ $cm$
