# Azure Machine Learning Pipeline Example - v2 SDK

Sample notebook (`AzureML_Pipeline_Example.ipynb`) showcasing how to convert a python script (ex: `./scripts/custom_logic.py`) into a reusable Azure Machine Learning pipeline that can be triggered on a schedule.

Here, we convert the python script at `./scripts/custom_logic.py` into a component that can be included as a step in an AML pipeline. Pipelines can contain multiple steps with intermediate outputs at each step. In this example we execute all logic as part of a single step as a standalone component. Moreover, this step utilizes a custom environment which includes all necessary python packages and is defined in `./environment.yml`.