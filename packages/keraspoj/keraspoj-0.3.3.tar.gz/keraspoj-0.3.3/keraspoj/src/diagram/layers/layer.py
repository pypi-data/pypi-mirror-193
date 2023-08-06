import keras.layers

from keraspoj.src.util.config import LayerConfig
from keraspoj.src.util.tools import str_shape
from keraspoj.src.backend.node import Node
from keraspoj.src.backend.misc.position import Position


class Layer:
    sort_order = 9999

    def get_style_name(self) -> str:
        return f"{self.type_group}_layer_style"

    @classmethod
    def get_keras_output_layers(cls, layer: keras.layers.Layer):
        outbound_layers = []
        for outbound_node in layer.outbound_nodes:
            outbound_layers.append(outbound_node.outbound_layer)

        return outbound_layers

    @classmethod
    def get_keras_input_layers(cls, layer: keras.layers.Layer):
        inbound_layers = []
        for inbound_node in layer.inbound_nodes:
            if isinstance(inbound_node.inbound_layers, list):
                for inbound_layer in inbound_node.inbound_layers:
                    inbound_layers.append(inbound_layer)
            else:
                inbound_layers.append(inbound_node.inbound_layers)

        return inbound_layers

    def __init__(self, layer: keras.layers.Layer):
        self.layer = layer
        self.name: str = layer.name
        self.type: str = layer.__class__.__name__
        self.type_group: str = LayerConfig.get_type_group(self.type)
        self.position = Position()

        self.inbound_layers_names = []
        self.outbound_layers_names = []
        self.dependency_layers = set()

        self._parse_input_layers()
        self._parse_output_layers()

    @property
    def trainable_params(self) -> int:
        trainable_params = 0
        for weight in self.layer.weights:
            if weight.trainable:
                trainable_params += weight.shape.num_elements()
        return trainable_params

    @property
    def keras_input_layers(self):
        return self.get_keras_input_layers(self.layer)

    @property
    def keras_output_layers(self):
        return self.get_keras_output_layers(self.layer)

    @property
    def output_shape(self):
        return str_shape(self.layer.output_shape)

    @property
    def input_shape(self):
        return str_shape(self.layer.input_shape)

    def _parse_input_layers(self):
        if len(self.layer.inbound_nodes) == 0:
            return
        for inbound_node in self.layer.inbound_nodes:
            inbound_layers = inbound_node.inbound_layers
            if isinstance(inbound_layers, list):
                for inbound_layer in inbound_layers:
                    self.inbound_layers_names.append(inbound_layer.name)
            else:
                self.inbound_layers_names.append(inbound_layers.name)

    def _parse_output_layers(self):
        if len(self.layer.outbound_nodes) == 0:
            return
        for outbound_node in self.layer.outbound_nodes:
            outbound_layer = outbound_node.outbound_layer
            self.outbound_layers_names.append(outbound_layer.name)

    def _get_siblings(self):
        siblings = set()
        if len(self.keras_input_layers) != 0:
            for inbound_layer in self.keras_input_layers:
                for sibling in self.get_keras_output_layers(inbound_layer):
                    siblings.add(sibling)

        if len(self.keras_output_layers) != 0:
            for outbound_layer in self.keras_output_layers:
                for sibling in self.get_keras_input_layers(outbound_layer):
                    siblings.add(sibling)
        # print(f"Siblings of {self.name}: {siblings}")
        siblings = list(siblings)
        siblings.sort(key=lambda x: x.name)
        return [sibling.name for sibling in siblings]

    def add_dependency_layer(self, layer):
        if isinstance(layer, Layer):
            self.dependency_layers.add(layer.name)
        else:
            self.dependency_layers.add(layer)

    @property
    def layer_description(self) -> tuple:
        layer_type = self.type
        layer = self.layer

        content_lst = [self.type]
        if self.type == "Bidirectional":
            layer_type = self.layer.layer.__class__.__name__
            layer = self.layer.layer
            content_lst = [f"{self.type}({layer_type})"]

        layer_content_config = LayerConfig.load_layer_content(layer_type)

        for content_config in layer_content_config:
            if content_config is None:
                continue

            content_label = content_config['label']
            content_prop = content_config['property']
            content_type = content_config['type']

            if content_prop == 'output_shape':
                content_value = str_shape(layer.output_shape)
            elif content_prop == 'input_shape':
                content_value = str_shape(layer.input_shape)
            else:
                content_value = layer.get_config()
                for prop in content_prop.split('.'):
                    content_value = content_value[prop]

            if content_type == 'int':
                content_value = format(content_value, ",d")
            elif content_type == 'float':
                content_value = format(content_value, ".2f")
            elif content_type == 'shape':
                content_value = str_shape(content_value)

            content_lst.append(f"{content_label}: {content_value}")

        return tuple(content_lst)

    def create_node(self, position: Position = None):

        return Node(self.name,
                    *self.layer_description,
                    node_style_name=self.get_style_name(),
                    position=position,
                    depends_on=[])

    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return f"Layer(name={self.name}, type={self.type})"

    def __lt__(self, other):
        return self.sort_order < other.sort_order or (self.sort_order == other.sort_order and self.name < other.name)
