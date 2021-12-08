import csv

# ----------input----------
v_list = [-250, 250, -250, 250]  # v-axis position of each point
w_list = [-100, -100, 100, 100]  # w-axis position of each point
load_list = [10, 20, 30, 100, 110, 120]  # loads on the center of pattern

# example:
# v_list = [-250, 250, -250, 250]  # v-axis position of each point
# w_list = [-100, -100, 100, 100]  # w-axis position of each point
# load_list = [10, 20, 30, 100, 110, 120]  # loads on the center of pattern

# -------------------------

# unit conversion from "mm" to "m"
v_list = [i * 0.001 for i in v_list]
w_list = [i * 0.001 for i in w_list]

Fu, Fv, Fw, Mu, Mv, Mw = load_list
n = len(v_list)

# check points
chp1 = bool(len(v_list) == len(w_list))
chp1 = f"numbers of v-list and of w-list is equal: {chp1}"
chp2 = bool(n > 1)
chp2 = f"number of bolts more than one piece: {chp2}"

v0 = sum(v_list) / n
w0 = sum(w_list) / n

Fax, Fshv, Fshw = Fu/n, Fv/n, Fw/n
Fax_by_Fu = [Fax] * n
Fshv_by_Fv = [Fshv] * n
Fshw_by_Fw = [Fshw] * n

sigma_ri_2 = sum([(vi-v0)**2+(wi-w0)**2 for vi, wi in zip(v_list, w_list)])
Fshv_by_Mu = [Mu*wi*(-1)/sigma_ri_2 for wi in w_list]
Fshw_by_Mu = [Mu*vi/sigma_ri_2 for vi in v_list]

sigma_w_2 = sum([wi**2 for wi in w_list])
sigma_v_2 = sum([vi**2 for vi in v_list])
Fax_by_MvMw = [Mv*wi/sigma_w_2+Mw*vi*(-1)/sigma_v_2 for vi, wi in zip(v_list, w_list)]

# sum up
Fax_list = [x + y for x, y in zip(Fax_by_Fu, Fax_by_MvMw)]
Fshv_list = [x + y for x, y in zip(Fshv_by_Fv, Fshv_by_Mu)]
Fshw_list = [x + y for x, y in zip(Fshw_by_Fw, Fshw_by_Mu)]

# export to csv file
with open("test.csv", "w", newline="") as f:  # "newline" to remove empty row
    writer = csv.writer(f)
    writer.writerow(["check points:"])
    writer.writerow([chp1])
    writer.writerow([chp2])
    writer.writerow([""])
    writer.writerow(["nr"] + list(range(1, n + 1)))
    writer.writerow(["v"] + v_list)
    writer.writerow(["w"] + w_list)
    writer.writerow(["Fax"] + Fax_list)
    writer.writerow(["Fshv"] + Fshv_list)
    writer.writerow(["Fshw"] + Fshw_list)
    writer.writerow(["center:", v0, w0])

print("job done.")

