# Azure Machine Learning Pipeline Example - v2 SDK

Sample notebook (`AzureML_Pipeline_Example.ipynb`) showcasing how to convert a python script (ex: `./scripts/custom_logic.py`) into a reusable Azure Machine Learning pipeline that can be triggered on a schedule.

Here, we convert the python script at `./scripts/custom_logic.py` into a component that can be included as a step in an AML pipeline. Pipelines can contain multiple steps with intermediate outputs at each step. In this example we execute all logic as part of a single step as a standalone component. Moreover, this step utilizes a custom environment which includes all necessary python packages and is defined in `./environment.yml`.

This notebook can be run from an Azure Machine Learning Compute Instance using the Python 3.10 - v2 SDK kernel.

### Helpful Articles

- [What are Azure Machine Learning pipelines?](https://learn.microsoft.com/en-us/azure/machine-learning/concept-ml-pipelines?view=azureml-api-2)

- [What is an Azure Machine Learning component?](https://learn.microsoft.com/en-us/azure/machine-learning/concept-component?view=azureml-api-2)

- [Create and run machine learning pipelines using components with the Azure Machine Learning SDK v2](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-create-component-pipeline-python?view=azureml-api-2)

- [Manage inputs and outputs of components and pipelines](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-manage-inputs-outputs-pipeline?view=azureml-api-2&tabs=cli)

- [Schedule machine learning pipeline jobs](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-schedule-pipeline-job?view=azureml-api-2&tabs=cliv2)