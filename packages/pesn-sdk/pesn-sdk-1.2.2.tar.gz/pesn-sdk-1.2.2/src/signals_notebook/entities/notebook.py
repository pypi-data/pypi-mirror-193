import json
import logging
from typing import Any, cast, List, Literal, Optional

from pydantic import BaseModel, Field

from signals_notebook.common_types import EntityCreationRequestPayload, EntityType
from signals_notebook.entities.container import Container
from signals_notebook.utils.fs_handler import FSHandler

log = logging.getLogger(__name__)


class _Attributes(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    organization: Optional[str] = None


class _RequestBody(BaseModel):
    type: EntityType
    attributes: _Attributes


class _RequestPayload(EntityCreationRequestPayload[_RequestBody]):
    pass


class Notebook(Container):
    type: Literal[EntityType.NOTEBOOK] = Field(allow_mutation=False)

    @classmethod
    def _get_entity_type(cls) -> EntityType:
        return EntityType.NOTEBOOK

    @classmethod
    def create(
        cls,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        digest: Optional[str] = None,
        force: bool = True,
        organization: Optional[str] = None,
    ) -> 'Notebook':
        """Create Notebook in Signals Notebooks

        Args:
            name: Notebook name
            description: Notebook description
            digest: Indicate digest
            force: Force to create without doing digest check
            organization: Organization
        Returns:

        """

        request = _RequestPayload(
            data=_RequestBody(
                type=cls._get_entity_type(),
                attributes=_Attributes(name=name, description=description, organization=organization),
            )
        )

        log.debug('Creating Notebook for: %s', cls.__name__)
        return cast('Notebook', super()._create(digest=digest, force=force, request=request))

    def dump(self, base_path: str, fs_handler: FSHandler, alias: Optional[List[str]] = None) -> None:
        metadata = {k: v for k, v in self.dict().items() if k in ('name', 'description', 'eid')}
        self._reload_properties()
        for prop in self._properties:
            if prop.name == 'Organization':
                metadata['Organization'] = prop.value
        fs_handler.write(
            fs_handler.join_path(base_path, self.eid, 'metadata.json'),
            json.dumps(metadata),
            alias + [self.name, '__Metadata'] if alias else None,
        )
        for child in self.get_children(order=None):
            child.dump(base_path + '/' + self.eid, fs_handler, alias + [self.name] if alias else None)

    @classmethod
    def load(cls, path: str, fs_handler: FSHandler) -> None:
        cls._load(path, fs_handler, None)

    @classmethod
    def _load(cls, path: str, fs_handler: FSHandler, parent: Any) -> None:
        from signals_notebook.item_mapper import ItemMapper

        metadata = json.loads(fs_handler.read(fs_handler.join_path(path, 'metadata.json')))
        try:
            notebook = cls.create(
                name='restore:' + metadata['name'],
                description=metadata['description'],
                organization=metadata['Organization'],
                force=True,
            )
        except Exception as e:
            log.error(str(e))
            if 'According to template, name is auto generated, can not be specified' in str(e):
                log.error('Retrying create')
                notebook = cls.create(
                    description=metadata['description'], organization=metadata['Organization'], force=True
                )
            else:
                raise e
        child_entities_folders = fs_handler.list_subfolders(path)
        for child_entity in child_entities_folders:
            child_entity_type = child_entity.split(':')[0]
            ItemMapper.get_item_class(child_entity_type)._load(
                fs_handler.join_path(path, child_entity), fs_handler, notebook
            )
