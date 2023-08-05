from django.forms import PasswordInput

from ipam.models import IPAddress
from netbox.forms import NetBoxModelForm
from ocp_project_plugin.models import OCPProject, AppEnvironment
from tenancy.models import Contact, Tenant
from utilities.forms import DynamicModelChoiceField, APISelectMultiple


class AppEnvironmentBaseForm(NetBoxModelForm):
    egress_ip = DynamicModelChoiceField(
        queryset=IPAddress.objects.all(),
        #queryset=Prefix.get_child_ips(Prefix.objects.get(prefix='10.190.1.64/26')),
        #queryset=IPAddress.objects.all(),
        label="Egress IP",
        help_text="Select your egress ip",
        widget=APISelectMultiple(
            api_url='/api/ipam/ip-addresses/?q=&parent=10.190.1.64/26',
        ),
        required=False
    )

    fieldsets = (
        ('OCP Project', ['ocp_project']),
        ('Environment', ('cluster_env', 'app_env')),
        ('Deployment', ('repo', 'branch', 'access_token', 'path', 'deployment_kind')),
        ('Monitoring', ('monitoring', 'postgres_monitoring')),
        ('Resources', ('limits_cpu', 'limits_memory', 'requests_cpu', 'requests_memory')),
        ('Additional Config', ('mtls', 'egress_ip')),
    )

    class Meta:
        model = AppEnvironment

        fields = ["access_token", "cluster_env", "app_env", "mtls", "repo", "branch", "path", "egress_ip", "deployment_kind", "monitoring",
                  "postgres_monitoring", "ocp_project", "requests_cpu", "requests_memory", "limits_cpu",
                  "limits_memory"]

        widgets = {
            'access_token': PasswordInput(),
        }


class AppEnvironmentAddForm(AppEnvironmentBaseForm):
    """Form for creating a new App Environment object."""
    ocp_project = DynamicModelChoiceField(
        queryset=OCPProject.objects.all(),
        label="OCP Project",
        help_text="Choose the ocp project e.g. web shop",
    )


class AppEnvironmentEditForm(AppEnvironmentBaseForm):
    """Form for creating a new App Environment object."""
    ocp_project = DynamicModelChoiceField(
        queryset=OCPProject.objects.all(),
        label="OCP Project",
        help_text="Choose the ocp project e.g. web shop",
        disabled=True
    )


class OCPProjectForm(NetBoxModelForm):
    """Form for creating a new App Environment object."""
    project_owner = DynamicModelChoiceField(
        queryset=Contact.objects.all(),
        label='Project Owner',
        help_text='Choose the Project Owner'
    )
    customer = DynamicModelChoiceField(
        queryset=Tenant.objects.all(),
        label='Customer name',
        help_text='Choose the tenant',
    )

    fieldsets = (
        ('Create OCP Project', ['name', 'description', 'display_name', 'project_owner', 'customer', 'docu_url',
                                'workload', 'request']),
    )

    class Meta:
        model = OCPProject

        fields = ['name', 'description', 'display_name', 'project_owner', 'customer', 'docu_url', 'workload',
                  'request']

