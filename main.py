import math
#   CNC HF 1

# ADATOK

asztal_l = 365
asztal_w = 305
asztal_h = 36


forgacsolas_h = 36
loket = 400
terhelo_tomeg = 50
m_mdb = terhelo_tomeg
F_g = 2
v_max = 1.2
v_gyors = 1.8
l_10h = 8000
eta = 0.9
pi = math.pi
g = 9.81
v_egyen = (v_max*60+v_gyors*60)/4

f_w = 1.6
F_a = 1


h_m = 0.030
h_mm = 30
# MUNKAPONTOK
print("Munkapontok")
#A
print("A\n")
n_A = ((v_max/2)/h_m)*60
M_A = (F_g*h_mm) / (0.9*2*pi)

print(f"n_A = {n_A}")
print(f"M_A = {M_A}")
print("\n")

#B
print("B\n")
n_B = (v_max / h_m) * 60
M_B = ((F_g / 2)*h_mm) / (eta*2*math.pi)

print(f"n_B = {n_B}")
print(f"M_B = {M_B}")
print("\n")

#C
print("C\n")
n_C = (v_gyors / h_m)*60
M_C = ((F_g/10)*h_mm)/(eta*2*pi)

print(f"n_C = {n_C}")
print(f"M_C = {M_C}")
print("\n")

print("Golyosorso meretezese")

print(f"v_egyen = {v_egyen} m/min")
l_10m = (l_10h*60*v_egyen) / h_m
print(f"l_10m = {l_10m} [fordulat]")

tiz_hatodikon = pow(10,6)
gyok = pow(l_10m /tiz_hatodikon, 1/3)
C_a = gyok*f_w*F_a

print("Dinamikus alapterheles")
print(f"C_a = {C_a} [kN]")

print("\n")

# KRITIKUS FORDULATSZAM
print("Kritikus fordulatszam")
lambda_2 = 15.1
d_1 = 32.4
l_b = 550
n_krit = lambda_2 * (d_1 / pow(l_b,2)) * pow(10,7)
print(f"n_krit = {n_krit}")

print("\n")

# HATARFORDULATSZAM
print("Hatarfordulatszam")
DN = 160000
d_p = 39

n_hatar = DN / d_p

print(f"n_hatar = {n_hatar}")
print("\n")

# KIHAJLAS
print("Kihajlas")
eta_2 = 10
l_szerelesi = 550

P_1 = eta_2 * (pow(d_1,4) / pow(l_szerelesi, 2) ) * pow(10, 4)
print(f"P_1 = {P_1}")
M_0 = 13.3
F_M = (M_0*2*pi*eta) / h_m
print(f"F_M = {F_M}")

print("\n")


#EROK MEGHATAROZASA
print("Vezetek meretezese")
v_asztal_mm = 365 * 305* 36
v_asztal_m = v_asztal_mm * pow(10, -9)
print(f"v_asztal = {v_asztal_mm} [mm^3] = {v_asztal_m} [m^3]")

ro_asztal = 7850
asztal_kitoltes = 1
m_asztal = v_asztal_m * ro_asztal
print(f"m_asztal = {m_asztal} [kg]")

print("\n")

F_f1 =  F_g*0.5
F_f2 = F_g*0.25
F_f3 =  F_g*0.5

W = (m_mdb * g + m_asztal * g) / 1000

print(f"F_f1 = {F_f1} [kN]")
print(f"F_f2 = {F_f2} [kN]")
print(f"F_f3 = {F_f3} [kN]")
print(f"W = {W} [kN]")

print("\n")
q_1 = F_f1
q_2 = F_f2 + W
q_3 = F_f3

print(f"Q_1 = {q_1} [kN]")
print(f"Q_2 = {q_2} [kN]")
print(f"Q_3 = {q_3} [kN]")

print("\n")

papucs_l = 68.3
papucs_w = 42
papucs_h = 28
papucs_w2 = 11

vezetek_h = 16.5
vezetek_w = 20

l3_s = 19.55 + asztal_h + forgacsolas_h
l5_s = 131.85

l_0 = asztal_l - 2*0.5*papucs_l
l_1 = asztal_w - 2*0.5*vezetek_w
l_2 = 0
l_4 = 0
l_3x = papucs_h + asztal_h + forgacsolas_h
l_3 = l3_s
l_5 = l5_s

print(f"l_3s = {l3_s}")
print(f"l_0 = {l_0}")
print(f"l_1= {l_1}")
print(f"l_2 = {l_2}")
print(f"l_3 = {l_3}")
print(f"l_4 = 0")
print(f"l_5 = {l_5}")

print("\n")

#UNDER FORCE Q1

q1f1 = (q_1*l_5) / (2*l_0)
q1f1t = (q_1*l_4) / (2*l_0)

