phy <- as.integer(readline("enter phy "))
che <- as.integer(readline("enter che "))
mat <- as.integer(readline("enter mat "))
passcount = 0
result = (phy + che + mat) * 100 / 300
if (phy > 69) {passcount = passcount + 1}
if (che > 69) {passcount = passcount + 1}
if (mat > 69) {passcount = passcount + 1}
if (phy < 0 | phy > 100) {print("phy invalid")}
if (che < 0 | che > 100) {print("che invalid")}
if (mat < 0 | mat > 100) {print("mat invalid")}
if (passcount == 0) {print("go home")}
if (passcount == 1) {print("retake course")}
if (passcount == 2) {print("retake exam")}
message("result: ", as.integer(result))