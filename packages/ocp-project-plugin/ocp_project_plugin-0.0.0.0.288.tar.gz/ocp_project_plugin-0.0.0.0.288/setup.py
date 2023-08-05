# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ocp_project_plugin',
 'ocp_project_plugin.api',
 'ocp_project_plugin.filters',
 'ocp_project_plugin.forms',
 'ocp_project_plugin.migrations',
 'ocp_project_plugin.models',
 'ocp_project_plugin.tables',
 'ocp_project_plugin.templatetags',
 'ocp_project_plugin.views']

package_data = \
{'': ['*'],
 'ocp_project_plugin': ['templates/ocp_project_plugin/*',
                        'templates/ocp_project_plugin/app_environment/*',
                        'templates/ocp_project_plugin/ocp_project/*']}

install_requires = \
['gitpython>=3.1.30,<4.0.0', 'python-gitlab>=3.13.0,<4.0.0']

setup_kwargs = {
    'name': 'ocp-project-plugin',
    'version': '0.0.0.0.288',
    'description': 'Netbox OCP Project Plugin',
    'long_description': '# General\n## Build Project\nTo build the project go to login in the pypi web ui and get your token. Add your token to the local pypi config.\n```\npoetry config pypi-token.pypi pypi-\n```\nAfter you made changes, change the version in the files pyproject.toml and netbox_storage/__init__.py\n\nNow you can build and publish the project.\n```\npoetry publish --build\n```\n\n## Use Project\nLink: https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins\n\ndocker-compose build --no-cache && docker-compose build --no-cache && docker-compose up -d\n\n\ngit clone https://oauth2:glpat-j2VmN5sYUoSfZiZReow9@gitlab.ti8m.ch:ti8m-siem/siem-ansible.git\n\n## Directory structure\n\n```\n+- api - The API Classes, consitsts of Serializer, URL Mapper and Views\n+- filters - Filters of the models, the implementation of the method search, for searching\n+- forms - The ModelForm, ModelFilterForm, ModelImportForm, ModelBulkEditForm, the forms which will be displayed\n+- migrations - DB Django Migration steps\n+- tables - The ModelTable, which has the configuration on how the table looks like\n+- templates\n  +- netbox_storage - The detail view of each model\n    +- drive - The template content of drive, with base and partition model\n    +- inc - The template content box in the Virtual Machine Model\n    +- partition - The template content of partition, with base and physicalvolume model\n    +- physicalvolume - The template content of physicalvolume with base and linuxvolume model\n    +- volumegroup - The template content of volumegroup with base, logicalvolume and physicalvolume\n+- views - PhysicalvolumeListView, PhysicalvolumeView, PhysicalvolumeEditView, PhysicalvolumeDeleteView, \n           PhysicalvolumeBulkImportView, PhysicalvolumeBulkEditView, PhysicalvolumeBulkDeleteView\n```\n## ERM\n\n![The ERM of the Project](documents/erm.jpg?raw=true "ERM Diagram")\n\n## Queues / Worker\n\n### 1. Job - add_project\n1. Git Repo pullen\n2. Überprüfen ob es einen Branch mit dem Ticket Namen schon gibt\n3. Neuer Branch erstellen mit dem Ticket Namen\n4. Secrets entschlüsseln\n5. OCPPRoject/AppEnvironment Model Daten in yaml konvertieren\n6. YAML Daten dem values.yaml anfügen\n7. Secrets der Secrets Datei anfügen\n8. Secret verschlüsseln\n9. Mergen\n\n# Static files\n/opt/netbox/netbox/static/models\n\n# Python documentation\nI used the Sphinx Format for the documentation of the methods and classes\n\n# Export Templates\n```\nApp Environment,Cluster Environment,Project Owner\n{# Rows #}\n{%- for env in queryset -%}\n{{ env.app_env }},{{ env.cluster_env }},{{ env.ocp_project.project_owner }}\n{% endfor %}\n```\n\n# Draw.io System Topography Algorithm\n1. Überprüfen ob Horizontal Pod Autoscaler verwendet wird\n2. Falls ja variable start_pod_x setzten, x sollte unter netpool sein\n3. y_axis_k8s_start setzten: 145\n4. Anzahl replicas auslesen\n5. Falls replicas grösser als 1 dann\n6. for 1, replicas:\n7. total_y_axis_deployment_start = total_y_axis_deployment_start + y_axis_deployment_start + (n * 90)\n8. Danach teilen durch anzahl replicas --> ergibt mittelwert auch durchschnitt genannt\n9. diesen wert für y_axis setzten\n10. Von start_pod_x 3 * + 90 hinzufügen --> hpa setzten\n11. Von start_pod_x 3 * + 90 hinzufügen --> deployment setzten\n12. Von start_pod_x 3 * + 90 hinzufügen --> replica set setzten\n13. Anzeigen aller deployments die nicht in hpa sind\n14. \n14. Anzeigen aller replicasets die nicht in deployments sind\n15. \n15. Anzeigen aller statefullsets\n16. ',
    'author': 'Tim Rhomberg',
    'author_email': 'timrhomberg@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