print("FORCE UNDER Q1\n")
print(f"f1=f2=f3=f4={q1f1}")
print(f"f1t=f2t=f3t=f4t={q1f1t}")

print("\n")

#UNDER FORCE Q2

q2f1 = (q_2 / 4) + (q_2 * l_2) / (2*l_0)
q2f2 = (q_2 / 4) - (q_2 * l_2 ) / (2*l_0)

print("FORCE UNDER Q2\n")
print(f"f1=f4={q2f1}")
print(f"f2=f3={q2f2}")

print("\n")

#UNDER FORCE Q3

q3f1 = (q_3*l_3) / (2 * l_1)
q3f1t = (q_3 / 4) + (q_3*l_2) / (2*l_0)
q3f2t = (q_3 / 4) - (q_3*l_2) / 2*l_0

print("FORCE UNDER Q3\n")
print(f"f1=f2=f3=f4={q3f1}")
print(f"f1t=f4t={q3f1t}")
print(f"f2t=f3t={q3f2t}")

print("\n")

p_1 = q1f1 + q1f1t + q2f1 + q3f1 + q3f1t
p_2 = q1f1 +q1f1t + q2f2 + q3f1 + q3f2t
p_3 = q1f1 + q1f1t + q2f2 + q3f1 + q3f2t
p_4 = q1f1 + q1f1t + q2f1 + q3f1 + q3f1t

print(f"p_1 = {p_1}")
print(f"p_2 = {p_2}")
print(f"p_3 = {p_3}")
print(f"p_4 = {p_4}")

f_h = 1
f_t = 1
f_c = 0.66
f_w = 1.6

print("\n")
print("Elettartam kilometerben\n")
v_egyen_kmh = ((v_max + v_gyors) / 4) * 3.6
print(f"v_egyen kilometerben = {v_egyen_kmh}")
L = l_10h * v_egyen_kmh
print(f"Elettartam kilometerben: L_km = {L}\n")

# DINAMIKUS ALAPTERHELÉS

C = pow((L/50),1/3) * (f_w/(f_h*f_t*f_c))*p_1

print(f"C = {C}")
print("\n")
# STATIKUS ALAPTERHELÉS
print("Statikus alapterhelés\n")

F_f1s = 2*F_f1
F_f2s = 2*F_f2
F_f3s = 2*F_f3
W_s = m_asztal * g + m_mdb * g

q_1s =  F_f1s
q_2s = F_f2s + W_s
q_3s = F_f3s

#UNDER FORCE Q1s

q1f1s = (q_1s*l_5) / (2*l_0)
q1f1ts = (q_1s*l_4) / (2*l_0)
print("FORCE UNDER Q1\n")
print(f"f1=f2=f3=f4={q1f1s}")
print(f"f1t=f2t=f3t=f4t={q1f1ts}\n")

#UNDER FORCE Q2s
print("FORCE UNDER Q2\n")
q2f1s = q_3s / 4
q2f2s = q2f1s

print(f"f1=f4={q2f1s}")
print(f"f2=f3={q2f2s}")
print("\n")
#UNDER FORCE Q3s
print("FORCE UNDER Q3\n")

q3f1s = (q_3s*l_3) / (2 * l_1)
q3f1ts = (q_3s / 4) + (q_3s*l_2) / (2*l_0)
q3f2ts = (q_3s / 4) - (q_3s*l_2) / 2*l_0

print(f"f1=f2=f3=f4={q3f1}")
print(f"f1t=f4t={q3f1t}")
print(f"f2t=f3t={q3f2t}")

print("\n")
p_1s = q1f1s + q1f1ts + q2f1s + q3f1s + q3f1ts
p_2s = q1f1s +q1f1ts + q2f2s + q3f1s + q3f2ts
p_3s = q1f1s + q1f1ts + q2f2s + q3f1s + q3f2ts
p_4s = q1f1s + q1f1ts + q2f1s + q3f1s + q3f1ts

print(f"p_1s = {p_1s}")
print(f"p_2s = {p_2s}")
print(f"p_3s = {p_3s}")
print(f"p_4s = {p_4s}")
print("\n")
f_s = 4.5
P_0 = p_1s

print(f"P_0 = {P_0}")
C_0 = f_s * P_0
print(f"C_0 = {C_0}")

# TEHETETLENSEGI NYOMATEKOK
print("Tehetetlensegi nyomatekok\n")

theta_m = 2.84 * 10**-4
theta_tkp = 200.3*10**-6
theta_g = 1.6*10**-6 * l_szerelesi
print(f"theta_g = {theta_g}")
print("\n")
# GYORSULAS
print("GYORSULAS\n")
a = (M_0 * h_m) / (theta_m + theta_g + theta_tkp + (m_asztal * h_m**2)/(4*pi**2)*2*pi)
print(f"a = {a}")





