from django.forms import CharField, BooleanField

from netbox.forms import NetBoxModelImportForm
from ocp_project_plugin.models import OCPProject, AppEnvironment
from tenancy.models import Contact, Tenant
from utilities.forms import CSVModelChoiceField


class AppEnvironmentImportForm(NetBoxModelImportForm):
    cluster_env = CharField(
        label="App Env",
        help_text="The app Env String used for creating the namespace e.g. tst",
    )
    app_env = CharField(
        label="App Env",
        help_text="The app Env String used for creating the namespace e.g. tst",
    )
    mtls = BooleanField(
        required=False,
        label="MTLS",
        help_text="Enable if mtls should be used",
    )
    repo = CharField(
        label="Git Repository",
        help_text="Path of git Repository, don't forget the .git at the end e.g. "
                  "https://gitlab.com/example/example-deployment-manifests.git",
    )
    branch = CharField(
        label="Git Branch",
        help_text="The git Branch of the Repository e.g. main"
    )
    path = CharField(
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
    ocp_project = CSVModelChoiceField(
        queryset=OCPProject.objects.all(),
        to_field_name='name',
        help_text='Choose the ocpproject'
    )

    class Meta:
        model = AppEnvironment

        fields = ["cluster_env", "app_env", "mtls", "repo", "branch", "path", "egress_ip", "deployment_kind",
                  "monitoring", "postgres_monitoring", "ocp_project"]


class OCPProjectImportForm(NetBoxModelImportForm):
    name = CharField(
        label='OCP Project Name',
        help_text='The ocp project name e.g. web-shop',
    )
    description = CharField(
        label='Description',
        help_text='The description of the project e.g. A web shop software',
    )
    display_name = CharField(
        label='Display name',
        help_text='Display Name of the project e.g. Web Shop Shopify'
    )
    project_owner = CSVModelChoiceField(
        queryset=Contact.objects.all(),
        to_field_name='name',
        help_text='Choose the customer'
    )
    customer = CSVModelChoiceField(
        queryset=Tenant.objects.all(),
        to_field_name='name',
        help_text='Choose the tenant'
    )
    docu_url = CharField(
        label='URL',
        help_text='The url of the project documentation',
    )
    workload = CharField(
        label='Workload',
        help_text='The workload contents e.g. Postgres DB, nginx',
    )
    request = CharField(
        label='Jira Request',
        help_text='The jira request id e.g. TICKET1234',
    )

    class Meta:
        model = OCPProject

        fields = ['name', 'description', 'display_name', 'project_owner', 'customer', 'docu_url', 'workload',
                  'request']
