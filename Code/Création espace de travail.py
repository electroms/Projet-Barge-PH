# Pour attacher env à un espace de travail azure ml
# az ml folder attach -w wsnew1 -g azureMLresourceGroup -e mldemoexperiment
from azureml.core import Workspace, Environment, Experiment, ScriptRunConfig
from azureml.core.compute import AmlCompute, ComputeTarget
from azureml.core.compute_target import ComputeTargetException

print("Start Creation of workspace")

ws = Workspace.create(name='projectworkspace',
                      subscription_id='your_subscribtion_id',
                      resource_group='azureMLresourceGroup',
                      create_resource_group=True,
                      location='eastus2'
                     )

# écrire les détails de l'espace de travail dans un fichier de configuration en .azureml/config.json
ws.write_config(path="./.azureml", file_name="config.json")

# Chargez votre espace de travail en lisant le fichier de configuration.
# ws_environment = Workspace.from_config(path="./.azureml/config.json")