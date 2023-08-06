from django.forms import CharField, BooleanField, DecimalField, NullBooleanField

from netbox.forms import NetBoxModelFilterSetForm
from ocp_project_plugin.choices import AppEnvironmentClusterEnvChoices, AppEnvironmentDeploymentKindChoices
from ocp_project_plugin.models import AppEnvironment, OCPProject
from tenancy.models import Contact, Tenant
from utilities.forms import MultipleChoiceField, DynamicModelMultipleChoiceField, DynamicModelChoiceField, StaticSelect, \
    BOOLEAN_WITH_BLANK_CHOICES


class AppEnvironmentFilterForm(NetBoxModelFilterSetForm):
    """Form for filtering App Environment instances."""

    model = AppEnvironment
    fieldsets = (
        (None, ('q', 'filter_id')),
        ('OCP Project', ['ocp_project']),
        ('Environment', ('cluster_env', 'app_env')),
        ('Deployment', ('repo', 'branch', 'path', 'deployment_kind')),
        ('Monitoring', ('monitoring', 'postgres_monitoring')),
        ('Resources', ('limits_cpu', 'limits_memory', 'requests_cpu', 'requests_memory')),
        ('Additional Config', ('mtls', 'egress_ip')),
    )
    # OCP Project Filters
    ocp_project = DynamicModelMultipleChoiceField(
        queryset=OCPProject.objects.all(),
        required=False,
        label='OCP Project',
    )
    # Environment Filters
    app_env = CharField(
        help_text="The app Env String used for creating the namespace e.g. tst",
        label="App Environment name",
        required=False,
    )
    cluster_env = MultipleChoiceField(
        choices=AppEnvironmentClusterEnvChoices,
        help_text="The Cluster Environment e.g. DEV, TST, INT, PRD",
        label="Cluster Environment",
        required=False,
    )
    # Deployment Filters
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
    deployment_kind = MultipleChoiceField(
        choices=AppEnvironmentDeploymentKindChoices,
        help_text="Choose the way how the deployment should work",
        label="Deployment Kind",
        required=False
    )
    # Monitoring Filters
    monitoring = NullBooleanField(
        required=False,
        label="Monitoring",
        help_text="Enable if monitoring should be used",
        widget=StaticSelect(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )
    postgres_monitoring = NullBooleanField(
        required=False,
        label="Postgres Monitoring",
        help_text="Enable if postgres monitoring should be used",
        widget=StaticSelect(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )
    # Resources Filters
    limits_cpu = DecimalField(
        required=False,
        label="CPU Limit",
        help_text="The CPU request value e.g. 2"
    )
    limits_memory = CharField(
        required=False,
        label="Memory Limit",
        help_text="The CPU memory value e.g. 400Mi or 2Gi"
    )
    requests_cpu = DecimalField(
        required=False,
        label="CPU request",
        help_text="The CPU request value e.g. 1"
    )
    requests_memory = CharField(
        required=False,
        label="Memory request",
        help_text="The memory value e.g. 200Mi or 1Gi"
    )
    # Additional Config
    mtls = NullBooleanField(
        required=False,
        label="MTLS",
        help_text="Enable if mtls should be used",
        widget=StaticSelect(
            choices=BOOLEAN_WITH_BLANK_CHOICES
        )
    )
    egress_ip = CharField(
        required=False,
        label="Egress IP",
        help_text="The egress IP e.g. 10.10.10.10"
    )


class OCPProjectFilterForm(NetBoxModelFilterSetForm):
    """Form for filtering App Environment instances."""

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
    project_owner = DynamicModelChoiceField(
        required=False,
        queryset=Contact.objects.all(),
        label='Project Owner',
        help_text='Choose the Project Owner'
    )
    customer = DynamicModelChoiceField(
        required=False,
        queryset=Tenant.objects.all(),
        label='Customer name',
        help_text='Choose the tenant',
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
