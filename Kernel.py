from matplotlib import pyplot as plt
import numpy as np
from tqdm import tqdm


class Kernel():
    def __init__(self, numOfRow, numOfColumn, anchorLocationRow, anchorLocationCol):
        self.numOfRowsOfKernel = numOfRow
        self.numOfColumnOfKernel = numOfColumn
        self.anchorLocationRow = anchorLocationRow
        self.anchorLocationCol = anchorLocationCol
        self.rowOfKernelInImage = 0
        self.columnOfKernelInImage = 0
        self.centerOfMassRight = [-1,-1]
        self.centerOfMassLeft = [-1,-1]
        self.massLeft = 0
        self.massRight = 0
        self.detectedObstacle = False

    def setKernelAnchorLocatioInImage(self,rowOfKernelInImage,columnOfKernelInImage):
        self.rowOfKernelInImage = rowOfKernelInImage
        self.columnOfKernelInImage = columnOfKernelInImage

    def calcCenterOfMassleft(self,leftImage, disparity):
        tempMass = 0
        tempXMass = 0
        tempYMass = 0
        for row in range(self.numOfRowsOfKernel):
            for column in range(self.numOfColumnOfKernel):
                mass = int(abs(int(leftImage[self.rowOfKernelInImage+row-self.anchorLocationRow][self.columnOfKernelInImage+column-self.anchorLocationCol+disparity])))
                tempMass = tempMass + mass
                tempXMass = tempXMass + column * mass
                tempYMass = tempYMass + row * mass

        self.massLeft = tempMass
        self.centerOfMassLeft = [int(tempXMass/self.massLeft), int(tempYMass/self.massLeft)]


    def calcCenterOfMassRight(self,rightImage):
        tempMass = 0
        tempXMass = 0
        tempYMass = 0
        for row in range(self.numOfRowsOfKernel):
            for column in range(self.numOfColumnOfKernel):
                mass = int(abs(int(rightImage[self.rowOfKernelInImage+row-self.anchorLocationRow][self.columnOfKernelInImage+column-self.anchorLocationCol])))
                tempMass = tempMass + mass
                tempXMass = tempXMass + column * mass
                tempYMass = tempYMass + row * mass

        self.massRight = tempMass
        self.centerOfMassRight = [int(tempXMass/self.massRight), int(tempYMass/self.massRight)]
