'''N - Number of rollers
Rr - Radius of the roller
R - Radius of the rollers PCD (Pitch Circle Diamater)
E - Eccentricity - offset from input shaft to a cycloidal disk
'''

'''
Equations for the cycloidal drive
x = (R*cos(t))-(Rr*cos(t+arctan(sin((1-N)*t)/((R/(E*N))-cos((1-N)*t)))))-(E*cos(N*t))
y = (-R*sin(t))+(Rr*sin(t+arctan(sin((1-N)*t)/((R/(E*N))-cos((1-N)*t)))))+(E*sin(N*t))
'''
# =================
N = int(input("Enter the number of rollers (N): "))
Rr = float(input("Enter the radius of the roller (Rr): "))
R = float(input("Enter the pitch circle radius of the rollers (R): "))
E = (R / N) * 0.6
print(f"\nCalculated Eccentricity (E): {E}")

x_eq = f"({R}*cos(t))-({Rr}*cos(t+arctan(sin((1-{N})*t)/(({R}/({E}*{N}))-cos((1-{N})*t)))))-({E}*cos({N}*t))"
y_eq = f"(-{R}*sin(t))+({Rr}*sin(t+arctan(sin((1-{N})*t)/(({R}/({E}*{N}))-cos((1-{N})*t)))))+({E}*sin({N}*t))"

print(f"X(t) = {x_eq}")
print(f"Y(t) = {y_eq}")

                                                                           