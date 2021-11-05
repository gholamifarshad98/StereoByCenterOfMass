import matplotlib.pyplot as plt
import numpy
import numpy as np
from Kernel import Kernel
class StereoByCenterOfMass:
    def __init__(self, leftImage, rightImage, selectedDisparity,numOfKernelInHorizon, numOfKernelInVertical):
        self.leftImage = leftImage
        self.rightImage = rightImage
        self.disparity = selectedDisparity
        self.numOfRowOfKernel = int(self.leftImage.shape[0]/numOfKernelInVertical)
        self.numOfColumnOfKernel = int((self.leftImage.shape[1]-self.disparity)/numOfKernelInHorizon)
        self.numOfKernelInVertical = numOfKernelInVertical
        self.numOfKernelInHorizon = numOfKernelInHorizon
        self.anchorLocationRow = int(self.numOfRowOfKernel/2)
        self.anchorLocationColumn = int(self.numOfColumnOfKernel/2)
        self.rowsInImage = leftImage.shape[0]
        self.columnsInImage = leftImage.shape[1]
        self.kernels = []
        self.result = numpy.zeros((self.rowsInImage,self.columnsInImage))
        self.createKernels()

    def createKernels(self):
        for row in range(self.numOfKernelInVertical):
            tempKernelsInRow = []
            for column in range(self.numOfKernelInHorizon):
                tempKernel =Kernel(numOfRow=self.numOfRowOfKernel,numOfColumn=self.numOfColumnOfKernel,anchorLocationRow=self.anchorLocationRow,anchorLocationCol=self.anchorLocationColumn)
                tempKernel.setKernelAnchorLocatioInImage(rowOfKernelInImage= row*self.numOfRowOfKernel+self.anchorLocationRow , columnOfKernelInImage= column*self.numOfColumnOfKernel+self.anchorLocationColumn)
                tempKernelsInRow.append(tempKernel)
            self.kernels.append(tempKernelsInRow)

    def drawColorInKernels(self):
        for row in range(self.numOfKernelInVertical):
            for column in range(self.numOfKernelInHorizon):
                if self.kernels[row][column].detectedObstacle:
                    for rowInKernel in range(self.kernels[row][column].numOfRowsOfKernel):
                        for columnInKernel in range(self.kernels[row][column].numOfColumnOfKernel):
                            rowIndex = rowInKernel + self.kernels[row][column].rowOfKernelInImage - self.kernels[row][column].anchorLocationRow
                            columnIndex = columnInKernel + self.kernels[row][column].columnOfKernelInImage - self.kernels[row][column].anchorLocationCol
                            self.result[rowIndex][columnIndex] = 255


    def calcStereo(self):
        for row in range(self.numOfKernelInVertical):
            for column in range(self.numOfKernelInHorizon):
                print("=========================")
                print("row",row,"column",column)
                self.kernels[row][column].calcCenterOfMassRight(self.rightImage)
                self.kernels[row][column].calcCenterOfMassleft(self.leftImage,self.disparity)
                print(self.kernels[row][column].centerOfMassLeft)
                print(self.kernels[row][column].centerOfMassRight)
                if self.kernels[row][column].centerOfMassLeft == self.kernels[row][column].centerOfMassRight:
                    self.kernels[row][column].detectedObstacle = True
        self.drawColorInKernels()
        # fig, ax1 = plt.plot()
        # ax1.plot(self.result)
        plt.imshow(self.result,cmap='gray', vmin=0, vmax=255)
        plt.show()

