import os
import unittest
import vtk, qt, ctk, slicer
import logging
from SimulatorGuideletLoadable import SimulatorGuideletLoadable, SimulatorGuideletLogic, SimulatorGuideletTest, SimulatorGuideletWidget
from SimulatorGuidelet import SimulatorGuidelet


class UsSimulatorTraining(SimulatorGuideletLoadable):
  """Uses GuideletLoadable class, available at:
  """

  def __init__(self, parent):
    SimulatorGuideletLoadable.__init__(self, parent)
    self.parent.title = "Us Simulation Navigation"
    self.parent.categories = ["USSimulator"]
    self.parent.dependencies = []
    self.parent.contributors = ["Carlos Luque (ULPGC)"]
    self.parent.helpText = """
    US simulations
    """
    self.parent.acknowledgementText = """
    NAMIC
    """ # replace with organization, grant and thanks.

class UsSimulatorTrainingWidget(SimulatorGuideletWidget):
  def __init__(self, parent = None):
    SimulatorGuideletWidget.__init__(self, parent)

  def setup(self):
    SimulatorGuideletWidget.setup(self)

  def addLauncherWidgets(self):
    SimulatorGuideletWidget.addLauncherWidgets(self)

  def createGuideletInstance(self):
    return UsSimulatorTrainingGuidelet(None, self.guideletLogic, self.selectedConfigurationName)

  def createGuideletLogic(self):
    return UsSimulatorTrainingLogic()

class UsSimulatorTrainingLogic(SimulatorGuideletLogic):
  """Uses GuideletLogic base class, available at:
  """ #TODO add path

  def __init__(self, parent = None):
    SimulatorGuideletLogic.__init__(self, parent)

class UsSimulatorTrainingTest(SimulatorGuideletTest):
  """This is the test case for your scripted module.
  """

  def runTest(self):
    """Run as few or as many tests as needed here.
    """
    SimulatorGuideletTest.runTest(self)
    

class UsSimulatorTrainingGuidelet(SimulatorGuidelet):

  def __init__(self, parent, logic, configurationName='Default'):
    SimulatorGuidelet.__init__(self, parent, logic, configurationName)

    logging.debug('UsSimulatorTrainingGuidelet.__init__')
    self.logic.addValuesToDefaultConfiguration()

     # Set up main frame.

    self.sliceletDockWidget.setObjectName('UsSimulatorTrainingPanel')
    self.sliceletDockWidget.setWindowTitle('UsSimulatorTraining')
    self.mainWindow.setWindowTitle('UsSimulatorTraining')

  def __del__(self):#common
    self.cleanup()

  # Clean up when slicelet is closed
  def cleanup(self):#common
    SimulatorGuidelet.cleanup(self)
    logging.debug('cleanup')

  def createFeaturePanels(self):
    # Create GUI panels.
    logging.debug('UsSimulatorTraining.createFeaturePanels()')

    self.LoadSceneCollapsibleButton = ctk.ctkCollapsibleButton()
    self.SetupLoadSceneCollapsibleButton()

    featurePanelList = SimulatorGuidelet.createFeaturePanels(self)


    featurePanelList[len(featurePanelList):] = [self.LoadSceneCollapsibleButton]


    return featurePanelList

  def setupConnections(self):
    logging.debug('UsSimulatorTraining.setupConnections()')
    SimulatorGuidelet.setupConnections(self)

    self.LoadSceneButton.connect('clicked()', self.openLoadSceneDialog)

  def disconnect(self):#TODO see connect
    logging.debug('UsSimulatorTraining.disconnect()')
    SimulatorGuidelet.disconnect(self)
  
  def SetupLoadSceneCollapsibleButton(self):
    logging.debug('SetupLoadSceneCollapsibleButton')

    self.LoadSceneCollapsibleButton.setProperty('collapsedHeight', 20)
    self.LoadSceneCollapsibleButton.text = 'Scene'
    self.sliceletPanelLayout.addWidget(self.LoadSceneCollapsibleButton)

    self.LoadSceneLayout = qt.QFormLayout(self.LoadSceneCollapsibleButton)
    self.LoadSceneLayout.setContentsMargins(12, 4, 4, 4)
    self.LoadSceneLayout.setSpacing(4)

    self.LoadSceneButton = qt.QPushButton('Load Scene')
    self.LoadSceneLayout.addRow(self.LoadSceneButton)

  def openLoadSceneDialog(self):
    slicer.app.ioManager().openLoadSceneDialog()
    self.layoutManager.setLayout(self.one2Ddual3dCustomLayoutId)
    self.setupConnectorNode()  # checking
    