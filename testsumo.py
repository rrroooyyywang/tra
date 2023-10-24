import traci

traci.start(["sumo-gui", "-b","0", "-e","3600", "-n", "./sumo/Road.net.xml","-r", "./sumo/Route.rou.xml"], numRetries=12000,verbose = True)
step = 0
while step < 3600:
    traci.simulationStep()
    step += 1
traci.close()