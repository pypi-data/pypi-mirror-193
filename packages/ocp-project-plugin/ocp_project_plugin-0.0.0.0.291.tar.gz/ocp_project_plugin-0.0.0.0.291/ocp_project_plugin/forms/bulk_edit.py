from django.forms import CharField, BooleanField

from netbox.forms import NetBoxModelBulkEditForm
from ocp_project_plugin.models import AppEnvironment, OCPProject


class AppEnvironmentBulkEditForm(NetBoxModelBulkEditForm):
    model = AppEnvironment

    app_env = CharField(
        required=False,
        label="App Env",
        help_text="The app Env String used for creating the namespace e.g. tst",
    )
    mtls = BooleanField(
        required=False,
        label="MTLS",
        help_text="Enable if mtls should be used",
    )
    repo = CharField(
        required=False,
        label="Git Repository",
        help_text="Path of git Repository, don't forget the .git at the end e.g. "
                  "https://gitlab.com/example/example-deployment-manifests.git",
    )
    branch = CharField(
        required=False,
        label="Git Branch",
        help_text="The git Branch of the Repository e.g. main"
    )
    path = CharField(
        required=False,
        label="Git Path",
        help_text="Path of the deployment files e.g. overlays/tst"
    )
    egress_ip = CharField(
        required=False,
        label="Egress IP",
        help_text="The egress IP e.g. 10.10.10.10"
    )
    monitoring = BooleanField(
        required=False,
        label="Monitoring",
        help_text="Enable if monitoring should be used",
    )
    postgres_monitoring = BooleanField(
        required=False,
        label="Postgres Monitoring",
        help_text="Enable if postgres monitoring should be used",
    )


class OCPProjectBulkEditForm(NetBoxModelBulkEditForm):
    model = OCPProject

    name = CharField(
        required=False,
        label='OCP Project Name',
        help_text='The ocp project name e.g. web-shop',
    )
    description = CharField(
        required=False,
        label='Description',
        help_text='The description of the project e.g. A web shop software',
    )
    display_name = CharField(
        required=False,
        label='Display name',
        help_text='Display Name of the project e.g. Web Shop Shopify'
    )
    project_owner = CharField(
        required=False,
        label='Owner',
        help_text='Choose the project owner'
    )
    customer = CharField(
        required=False,
        label='Customer name',
        help_text='Choose the tenant'
    )
    docu_url = CharField(
        required=False,
        label='URL',
        help_text='The url of the project documentation',
    )
    workload = CharField(
        required=False,
        label='Workload',
        help_text='The workload contents e.g. Postgres DB, nginx',
    )
    request = CharField(
        required=False,
        label='Jira Request',
        help_text='The jira request id e.g. TICKET1234',
    )
