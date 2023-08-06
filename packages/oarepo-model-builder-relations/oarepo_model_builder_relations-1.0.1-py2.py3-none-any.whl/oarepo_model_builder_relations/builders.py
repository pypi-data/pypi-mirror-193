from munch import unmunchify
from oarepo_model_builder.builders import process
from oarepo_model_builder.invenio.invenio_base import InvenioBaseClassPythonBuilder
from oarepo_model_builder.utils.python_name import convert_name_to_python


class InvenioRecordRelationsBuilder(InvenioBaseClassPythonBuilder):
    TYPE = "invenio_record_relations"
    class_config = "record-class"
    template = "record_relations"

    def begin(self, schema, settings):
        super().begin(schema, settings)
        self.relations = []

    @process("**", condition=lambda current, stack: stack.schema_valid)
    def enter_model_element(self):
        self.build_children()
        data = self.stack.top.data
        if self.stack.top.schema_element_type not in (
            "property",
            "items",
        ) or not isinstance(data, dict):
            return
        if "relation" not in data:
            return
        relation_extension = data["relation"]

        relation = {
            x.replace("-", "_"): relation_extension[x] for x in relation_extension
        }

        keys = relation["keys"]
        model_class = relation["model_class"]
        relation_args = relation["relation_args"]
        pid_field = relation.get("pid_field")
        related_part = relation.get("related_part")

        written_keys = []
        for k in keys:
            if k["key"] == k["target"]:
                written_keys.append(k["key"])
            else:
                written_keys.append({"key": k["key"], "target": k["target"]})

        relation_args.setdefault("keys", repr(written_keys))

        if pid_field or model_class:
            relation_args.setdefault("pid_field", pid_field or f"{model_class}.pid")
        if related_part:
            relation_args.setdefault("related_part", related_part)

        relation.setdefault("path", self._property_path(self.stack))
        relation = {k.replace("-", "_"): v for k, v in unmunchify(relation).items()}
        relation["relation_args"] = {
            k.replace("-", "_"): v for k, v in relation["relation_args"].items()
        }
        relation["name"] = convert_name_to_python(relation["name"])
        for suffix in ("", *[f"_{i}" for i in range(1, 100)]):
            name = relation["name"] + suffix
            for rr in self.relations:
                if name == rr["name"]:
                    break
            else:
                relation["name"] = name
                break

        self.relations.append(relation)

    def process_template(self, python_path, template, **extra_kwargs):
        if self.relations:
            return super().process_template(
                python_path,
                template,
                **{**extra_kwargs, "invenio_relations": self.relations},
            )

    def _property_path(self, stack):
        path = []
        for entry in stack:
            if entry.schema_element_type == "property":
                path.append(entry.key)
        return ".".join(path)
