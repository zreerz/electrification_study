import gridlabd

total_homes = 100
gas_fraction = 0.25

gridlabd.command("-D")
gridlabd.command("NHOMES=%.0f" % (total_homes*gas_fraction))
gridlabd.command("model.glm")

gridlabd.start("wait")
