class StatefulSet:
    def __init__(self, name, replicas):
        self.name = name
        self.replicas = replicas
        self.pod_list = []
        self.xml_id = None
        self.y_axis = None
        self.x_axis = None


class HorizontalPodAutoscaler:
    def __init__(self, name, deployment):
        self.name = name
        # Label: app.kubernetes.io/instance + app.kubernetes.io/component
        self.deployment = deployment
        self.xml_id = None
        self.y_axis = None
        self.x_axis = None


class Deployment:
    def __init__(self, name, replicas, replica_set):
        self.name = name
        self.replicas = replicas
        self.replica_set = replica_set
        self.xml_id = None
        self.y_axis = None
        self.x_axis = None


class ReplicaSet:
    def __init__(self, owner_kind, owner_name, name):
        self.owner_kind = owner_kind
        self.owner_name = owner_name
        self.pod_list = []
        self.name = name
        self.xml_id = None
        self.y_axis = None
        self.x_axis = None


class Pod:
    def __init__(self, name, owner_kind, owner_name, label):
        self.name = name
        self.owner_kind = owner_kind
        self.owner_name = owner_name
        self.label = label
        self.xml_id = None
        self.y_axis = None
        self.x_axis = None


class Service:
    def __init__(self, name, selector):
        self.name = name
        self.selector = selector
        self.xml_id = None
        self.y_axis = None
        self.x_axis = None
        self.pod_list = []


class Route:
    def __init__(self, host, to_kind, to_name):
        self.host = host
        self.to_kind = to_kind
        self.to_name = to_name
        self.service = None
        self.xml_id = None
        self.y_axis = None
        self.x_axis = None


class Egress:
    def __init__(self, name, egress_ip, namespace_selector):
        self.name = name
        self.egress_ip = egress_ip
        self.namespace_selector = namespace_selector
        self.xml_id = None
        self.y_axis = None
        self.x_axis = None


class PersistentVolumeClaim:
    def __init__(self, name, storage, pv, storage_class):
        self.name = name
        self.storage = storage
        self.pv = pv
        self.storage_class = storage_class
        self.xml_id = None
        self.y_axis = None
        self.x_axis = None

    def set_xml_id(self, xml_id):
        self.xml_id = xml_id


class PersistentVolume:
    def __init__(self, name):
        self.name = name
        self.xml_id = None
        self.y_axis = None
        self.x_axis = None

    def set_xml_id(self, xml_id):
        self.xml_id = xml_id


class StorageClass:
    def __init__(self, name):
        self.xml_id = None
        self.y_axis = None
        self.x_axis = None
        self.name = name

    def set_xml_id(self, xml_id):
        self.xml_id = xml_id
