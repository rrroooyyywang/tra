import traci
import time
import os
import sys

class SUMOEnv():
    
    def runSUMO():
        #traci.start(["sumo-gui", "-b","0", "-e","3600", "-n", "./sumo/Road.net.xml","-r", "./sumo/Route.rou.xml"], numRetries=12000,verbose = True)
        traci.start(["sumo-gui", "-c","./sumo/RunSimulator.sumocfg"], numRetries=12000,verbose = True)

        return True
        

    def step()

        step = 0
        while step < 3600:
            traci.simulationStep()
            step += 1
        return True
        

    def closeSimulator():
        traci.close()
        return True      

    def getTrafficLightIds():
        traffic_light_ids = traci.trafficlight.getIDList()
        return traffic_light_ids


    def setRedLight(light_ids):
        
        traffic_light_ids = SUMOEnv.getTrafficLightIds()
        
        for light in traffic_light_ids:
            traci.trafficlight.setRedYellowGreenState(light, "rrrr")
        
        return True


    def setGreenLight(light_ids):

        traffic_light_ids = SUMOEnv.getTrafficLightIds()
        
        for light in traffic_light_ids:
            traci.trafficlight.setRedYellowGreenState(light, "gggg")
        
        return True
