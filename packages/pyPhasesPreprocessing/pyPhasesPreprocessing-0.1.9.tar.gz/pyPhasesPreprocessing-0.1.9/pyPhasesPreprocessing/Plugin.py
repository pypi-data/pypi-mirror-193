from pyPhases import PluginAdapter

from .Preprocessing import Preprocessing


class Plugin(PluginAdapter):
    def __init__(self, project, options=...):
        super().__init__(project, options)
        self.project.systemExporter["RecordNumpyMemmapExporter"] = "pyPhasesPreprocessing"
        self.project.systemExporter["MemmapRecordExporter"] = "pyPhasesPreprocessing"

        def update(value):
            if value is None or value == "preprocessing":
                self.setupPreprocessing()

        self.project.on("configChanged", update)

    def setupPreprocessing(self):
        Preprocessing.setup(self.project.config)

    def initPlugin(self):
        self.setupPreprocessing()
