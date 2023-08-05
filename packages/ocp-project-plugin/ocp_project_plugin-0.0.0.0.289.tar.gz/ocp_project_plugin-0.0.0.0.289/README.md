# General
## Build Project
To build the project go to login in the pypi web ui and get your token. Add your token to the local pypi config.
```
poetry config pypi-token.pypi pypi-
```
After you made changes, change the version in the files pyproject.toml and netbox_storage/__init__.py

Now you can build and publish the project.
```
poetry publish --build
```

## Use Project
Link: https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

docker-compose build --no-cache && docker-compose build --no-cache && docker-compose up -d


git clone https://oauth2:glpat-j2VmN5sYUoSfZiZReow9@gitlab.ti8m.ch:ti8m-siem/siem-ansible.git

## Directory structure

```
+- api - The API Classes, consitsts of Serializer, URL Mapper and Views
+- filters - Filters of the models, the implementation of the method search, for searching
+- forms - The ModelForm, ModelFilterForm, ModelImportForm, ModelBulkEditForm, the forms which will be displayed
+- migrations - DB Django Migration steps
+- tables - The ModelTable, which has the configuration on how the table looks like
+- templates
  +- netbox_storage - The detail view of each model
    +- drive - The template content of drive, with base and partition model
    +- inc - The template content box in the Virtual Machine Model
    +- partition - The template content of partition, with base and physicalvolume model
    +- physicalvolume - The template content of physicalvolume with base and linuxvolume model
    +- volumegroup - The template content of volumegroup with base, logicalvolume and physicalvolume
+- views - PhysicalvolumeListView, PhysicalvolumeView, PhysicalvolumeEditView, PhysicalvolumeDeleteView, 
           PhysicalvolumeBulkImportView, PhysicalvolumeBulkEditView, PhysicalvolumeBulkDeleteView
```
## ERM

![The ERM of the Project](documents/erm.jpg?raw=true "ERM Diagram")

## Queues / Worker

### 1. Job - add_project
1. Git Repo pullen
2. Überprüfen ob es einen Branch mit dem Ticket Namen schon gibt
3. Neuer Branch erstellen mit dem Ticket Namen
4. Secrets entschlüsseln
5. OCPPRoject/AppEnvironment Model Daten in yaml konvertieren
6. YAML Daten dem values.yaml anfügen
7. Secrets der Secrets Datei anfügen
8. Secret verschlüsseln
9. Mergen

# Static files
/opt/netbox/netbox/static/models

# Python documentation
I used the Sphinx Format for the documentation of the methods and classes

# Export Templates
```
App Environment,Cluster Environment,Project Owner
{# Rows #}
{%- for env in queryset -%}
{{ env.app_env }},{{ env.cluster_env }},{{ env.ocp_project.project_owner }}
{% endfor %}
```

# Draw.io System Topography Algorithm
1. Überprüfen ob Horizontal Pod Autoscaler verwendet wird
2. Falls ja variable start_pod_x setzten, x sollte unter netpool sein
3. y_axis_k8s_start setzten: 145
4. Anzahl replicas auslesen
5. Falls replicas grösser als 1 dann
6. for 1, replicas:
7. total_y_axis_deployment_start = total_y_axis_deployment_start + y_axis_deployment_start + (n * 90)
8. Danach teilen durch anzahl replicas --> ergibt mittelwert auch durchschnitt genannt
9. diesen wert für y_axis setzten
10. Von start_pod_x 3 * + 90 hinzufügen --> hpa setzten
11. Von start_pod_x 3 * + 90 hinzufügen --> deployment setzten
12. Von start_pod_x 3 * + 90 hinzufügen --> replica set setzten
13. Anzeigen aller deployments die nicht in hpa sind
14. 
14. Anzeigen aller replicasets die nicht in deployments sind
15. 
15. Anzeigen aller statefullsets
16. 